"""Run the same fixtures and deterministic differential checks in all languages.

python scripts/verify_codes.py --language cpp
python scripts/verify_codes.py --language python --python pypy3
python scripts/verify_codes.py --language java --javac javac --java java
"""
import argparse
import json
import os
from pathlib import Path
import random
import shutil
import subprocess
import sys
from catalog import entries, case_path
from algorithm_cases import algorithm_cases
from utility_cases import utility_cases

ROOT = Path(__file__).resolve().parents[1]


def differential_cases(topic):
    rng = random.Random(20260924)
    cases = []
    if topic == 'string':
        for n in [1, 7, 100]:
            s = ''.join(rng.choices('abcd', k=n))
            for l, r in [(1, n), (n, n), (1, 1), (2, n-1)] if n > 2 else [(1, n)]:
                out = ''.join(c for i, c in enumerate(s, 1) if l <= i <= r)
                cases.append({'name': f'extract-{n}-{l}-{r}', 'input': f'{s}\n{l} {r}\n', 'output': out+'\n', 'compare': 'exact'})
    elif topic == 'trie':
        for n in [1, 20, 100]:
            words = [''.join(rng.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20)) for _ in range(n)]
            queries, expected = [], []
            for i in range(100):
                s = rng.choice(words)
                if i % 3 == 0:
                    s = s[:rng.randint(1, 19)]
                elif i % 3 == 1:
                    s = ''.join(rng.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(20))
                op = 'word' if i % 2 else 'prefix'
                ok = s in words if op == 'word' else any(w.startswith(s) for w in words)
                queries.append(f'{op} {s}')
                expected.append('YES' if ok else 'NO')
            cases.append({'name': f'word-list-oracle-{n}', 'input': f'{n} 100\n'+'\n'.join(words+queries)+'\n', 'output': '\n'.join(expected)+'\n'})
    elif topic == 'priority-queue':
        for n in [1, 2, 37, 100000]:
            a = [rng.randint(1, 9999) for _ in range(n)]
            cases.append({'name': f'sorted-n{n}', 'input': str(n) + '\n' + ' '.join(map(str, a)) + '\n', 'output': ' '.join(map(str, sorted(a))) + '\n'})
    elif topic == 'segment-tree':
        for n in [1, 3, 16, 19]:
            values = [rng.randint(1, 9999) for _ in range(n)]
            initial = values[:]
            ops, expected = [], []
            for _ in range(180):
                if rng.random() < .4:
                    i, value = rng.randrange(n), rng.randint(1, 9999)
                    ops.append(f'set {i} {value}')
                    values[i] = value
                else:
                    l = rng.randrange(n + 1)
                    r = rng.randint(l, n)
                    ops.append(f'sum {l} {r}')
                    expected.append(str(sum(values[l:r])))
            cases.append({'name': f'differential-n{n}', 'input': f'{n} {len(ops)}\n' + ' '.join(map(str, initial)) + '\n' + '\n'.join(ops) + '\n', 'output': '\n'.join(expected) + '\n'})
    elif topic == 'disjoint-set':
        n = 25
        # A simple component label model, independent of Union-Find.
        labels = list(range(n + 1))
        ops, expected = [], []
        for _ in range(250):
            a, b = rng.randint(1, n), rng.randint(1, n)
            kind = rng.choice(['union', 'same', 'size'])
            if kind == 'union':
                old, new = labels[b], labels[a]
                labels = [new if label == old else label for label in labels]
                ops.append(f'union {a} {b}')
            elif kind == 'same':
                ops.append(f'same {a} {b}')
                expected.append('YES' if labels[a] == labels[b] else 'NO')
            else:
                ops.append(f'size {a}')
                expected.append(str(labels[1:].count(labels[a])))
        cases.append({'name': 'differential-components', 'input': f'{n} {len(ops)}\n' + '\n'.join(ops) + '\n', 'output': '\n'.join(expected) + '\n'})
    elif topic in ['dynamic-array', 'stack', 'queue', 'deque']:
        values, ops, expected = [], [], []
        for _ in range(180):
            choices = ['push', 'pop', 'peek', 'size']
            kind = rng.choice(choices)
            if kind == 'push':
                x = rng.randint(1, 9999)
                front = topic == 'deque' and rng.choice([True, False])
                if front:
                    values.insert(0, x)
                else:
                    values.append(x)
                op = 'append' if topic == 'dynamic-array' else ('push_front' if front else 'push_back') if topic == 'deque' else 'push'
                ops.append(f'{op} {x}')
            elif kind == 'size':
                ops.append('size'); expected.append(str(len(values)))
            elif kind == 'peek' and topic == 'dynamic-array':
                if values:
                    i = rng.randrange(len(values)); ops.append(f'get {i}'); expected.append(str(values[i]))
            else:
                front = topic == 'queue' or (topic == 'deque' and rng.choice([True, False]))
                op = ('pop_front' if front else 'pop_back') if topic == 'deque' and kind == 'pop' else ('front' if front else 'back') if topic == 'deque' else ('pop' if kind == 'pop' else 'front' if front else 'top')
                ops.append(op)
                index = 0 if front else -1
                expected.append(str(values[index]) if values else 'EMPTY')
                if values and kind == 'pop': values.pop(index)
        cases.append({'name':'differential-operations','input':str(len(ops))+'\n'+'\n'.join(ops)+'\n','output':'\n'.join(expected)+'\n'})
    return cases


def valid_subsequence_output(topic, case, actual):
    """Accept any optimal witness; verify its length, values, and original order."""
    lines = actual.splitlines()
    if len(lines) != 2:
        return False
    try:
        length = int(lines[0])
        if length != int(case['output'].split()[0]):
            return False

        def is_subsequence(seq, values):
            i = 0
            for x in values:
                if i < len(seq) and seq[i] == x:
                    i += 1
            return i == len(seq)

        if topic == 'lis':
            seq = list(map(int, lines[1].split()))
            values = list(map(int, case['input'].split()))[1:]
            return (len(seq) == length
                    and all(x < y for x, y in zip(seq, seq[1:]))
                    and is_subsequence(seq, values))

        a, b = case['input'].split()
        seq = lines[1]
        return len(seq) == length and is_subsequence(seq, a) and is_subsequence(seq, b)
    except ValueError:
        return False


def run(command, **kwargs):
    result = subprocess.run(command, encoding='utf-8', errors='replace', capture_output=True, timeout=40, **kwargs)
    if result.returncode:
        raise RuntimeError(f"Command failed: {' '.join(map(str, command))}\n{result.stderr}\n{result.stdout}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', choices=['cpp','java','python','all'], default='all')
    parser.add_argument('--cpp', default='g++')
    parser.add_argument('--javac', default='javac')
    parser.add_argument('--java', default='java')
    parser.add_argument('--python', default='pypy3')
    parser.add_argument('--category', choices=['data-structures', 'algorithms', 'utilities'])
    parser.add_argument('--topic', action='append', help='Verify only this topic; may be repeated.')
    args = parser.parse_args()
    languages = ['cpp','java','python'] if args.language == 'all' else [args.language]
    topics = entries()
    if args.category:
        topics = [(category, topic) for category, topic in topics if category == args.category]
    if args.topic:
        unknown = set(args.topic) - {topic for _, topic in topics}
        if unknown: raise RuntimeError(f'Unknown topics: {sorted(unknown)}')
        topics = [(category, topic) for category, topic in topics if topic in args.topic]
    config = json.loads((ROOT/'src/data/example-languages.json').read_text(encoding='utf-8'))
    total = 0
    for language in languages:
        tools = [args.cpp] if language == 'cpp' else [args.javac,args.java] if language == 'java' else [args.python]
        for tool in tools:
            if not shutil.which(tool): raise RuntimeError(f'Required executable: {tool}')
        for category, topic in topics:
            if language not in config.get(topic, ['cpp', 'java', 'python']):
                continue
            source = ROOT/'codes'/language/category/topic
            build = ROOT/'.build'/language/category/topic
            build.mkdir(parents=True, exist_ok=True)
            if language == 'cpp':
                binary = build/('main.exe' if os.name == 'nt' else 'main')
                run([args.cpp,'-std=c++20','-O2','-Wall','-Wextra','-pedantic-errors',str(source/'main.cpp'),'-o',str(binary)])
                command = [str(binary)]
            elif language == 'java':
                run([args.javac,'--release','17','-encoding','UTF-8','-d',str(build),str(source/'Main.java')])
                command = [args.java,'-cp',str(build),'Main']
            else:
                command = [args.python,str(source/'main.py')]
            cases = json.loads(case_path(category, topic).read_text(encoding='utf-8')) + (algorithm_cases(topic) if category == 'algorithms' else utility_cases(topic) if category == 'utilities' else differential_cases(topic))
            for case in cases:
                actual = run(command, input=case['input'])
                if category == 'algorithms' and topic in ['lis', 'lcs']:
                    matches = valid_subsequence_output(topic, case, actual)
                else:
                    matches = actual == case['output'] if case.get('compare') == 'exact' else actual.split() == case['output'].split()
                if not matches:
                    raise AssertionError(f"{language}/{topic}/{case['name']}\nExpected: {case['output']!r}\nActual: {actual!r}")
                total += 1
            print(f'PASS {language}/{topic}: {len(cases)} cases', flush=True)
    print(f'Passed {total} executions.')


if __name__ == '__main__':
    try:
        main()
    except (RuntimeError, AssertionError, subprocess.TimeoutExpired) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)

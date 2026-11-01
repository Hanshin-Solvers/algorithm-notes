"""Deterministic utility fixtures including whitespace and arithmetic boundaries."""
import random


def utility_cases(topic):
    rng = random.Random(20261030)
    cases = []

    def row(a):
        return ' '.join(map(str, a)) + '\n'

    def add(inp, out, exact=False):
        case = {'name': f'utility-{len(cases)+1}', 'input': inp, 'output': out}
        if exact:
            case['compare'] = 'exact'
        cases.append(case)

    if topic in ['submission-template', 'numeric-types']:
        for a,b in [(1,9999),(9999,1),(123,456)]:
            ans = a+b if topic=='submission-template' else a*b
            add(f'{a} {b}\n',f'{ans}\n')
    elif topic == 'basic-io':
        for s in ['   A  B   ', 'ONLY ONE LINE', 'Z'*100, ' ']:
            add(s+'\n7 8\n',s+'\n15\n',True)
    elif topic == 'fast-io':
        for n in [1,37,10000]:
            a = [rng.randint(1,9999) for _ in range(n)]
            tokens = [str(n)] + list(map(str,a))
            text = ''.join(x+rng.choice([' ', '\t', '\n', '\n\n','\r\n']) for x in tokens)
            add(text.rstrip(),''.join(f'{x*2}\n' for x in a),True)
    elif topic == 'test-cases':
        for t in [1,7,100]:
            rows = [[rng.randint(1,9999) for _ in range(rng.randint(1,100))] for _ in range(t)]
            inp = f'{t}\n'+''.join(f'{len(a)}\n'+row(a) for a in rows)
            add(inp,''.join(f'{sum(a)}\n' for a in rows),True)
    elif topic == 'eof-input':
        a=[(rng.randint(1,9999),rng.randint(1,9999)) for _ in range(100)]
        add('\n\n'+'\n\n'.join(f'{x}\t{y}' for x,y in a),''.join(f'{x+y}\n' for x,y in a),True)
    elif topic == 'complexity':
        for n in [2,3,17,99]:
            add(f'{n}\n',f'{n}\n{n*(n-1)//2}\n')
    elif topic == 'division-modulo':
        for a,b in [(-9999,100),(-1,100),(1,100),(9999,100),(-9999,1),(0,1),(9999,1),(-100,100)]:
            add(f'{a} {b}\n',f'{a%b}\n')
    elif topic == 'decimal-formatting':
        # 정수 계산으로 평균의 출력 자릿수와 올림·내림·반올림 검증
        for scores in [(0, 0, 0), (100, 100, 100), (1, 0, 0), (1, 1, 0), (99, 100, 100), (12, 34, 56)]:
            total = sum(scores)
            for digits in [0, 1, 3, 6]:
                scale = 10 ** digits
                scaled = (total * scale + 1) // 3
                fixed = str(scaled) if digits == 0 else f'{scaled // scale}.{scaled % scale:0{digits}d}'
                up, down, near = (total + 2) // 3, total // 3, (total + 1) // 3
                add(' '.join(map(str, (*scores, digits))) + '\n', f'{fixed}\n{up} {down} {near}\n', True)
    elif topic == 'container-operations':
        for n in [1,8,100]:
            a=[rng.randint(1,9999) for _ in range(n)]
            k=rng.randrange(n)
            x=rng.randint(1,9999)
            b=a[:]
            b[k]=x
            add(f'{n}\n'+row(a)+f'{k+1} {x}\n',row(a)+row(b))
    elif topic == 'bit-operations':
        for x in [0,255,170,85]:
            for k in [0,3,7]:
                bits=list(reversed(f'{x:08b}'))
                bit=int(bits[k])
                values=[]
                for new in [1,0,1-bit]:
                    tmp=bits[:]
                    tmp[k]=str(new)
                    values.append(int(''.join(reversed(tmp)),2))
                add(f'{x} {k}\n',row([bit]+values))
    elif topic == 'priority-queue-ordering':
        for n in [1, 20, 100]:
            ids = rng.sample(range(1, 1001), n)
            jobs = [(i, rng.randint(1, 5)) for i in ids]
            expected = [i for i, p in sorted(jobs, key=lambda a: (a[1], a[0]))]
            add(f'{n}\n'+''.join(f'{i} {p}\n' for i, p in jobs), row(expected))
    elif topic == 'custom-hash':
        for n in [1, 20, 100]:
            points = [(rng.randrange(10), rng.randrange(10)) for _ in range(n)]
            queries = [rng.choice(points) for _ in range(50)]
            queries += [(rng.randrange(1000), rng.randrange(1000)) for _ in range(50)]
            # Direct tuple comparison is independent of the C++ hash formula.
            out = ''.join(f'{points.count(p)}\n' for p in queries)
            add(f'{n} 100\n'+''.join(f'{x} {y}\n' for x, y in points+queries), out)
    return cases

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
            add(f'{a} {b}\n',f'{a//b} {-(-a//b)} {a%b}\n')
    elif topic == 'type-conversion':
        for s in ['0001','0100','9990','7']:
            add(s+'\n',f'{int(s)}\n{sum(map(int,s))}\n',True)
    elif topic == 'string-operations':
        for n in [1,7,100]:
            s=''.join(rng.choices('abcd',k=n))
            for l,r in [(1,n),(n,n),(1,1)]:
                add(s+f'\n{l} {r}\n',s[l-1:r]+'\n',True)
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
    elif topic == 'grid-directions':
        for n,m,r,c in [(1,10,1,10),(10,1,10,1),(10,10,10,10),(10,10,1,10),(10,10,10,1)]:
            neighbors=[(r-1,c),(r,c+1),(r+1,c),(r,c-1)]
            out=''.join(row([x,y]) for x,y in neighbors if 1<=x<=n and 1<=y<=m)
            add(f'{n} {m}\n{r} {c}\n',out or 'NONE\n',True)
    elif topic == 'debugging':
        for n in [1,17,100]:
            a=[rng.randint(1,9999) for _ in range(n)]
            add(f'{n}\n'+row(a),f'{sum(a)}\n',True)
    return cases

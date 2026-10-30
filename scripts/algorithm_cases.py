"""Small deterministic oracle cases, shared by the three language runners."""
from functools import lru_cache
from itertools import combinations, permutations, product
from fractions import Fraction
from math import comb, factorial, gcd
import random


def algorithm_cases(topic):
    rng = random.Random(20261030)
    cases = []

    def add(inp, out):
        cases.append({'name': f'oracle-{len(cases) + 1}', 'input': inp, 'output': str(out) + '\n'})

    def row(values):
        return ' '.join(map(str, values)) + '\n'

    def matrix(rows):
        return ''.join(row(r) for r in rows)

    def primes(n):
        return [x for x in range(2, n + 1) if all(x % d for d in range(2, x))]

    def subs(s):
        return {''.join(s[i] for i in range(len(s)) if mask >> i & 1) for mask in range(1 << len(s))}

    def cross(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

    if topic == 'gcd-lcm':
        for a, b in [(1, 1000), (999, 1000), (24, 36), (42, 42)]:
            add(f'{a} {b}\n', f'{gcd(a,b)} {a*b//gcd(a,b)}')
    elif topic in ['divisors', 'primality', 'sieve', 'factorization']:
        for n in [2, 49, 97, 120]:
            if topic == 'divisors':
                out = row(x for x in range(1, n+1) if n % x == 0)
            elif topic == 'primality':
                out = 'YES' if n in primes(n) else 'NO'
            elif topic == 'sieve':
                out = row(primes(n))
            else:
                out = []
                tmp = n
                for p in primes(n):
                    while tmp % p == 0:
                        out.append(p)
                        tmp //= p
                out = row(out)
            add(f'{n}\n', out)
    elif topic == 'base-conversion':
        for n, b, c in [(9999,16,2), (9999,2,16), (255,8,10), (15,16,16)]:
            def numeral(x, base):
                if x == 0:
                    return '0'
                digits = []
                for k in range(14, -1, -1):
                    digits.append('0123456789ABCDEF'[(x // base**k) % base])
                return ''.join(digits).lstrip('0')
            add(f'{b} {c}\n{numeral(n,b)}\n', numeral(n,c))
    elif topic == 'combinatorics':
        for n, r in [(10,10), (10,0), (8,3)]:
            add(f'{n} {r}\n', f'{factorial(n)//factorial(n-r)}\n{comb(n,r)}')
    elif topic == 'sorting':
        for n in [1, 8, 30]:
            a = [(x, rng.randint(1, 5)) for x in rng.sample(range(1,100),n)]
            ans = []
            for score in range(5,0,-1):
                ans.extend(sorted(x for x,s in a if s == score))
            add(f'{n}\n'+matrix(a), row(ans))
    elif topic == 'brute-force':
        for n, t in [(6,2),(6,12),(4,5)]:
            add(f'{n} {t}\n', sum(a+b==t for a,b in product(range(1,n+1),repeat=2)))
    elif topic == 'backtracking':
        for n,r in [(5,1),(5,5),(8,4)]:
            add(f'{n} {r}\n', matrix(combinations(range(1,n+1),r)))
    elif topic == 'power':
        for a,b in [(10,8),(1,8),(7,0),(2,7)]:
            add(f'{a} {b}\n', a**b)
    elif topic == 'matrix-power':
        for n,b in [(1,0),(3,8),(3,5),(2,2)]:
            a = [[rng.randrange(3) for _ in range(n)] for _ in range(n)]
            res = [[int(i==j) for j in range(n)] for i in range(n)]
            for _ in range(b):
                res = [[sum(res[i][k]*a[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
            add(f'{n} {b}\n'+matrix(a), matrix(res))
    elif topic in ['merge-sort','binary-search','sliding-window','two-pointers','lis']:
        for n in [1,5,10]:
            a = [rng.randint(1,20) for _ in range(n)]
            if topic == 'merge-sort':
                add(f'{n}\n'+row(a), row(sorted(a)))
            elif topic == 'binary-search':
                a.sort()
                x = rng.choice(a+[100])
                add(f'{n} {x}\n'+row(a), a.count(x))
            elif topic == 'sliding-window':
                k = rng.randint(1,n)
                add(f'{n} {k}\n'+row(a), max(sum(a[i:i+k]) for i in range(n-k+1)))
            elif topic == 'two-pointers':
                s = rng.randint(1,sum(a)+10)
                lengths = [j-i for i in range(n) for j in range(i+1,n+1) if sum(a[i:j])>=s]
                add(f'{n} {s}\n'+row(a), min(lengths,default=0))
            else:
                best = 0
                for mask in range(1<<n):
                    seq = [a[i] for i in range(n) if mask>>i&1]
                    if all(x<y for x,y in zip(seq,seq[1:])):
                        best = max(best,len(seq))
                add(f'{n}\n'+row(a), best)
    elif topic == 'parametric-search':
        for n in [1,5,10]:
            a = [rng.randint(1,40) for _ in range(n)]
            k = rng.randint(1,sum(a)+2)
            ans = max((x for x in range(1,max(a)+1) if sum(v//x for v in a)>=k),default=0)
            add(f'{n} {k}\n'+row(a), ans)
    elif topic == 'greedy':
        for n in [1,5,9]:
            a = [tuple(sorted(rng.sample(range(1,20),2))) for _ in range(n)]
            best = 0
            for mask in range(1<<n):
                intervals = sorted(a[i] for i in range(n) if mask>>i&1)
                if all(x[1]<=y[0] for x,y in zip(intervals,intervals[1:])):
                    best=max(best,len(intervals))
            covered = {x for l,r in a for x in range(l,r)}
            starts = sorted(x for x in covered if x-1 not in covered)
            ends = sorted(x+1 for x in covered if x+1 not in covered)
            add(f'{n}\n'+matrix(a), f'{best}\n{len(starts)}\n'+matrix(zip(starts,ends)))
    elif topic in ['prefix-sum','difference-array']:
        for n in [1,9]:
            a = [rng.randint(1,100) for _ in range(n)]
            queries, out = [], []
            res = [0]*n
            for _ in range(15):
                l = rng.randint(1,n)
                r = rng.randint(l,n)
                if topic == 'prefix-sum':
                    queries.append((l,r))
                    out.append(sum(a[l-1:r]))
                else:
                    x = rng.randint(1,100)
                    queries.append((l,r,x))
                    for j in range(l-1,r):
                        res[j]+=x
            if topic == 'prefix-sum':
                add(f'{n} 15\n'+row(a)+matrix(queries), row(out))
            else:
                add(f'{n} 15\n'+matrix(queries), row(res))
    elif topic == 'prefix-grid':
        for n,m in [(1,5),(4,3)]:
            a = [[rng.randint(1,100) for _ in range(m)] for _ in range(n)]
            queries,out=[],[]
            for _ in range(15):
                x1,y1=rng.randint(1,n),rng.randint(1,m)
                x2,y2=rng.randint(x1,n),rng.randint(y1,m)
                queries.append((x1,y1,x2,y2))
                out.append(sum(a[i][j] for i in range(x1-1,x2) for j in range(y1-1,y2)))
            add(f'{n} {m} 15\n'+matrix(a)+matrix(queries), row(out))
    elif topic == 'dp-basics':
        for n in [2,7,19]:
            add(f'{n}\n', sum(comb(n-k,k) for k in range(n//2+1)))
    elif topic in ['bfs','grid-dp']:
        for n,m in [(1,1),(3,4),(5,5)]:
            a = [[int(rng.random()>.25) for _ in range(m)] for _ in range(n)]
            a[0][0]=a[-1][-1]=1
            if topic == 'grid-dp':
                def paths(i,j):
                    if i==n or j==m or not a[i][j]:
                        return 0
                    if (i,j)==(n-1,m-1):
                        return 1
                    return paths(i+1,j)+paths(i,j+1)
                ans = paths(0,0)
            else:
                # Bellman relaxation as an independent grid distance oracle.
                d = [[1000]*m for _ in range(n)]
                d[0][0]=0
                for _ in range(n*m):
                    for i in range(n):
                        for j in range(m):
                            if not a[i][j]:
                                continue
                            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                                if 0<=x<n and 0<=y<m and a[x][y]:
                                    d[x][y]=min(d[x][y],d[i][j]+1)
                ans = -1 if d[-1][-1]==1000 else d[-1][-1]
            add(f'{n} {m}\n'+''.join(''.join(map(str,r))+'\n' for r in a), ans)
    elif topic == 'knapsack':
        for n,w in [(1,8),(4,10),(6,15)]:
            a = [(rng.randint(2,8),rng.randint(1,20)) for _ in range(n)]
            single = max(sum(a[i][1] for i in range(n) if mask>>i&1) for mask in range(1<<n) if sum(a[i][0] for i in range(n) if mask>>i&1)<=w)
            @lru_cache(None)
            def unlimited(i,cap):
                if i==n:
                    return 0
                weight,value=a[i]
                return max(k*value+unlimited(i+1,cap-k*weight) for k in range(cap//weight+1))
            add(f'{n} {w}\n'+matrix(a), f'{single}\n{unlimited(0,w)}')
    elif topic == 'lcs':
        for n,m in [(1,7),(7,8),(8,8)]:
            s=''.join(rng.choices('ABC',k=n))
            p=''.join(rng.choices('ABC',k=m))
            add(s+'\n'+p+'\n', max(map(len,subs(s)&subs(p))))
    elif topic == 'binomial':
        for n,r in [(30,15),(30,29),(1,0),(20,8)]:
            add(f'{n} {r}\n', comb(n,r))
    elif topic in ['dfs','bipartite','topological-sort','kruskal']:
        for n in [1,4,6]:
            edges = [(i,j) for i in range(1,n+1) for j in range(i+1,n+1) if rng.random()<.5]
            if topic in ['dfs','kruskal']:
                def components(es):
                    labels=list(range(n+1))
                    for u,v in es:
                        x,y=labels[u],labels[v]
                        labels=[x if z==y else z for z in labels]
                    return len(set(labels[1:]))
                if topic=='dfs':
                    ans=components(edges)
                else:
                    edges=[(u,v,rng.randint(1,20)) for u,v in edges]
                    vals=[sum(e[2] for e in es) for es in combinations(edges,n-1) if components((e[:2] for e in es))==1]
                    ans=min(vals,default='IMPOSSIBLE')
            elif topic=='bipartite':
                ans='YES' if any(all(((mask>>(u-1))&1)!=((mask>>(v-1))&1) for u,v in edges) for mask in range(1<<n)) else 'NO'
            else:
                edges=[(u,v) if rng.random()<.5 else (v,u) for u,v in edges]
                ans='IMPOSSIBLE'
                for seq in permutations(range(1,n+1)):
                    if all(seq.index(u)<seq.index(v) for u,v in edges):
                        ans=row(seq)
                        break
            add(f'{n} {len(edges)}\n'+matrix(edges), ans)
    elif topic in ['dijkstra','bellman-ford','floyd-warshall']:
        for n in [2,4,6]:
            if topic=='dijkstra':
                # An oriented tree has at most one path to every vertex.
                edges=[(rng.randrange(1,v),v,rng.randint(1,20)) for v in range(2,n+1)]
            else:
                edges=[(i,j,rng.randint(-3,8) if topic=='bellman-ford' else rng.randint(1,20)) for i in range(1,n+1) for j in range(1,n+1) if rng.random()<.3]
            inf=10**8
            d=[[inf]*n for _ in range(n)]
            for i in range(n):
                d[i][i]=0
            for u,v,w in edges:
                d[u-1][v-1]=min(d[u-1][v-1],w)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if d[i][k]<inf and d[k][j]<inf:
                            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
            header=f'{n} {len(edges)}\n'
            if topic=='dijkstra':
                header=f'{n} {len(edges)} 1 {n}\n'
                p={v:u for u,v,_ in edges}
                seq=[n]
                while seq[-1]!=1:
                    seq.append(p[seq[-1]])
                ans=f'{d[0][-1]}\n'+row(reversed(seq))
            elif topic=='bellman-ford':
                ans='NEGATIVE CYCLE' if any(d[0][i]<inf and d[i][i]<0 for i in range(n)) else row('INF' if x==inf else x for x in d[0])
            else:
                ans=matrix([-1 if x==inf else x for x in r] for r in d)
            add(header+matrix(edges),ans)
    elif topic in ['tree-traversal','tree-diameter']:
        for n in [1,6,12]:
            parents=[0,0]+[rng.randrange(1,v) for v in range(2,n+1)]
            edges=[(parents[v],v,rng.randint(1,20)) for v in range(2,n+1)]
            if topic=='tree-traversal':
                depth=[0]*(n+1)
                size=[1]*(n+1)
                for v in range(2,n+1):
                    u=parents[v]
                    depth[v]=depth[u]+1
                    while u:
                        size[u]+=1
                        u=parents[u]
                ans=matrix((parents[v],depth[v],size[v]) for v in range(1,n+1))
                edges=[(u,v) for u,v,_ in edges]
            else:
                d=[[100000]*n for _ in range(n)]
                for i in range(n):
                    d[i][i]=0
                for u,v,w in edges:
                    d[u-1][v-1]=d[v-1][u-1]=w
                for k in range(n):
                    for i in range(n):
                        for j in range(n):
                            d[i][j]=min(d[i][j],d[i][k]+d[k][j])
                ans=max(map(max,d))
            add(f'{n}\n'+matrix(edges),ans)
    elif topic in ['palindrome','pattern-search','kmp']:
        for _ in range(6):
            s=''.join(rng.choices('AB',k=20))
            if topic=='palindrome':
                if rng.random()<.5:
                    s=s+s[::-1]
                add(s+'\n','YES' if s==s[::-1] else 'NO')
            else:
                p=''.join(rng.choices('AB',k=rng.randint(1,7)))
                positions=[i for i in range(len(s)) if s.startswith(p,i)]
                add(s+'\n'+p+'\n',f'{len(positions)}\n'+row(positions))
    elif topic == 'ccw':
        for _ in range(6):
            a,b,c=[(rng.randrange(101),rng.randrange(101)) for _ in range(3)]
            det=a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0]*(a[1]-b[1])
            add(matrix([a,b,c]),(det>0)-(det<0))
    elif topic == 'segment-intersection':
        for _ in range(12):
            a,b,c,d=rng.sample(list(product(range(6),repeat=2)),4)
            ux,uy=b[0]-a[0],b[1]-a[1]
            vx,vy=d[0]-c[0],d[1]-c[1]
            wx,wy=c[0]-a[0],c[1]-a[1]
            den=ux*vy-uy*vx
            if den:
                t=Fraction(wx*vy-wy*vx,den)
                s=Fraction(wx*uy-wy*ux,den)
                ok=0<=t<=1 and 0<=s<=1
            else:
                def on(p,q,r):
                    return cross(p,q,r)==0 and min(p[0],q[0])<=r[0]<=max(p[0],q[0]) and min(p[1],q[1])<=r[1]<=max(p[1],q[1])
                ok=on(a,b,c) or on(a,b,d) or on(c,d,a) or on(c,d,b)
            add(row(a+b)+row(c+d),'YES' if ok else 'NO')
    elif topic=='polygon-area':
        for w,h in [(1,1),(100,100),(7,9)]:
            a=[(0,0),(w,0),(0,h)]
            area=w*h
            add('3\n'+matrix(a),f'{area//2}.{5 if area%2 else 0}')
            add('3\n'+matrix(reversed(a)),f'{area//2}.{5 if area%2 else 0}')
    elif topic=='convex-hull':
        # Gift wrapping oracle, independent of the monotone chain examples.
        for n in [1,2,8,20]:
            a=[(rng.randrange(11),rng.randrange(11)) for _ in range(n)]
            points=sorted(set(a))
            hull=[points[0]]
            if len(points)>1:
                while True:
                    u=hull[-1]
                    v=next(p for p in points if p!=u)
                    for p in points:
                        turn=cross(u,v,p)
                        if turn<0 or (turn==0 and sum((p[i]-u[i])**2 for i in [0,1])>sum((v[i]-u[i])**2 for i in [0,1])):
                            v=p
                    if v==hull[0]:
                        break
                    hull.append(v)
            add(f'{n}\n'+matrix(a),f'{len(hull)}\n'+matrix(hull))
    return cases

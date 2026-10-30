import java.util.*;

public class Main {
    static final int N = 10000;
    static int[] p = new int[N + 1], sz = new int[N + 1];

    static int find(int x) {
        while (p[x] != x) {
            p[x] = p[p[x]]; // 경로 절반 압축
            x = p[x];
        }
        return x;
    }

    // Union by Size: 집합의 원소 수를 기준으로 합침
    static void unite(int a, int b) {
        int tmp;

        a = find(a);
        b = find(b);
        if (a == b) return;
        if (sz[a] < sz[b]) {
            tmp = a;
            a = b;
            b = tmp;
        }
        p[b] = a;
        sz[a] += sz[b]; // 합친 집합의 원소 수 갱신
    }

    public static void main(String[] args) {
        Scanner in;
        int n, q, i, a, b;
        String op;

        in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();

        for (i = 1; i <= n; ++i) {
            p[i] = i;
            sz[i] = 1;
        }

        for (i = 0; i < q; ++i) {
            op = in.next();
            a = in.nextInt();

            if (op.equals("size")) System.out.println(sz[find(a)]);
            else {
                b = in.nextInt();

                if (op.equals("union")) unite(a, b);
                else if (find(a) == find(b)) System.out.println("YES");
                else System.out.println("NO");
            }
        }
    }
}

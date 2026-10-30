import java.util.*;

public class Main {
    static int[] p = new int[101], sz = new int[101];

    static int find(int x) {
        while (x != p[x]) {
            p[x] = p[p[x]];
            x = p[x];
        }
        return x;
    }

    static boolean unite(int a, int b) {
        int tmp;

        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (sz[a] < sz[b]) {
            tmp = a;
            a = b;
            b = tmp;
        }
        p[b] = a;
        sz[a] += sz[b];
        return true;
    }

    public static void main(String[] args) {
        Scanner sc;
        int n, m, i, j, cnt, ans;
        int[][] edges;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (i = 1; i <= n; ++i) {
            p[i] = i;
            sz[i] = 1;
        }
        edges = new int[m][3];
        for (i = 0; i < m; ++i) {
            for (j = 0; j < 3; ++j) {
                edges[i][j] = sc.nextInt();
            }
        }
        Arrays.sort(edges, Comparator.comparingInt(e -> e[2]));
        cnt = 0;
        ans = 0;

        for (int[] e : edges) {
            if (unite(e[0], e[1])) {
                ans += e[2];
                ++cnt;
            }
        }

        if (cnt == n - 1) System.out.println(ans);
        else System.out.println("IMPOSSIBLE");
    }
}

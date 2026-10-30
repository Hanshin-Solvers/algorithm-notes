import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static int[] p = new int[101], d = new int[101], sz = new int[101];

    static void dfs(int u, int par) {
        // 자식 탐색 전 부모와 크기 초기값 설정
        p[u] = par;
        sz[u] = 1;
        for (int v : g.get(u)) {
            if (v == par) continue;
            d[v] = d[u] + 1;
            dfs(v, u);
            // 자식 탐색 후 서브트리 크기 합산
            sz[u] += sz[v];
        }
    }

    public static void main(String[] args) {
        Scanner sc;
        int n, i, a, b;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        for (i = 0; i < n - 1; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            g.get(a).add(b);
            g.get(b).add(a);
        }

        dfs(1, 0);

        for (i = 1; i <= n; ++i) {
            System.out.println(p[i] + " " + d[i] + " " + sz[i]);
        }
    }
}

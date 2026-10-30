import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static boolean[] seen = new boolean[101];

    static void dfs(int u) {
        seen[u] = true;
        for (int v : g.get(u)) {
            if (!seen[v]) dfs(v);
        }
    }

    public static void main(String[] args) {
        Scanner in;
        int n, m, i, a, b, cnt;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        for (i = 0; i < m; ++i) {
            a = in.nextInt();
            b = in.nextInt();
            g.get(a).add(b);
            g.get(b).add(a);
        }

        cnt = 0;
        for (i = 1; i <= n; ++i) {
            if (!seen[i]) {
                ++cnt;
                dfs(i);
            }
        }
        System.out.println(cnt);
    }
}

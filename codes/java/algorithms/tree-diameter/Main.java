import java.util.*;

public class Main {
    static ArrayList<ArrayList<int[]>> g = new ArrayList<>();
    static int far, best;

    static void dfs(int u, int par, int dist) {
        if (dist > best) {
            best = dist;
            far = u;
        }
        for (int[] e : g.get(u)) {
            if (e[0] == par) continue;
            dfs(e[0], u, dist + e[1]);
        }
    }

    public static void main(String[] args) {
        Scanner sc;
        int n, i, a, b, w;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        for (i = 0; i < n - 1; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            w = sc.nextInt();
            g.get(a).add(new int[]{b, w});
            g.get(b).add(new int[]{a, w});
        }

        far = 1;
        best = 0;
        dfs(1, 0, 0);
        a = far;
        best = 0;
        dfs(a, 0, 0);

        System.out.println(best);
    }
}

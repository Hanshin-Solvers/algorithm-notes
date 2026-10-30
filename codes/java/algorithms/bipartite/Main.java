import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, m, i, a, b, u;
        int[] c;
        boolean ok;
        ArrayList<ArrayList<Integer>> g;
        ArrayDeque<Integer> q;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        g = new ArrayList<>();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        c = new int[n + 1];
        Arrays.fill(c, -1);
        q = new ArrayDeque<>();
        for (i = 0; i < m; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            g.get(a).add(b);
            g.get(b).add(a);
        }

        ok = true;
        for (i = 1; i <= n; ++i) {
            if (c[i] != -1) continue;
            c[i] = 0;
            q.addLast(i);
            while (!q.isEmpty()) {
                u = q.removeFirst();
                for (int v : g.get(u)) {
                    if (c[v] == -1) {
                        c[v] = 1 - c[u];
                        q.addLast(v);
                    }
                    else if (c[v] == c[u]) ok = false;
                }
            }
        }

        System.out.println(ok ? "YES" : "NO");
    }
}

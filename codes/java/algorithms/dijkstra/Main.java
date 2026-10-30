import java.util.*;

public class Main {
    public static void main(String[] args) {
        final int INF = 1000000;
        Scanner sc;
        int n, m, s, t, i, a, b, w, u, du;
        int[] d, p, cur;
        ArrayList<ArrayList<int[]>> g;
        ArrayList<Integer> ans;
        PriorityQueue<int[]> pq;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        s = sc.nextInt();
        t = sc.nextInt();
        g = new ArrayList<>();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        d = new int[n + 1];
        p = new int[n + 1];
        Arrays.fill(d, INF);
        ans = new ArrayList<>();
        pq = new PriorityQueue<>(Comparator.comparingInt(e -> e[0]));
        for (i = 0; i < m; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            w = sc.nextInt();
            g.get(a).add(new int[]{b, w});
        }
        d[s] = 0;
        pq.add(new int[]{0, s});

        while (!pq.isEmpty()) {
            cur = pq.poll();
            du = cur[0];
            u = cur[1];
            if (du != d[u]) continue;
            for (int[] e : g.get(u)) {
                if (du + e[1] < d[e[0]]) {
                    d[e[0]] = du + e[1];
                    p[e[0]] = u;
                    pq.add(new int[]{d[e[0]], e[0]});
                }
            }
        }

        if (d[t] == INF) System.out.println(-1);
        else {
            for (u = t; u != 0; u = p[u]) {
                ans.add(u);
            }
            Collections.reverse(ans);
            System.out.println(d[t]);
            for (int v : ans) {
                System.out.print(v + " ");
            }
            System.out.println();
        }
    }
}

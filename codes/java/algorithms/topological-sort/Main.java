import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, m, i, a, b, u;
        int[] d;
        ArrayList<ArrayList<Integer>> g;
        ArrayList<Integer> ans;
        PriorityQueue<Integer> pq;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        g = new ArrayList<>();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        d = new int[n + 1];
        ans = new ArrayList<>();
        pq = new PriorityQueue<>();
        for (i = 0; i < m; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            g.get(a).add(b);
            ++d[b];
        }
        for (i = 1; i <= n; ++i) {
            if (d[i] == 0) pq.add(i);
        }

        while (!pq.isEmpty()) {
            u = pq.poll();
            ans.add(u);
            for (int v : g.get(u)) {
                --d[v];
                if (d[v] == 0) pq.add(v);
            }
        }

        if (ans.size() != n) System.out.println("IMPOSSIBLE");
        else {
            for (int v : ans) {
                System.out.print(v + " ");
            }
            System.out.println();
        }
    }
}

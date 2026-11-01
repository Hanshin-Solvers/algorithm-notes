import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, u, v;
        int[] d;
        ArrayList<ArrayList<Integer>> g;
        ArrayDeque<Integer> q;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        g = new ArrayList<>();
        d = new int[n + 1];
        q = new ArrayDeque<>();
        for (i = 0; i <= n; ++i) {
            g.add(new ArrayList<>());
        }
        for (i = 0; i < m; ++i) {
            u = in.nextInt();
            v = in.nextInt();
            g.get(u).add(v);
            g.get(v).add(u);
        }
        Arrays.fill(d, -1);
        d[1] = 0;
        q.offer(1);

        while (!q.isEmpty()) {
            u = q.poll();
            for (int next : g.get(u)) {
                if (d[next] != -1) continue;
                // 큐에 넣을 때 거리와 방문 여부 기록
                d[next] = d[u] + 1;
                q.offer(next);
            }
        }
        System.out.println(d[n]);
    }
}

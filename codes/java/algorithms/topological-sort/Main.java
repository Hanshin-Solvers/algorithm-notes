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
            // d[v]: 아직 처리하지 않은 진입 간선의 수
            ++d[b];
        }
        for (i = 1; i <= n; ++i) {
            // 선행 조건이 없는 정점을 넣고 작은 번호부터 선택
            if (d[i] == 0) pq.add(i);
        }

        while (!pq.isEmpty()) {
            u = pq.poll();
            ans.add(u);
            for (int v : g.get(u)) {
                // 현재 정점에서 나가는 간선을 제거하여 다음 정점의 진입 차수 감소
                --d[v];
                if (d[v] == 0) pq.add(v);
            }
        }

        // 모든 정점을 처리하지 못했으면 방향 사이클 존재
        if (ans.size() != n) System.out.println("IMPOSSIBLE");
        else {
            for (int v : ans) {
                System.out.print(v + " ");
            }
            System.out.println();
        }
    }
}

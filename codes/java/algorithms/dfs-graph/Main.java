import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static boolean[] seen = new boolean[101];

    static void dfs(int u) {
        // 다른 정점으로 이동하기 전에 방문을 표시하여 사이클의 재방문 방지
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
            // 미방문 정점에서 시작한 DFS 하나가 연결 요소 하나를 탐색함
            if (!seen[i]) {
                ++cnt;
                dfs(i);
            }
        }
        System.out.println(cnt);
    }
}

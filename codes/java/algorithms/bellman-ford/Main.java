import java.util.*;

public class Main {
    public static void main(String[] args) {
        final int INF = 1000000;
        Scanner sc;
        int n, m, i, j, a, b, w;
        int[][] edges;
        int[] d;
        boolean changed, cycle;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        edges = new int[m][3];
        for (i = 0; i < m; ++i) {
            for (j = 0; j < 3; ++j) {
                edges[i][j] = sc.nextInt();
            }
        }
        d = new int[n + 1];
        Arrays.fill(d, INF);
        d[1] = 0;
        cycle = false;

        for (i = 1; i <= n; ++i) {
            changed = false;
            for (int[] e : edges) {
                a = e[0];
                b = e[1];
                w = e[2];
                // 시작점에서 도달한 정점의 간선만 사용
                if (d[a] == INF) continue;
                if (d[a] + w < d[b]) {
                    d[b] = d[a] + w;
                    changed = true;
                    // n번째 반복에도 갱신되면 시작점에서 도달 가능한 음수 사이클 존재
                    if (i == n) cycle = true;
                }
            }
            // 거리 변화가 없으면 이후 반복에서도 갱신되지 않으므로 종료
            if (!changed) break;
        }

        if (cycle) System.out.println("NEGATIVE CYCLE");
        else {
            for (j = 1; j <= n; ++j) {
                if (d[j] == INF) System.out.print("INF ");
                else System.out.print(d[j] + " ");
            }
            System.out.println();
        }
    }
}

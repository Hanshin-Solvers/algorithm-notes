import java.util.*;

public class Main {
    public static void main(String[] args) {
        final int INF = 1000000;
        Scanner sc;
        int n, m, i, j, k, a, b, w;
        int[][] d;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        d = new int[n + 1][n + 1];
        for (i = 1; i <= n; ++i) {
            Arrays.fill(d[i], INF);
            d[i][i] = 0;
        }
        for (i = 0; i < m; ++i) {
            a = sc.nextInt();
            b = sc.nextInt();
            w = sc.nextInt();
            // 같은 두 정점 사이의 여러 간선 중 최소 가중치 저장
            d[a][b] = Math.min(d[a][b], w);
        }

        // 경유 가능한 정점을 k까지 확장하므로 k를 가장 바깥에서 순회
        for (k = 1; k <= n; ++k) {
            for (i = 1; i <= n; ++i) {
                for (j = 1; j <= n; ++j) {
                    // i에서 k 또는 k에서 j로 갈 수 없으면 경로 결합 제외
                    if (d[i][k] == INF || d[k][j] == INF) continue;
                    // 기존 거리와 i → k → j 경로의 거리 비교
                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
                }
            }
        }

        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= n; ++j) {
                if (d[i][j] == INF) System.out.print(-1 + " ");
                else System.out.print(d[i][j] + " ");
            }
            System.out.println();
        }
    }
}

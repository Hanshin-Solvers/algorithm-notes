import java.util.*;

public class Main {
    static int n, m;
    static int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};
    static int[][] g;
    static boolean[][] seen;

    static void dfs(int r, int c) {
        int k, nr, nc;

        seen[r][c] = true;
        for (k = 0; k < 4; ++k) {
            nr = r + dr[k];
            nc = c + dc[k];
            // 범위 확인 후 벽과 방문 여부 확인
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            if (g[nr][nc] == 0 || seen[nr][nc]) continue;
            dfs(nr, nc);
        }
    }

    public static void main(String[] args) {
        Scanner in;
        int i, j, cnt;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        g = new int[n][m];
        seen = new boolean[n][m];
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                g[i][j] = in.nextInt();
            }
        }
        cnt = 0;

        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                if (g[i][j] == 1 && !seen[i][j]) {
                    // 새 영역 탐색
                    ++cnt;
                    dfs(i, j);
                }
            }
        }
        System.out.println(cnt);
    }
}

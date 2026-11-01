import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, j, x, y, nx, ny, k;
        int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1}, cur;
        int[][] d, g;
        ArrayDeque<int[]> q;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        g = new int[n][m];
        d = new int[n][m];
        q = new ArrayDeque<>();
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                g[i][j] = in.nextInt();
            }
            Arrays.fill(d[i], -1);
        }
        // d[x][y]: 시작 칸에서의 최소 이동 횟수, -1은 미방문
        d[0][0] = 0;
        q.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            cur = q.poll();
            x = cur[0];
            y = cur[1];
            for (k = 0; k < 4; ++k) {
                nx = x + dx[k];
                ny = y + dy[k];
                // 배열에 접근하기 전에 다음 칸이 격자 안인지 확인
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (g[nx][ny] == 0 || d[nx][ny] != -1) continue;
                // 처음 발견한 거리가 최단 거리이므로 큐에 넣기 전에 방문 처리
                d[nx][ny] = d[x][y] + 1;
                q.offer(new int[]{nx, ny});
            }
        }
        System.out.println(d[n - 1][m - 1]);
    }
}

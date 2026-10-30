import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, m, i, x, y, nx, ny, k;
        int[] dx = {-1, 1, 0, 0}, dy = {0, 0, -1, 1}, cur;
        int[][] d;
        String[] g;
        ArrayDeque<int[]> q;

        in = new Scanner(System.in);
        n = in.nextInt();
        m = in.nextInt();
        g = new String[n];
        d = new int[n][m];
        q = new ArrayDeque<>();
        for (i = 0; i < n; ++i) {
            g[i] = in.next();
            Arrays.fill(d[i], -1);
        }
        d[0][0] = 0;
        q.offer(new int[]{0, 0});

        while (!q.isEmpty()) {
            cur = q.poll();
            x = cur[0];
            y = cur[1];
            for (k = 0; k < 4; ++k) {
                nx = x + dx[k];
                ny = y + dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
                if (g[nx].charAt(ny) == '0' || d[nx][ny] != -1) continue;
                d[nx][ny] = d[x][y] + 1;
                q.offer(new int[]{nx, ny});
            }
        }
        System.out.println(d[n - 1][m - 1]);
    }
}

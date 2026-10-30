import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, m, r, c, nr, nc, k, cnt;
        int[] dr = {-1, 0, 1, 0}, dc = {0, 1, 0, -1};

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        r = sc.nextInt() - 1;
        c = sc.nextInt() - 1;
        cnt = 0;

        for (k = 0; k < 4; ++k) {
            nr = r + dr[k];
            nc = c + dc[k];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            // 출력 번호는 1부터 시작
            System.out.println((nr + 1) + " " + (nc + 1));
            ++cnt;
        }

        if (cnt == 0) System.out.println("NONE");
    }
}

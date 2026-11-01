import java.util.*;

public class Main {
    // 세 점의 외적으로 기준 직선에 대한 방향 계산
    static int cross(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]);
    }

    static boolean overlap(int a, int b, int c, int d) {
        return Math.max(Math.min(a, b), Math.min(c, d))
            <= Math.min(Math.max(a, b), Math.max(c, d));
    }

    public static void main(String[] args) {
        Scanner sc;
        int[] a, b, c, d;
        int x, y, z, w;
        boolean ok;

        sc = new Scanner(System.in);
        a = new int[]{sc.nextInt(), sc.nextInt()};
        b = new int[]{sc.nextInt(), sc.nextInt()};
        c = new int[]{sc.nextInt(), sc.nextInt()};
        d = new int[]{sc.nextInt(), sc.nextInt()};
        // 외적을 -1, 0, 1로 바꾸어 양쪽 선분의 방향 조건 비교
        x = Integer.signum(cross(a, b, c));
        y = Integer.signum(cross(a, b, d));
        z = Integer.signum(cross(c, d, a));
        w = Integer.signum(cross(c, d, b));

        // 네 점이 일직선이면 x좌표와 y좌표의 공통 구간 확인
        if (x == 0 && y == 0 && z == 0 && w == 0) {
            ok = overlap(a[0], b[0], c[0], d[0])
              && overlap(a[1], b[1], c[1], d[1]);
        }
        // 각 직선의 양쪽에 상대 선분의 끝점이 놓이는지 확인
        else ok = (x * y <= 0 && z * w <= 0);

        System.out.println(ok ? "YES" : "NO");
    }
}

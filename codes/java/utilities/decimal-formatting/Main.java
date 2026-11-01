import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int a, b, c, n, up, down, near;
        double x;

        sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        n = sc.nextInt();

        // 소수 부분까지 계산하도록 실수로 평균 계산
        x = (a + b + c) / 3.0;
        up = (int)Math.ceil(x);
        down = (int)Math.floor(x);
        near = (int)Math.round(x);

        // 소수 구분자를 점으로 고정하여 소수점 아래 n자리 출력
        System.out.printf(Locale.ROOT, "%." + n + "f%n", x);
        System.out.println(up + " " + down + " " + near);
    }
}

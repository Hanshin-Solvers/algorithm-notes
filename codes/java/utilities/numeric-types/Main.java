import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int a, b;
        long area;

        sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();

        // 곱셈 전에 long으로 확장
        area = 1L * a * b;

        System.out.println(area);
    }
}

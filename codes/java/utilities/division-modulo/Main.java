import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int a, m, r;

        sc = new Scanner(System.in);
        a = sc.nextInt();
        m = sc.nextInt();

        // 양수 m에 대해 0 이상 m 미만의 나머지 계산
        r = Math.floorMod(a, m);

        System.out.println(r);
    }
}

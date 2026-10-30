import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int[] a;
        int i;

        in = new Scanner(System.in);
        a = new int[5];
        for (i = 0; i < 5; ++i) {
            a[i] = in.nextInt();
        }

        // 첫 번째와 세 번째 원소 조회
        System.out.println(a[0]);
        System.out.println(a[2]);

        a[2] = 9; // 세 번째 원소 갱신

        System.out.println(a[2]);
    }
}

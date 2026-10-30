import java.util.*;

public class Main {
    static int n, r;
    static int[] a = new int[9];

    static void search(int d, int start) {
        int i;

        if (d == r) {
            for (i = 0; i < r; ++i) {
                System.out.print(a[i] + " ");
            }
            System.out.println();
            return;
        }
        // 남은 수로 필요한 자리를 채울 수 있을 때만 선택
        for (i = start; i <= n - (r - d) + 1; ++i) {
            a[d] = i;
            search(d + 1, i + 1);
        }
    }

    public static void main(String[] args) {
        Scanner in;

        in = new Scanner(System.in);
        n = in.nextInt();
        r = in.nextInt();
        search(0, 1);
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, k, x, i;
        int[] a, b;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = sc.nextInt();
        }
        k = sc.nextInt();
        x = sc.nextInt();

        // 원소를 복사한 뒤 복사본 수정
        b = a.clone();
        b[k - 1] = x;

        for (int v : a) {
            System.out.print(v + " ");
        }
        System.out.println();
        for (int v : b) {
            System.out.print(v + " ");
        }
        System.out.println();
    }
}

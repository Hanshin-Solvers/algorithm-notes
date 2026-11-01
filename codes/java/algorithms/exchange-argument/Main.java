import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, sum, ans;
        int[] a;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n];
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }

        Arrays.sort(a);
        sum = 0;
        ans = 0;
        for (int x : a) {
            // 현재 작업의 완료 시각과 전체 합 갱신
            sum += x;
            ans += sum;
        }

        System.out.println(ans);
    }
}

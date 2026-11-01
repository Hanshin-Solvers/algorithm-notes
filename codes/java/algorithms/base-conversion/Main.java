import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        String s;
        StringBuilder ans;
        int n, x, r;

        in = new Scanner(System.in);
        s = in.next();
        n = in.nextInt();
        ans = new StringBuilder();
        x = 0;

        // 왼쪽부터 26진수의 자릿값을 누적함
        for (char c : s.toCharArray()) {
            x = x * 26 + (c - 'a');
        }
        System.out.println(x);

        // 낮은 자리부터 구한 뒤 순서를 뒤집음
        if (n == 0) ans.append('a');
        while (n > 0) {
            r = n % 26;
            ans.append((char) ('a' + r));
            n /= 26;
        }
        ans.reverse();
        System.out.println(ans);
    }
}

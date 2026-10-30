import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        String s, out;
        int n, sum;

        sc = new Scanner(System.in);
        s = sc.next();
        n = Integer.parseInt(s);
        sum = 0;

        for (char c : s.toCharArray()) {
            sum += c - '0';
        }
        // 정수를 문자열로 변환
        out = String.valueOf(n);

        System.out.println(out);
        System.out.println(sum);
    }
}

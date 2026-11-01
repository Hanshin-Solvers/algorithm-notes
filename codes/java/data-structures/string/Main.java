import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        String s, t;
        int l, r;

        sc = new Scanner(System.in);
        s = sc.next();
        l = sc.nextInt();
        r = sc.nextInt();

        // 끝 인덱스 r은 추출 범위에서 제외됨
        t = s.substring(l - 1, r);

        System.out.println(t);
    }
}

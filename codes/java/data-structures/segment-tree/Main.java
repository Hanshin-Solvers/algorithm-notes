import java.util.*;

public class Main {
    static final int N = 10000; // 최대 원소 수
    static int[] t = new int[N * 4];

    // 노드 k의 담당 구간 [s, e)에서 인덱스 i의 값을 x로 갱신
    static void update(int k, int s, int e, int i, int x) {
        int m;

        if (e - s == 1) {
            t[k] = x;
            return;
        }

        m = (s + e) / 2;
        if (i < m) update(k * 2, s, m, i, x);
        else update(k * 2 + 1, m, e, i, x);

        t[k] = t[k * 2] + t[k * 2 + 1];
    }

    // [l, r) 구간 합 질의
    static int query(int k, int s, int e, int l, int r) {
        int m;

        if (r <= s || e <= l) return 0;
        if (l <= s && e <= r) return t[k];

        m = (s + e) / 2;
        return query(k * 2, s, m, l, r) + query(k * 2 + 1, m, e, l, r);
    }

    public static void main(String[] args) {
        Scanner in;
        int n, q, i, j, l, r, x;
        String op;

        in = new Scanner(System.in);
        n = in.nextInt();
        q = in.nextInt();

        // 루트 1에서 [0, n) 구간을 기준으로 입력값 저장
        for (i = 0; i < n; ++i) {
            x = in.nextInt();
            update(1, 0, n, i, x);
        }

        for (i = 0; i < q; ++i) {
            op = in.next();

            if (op.equals("set")) {
                j = in.nextInt();
                x = in.nextInt();

                update(1, 0, n, j, x);
            }
            else {
                l = in.nextInt();
                r = in.nextInt();

                System.out.println(query(1, 0, n, l, r));
            }
        }
    }
}

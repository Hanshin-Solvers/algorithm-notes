import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, l, r, m, len;
        // t[k]: 길이 k+1 수열의 최소 끝값, pos[k]: 해당 원소 위치, p[i]: 이전 원소 위치
        int[] a, t, pos, p;
        ArrayList<Integer> lst;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n];
        t = new int[n];
        pos = new int[n];
        p = new int[n];
        Arrays.fill(p, -1);
        lst = new ArrayList<>();
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }

        len = 0;
        for (i = 0; i < n; ++i) {
            // 현재 값 이상인 첫 위치 탐색
            l = 0;
            r = len;
            while (l < r) {
                m = (l + r) / 2;
                if (t[m] < a[i]) l = m + 1;
                else r = m;
            }

            // 후보 교체 전에 이전 원소의 위치 저장
            if (l > 0) p[i] = pos[l - 1];
            t[l] = a[i];
            pos[l] = i;
            if (l == len) ++len;
        }

        // 가장 긴 수열의 끝에서 이전 위치를 따라 복원
        i = pos[len - 1];
        while (i != -1) {
            lst.add(a[i]);
            i = p[i];
        }
        Collections.reverse(lst);

        System.out.println(len);
        for (int x : lst) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}

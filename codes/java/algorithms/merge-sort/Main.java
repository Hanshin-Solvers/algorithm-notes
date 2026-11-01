import java.util.*;

public class Main {
    static int[] a = new int[101], t = new int[101];

    static void sortRange(int l, int r) {
        int m, i, j, k;

        // 구간 [l, r)의 원소가 하나 이하이면 정렬 종료
        if (r - l <= 1) return;
        m = (l + r) / 2;
        // 왼쪽 [l, m)과 오른쪽 [m, r)을 각각 정렬
        sortRange(l, m);
        sortRange(m, r);

        i = l;
        j = m;
        k = l;
        // 두 구간의 맨 앞 값 중 작은 값을 임시 배열에 저장
        while (i < m && j < r) {
            // 값이 같으면 왼쪽 원소를 먼저 선택하여 기존 순서 유지
            if (a[i] <= a[j]) {
                t[k] = a[i];
                ++i;
            }
            else {
                t[k] = a[j];
                ++j;
            }
            ++k;
        }
        while (i < m) {
            t[k] = a[i];
            ++k;
            ++i;
        }
        while (j < r) {
            t[k] = a[j];
            ++k;
            ++j;
        }
        // 병합한 결과를 원래 구간에 반영
        for (i = l; i < r; ++i) {
            a[i] = t[i];
        }
    }

    public static void main(String[] args) {
        Scanner in;
        int n, i;

        in = new Scanner(System.in);
        n = in.nextInt();
        for (i = 0; i < n; ++i) {
            a[i] = in.nextInt();
        }
        sortRange(0, n);

        for (i = 0; i < n; ++i) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}

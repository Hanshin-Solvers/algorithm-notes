import java.util.*;

public class Main {
    static int cross(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]);
    }

    public static void main(String[] args) {
        Scanner sc;
        int n, i;
        int[][] a;
        ArrayList<int[]> lst, lo, hi, ans;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n][2];
        for (int[] pt : a) {
            pt[0] = sc.nextInt();
            pt[1] = sc.nextInt();
        }
        Arrays.sort(a, (u, v) -> {
            if (u[0] != v[0]) return Integer.compare(u[0], v[0]);
            else return Integer.compare(u[1], v[1]);
        });
        lst = new ArrayList<>();
        for (int[] pt : a) {
            if (lst.isEmpty() || !Arrays.equals(lst.get(lst.size() - 1), pt)) lst.add(pt);
        }
        lo = new ArrayList<>();
        hi = new ArrayList<>();
        ans = new ArrayList<>();

        if (lst.size() == 1) ans.add(lst.get(0));
        else {
            // 아래쪽 경계 구성
            for (int[] pt : lst) {
                while (lo.size() >= 2 && cross(lo.get(lo.size() - 2), lo.get(lo.size() - 1), pt) <= 0) {
                    lo.remove(lo.size() - 1);
                }
                lo.add(pt);
            }
            Collections.reverse(lst);
            // 위쪽 경계 구성
            for (int[] pt : lst) {
                while (hi.size() >= 2 && cross(hi.get(hi.size() - 2), hi.get(hi.size() - 1), pt) <= 0) {
                    hi.remove(hi.size() - 1);
                }
                hi.add(pt);
            }
            lo.remove(lo.size() - 1);
            hi.remove(hi.size() - 1);
            ans.addAll(lo);
            ans.addAll(hi);
        }

        System.out.println(ans.size());
        for (int[] pt : ans) {
            System.out.println(pt[0] + " " + pt[1]);
        }
    }
}

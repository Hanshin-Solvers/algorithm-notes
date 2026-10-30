import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i, cnt, end;
        int[][] a;
        ArrayList<int[]> merged;
        int[] last;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n][2];
        for (i = 0; i < n; ++i) {
            a[i][0] = in.nextInt();
            a[i][1] = in.nextInt();
        }
        Arrays.sort(a, Comparator.comparingInt(x -> x[1]));
        cnt = 0;
        end = 0;
        for (int[] x : a) {
            if (x[0] >= end) {
                ++cnt;
                end = x[1];
            }
        }

        // 시작점 순서로 구간 병합
        Arrays.sort(a, Comparator.comparingInt(x -> x[0]));
        merged = new ArrayList<>();
        for (int[] x : a) {
            if (merged.isEmpty() || merged.get(merged.size() - 1)[1] < x[0]) merged.add(x.clone());
            else {
                last = merged.get(merged.size() - 1);
                last[1] = Math.max(last[1], x[1]);
            }
        }
        System.out.println(cnt);
        System.out.println(merged.size());
        for (int[] x : merged) {
            System.out.println(x[0] + " " + x[1]);
        }
    }
}

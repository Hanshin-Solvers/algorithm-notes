import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        int[][] a;
        int[] last;
        ArrayList<int[]> lst;

        in = new Scanner(System.in);
        n = in.nextInt();
        a = new int[n][2];
        for (i = 0; i < n; ++i) {
            a[i][0] = in.nextInt();
            a[i][1] = in.nextInt();
        }

        // 시작점 순서로 정렬 후 병합
        Arrays.sort(a, Comparator.comparingInt(x -> x[0]));
        lst = new ArrayList<>();
        for (int[] x : a) {
            if (lst.isEmpty() || lst.get(lst.size() - 1)[1] < x[0]) lst.add(x.clone());
            else {
                last = lst.get(lst.size() - 1);
                last[1] = Math.max(last[1], x[1]);
            }
        }

        System.out.println(lst.size());
        for (int[] x : lst) {
            System.out.println(x[0] + " " + x[1]);
        }
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int n, i, j, area;
        int[][] a;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        a = new int[n][2];
        for (int[] row : a) {
            row[0] = sc.nextInt();
            row[1] = sc.nextInt();
        }

        area = 0;
        for (i = 0; i < n; ++i) {
            j = (i + 1) % n;
            area += a[i][0] * a[j][1] - a[i][1] * a[j][0];
        }
        area = Math.abs(area);

        System.out.print(area / 2);
        if (area % 2 == 0) System.out.println(".0");
        else System.out.println(".5");
    }
}

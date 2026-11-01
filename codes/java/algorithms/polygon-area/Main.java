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
            // 마지막 꼭짓점 다음은 첫 꼭짓점으로 연결
            j = (i + 1) % n;
            // 인접한 두 꼭짓점의 외적을 부호 그대로 누적
            area += a[i][0] * a[j][1] - a[i][1] * a[j][0];
        }
        // 합을 구한 뒤 절댓값을 취하여 넓이의 두 배 계산
        area = Math.abs(area);

        System.out.print(area / 2);
        if (area % 2 == 0) System.out.println(".0");
        else System.out.println(".5");
    }
}

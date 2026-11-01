import java.util.*;

public class Main {
    static boolean[] seen = new boolean[101];

    static void dfs(int x) {
        seen[x] = true;

        // 연산 결과가 범위 안이고 미방문 상태이면 탐색
        if (x + 1 <= 100 && !seen[x + 1]) dfs(x + 1);
        if (x * 2 <= 100 && !seen[x * 2]) dfs(x * 2);
    }

    public static void main(String[] args) {
        Scanner in;
        int a, b;

        in = new Scanner(System.in);
        a = in.nextInt();
        b = in.nextInt();
        dfs(a);

        if (seen[b]) System.out.println("YES");
        else System.out.println("NO");
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int a, b, x;
        int[] d;
        ArrayDeque<Integer> q;

        in = new Scanner(System.in);
        a = in.nextInt();
        b = in.nextInt();
        d = new int[101];
        q = new ArrayDeque<>();
        Arrays.fill(d, -1);
        d[a] = 0;
        q.offer(a);

        while (!q.isEmpty()) {
            x = q.poll();
            for (int y : new int[]{x + 1, x * 2}) {
                if (y > 100 || d[y] != -1) continue;
                // 처음 도달한 횟수가 최소 연산 횟수임
                d[y] = d[x] + 1;
                q.offer(y);
            }
        }
        System.out.println(d[b]);
    }
}

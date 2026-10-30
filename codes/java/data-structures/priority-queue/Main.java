import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        PriorityQueue<Integer> pq;
        StringJoiner out;

        in = new Scanner(System.in);
        n = in.nextInt();

        pq = new PriorityQueue<>();
        for (i = 0; i < n; ++i) {
            pq.offer(in.nextInt());
        }
        out = new StringJoiner(" ");
        while (!pq.isEmpty()) {
            out.add(Integer.toString(pq.poll()));
        }

        System.out.println(out);
    }
}

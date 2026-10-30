import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        ArrayDeque<Integer> q;
        String op;

        in = new Scanner(System.in);
        n = in.nextInt();

        q = new ArrayDeque<>();
        for (i = 0; i < n; ++i) {
            op = in.next();

            if (op.equals("push")) q.offerLast(in.nextInt());
            else if (op.equals("size")) System.out.println(q.size());
            else if (q.isEmpty()) System.out.println("EMPTY");
            else if (op.equals("front")) System.out.println(q.peekFirst());
            else System.out.println(q.pollFirst());
        }
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int q, i;
        ArrayDeque<Integer> dq;
        String op;

        in = new Scanner(System.in);
        q = in.nextInt();

        dq = new ArrayDeque<>();
        for (i = 0; i < q; ++i) {
            op = in.next();

            if (op.equals("push_front")) dq.addFirst(in.nextInt());
            else if (op.equals("push_back")) dq.addLast(in.nextInt());
            else if (op.equals("size")) System.out.println(dq.size());
            else if (dq.isEmpty()) System.out.println("EMPTY");
            else if (op.equals("front")) System.out.println(dq.peekFirst());
            else if (op.equals("back")) System.out.println(dq.peekLast());
            else if (op.equals("pop_front")) System.out.println(dq.removeFirst());
            else System.out.println(dq.removeLast());
        }
    }
}

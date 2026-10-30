import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int q, i;
        ArrayDeque<Integer> st;
        String op;

        in = new Scanner(System.in);
        q = in.nextInt();

        st = new ArrayDeque<>();
        for (i = 0; i < q; ++i) {
            op = in.next();

            if (op.equals("push")) st.push(in.nextInt());
            else if (op.equals("size")) System.out.println(st.size());
            else if (st.isEmpty()) System.out.println("EMPTY");
            else if (op.equals("top")) System.out.println(st.peek());
            else System.out.println(st.pop());
        }
    }
}

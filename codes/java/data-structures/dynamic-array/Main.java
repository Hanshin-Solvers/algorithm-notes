import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int q, i;
        ArrayList<Integer> lst;
        String op;

        in = new Scanner(System.in);
        q = in.nextInt();

        lst = new ArrayList<>();
        for (i = 0; i < q; ++i) {
            op = in.next();

            if (op.equals("append")) lst.add(in.nextInt());
            else if (op.equals("pop")) {
                if (lst.isEmpty()) System.out.println("EMPTY");
                else System.out.println(lst.remove(lst.size() - 1));
            }
            else if (op.equals("get")) System.out.println(lst.get(in.nextInt()));
            else System.out.println(lst.size());
        }
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        ArrayList<Integer> lst;

        in = new Scanner(System.in);
        n = in.nextInt();
        lst = new ArrayList<>();
        for (i = 1; i <= n / i; ++i) {
            if (n % i == 0) {
                lst.add(i);
                if (i != n / i) lst.add(n / i);
            }
        }
        Collections.sort(lst);

        for (int x : lst) {
            System.out.print(x + " ");
        }
        System.out.println();
    }
}

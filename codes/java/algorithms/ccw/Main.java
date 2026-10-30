import java.util.*;

public class Main {
    static int cross(int[] a, int[] b, int[] c) {
        return (b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]);
    }

    public static void main(String[] args) {
        Scanner sc;
        int[] a, b, c;
        int v;

        sc = new Scanner(System.in);
        a = new int[]{sc.nextInt(), sc.nextInt()};
        b = new int[]{sc.nextInt(), sc.nextInt()};
        c = new int[]{sc.nextInt(), sc.nextInt()};

        v = cross(a, b, c);
        if (v > 0) System.out.println(1);
        else if (v == 0) System.out.println(0);
        else System.out.println(-1);
    }
}

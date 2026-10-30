import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc;
        int x, k, mask, bit, on, off, flip;

        sc = new Scanner(System.in);
        x = sc.nextInt();
        k = sc.nextInt();
        mask = 1 << k;

        bit = (x >> k) & 1;
        on = x | mask;
        off = x & ~mask;
        flip = x ^ mask;

        System.out.println(bit + " " + on + " " + off + " " + flip);
    }
}

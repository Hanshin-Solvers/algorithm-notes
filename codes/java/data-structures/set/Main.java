import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in;
        int n, i;
        TreeSet<Integer> set;
        StringJoiner out;

        in = new Scanner(System.in);
        n = in.nextInt();

        set = new TreeSet<>();
        for (i = 0; i < n; ++i) {
            set.add(in.nextInt()); // 중복 값은 한 번만 저장
        }

        System.out.println(set.size());
        out = new StringJoiner(" ");
        // 정렬 집합의 원소를 오름차순으로 출력
        for (int x : set) {
            out.add(Integer.toString(x));
        }

        System.out.println(out);
    }
}

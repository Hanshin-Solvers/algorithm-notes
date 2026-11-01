import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static StringTokenizer st;

    static String next() throws IOException {
        String s;

        // 현재 줄의 값을 모두 읽었으면 다음 줄을 읽음
        while (st == null || !st.hasMoreTokens()) {
            s = br.readLine();
            if (s == null) return null;
            st = new StringTokenizer(s);
        }
        return st.nextToken();
    }

    public static void main(String[] args) throws IOException {
        int n, i, x;
        StringBuilder sb;

        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        n = Integer.parseInt(next());

        for (i = 0; i < n; ++i) {
            x = Integer.parseInt(next());
            sb.append(x * 2).append('\n');
        }

        System.out.print(sb);
    }
}

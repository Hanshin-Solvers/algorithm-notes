import java.util.*;

public class Main {
    static int[] p = new int[101], sz = new int[101];

    static int find(int x) {
        while (x != p[x]) {
            // 조부모로 연결하여 대표까지의 경로 단축
            p[x] = p[p[x]];
            x = p[x];
        }
        return x;
    }

    static boolean unite(int a, int b) {
        int tmp;

        a = find(a);
        b = find(b);
        // 이미 같은 집합이면 간선 추가 시 사이클이 생기므로 제외
        if (a == b) return false;
        // 작은 집합을 큰 집합 아래에 연결하도록 대표 교환
        if (sz[a] < sz[b]) {
            tmp = a;
            a = b;
            b = tmp;
        }
        p[b] = a;
        sz[a] += sz[b];
        return true;
    }

    public static void main(String[] args) {
        Scanner sc;
        int n, m, i, j, cnt, ans;
        int[][] edges;

        sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        for (i = 1; i <= n; ++i) {
            p[i] = i;
            sz[i] = 1;
        }
        edges = new int[m][3];
        for (i = 0; i < m; ++i) {
            for (j = 0; j < 3; ++j) {
                edges[i][j] = sc.nextInt();
            }
        }
        // 가중치가 작은 간선부터 검사
        Arrays.sort(edges, Comparator.comparingInt(e -> e[2]));
        cnt = 0;
        ans = 0;

        for (int[] e : edges) {
            if (unite(e[0], e[1])) {
                ans += e[2];
                ++cnt;
            }
        }

        // n-1개 간선을 선택했으면 모든 정점을 연결한 신장 트리 완성
        if (cnt == n - 1) System.out.println(ans);
        else System.out.println("IMPOSSIBLE");
    }
}

import java.util.*;

public class j1011 {
    public static long gcd(long a, long b) {
        while(b != 0){
            long r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    public static long bcnn(long a, long b) {
        return a * b / gcd(a, b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            long a = sc.nextInt();
            long b = sc.nextInt();
            System.out.printf("%d %d \n", bcnn(a, b), gcd(a, b));
        }
    }
}

import java.util.Scanner;

public class j1013 {
    public static long thuaso(long a){
        long result = 0;
        for(long i = 2; i * i <= a; i++){
            while (a % i == 0) {
                a /= i;
                result += i;
            }
        }
        if (a > 1) result += a;
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        long a = 0;
        while (t-- > 0) {
            long b = sc.nextLong();
            a += thuaso(b);
        }
        System.out.println(a);
    }
}

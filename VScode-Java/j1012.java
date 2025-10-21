import java.util.Scanner;

public class j1012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            long a = sc.nextLong();
            int sum = 0;
            for(long i = 1; i * i <= a; i++){
                if(a % i == 0){
                    if(i % 2 == 0) sum++;
                    if(i != a / i && (a / i) % 2 == 0) sum++;
                }
            }
            System.out.println(sum);
        }
    }
}

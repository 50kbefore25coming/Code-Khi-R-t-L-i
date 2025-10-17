import java.util.*;

public class j1009 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = 1;
        while(t-- > 0){
            long a = sc.nextLong();
            long b = 0;
            long res = 1;
            for(int i = 1; i <= a; i++){
                res *= i;
                b = b + res;
            }
            System.out.println(b);
        }
    }
}
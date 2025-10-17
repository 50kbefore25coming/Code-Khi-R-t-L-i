import java.util.*;

public class j1008 {
    public static boolean snt (long a){
        if(a < 2){
            return false;
        }
        for(int i = 2; i <= Math.sqrt(a); i++){
            if(a % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        int Case = 1;
        while(t-- > 0){
            int a = sc.nextInt();
            System.out.printf("Test %d: ", Case);
            Case++;
            for(int i = 2; i <= a; i++){
                int num = 0;
                while(a % i == 0){
                    a /= i;
                    num++;
                }
                if(num > 0){
                    System.out.printf("%d(%d) ", i, num);
                }
            }
            System.out.printf("\n");
        }
    }
}
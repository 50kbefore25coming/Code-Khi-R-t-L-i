import java.util.*;

public class j1006 {
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
        while(t-- > 0){
            int a = sc.nextInt();
            long f1 = 1;
            long f2 = 1;
            long fn = 1;
            for(int i = 3; i <= a; i++){
                fn = f2 + f1;
                f2 = f1;
                f1 = fn;
            }
            System.out.println(fn);
        }
        sc.close();
    }
}

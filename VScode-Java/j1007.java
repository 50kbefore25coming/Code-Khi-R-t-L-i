import java.util.*;

public class j1007 {
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
        long a[] = new long[100];
        // sang
        a[0] = 0;
        a[1] = 1;
        for(int i = 2; i <= 93; i++){
            a[i] = a[i - 2] + a[i - 1];
        }
        while(t-- > 0){
            int flag = 0;
            long b = sc.nextLong();
            for(int i = 0; i <= 92; i++){
                if(b == a[i]){
                    flag = 1;
                    break;
                }
            }
            if(flag == 1){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
    }
}
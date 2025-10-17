import java.util.*;

public class j1004 {
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
        long t = sc.nextLong();
        while(t-- > 0){
            long a = sc.nextLong();
            if(snt(a)){
                System.out.println("YES");
            }else{
                System.out.println("NO");
            }
        }
    }
}

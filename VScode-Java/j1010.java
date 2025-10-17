import java.util.*;

public class j1010 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            String a = sc.next();
            String res = "0";
            for(int i = 0; i < a.length(); i++){
                if (a.charAt(i) == '0' || a.charAt(i) == '8' || a.charAt(i) == '9') {
                    res.charAt(i) = 0;
                    continue;
                }
                res.charAt(i) = a.charAt(i);
            }
            System.out.println(res);
        }
    }
}
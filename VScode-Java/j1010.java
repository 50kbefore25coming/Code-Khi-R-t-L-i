import java.math.BigInteger;
import java.util.*;

public class j1010 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while(t-- > 0){
            int flag = 1;
            String a = sc.next();
            StringBuilder res = new StringBuilder();

            for (char c : a.toCharArray()) {
                if (c == '0' || c == '8' || c == '9') res.append('0');
                else if (c == '1') res.append('1');
                else { flag = 0; break; }
            }
            
            if (flag == 0) {
                System.out.println("INVALID");
            }else {
                String result = res.toString().replaceFirst("^0+", "");
                System.out.println(result.isEmpty() ? "INVALID" : result);
            }
        }
    }
}
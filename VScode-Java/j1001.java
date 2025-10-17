import java.util.*;

public class j1001 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        if(a <= 0 || b <= 0){
            System.out.println(0);
            return;
        }else{
            System.out.print((a + b) * 2);
            System.out.println(" " + (a * b));
        }
    }
}

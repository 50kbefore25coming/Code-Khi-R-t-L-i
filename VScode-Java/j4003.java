import java.util.Scanner;

public class j4003 {
    static class PhanSo {
        private long tu;
        private long mau;

        public PhanSo (long tu, long mau) {
            this.tu = tu;
            this.mau = mau;
        }

        private static long gcd(long a, long b) {
            a = Math.abs(a);
            b = Math.abs(b);
            
            while (b != 0) {
                long temp = a % b;
                a = b;
                b = temp;
            }
            return a;
        }

        public void tuSo() {
            long ucln = gcd(this.tu, this.mau);
            this.tu /= ucln;
            this.mau /= ucln;

            System.out.println(this.tu + "/" + this.mau);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        long a = sc.nextLong();
        long b = sc.nextLong();

        PhanSo so = new PhanSo(a, b);
        so.tuSo();
    }
}

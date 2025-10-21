import java.util.Scanner;

public class j4004 {
    static class PhanSo {
        private long tu;
        private long mau;

        private static long gcd(long a, long b) {
            while (b != 0) {
                long temp = a % b;
                a = b;
                b = temp;
            }
            return a;
        }

        public PhanSo(long tu, long mau) {
            long ucln = gcd(tu, mau);
            this.tu = tu / ucln;
            this.mau = mau / ucln;
        }

        public PhanSo cong(PhanSo p2) {
            long newTu = (this.tu * p2.mau) + (p2.tu * this.mau);
            long newMau = this.mau * p2.mau;
            return new PhanSo(newTu, newMau);
        }

        @Override
        public String toString() {
            return this.tu + "/" + this.mau;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int d = sc.nextInt();

        PhanSo p = new PhanSo(a, b);
        PhanSo q = new PhanSo(c, d);

        PhanSo tong = p.cong(q);

        System.out.println(tong);
    }
}
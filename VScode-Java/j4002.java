import java.util.Scanner;

public class j4002 {
    static class Rectange{
        private double rong;
        private double dai;
        private String mau;
        
        public Rectange(double dai, double rong, String mau){
            this.rong = rong;
            this.dai = dai;
            this.mau = mau;
        }
        public String getMau(){
            return mau;
        }

        public double dientich(){
            double dt = this.dai * this.rong;
            return dt;
        }

        public double chuvi(){
            double cv = (this.dai + this.rong) * 2;
            return cv;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double dai = sc.nextDouble();
        double rong = sc.nextDouble();
        String mau = sc.next();

        if(dai <= 0 || rong <= 0){
            System.out.println("INVALID");
        }else{
            String ChinhMau = mau.substring(0, 1).toUpperCase() + mau.substring(1).toLowerCase();
            Rectange hcn = new Rectange(dai, rong, ChinhMau);

            System.out.printf("%.0f %.0f %s\n", hcn.chuvi(), hcn.dientich(), hcn.getMau());
        }
    }
}
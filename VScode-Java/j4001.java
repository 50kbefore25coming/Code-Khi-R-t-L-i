import java.util.Scanner;

public class j4001 {
    static class point {
        private double x;
        private double y;

        public point(double x, double y){
            this.x = x;
            this.y = y;
        }

        public double distance(point secondPoint){
            double dx = this.x - secondPoint.x;
            double dy = this.y - secondPoint.y;
            return Math.sqrt(dx * dx + dy * dy);
        }
        public double distance(point p1, point p2){
            double dx = p1.x - p2.x;
            double dy = p1.y - p2.y;
            return Math.sqrt(dx * dx + dy * dy);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n-- > 0){
            double x1 = sc.nextDouble();
            double y1 = sc.nextDouble();
            double x2 = sc.nextDouble();
            double y2 = sc.nextDouble();

            point p1 = new point(x1, y1);
            point p2 = new point(x2, y2);

            System.out.printf("%.4f", p1.distance(p2));
            System.out.println();
        }
    }
}

import java.util.Scanner;

public class Primo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("los números primos que hay entre 1 hasta N");
        System.out.print("Ingrese el valor de N : ");
        int n = sc.nextInt();
        System.out.println("Los numeros primos del " + n + " son:");
        while (n > 1) {
            int primo = 1;
            for (int i = 2; i < n - 1; i++) {
                if (n % i == 0) {
                    primo += 1;
                }
            }
            if (primo == 1) {
                System.out.println(n);
            }
            n -= 1;
        }
    }
}

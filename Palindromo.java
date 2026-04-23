import java.util.Scanner;

public class Palindromo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Verificador de palindromos");
        System.out.println("Escribe una palabra: ");
        String palabra = sc.nextLine();
        String invertida = "";
        for (int i = palabra.length() - 1; i >= 0; i--) {
            invertida += palabra.charAt(i);
        }
        if (palabra.equals(invertida)) {
            System.out.println("La palabra " + palabra + " es un palindromo");
        } else {
            System.out.println("La palabra " + palabra + " no es un palindromo");
        }
    }
}

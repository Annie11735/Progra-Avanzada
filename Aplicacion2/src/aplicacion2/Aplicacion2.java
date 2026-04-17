package aplicacion2;
import java.util.Scanner;

public class Aplicacion2 {

    public static void main(String[] args) 
    {
        Scanner lector=new Scanner(System.in);
        System.out.println("Ingresa la base: ");
        double base=lector.nextDouble();
        System.out.println("Ingresa tu altura: ");
        double altura=lector.nextDouble();
        lector.close();
        double area = (base*altura)/2;
        
        System.out.println("El triangulo con base " +base+ " y altura "+altura+ " tiene area de "+ area);
        System.out.printf("El triangulo con base %.2f y altura %.2f tiene area de: %.2f \n",base,altura,area);
        System.out.println("El area del triangulo es: " + area);
    }
    
}

package aplicacion3;
import java.util.Scanner;

public class Aplicacion3 {

    public static void main(String[] args) 
    {
        Scanner lector=new Scanner(System.in);
        
        System.out.println("Ingresa tu altura: ");
        double altura=lector.nextDouble();
        lector.nextLine();
        System.out.println("Ingresa tu nombre: ");
        String nombre=lector.nextLine();
        
        System.out.println("Ingresa tu edad: ");
        int edad=lector.nextInt();
        lector.close();
        System.out.println("Tu nombre es: "+nombre+" mides "+altura+" y tienes "+edad+" años ");
        if (edad>=18){
            System.out.println("Eres mayor de edad.");
        }
        else{
            System.out.println("Eres menor de edad.");
        }
    }
    
}

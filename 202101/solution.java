import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class solution {

    public static void main(String[] args)  {
        try{
            File input =  new File("input.txt");
            Scanner scanner = new Scanner(input);
            int last = Integer.parseInt(scanner.nextLine());
            int counter = 0;
            while(scanner.hasNextLine()){
                int current = Integer.parseInt(scanner.nextLine());
                if(current > last)
                    counter++;
                last = current;
            }
            System.out.println(counter);
        }
        catch (FileNotFoundException e){
            System.out.println("POGCHAMP");
        }
    }
}

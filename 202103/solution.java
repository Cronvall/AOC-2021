import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class solution {

    public static void main(String[] args){
        solution1();
    }

    static void solution1(){

        int counter[] = new int[12];
        try{
            File input = new File("input.txt");
            Scanner reader = new Scanner(input);

            ArrayList<String> rows = new ArrayList<>();
            while (reader.hasNextLine())
                rows.add(reader.nextLine());

            for(int j = 0; j < rows.size(); j++){
                char[] row = rows.get(j).toCharArray();

                for(int i = 0; i < row.length; i++){
                    if(row[i] == '1')
                        counter[i] += 1;
                    else counter[i] -= 1;
                }
            }
            System.out.println(Arrays.toString(counter));

            String gResult = "";
            String eResult = "";
            for(int i = 0; i < counter.length; i++){
                if(counter[i] > 0){
                    gResult += '1';
                    eResult += '0';
                }
                else {
                    gResult += '0';
                    eResult += '1';
                }
            }
            int ganswer = Integer.parseInt(gResult,2);
            int eanswer = Integer.parseInt(eResult,2);
            System.out.println(ganswer * eanswer);
        }
        catch (FileNotFoundException e){
            System.out.println("POG");
        }
    }

}

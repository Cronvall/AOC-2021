using System;

public class solution
{
    static void Main(string[] args){
	string[] lines = System.IO.File.ReadAllLines("input.txt");
	Console.WriteLine(Solution1(lines));
}  
    static int Solution1(string[] lines){
	int counter = 0;
	int last  = int.Parse(lines[0]);
	foreach(string line in lines){
	   int a = int.Parse(line);
	   if(a > last)
		counter++;
	   last = a;		
	}
	return counter;
}
}

using  System;

class sol{


public static void Main(string[] args){
	Console.WriteLine(solution());
}

static int solution(){
	string[] commands = System.IO.File.ReadAllLines("input.txt");
	int x = 0;
	int y = 0;
	for(int i = 0; i < commands.Length; i++){
		string[] curr_com = commands[i].Split(' ');
		
		if(curr_com[0] == "forward")
			x += int.Parse(curr_com[1]);
			
		else if(curr_com[0] == "up")
			y -= int.Parse(curr_com[1]);
		else if(curr_com[0] == "down")
			y += int.Parse(curr_com[1]);
	}
	return x * y;
}
}

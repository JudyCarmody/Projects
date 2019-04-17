import java.util.Random;
import java.util.Scanner;

public class DieRoller{
	Scanner input = new Scanner(System.in);
	int numDie = 0, numSides = 0;
	
	// get the number of dice and the sides of the dice (example: 2 dice with 6 sides)
	private void getDie(){
		System.out.println("Enter number of dice: ");
		numDie = input.nextInt();
		
		System.out.println("Enter number of sides on the dice: ");
		numSides = input.nextInt();
		System.out.println();
		
		roll(numDie,numSides);
	}
	
	private void roll(int numDie, int dieSides){
		Random rand = new Random();
		int rolled = 0;
		
		if(numDie == 1){System.out.println("D" + dieSides + ": ");}
		else{System.out.println(numDie + "D" + dieSides + ": ");}
		
		// loop for simulating a die roll
		// a die is rolled and a number is randomly generated based on the number
		//	of sides.
		for(int i=1; i<=numDie; i++){	// roll each die
			rolled = rand.nextInt(dieSides); // RNG based on the number of sides for one die
			if( rolled == 0){rolled++;} // accounting for 0
			System.out.println(rolled);
		}
	}
	
	// main method //
	public static void main(String[] args){
		DieRoller rollDie = new DieRoller();
		rollDie.getDie();
	}
}

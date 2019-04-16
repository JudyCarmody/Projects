/* 	takes a word and formats it in Pig Latin
	examples:
		apple = ppleay
		banana = ananabay
		tree = reetay
*/

import java.util.*;

public class PigLatin{
	public static void main(String[] args){
		PigLatin generate = new PigLatin();
		System.out.println(generate.pigLatinGen());
	}
	
	private String pigLatinGen(){
		StringBuilder pigLatinText = new StringBuilder();
		String pigLatinStr = "";
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a word: ");
		String originalText = input.nextLine();
		
		// puts input into character array
		char[] origTextArr = originalText.toCharArray();
		
		// iterate through the character array, beginning with index 1
		for(int i=1; i<origTextArr.length; i++){
			// put the letters into a String
			pigLatinText.append(origTextArr[i]);
		}
		
		// concatenate the text generated in the for loop
		// with index 0 of character array and String "ay"
		pigLatinStr = pigLatinText.toString() + origTextArr[0] + "ay";
		
		// return the String
		return pigLatinStr;
	}
}
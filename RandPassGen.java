/*
	Generates a random password, then saves it to a text file.
*/

import java.util.*;
import java.io.*;

public class RandPassGen{
	public static void main(String[] args){
		int length = 10;
		System.out.println(password(length));
		System.out.println("Password saved to passGen.txt");
	}
	
	static char[] password(int length){
		System.out.print("Generated Password: ");
		
		// characters being used to generate password. No number zero or letter O.
		String capital_char = "ABCDEFGHIJKLMNPQRSTUVWXYZ";
		String lower_char = "abcdefghijklmnpqrstuvwxyz";
		String numbers = "123456789";
		String symbols ="!@#$%^&*_=+-/.?<>";
		
		String values = capital_char + lower_char + numbers + symbols;
		
		// generates random password
		Random randPass = new Random();
		char[] passwordArr = new char[length];
		for(int i =0; i<length; i++){
			passwordArr[i] = values.charAt(randPass.nextInt(values.length()));
		}
		
		// convert char[] to String
		String passStr = String.valueOf(passwordArr);
		
		// write generated password to a file.
		try(PrintWriter outputStream = new PrintWriter(new FileOutputStream("passGen.txt"))){
			outputStream.write(passStr);
			outputStream.close();
		}
		
		catch(IOException e){System.out.println("Error.");}
		return passwordArr;
	}
}
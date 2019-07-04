/* 
	Just for giggles.
	Googol displays correctly,
	but the Googol Plex is displayed as infinity
*/

import java.lang.Math;	// to use Math.pow, must use the double data type in order to use Math.pow

public class GoogolPlex{
	public static void main(String[] args){
		double i=10, j=100, googol=Math.pow(i,j);	// googol is already calculated (10^100)
		System.out.println("Googol:\n" + googol + "\n");	// make sure googol is correctly calculated
		System.out.println("Googol Plex:\n" + Math.pow(i,googol));	// 10^googol, displays as infinity
	}
}
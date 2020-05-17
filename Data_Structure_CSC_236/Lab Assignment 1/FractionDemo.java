//----------------------------------------------------------------------
// Asks the user to enter file name
//----------------------------------------------------------------------

import java.util.*;
import java.io.*;
import javax.swing.*;

public class FractionDemo
{
public static void main(String [] args)throws IOException, DenominatorZero
{

File file;
Scanner inputFile;
String fileName;

//intialize fraction array of size 20
Fraction[] f = new Fraction[20];

int i = 0, inputMismatchCOUNTER = 0, zeroDenominator = 0;  //set the conter as zero


//ask user to input the file name
fileName = JOptionPane.showInputDialog("Please enter the .txt extension after the File Name. For example: Input.txt \n" +
												 "Enter the name of a file:");

//create the output file
PrintWriter outputFile = new PrintWriter("Fraction_output.txt");

outputFile.println("\nFractions created in lowest terms:");

	try
	{
			//open the file
			file = new File(fileName);
			inputFile = new Scanner(file);
			JOptionPane.showMessageDialog(null,"The file was found. The output file has been created as name of: Fraction_output.txt." +
												"\nPlease check your folder(where your java program is) for the output file.");

		//read the file's contents
		while(inputFile.hasNext())
		{

			try
			{
				int Numerator = inputFile.nextInt();
					try
					{
						int Denominator = inputFile.nextInt();
						check(Denominator);
						f[i] = new Fraction(Numerator,Denominator);

						//to display all the elements of Fractor array
						outputFile.println(f[i].toString());
						i++;
						}
					catch(DenominatorZero e)
						{
						inputFile.nextLine();
						zeroDenominator++;
						}


			}
			catch(InputMismatchException e)
			{
				inputFile.nextLine();
				inputMismatchCOUNTER++;
			}

		}//end of while
				inputFile.close();
	}//end of fist try block
	catch(FileNotFoundException e)
	{
		JOptionPane.showMessageDialog(null,e.getMessage());
	}
outputFile.println();

outputFile.println("Add Demo:");
outputFile.println("The result of " + f[0] +" + " + f[1] + " is " + f[0].add(f[1]));
outputFile.println();

outputFile.println("Subtract Demo:");
outputFile.println("The result of " + f[2] +" - " + f[3] + " is " + f[2].subtract(f[3]));
outputFile.println();

outputFile.println("Divide Demo:");
outputFile.println("The result of " + f[4] +" / " + f[5] + " is " + f[4].divide(f[5]));
outputFile.println();

outputFile.println("Multiply Demo:");
outputFile.println("The result of " + f[6] +" * " + f[7] + " is " + f[6].multiply(f[7]));
outputFile.println();

outputFile.println("Equality Demo:");
outputFile.println("Fraction " + f[8] + displayEquality(f[8].equals(f[9])) + " Fraction " +f[7]);
outputFile.println();

outputFile.println("Fraction " + f[1] + displayEquality(f[1].equals(f[10])) + " Fraction " +f[10]);
outputFile.println();

outputFile.println("Compare Demo:");
outputFile.println("Fraction " + f[2] + displayCompare(f[2].compareTo(f[4])) + " Fraction " +f[4]);
outputFile.println();

outputFile.println("Reciprocal Demo:");
outputFile.println("The reciprocal of Fraction " + f[4] + " is "+ f[4].getReciprocal());

outputFile.println();
outputFile.println("There were " + inputMismatchCOUNTER + " lines skipped due to an input mismatch exception.");

outputFile.println("There were " + zeroDenominator + " lines skipped due to an denominator exception.");

outputFile.close();

}//end of main


/**
This method determines the denominator that is is zero or not
	@param Num The integer Denominator
*/
public static void check(int Num)throws DenominatorZero
{
	if(Num ==0)
	throw new DenominatorZero();
}

/**
The displayCompare method display fraction is larger, smaller or equal
	@param Num The integer number
	@return The information about fraction is greater, less, or equal
*/
public static String displayCompare(int Num)
{
	String s;
	if(Num > 0)
	s= " is greater than";
	else if(Num < 0)
	s= " is less than";
	else
	s= " is equal to";

	return s;
}


/**
The displayEquality method display fraction is equal or not
	@param Status The boolean value true or false
	@return The information about two fraction is equal or not
*/
public static String displayEquality(boolean status)
{
	String s;
	if(status == true)
	s= " is equal to";
	else
	s= " is not equal to";

	return s;
}
}//end of class
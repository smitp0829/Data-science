import java.util.*;
import java.io.*;
import javax.swing.*;

public class CheckMain
{
public static void main(String [] args)throws IOException
{
File file;
Scanner inputFile;
String fileName;

//create the HTMLChecker object
HTMLChecker check = new HTMLChecker();

//ask user to input the file name
fileName = JOptionPane.showInputDialog("Please enter the .html extension after the File Name. For example: Input.html \n" +
												 "Enter the name of a file:");

	try
	{
		//open the file
		file = new File(fileName);
		inputFile = new Scanner(file);
		//ok is for identify that the file is valid or not
		boolean ok;

		ok = check.Check(inputFile);
		if(ok)
			System.out.println("html file is valid");
		else
			System.out.println("html file is not valid");

		JOptionPane.showMessageDialog(null,"The file is found.");
		inputFile.close();
 	}
 	catch(FileNotFoundException e)
 	{
 		JOptionPane.showMessageDialog(null,e.getMessage());
	}
}//end of main
}//end of class
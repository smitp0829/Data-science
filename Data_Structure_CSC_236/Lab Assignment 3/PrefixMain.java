import java.util.*;
import java.io.*;
import javax.swing.*;

public class PrefixMain
{
public static void main(String [] args)throws IOException
{
	File file;
	Scanner inputFile;
	String fileName;
	boolean ok;


	//ask user to input the file name
	fileName = JOptionPane.showInputDialog("Please enter the .txt extension after the File Name. For example: Input.html \n" +
												 "Enter the name of a file:");

	//create the output file
	PrintWriter outputFile = new PrintWriter("prefix_output.txt");

	try
		{
		//open the file
		file = new File(fileName);
		inputFile = new Scanner(file);


			//read the file's contents
			while(inputFile.hasNext())
			{
				String line = inputFile.nextLine();
				//make the scanner object with passing string in to parameter
				Scanner tokenForValidate = new Scanner(line);

				outputFile.printf("The prefix expression "+line);
			if(PrefixProcess.validate(tokenForValidate,1))     //call the prefixProcess class validate method to validate prefix expression
				{
				Scanner tokenForEvaluate = new Scanner(line);

				//Call the PrefixProcess class evaluate method to get result of prefix expression
				outputFile.printf(" = %.2f\r\n\r\n",PrefixProcess.evaluate(tokenForEvaluate));
				}
			else
				{
				outputFile.printf(" is not valid\r\n\r\n");
				}

			}

			JOptionPane.showMessageDialog(null,"The file is found. The output file has been created as name of: prefix_output" +
												"\nPlease check your folder(where your java program is) for the output file.");

			inputFile.close();
		 }
	catch(FileNotFoundException e)
		 {
		 JOptionPane.showMessageDialog(null,e.getMessage());
		}

outputFile.close();
}//end of main
}//end of class
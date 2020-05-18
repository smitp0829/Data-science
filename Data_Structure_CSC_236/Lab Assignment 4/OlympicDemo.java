import java.io.*;
import java.util.*;
import javax.swing.*;

public class OlympicDemo
{
public static void main(String [] args)throws InterruptedException
{
boolean done = false;

//Create Scanner object
Scanner keyboard = new Scanner(System.in);

//Create OlympicAthletes object
OlympicAthletes athletes = new OlympicAthletes();

//call the getData method
getData(athletes);

do
{
System.out.println();
System.out.println("1: Add an athlete");
System.out.println("2: Delete an athlete");
System.out.println("3: Print all athletes");
System.out.println("4: Print an athlete");
System.out.println("5: Print an event");
System.out.println("6: Print medal winners by country");
System.out.println("7: Print medal winners by event");
System.out.println("8: Print medal winners by medal");
System.out.println("9: Print athletes by alpabetical order(last name,frist name)");
System.out.println("10: Print athletes by alpabetical order(event)");
System.out.println("11: Exit");



		System.out.println("Selection ==>");
		int choice = keyboard.nextInt();
		keyboard.nextLine();

	switch(choice)
	{
		case 1:
			athletes.addAthlete(keyboard);
			break;
		case 2:
			athletes.delete(keyboard);
			break;
		case 3:
			athletes.display();
			break;
		case 4:
			athletes.particularAthlete(keyboard);
			break;
		case 5:
			athletes.particularEvent(keyboard);
			break;
		case 6:
			athletes.countryWon(keyboard);
			break;
		case 7:
			athletes.eventWon(keyboard);
			break;
		case 8:
			athletes.won(keyboard);
			break;
		case 9:
			athletes.alphabetical();
			break;
		case 10:
			athletes.alphabeticalEvent();
			break;
		case 11:
			done = true;
	 		break;
		}
	}while(!done);


}//end of main

/**
This method gets the data from given input file
@param athletes The OlympicAthletes object
*/
public static void getData(OlympicAthletes athletes)
{
File file;
Scanner inputFile;
String fileName;
//ask user to input the file name
fileName = JOptionPane.showInputDialog("Please enter the .txt extension after the File Name. For example: Input.txt \n" +
												 "Enter the name of a file:");

	try
		{
		//open the file
		file = new File(fileName);
		inputFile = new Scanner(file);
		JOptionPane.showMessageDialog(null,"The file was found.");

		    String fname, lname, country, sport, event;
		    int result;

		   while (inputFile.hasNext())
		   {

		      fname = inputFile.nextLine();
		      lname = inputFile.nextLine();
		      country = inputFile.nextLine();
		      sport = inputFile.nextLine();
		      event = inputFile.nextLine();
		      result = inputFile.nextInt();
			  inputFile.nextLine();
			  //call the OlympicAtheles call add method
		      athletes.add(fname, lname, country, sport, event, result);
	    	}

		inputFile.close();
		}
	    catch(FileNotFoundException e)
		{
				JOptionPane.showMessageDialog(null,e.getMessage());
		}
}
}//end of class
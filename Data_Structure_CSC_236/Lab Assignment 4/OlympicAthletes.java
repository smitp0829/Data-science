import java.io.*;
import java.util.*;


public class OlympicAthletes extends Athlete
{
// Instantiate sorted list
private ListInterface<Athlete> OlympicAthletes;

/**
no argument Constructor
*/
public OlympicAthletes()
{
 this.OlympicAthletes = new SortedABList<Athlete>();
}

/**
This method adds Athlete object in Sorted array based list
@param first The athlete's fist name
@param last The athlete's last name
@param country The athlete's country
@param sport The athlete's sport
@param event The athlete's event
@param result The athlete's result
*/
public void add(String first, String last, String country, String sport,String event,int result)
{
OlympicAthletes.add(new Athlete(first,last,country,sport,event,result));
}

/**
This method deteles Athlete object form the list if the traget object is equals
@param target The Athlete object
*/
private void deleteFromList(Athlete target)
{
	boolean remove = false;
	//create Iterator object
	Iterator<Athlete> iter = OlympicAthletes.iterator();
		while(iter.hasNext())
		{
		Athlete hold = iter.next();
			if(hold.equals(target))
			{
				remove = true;
				iter.remove();
			}
		}

	if(remove)
	System.out.println("You have successfully delete an athlete.");
	else
	System.out.println("Entered Athlete is not in the list.");
}

/**
This method prints list's all objects
*/
public void display() throws InterruptedException
{
System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
	Iterator<Athlete> iter = OlympicAthletes.iterator();
	while(iter.hasNext())
	{
		Athlete hold1 = iter.next();
		Thread.sleep(500);
		System.out.println(hold1);
	}
}

/**
This method adds an athlete to list
@param Kbd The Scanner object
*/
public void addAthlete(Scanner Kbd)
{
	System.out.printf("Enter FirstName: ");
	String fName = Kbd.nextLine();
	System.out.printf("Enter LastName: ");
	String lName = Kbd.nextLine();
	System.out.printf("Enter County: ");
	String country = Kbd.nextLine();
	System.out.printf("Enter Sport: ");
	String sport = Kbd.nextLine();
	System.out.printf("Enter Event: ");
	String event = Kbd.nextLine();
	System.out.printf("Enter Result: ");
	int result = Kbd.nextInt();
	add(fName,lName,country,sport,event,result);
	System.out.println("You have successfully add an athlete.");
}

/*
This method deletes all the entries of an athletes
@param Kbd The Scanner object
*/
public void delete(Scanner Kbd)
{
	System.out.printf("Enter FirstName: ");
	String fName = Kbd.nextLine();
	System.out.printf("Enter LastName: ");
	String lName = Kbd.nextLine();
	System.out.printf("Enter County: ");
	String country = Kbd.nextLine();

	deleteFromList(new Athlete(fName,lName,country,"","",0));

}

/**
This method displays an Athletes all the entries
@param Kbd The Scanner object
*/
public void particularAthlete(Scanner Kbd)throws InterruptedException
{
	System.out.printf("Enter FirstName: ");
	String fName = Kbd.nextLine();
	System.out.printf("Enter LastName: ");
	String lName = Kbd.nextLine();
	System.out.printf("Enter County: ");
	String country = Kbd.nextLine();

System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
	Iterator<Athlete> iter = OlympicAthletes.iterator();
	while(iter.hasNext())
		{
		Athlete hold = iter.next();
		if(hold.equals(new Athlete(fName,lName,country,"","",0)))
			{
			Thread.sleep(500);
			System.out.println(hold);
			}
		}


}

/**
This method displays the praticular event's athletes
@param Kbd The Scanner object
*/
public void particularEvent(Scanner Kbd)throws InterruptedException
{
	System.out.printf("Enter Sport: ");
	String sportName = Kbd.nextLine();
	System.out.printf("Enter Event: ");
	String eventName = Kbd.nextLine();

System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
		Iterator<Athlete> iter = OlympicAthletes.iterator();
			while(iter.hasNext())
			{
				Athlete hold = iter.next();
				if(hold.getSport(sportName) && hold.getEvent(eventName))
				{
					Thread.sleep(500);
					System.out.println(hold);
				}
			}

}

/**
This method displays all the country winners athletes
@param Kbd The Scanner object
*/
public void countryWon(Scanner Kbd)throws InterruptedException
{
	System.out.printf("Enter Country: ");
	String country = Kbd.nextLine();

System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
	Iterator<Athlete> iter = OlympicAthletes.iterator();
			while(iter.hasNext())
			{
				Athlete hold = iter.next();
				if(hold.getCountry(country)&& hold.getMedal())
				{
					Thread.sleep(500);
					System.out.println(hold);
				}
			}

}

/**
This method displays all the event winner athletes
@param Kbd The Scanner object
*/
public void eventWon(Scanner Kbd)throws InterruptedException
{
	System.out.printf("Enter Sport: ");
	String sportName = Kbd.nextLine();
	System.out.printf("Enter Event: ");
	String eventName = Kbd.nextLine();

System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
		Iterator<Athlete> iter = OlympicAthletes.iterator();
			while(iter.hasNext())
			{
				Athlete hold = iter.next();
				if(hold.getSport(sportName) && hold.getEvent(eventName)&& hold.getMedal())
				{
					Thread.sleep(500);
					System.out.println(hold);
				}
			}

}

/**
This method displays all the winner in the olympic
@param Kbd The Scanner object
*/
public void won(Scanner Kbd)throws InterruptedException
{
	System.out.printf("Enter Medal: ");
	String medalName = Kbd.nextLine();


System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
		Iterator<Athlete> iter = OlympicAthletes.iterator();
			while(iter.hasNext())
			{
				Athlete hold = iter.next();
				if(hold.getByMedal(medalName))
				{
					Thread.sleep(500);
					System.out.println(hold);
				}
			}

}

/**
This method displays all the athlets in last name, first name order
*/
public void alphabetical()throws InterruptedException
{
//create an temp list to store athletes object in last name, first name order
ListInterface<Athlete> temp = new SortedABList<Athlete>(Athlete.alphabeticalComparator());

	Iterator<Athlete> iter = OlympicAthletes.iterator();
	while(iter.hasNext())
	{
		Athlete hold = iter.next();
		temp.add(hold);
	}

System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
	Iterator<Athlete> it = temp.iterator();
	while(it.hasNext())
		{
			Athlete hold = it.next();
			Thread.sleep(500);
			System.out.println(hold);
		}

}

/**
This method displays all the athletes object in event order
*/
public void alphabeticalEvent()throws InterruptedException
{
ListInterface<Athlete> temp = new SortedABList<Athlete>(Athlete.alphabeticalEventComparator());

	Iterator<Athlete> iter = OlympicAthletes.iterator();
	while(iter.hasNext())
	{
		Athlete hold = iter.next();
		temp.add(hold);
	}


System.out.printf("\n%-15s %-15s %-20s %-20s %-40s %-5s", "FristName","LastName","Country","Sport","Event","Result");
System.out.println("\n--------------------------------------------------------------------------------------------------------------------------");
	Iterator<Athlete> it = temp.iterator();
		while(it.hasNext())
			{
				Athlete hold = it.next();
				Thread.sleep(500);
				System.out.println(hold);
			}

}

}//end of class
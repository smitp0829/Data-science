import java.util.*;

public class Athlete implements Comparable<Athlete>
{
private String first;   		  // first name
private String last;    		  // last name
private String country;  	      //country
private String sport;	          // sports
private String event;             //events
private int result;               //result

/**
no- argumnet constructor
*/
 public Athlete()
    {

  }

/**
constructor
@param first The athlete's fist name
@param last The athlete's last name
@param country The athlete's country
@param sport The athlete's sport
@param event The athlete's event
@param result The athlete's result
*/
public Athlete(String first, String last, String country, String sport,String event,int result)
    {
        this.first   = first;		// first name
        this.last    = last;		// last name
        this.country    = country;	//country
        this.sport = sport;			// sports
        this.event = event;			//events
        this.result = result;		//result

    }

/**
This method compare to athelte object and if county and fistName and lastName are same then return true
@param b The Athelete object
@return true/false
*/
	 public boolean equals(Athlete b)
	 {
	       return ((this.country.equals(b.country)) && (this.first.equals(b.first)) && (this.last.equals(b.last)));
	   }

/**
This method compare to Athlete object
@param The Athlete object
@return -1/0/1
*/
	 public int compareTo(Athlete b)
	     {
		if (!this.country.equals(b.country))
	      return this.country.compareTo(b.country);
	   else if(!this.last.equals(b.last))
	      return this.last.compareTo(b.last);
	      else
	       return this.first.compareTo(b.first);
   		}

@Override
/**
This method represent athlete object in specific format
@return The string which contains the infomation of Athlete
*/
	    public String toString()
	    {
			String display;
			if(result == 1)
			display = String.format("%-15s %-15s %-20s %-20s %-40s %-5s", first,last, country,sport,event,"Gold");
			else if(result == 2)
			display = String.format("%-15s %-15s %-20s %-20s %-40s %-5s", first,last, country,sport,event,"Silver");
			else if(result == 3)
			display = String.format("%-15s %-15s %-20s %-20s %-40s %-5s", first,last, country,sport,event,"Bronze");
			else
			display = String.format("%-15s %-15s %-20s %-20s %-40s %-5d", first,last, country,sport,event,result);
	        return display;
    	}

/**
This method compare object country with given user country
@param country The name of country
@return true/false
*/
	public boolean getCountry(String country)
	{
		if(this.country.equals(country))
		return true;
		else
		return false;
	}

/**
This method compare object event with given user event
@param event The name of event
@return true/false
*/
	public boolean getEvent(String event)
	{
		if(this.event.equals(event))
		return true;
		else
		return false;
	}


/**
This method compare object sport with given user sport
@param sport The name of sport
@return true/false
*/
	public boolean getSport(String sport)
	{
		if(this.sport.equals(sport))
		return true;
		else
		return false;
	}

/**
This method returns true if object result is 1 or 2 or 3
@return true/false
*/
	public boolean getMedal()
	{
	if(this.result == 1 || this.result == 2 || this.result == 3)
	return true;
	else
	return false;
	}

/**
This method compare object medal with given user medal
@param medal The name of the medal
@return true/false
*/
	public boolean getByMedal(String medal)
	{
		if(medal.equalsIgnoreCase("Gold"))
		{
			if(this.result == 1)
			return true;
			else
			return false;
	}

	else if(medal.equalsIgnoreCase("Silver"))
		{
			if(this.result == 2)
			return true;
			else
			return false;
	}

	else if(medal.equalsIgnoreCase("Bronze"))
		{
			if(this.result == 3)
			return true;
			else
			return false;
		}
		else
		return false;

	}

/**
This method will comopare to Athlete object based on last name and first name
@return positive/negative/zero
*/
	 public static Comparator<Athlete> alphabeticalComparator()
	   {
     return new Comparator<Athlete>()
     {
        public int compare(Athlete element1, Athlete element2)
        {
          if(!element1.last.equals(element2.last))
		  	 return element1.last.compareTo(element2.last);
		  else
	       return element1.first.compareTo(element2.first);
        }
     };
	  }

/**
This method will comopare to Athlete object based on event
@return positive/negative/zero
*/
	public static Comparator<Athlete> alphabeticalEventComparator()
 	  {
     return new Comparator<Athlete>()
     {
        public int compare(Athlete element1, Athlete element2)
        {
	       return element1.event.compareTo(element2.event);
        }
     };
 	 }



}//end of class
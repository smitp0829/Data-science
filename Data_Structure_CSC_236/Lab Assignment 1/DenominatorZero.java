/**
DenominatorZero exceptions are thrown by the Fraction class when a zero(0) is passed to the constructor.
*/
public class DenominatorZero extends Exception
{

/**
This constructor uses a generic error message.
*/
public DenominatorZero()
{
	super();
}

/**
This constructor specifies the bad denominator in the error messsage.
@param The bad denominator.
*/
public DenominatorZero(int num)
{
	super("Error: Denominator is: " + num);
}
}//end of class
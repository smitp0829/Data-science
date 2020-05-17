import java.util.*;
import java.io.*;

/**
This class will implements the FractionInterface.
Also, this class do fraction additon, subtraction, multiplication, division, give reciprocal of fraction, compare to fracrion, and
determines the two fraction are equals or not.
*/
public class Fraction implements FractionInterface
{

//class fields which hold the numerator and denominator of fraction
private int Numerator, Denominator;

/**
No-argument constructor
*/
public Fraction()
{
	Numerator = 0;
	Denominator = 1;        //denominator sets to one because denominator can not be zero
}

/**
Constructor
	@param N The fraction's numerator
	@param D The fraction's denominator
*/
public Fraction(int N, int D)
{
	Numerator = N;
	Denominator = D;

	//pass Numerator and Denominator to GCD method to get the fraction in lowest term
	GCD(Numerator,Denominator);
}


/** Sets this fraction to a given value.
		 @param newNumerator	The integer numerator.
		 @param newDenominator  The integer denominator.
 */
public void setFraction(int newNumerator, int newDenominator)
{
	Numerator = newNumerator;
	Denominator = newDenominator;

	//pass Numerator and Denominator to GCD method to get the fraction in lowest term
	GCD(Numerator,Denominator);
}


/**
getNumerator method
	@return The fraction's numerator
*/
public int getNumerator()
{
	return Numerator;
}


/**
getDenominator
	@return The fraction's denominator
*/
public int getDenominator()
{
	return Denominator;
}


/**
 This fraction adds to a given fraction without changing either one.
		 @param operand  A fraction that is the second operand of the addition.
		 @return  The sum of the two fractions.
*/
public Fraction add(Fraction operand)
{
Fraction add = new Fraction();

	  add.Numerator = this.Numerator * operand.Denominator + this.Denominator * operand.Numerator;
      add.Denominator = this.Denominator * operand.Denominator;

	 //pass add object's Numerator and add object's Denominator to GCD method to get the add fraction in lowest term
	  add.GCD(add.Numerator, add.Denominator);
        return add;
}

/**
Subtracts a given fraction from this fraction without changing either one.
		 @param operand  A fraction that is the second operand of the subtraction.
		 @return  The difference of the two fractions.
*/
public Fraction subtract(Fraction operand)
{
	Fraction subtract = new Fraction();

	subtract.Numerator = this.Numerator*operand.Denominator - this.Denominator * operand.Numerator;
	subtract.Denominator = this.Denominator * operand.Denominator;

	//pass subtract object's Numerator and subtract object's Denominator to GCD method to get the subtract fraction in lowest term
	subtract.GCD(subtract.Numerator, subtract.Denominator);
        return subtract;
}


/**
Multiplies this fraction by another fraction without changing either one.
		 @param operand  A fraction that is the second operand of the
						   multiplication.
		 @return  The product of the two fractions.
*/
public Fraction multiply(Fraction operand)
{
	Fraction multiplication = new Fraction();

	multiplication.Numerator = this.Numerator*operand.Numerator;
	multiplication.Denominator = this.Denominator*operand.Denominator;

	/*pass multiplication object's Numerator and multiplication object's Denominator to GCD method
						to get the multiplication fraction in lowest term*/
	multiplication.GCD(multiplication.Numerator, multiplication.Denominator);
	return multiplication;

}


/** Divides this fraction by another fraction without changing either one.
		 @param operand  A fraction that is the second operand of the division.
		 @return  The quotient of the two fractions.
*/
public Fraction divide(Fraction operand)
{
	Fraction division = new Fraction();

	division.Numerator = this.Numerator*operand.Denominator;
	division.Denominator = this.Denominator*operand.Numerator;

	//pass division object's Numerator and division object's Denominator to GCD method to get the division fraction in lowest term
	division.GCD(division.Numerator, division.Denominator);
	return division;

}


/**
Gets this fraction's reciprocal.
		 @return  The reciprocal of the fraction.
*/
public Fraction getReciprocal()
{
	Fraction Reciprocal = new Fraction();

	Reciprocal.Numerator = this.Denominator;
	Reciprocal.Denominator = this.Numerator;

	//pass Reciprocal object's Numerator and Reciprocal object's Denominator to GCD method to get the Reciprocal fraction in lowest term
	Reciprocal.GCD(Reciprocal.Numerator, Reciprocal.Denominator);
	return Reciprocal;
}



/**
Compares this fraction to another fraction to determine which one is
		larger, smaller or if they are equal, without changing either one.
		 @param other  The other fraction we are comparing to this fraction.
		 @return  An integer representing how the fractions compare.
*/
public int compareTo(Fraction other)
{
int result = this.Numerator*other.Denominator - this.Denominator* other.Numerator;

return result;
}


/**
This method find the greatest common denominator(GCD)  and divide the Numerator and Denominator by GCD
to get the lowest term fraction
	 @param Numerator	The integer numerator.
	 @param Denominator  The integer denominator.
*/
private void GCD(int Numerator, int Denominator)
{

	if(Numerator == 0)
	{
		this.Numerator = this.Numerator/Denominator;
		this.Denominator = this.Denominator/Denominator;

	}
	else if(Denominator == 0)
	{
		this.Numerator = this.Numerator/Numerator;
		this.Denominator = this.Denominator/Numerator;
	}
	else
	{
		//set the newDenominator as the mod of parameter's Numerator and Denominator
		int newDenominator = Numerator % Denominator;

		//set the newNumerator as the parameter's Denominator
		int newNumerator = Denominator;

		//call method itself (recursion) by passing the newNumerator and newDenominator as an arguments
		GCD(newNumerator,newDenominator);
	}

	/*	Find the GCD by For loop
	if(N >= D)
	largest = N;
	else
	largest = D;

	for(int i = largest ; i >= 2; i--)
	{
	if(N%i == 0 && D%i == 0)
		{
		gcd = i;
		N = N/gcd;
		D = D/gcd;
		}
	}
	Numerator = N;
	Denominator = D;
	*/

}


/**
This method determine that this fraction and other fraction are equal or not
	@param other The other fraction we are comparing to this fraction.
	@return true/false depends if equal than return true else return false
*/
public boolean equals(Fraction other)
{
        return (this.Numerator == other.Numerator) && (this.Denominator == other.Denominator);
 }

@Override
/**
This method display the fraction in sepcific foramt
	@return The string which contains the infomation of fraction.
*/
public String toString()
{
	 String str = String.format("%d/%d" , this.getNumerator() , this.getDenominator());
 	 return str;
}

}//end of class
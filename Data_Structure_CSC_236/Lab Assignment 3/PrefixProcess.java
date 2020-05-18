import java.util.*;
import java.io.*;

public class PrefixProcess
{

/**
@param token The scanner object
@param count The counter to evaluate the expression is valid or Invalid
@return if the count is 0 and the there is no more token then it return true else false
*/
public static boolean validate(Scanner token, int count)
{
	//if count get less than and token has next is true
	if(count <= 0 && token.hasNext())
	return false;

	//if count is equal to zero and there is no token left
	else if(count == 0 && !(token.hasNext()))
	return true;

	//if count is not equal to zero and there is no token left
	else if(count != 0 && !(token.hasNext()))
	return false;

	else
	{
			try
			{
			token.nextDouble();
			count--;
			}
			catch(InputMismatchException e)
			{
			String operator = token.next();
			if((operator).equals("/") || (operator).equals("*") || (operator).equals("+") || (operator).equals("-"))
			count++;
			else
			count = -1;
			}
			//call itself doing recusion call
			return validate(token,count);
		}
}//end of validator method

/**
@param token The scanner object
@return The result to prefix expression
*/
public static double evaluate(Scanner token)
{
	String operator;
	double operand1,operand2;

		try
		{
		double simpleNumber = token.nextDouble();
		return simpleNumber;
		}
		catch(InputMismatchException e)
		{
		 operator = token.next();
		if(operator.equals("/"))
		{
			//doing recusion call
			operand1 = evaluate(token);
			//doing recusion call
			operand2 = evaluate(token);
			return operand1/operand2;
		}
		else if(operator.equals("*"))
		{
			//doing recusion call
			operand1 = evaluate(token);
			//doing recusion call
			operand2 = evaluate(token);
			return operand1*operand2;
		}
		else if(operator.equals("+"))
		{
			//doing recusion call
			operand1 = evaluate(token);
			//doing recusion call
			operand2 = evaluate(token);
			return operand1+operand2;
		}
		else
		{
			//doing recusion call
			operand1 = evaluate(token);
			//doing recusion call
			operand2 = evaluate(token);
			return operand1-operand2;
		}

		}//end of catch block

}//end of evaluate method

}//end of class

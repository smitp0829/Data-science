import java.util.*;
import java.io.*;

public class HTMLChecker
{
//create stack to hold open tags
StackInterface<String> tagStack = new LinkedStack<String>();

//create arraylist to hold open tags which helps to identify that open tags are missing or not
ArrayList<String> tagStackforMissStartTag = new ArrayList<String>();


/**
This mehtod get the inputFile and determine the file is valid or not. Furthermore, it provide information
ot matched tags, missing tags, and no needed end tags.
@param inputFile The file that needs to get checked for correct nesting of tags
@return stillBalanced The status of the file (Valid/inValid)
*/
public boolean Check(Scanner inputFile)
{
	boolean stillBalanced = true;

	//to hold the open tags
	ArrayList<String> Tags = new ArrayList<String>();

	while(inputFile.hasNext())
	{
		//read line from the file
		String line = inputFile.nextLine();

		//call Tag class getTags method to get Tags from the line
		Tags = Tag.getTags(line);

			//for loop to identify the tags type(open tag or end tag) and processor on that tags
			for(int i = 0; i < Tags.size(); i++)
				{
					//create Tag object
				Tag T = new Tag(Tags.get(i));

					//for identify the tag is start tag or not
				if(T.isStart())
					{
						//store in tagStack linked stack
						tagStack.push(Tags.get(i));

						//store in tagStackforMissStartTag arraylist
						tagStackforMissStartTag.add(Tags.get(i));
					}

				//if the tag is end tag
				else if(T.isEnd() && !(T.isIgnoreTag()))
					{
							try
							{
									//Call Tag class noEndTagNeeded method and identify that tag does need end tag or not
									while(Tag.noEndTagNeeded(tagStack.top()))
									{
									System.out.println("no match needed: " + tagStack.top());
									tagStack.pop();
									tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
									}

									//compare end tag which tagStack top
									if(T.isEqual(tagStack.top()))
										{
										System.out.println("matched: " + tagStack.top() + " and " + T.toString());
										tagStack.pop();
										tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
										}//end of inner if

									//determine that if the start tag is missing or not
									else if(!T.isStartTagMissing(tagStackforMissStartTag))
										{
											System.out.println("missing start tag: "+ T);
											stillBalanced = false;  // start tag is missing so not balanced
										}
									else
										{
											//compare the end tag with tagStack top
											while(!(T.isEqual(tagStack.top())))
												{
													//if not equal than check the Tag does need end tag or not
													if(Tag.noEndTagNeeded(tagStack.top()))
														{
														System.out.println("no match needed: " + tagStack.top());
														tagStack.pop();
														tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
														}
													else
														{
														//else pop the tagStack top
														System.out.println("missing end tag: " +tagStack.top());
														tagStack.pop();
														tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
														stillBalanced = false;     // end tag is missing so not balanced
												  		}
												} //end of inner while loop
												System.out.println("matched: " + tagStack.top() + " and " + T.toString());
												tagStack.pop();
												tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);

										}//end of inner else

								}//end of try
							catch(StackUnderflowException e)   //if the tagStack is empty
								{
									stillBalanced = false;       //missing start tags so not balanced
									System.out.println("missing start tag: " + T);
								}//end of catch

					}//end of else if

				}//end of for loop
	}//end of while loop

	while(!(tagStack.isEmpty())) //if tag stack is not empty
	{

		//check tagStack top then tag needs the end tag or not
		if(Tag.noEndTagNeeded(tagStack.top()))
			{
			System.out.println("no match needed: " + tagStack.top());
			tagStack.pop();
			tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
			}
		else
			{
			System.out.println("missing end tag: " + tagStack.top());
			tagStack.pop();
			tagStackforMissStartTag.remove(tagStackforMissStartTag.size()-1);
			stillBalanced = false;     //missing end tag so not balanced
			}
	}//end of while loop

return stillBalanced;
}//end of method check

}//end of class
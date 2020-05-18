import java.util.*;
import java.io.*;

public class Tag
{

private String Tag;

//Tags that do not need end tags
private String[] noEndTagNeed = { "<area>", "<base>", "<br>", "<col>" , "<command>", "<embed>", "<hr>",
									  "<image>", "<input>", "<keygen>", "<link>", "<meta>", "<param>",
									  "<source>", "<track>", "<wbr>"};

//Tags that need to be ignore
private String[] ignoreTags = {"</area>", "</base>", "</br>", "</col>" , "</command>", "</embed>", "</hr>",
									  "</image>", "</input>", "</keygen>", "</link>", "</meta>", "</param>",
									  "</source>", "</track>", "</wbr>"};

/**
constructor
@param Tag The tag of html file
*/
public Tag(String Tag)
{
	this.Tag = Tag;
}

/**
This method accept the line as parameter and separate tags from the line and return it
@param line The string line
@return Tag The arraylist that holds the tags of the line
*/
public static ArrayList<String> getTags(String line)
{
//create Tag arraylist to hold Tags of the line
ArrayList<String> Tag = new ArrayList<String>();

char currChar = ' ';
int currCharIndex = 0;
int lastCharIndex = line.length();


while(currCharIndex < lastCharIndex)
{
	StringBuilder str = new StringBuilder();
	currChar = line.charAt(currCharIndex);

		if(currChar == '<')
		{
				//run while loop until currChar is != >  and currCharIndex  is less than line length
				while(currChar != '>' && currCharIndex < lastCharIndex)
				{
						//if currChar is equal to white Space than ignore inbetween characters until currChar is equal to >
						if(currChar == ' ')
						{
							while(currChar != '>' && currCharIndex < lastCharIndex)
							{
							currCharIndex++;
							currChar = line.charAt(currCharIndex);
							}
						}

						else
						{
							//if currCharIndex  is less than line length then attached the character again
							if(currCharIndex < lastCharIndex)
							{
							str.append(currChar);
							currCharIndex++;
							currChar = line.charAt(currCharIndex);
							}
						}
					}

					str.append(currChar);
					//conver the stringbuilder object to String and store in Tag arraylist
					Tag.add(str.toString());
		}

	currCharIndex++;
	}

return Tag;
}//end of method

/**
This method determine that tag is start tag or not
@return true if start tag else return false
*/
public boolean isStart()
{
	return (Tag.charAt(1) != '!' && Tag.charAt(1)!= '/' );
}

/**
This method determine that tag is end tag or not
@return true if end tag else return false
*/
public  boolean isEnd()
{
	return (Tag.charAt(1) =='/');
}

/**
This method determine that the tag needs the end tag or not
@return ture If the tag is in noEndTagNeed array else false
*/
public boolean noEndTagNeed()
{
	int index = 0;
	boolean found = false;
	while(!(found) && index < noEndTagNeed.length)
	{
	if(Tag.equalsIgnoreCase(noEndTagNeed[index]))
	found = true;
	index++;
	}
	return found;
}

/**
This method accept String tag and return if the Tag needs the end tag or not
@param tag The tag of html file
@return true if tag does not need end tag else false
*/
public static boolean noEndTagNeeded(String tag)
{
	boolean found = false;
	Tag T = new Tag(tag);
	if(T.noEndTagNeed())
	found = true;

	return found;
}

/**
This method determine if the tag is in ignoreTags array or not
@return true if tag found in ignoreTags array else false
*/
public boolean isIgnoreTag()
{
	int index = 0;
	boolean found = false;
	while(!(found) && index < ignoreTags.length)
	{
	if(Tag.equalsIgnoreCase(ignoreTags[index]))
	found = true;
	index++;
	}
	return found;
}

/**
This method determine that end tag(this tag) equals to start tag or not
@param Tag The html tag
@return true if they are equal else false
*/
public boolean isEqual(String Tag)
{	int i = 1;
	boolean isEqual = true;
	if((this.Tag).length()-1 != Tag.length())
	isEqual = false;

	else if(Character.toUpperCase((this.Tag).charAt(0)) == Character.toUpperCase(Tag.charAt(0)))
	{
		isEqual = true;
		while(i < Tag.length() && isEqual)
		{
			if(Character.toUpperCase((this.Tag).charAt(i+1)) != Character.toUpperCase(Tag.charAt(i)))
			isEqual = false;
			i++;
		}
	}
	return isEqual;
}

/**
This method determine that givin end tag's start tag is in the arraylist tagStackforMissStartTag or not
@param tagStackforMissStartTag The arraylist that holds the start tags
@return true if givin end tag's start tag found in arraylist else return false
*/
public boolean isStartTagMissing(ArrayList<String> tagStackforMissStartTag)
{
boolean found = false;
int i = 0;
int j = 1;
 while(i < tagStackforMissStartTag.size() && !(found))
 {

	if((this.Tag).length()-1 != (tagStackforMissStartTag.get(i)).length())
	found = false;

	  else if(Character.toUpperCase((tagStackforMissStartTag.get(i)).charAt(0)) == Character.toUpperCase((this.Tag).charAt(0)))
	 			 	{
						found = true;
						while(j < (tagStackforMissStartTag.get(i)).length() && found)
						{
							if(Character.toUpperCase((tagStackforMissStartTag.get(i)).charAt(j)) != Character.toUpperCase((this.Tag).charAt(j+1)))
							found = false;
							j++;
						}
				}

	i++;
 }

 return found;
}

@Override
/**
This method display tag
@return The string which contains the infomation of tag.
*/
public String toString()
{
	String S = this.Tag;
	return S;
}
}//end of class
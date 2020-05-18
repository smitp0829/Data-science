import java.util.*;

public class BSTDemo
{
public static void main(String [] args)
{

//Intialize the BST object
BSTInterface<Integer> tree = new BinarySearchTree<Integer>();

//Intialize Scanner object
Scanner keyboard = new Scanner(System.in);
boolean done = false;

//Intialize iterator
Iterator<Integer> iter;
int value;
do
{
System.out.println();
System.out.println("1: Add");
System.out.println("2: Remove");
System.out.println("3: Size");
System.out.println("4: Count of less than or equal to value");
System.out.println("5: Count of greater than or equal to value");
System.out.println("6: Height");
System.out.println("7: Breadth-first order traversal (Level order)");
System.out.println("8: Inorder traversal");
System.out.println("9: PreOrder traversal");
System.out.println("10: PostOrder traversal");
System.out.println("11: GetRatio");
System.out.println("12: Balance the tree");
System.out.println("13: Exit");

System.out.print("\nEntet your choice ==> ");
int choice = keyboard.nextInt();

keyboard.nextLine();
switch(choice)
{
case 1:
	value = getValue(keyboard);
	tree.add(value);

		if(tree.fRatio() <= 0.50)
		{
	 	System.out.println("The tree requires to be balance.");
		}
	break;

case 2:
	value = getValue(keyboard);
	tree.remove(value);
	if(tree.fRatio() == -1)
	System.out.println("The tree is empty");
	else
	{
		if(tree.fRatio() <= 0.50)
		{
			 System.out.println("The tree requires to be balance.");
		}
	}
	break;

case 3:
	System.out.println("The size of the tree is: " + tree.size());
	break;

case 4:
	value = getValue(keyboard);
	System.out.println("The count of all the vlaues less than or equal to " + value + " is: "+ tree.countLess(value));
	break;

case 5:
	value = getValue(keyboard);
	System.out.println("The count of all the vlaues greater than or equal to " + value + " is: "+tree.countGreater(value));
	break;

case 6:
	System.out.println("The hieght of the tree is: "+ tree.height());
	break;

case 7:
	System.out.print("Breath-first order traversal: ");
	tree.levelOrder();
	break;

case 8:
	System.out.println("Inorder  order traversal: ");
	iter = tree.getIterator(BSTInterface.Traversal.Inorder);
	while(iter.hasNext())
	System.out.printf("%d ",iter.next());
	System.out.println();
	break;

case 9:
	System.out.println("Preorder  order traversal: ");
	iter = tree.getIterator(BSTInterface.Traversal.Preorder);
	while(iter.hasNext())
	System.out.printf("%d ",iter.next());
	System.out.println();
	break;

case 10:
	System.out.println("Postorder  order traversal: ");
	iter = tree.getIterator(BSTInterface.Traversal.Postorder);
	while(iter.hasNext())
	System.out.printf("%d ",iter.next());
	System.out.println();
	break;

case 11:

	if(tree.fRatio() == -1)
	System.out.println("The tree is empty");
	else
	{
		System.out.printf("The ratio is: %.2f",tree.fRatio());
		if(tree.fRatio() <= 0.50)
		{
			System.out.println("\nThe tree requires to be balance.");
		}
	}
	break;

case 12:
	if(tree.fRatio() == -1)
	System.out.println("The tree is empty");
	else
	{
		if(tree.fRatio() <= 0.50)
		{
    		tree.balance();
      		System.out.println("You have successfully balanced the tree.");
  		}
	}
      break;

case 13:
	done = true;
	break;
}
}while(!done);


}//end of main

//This method gets the value from user
public static int getValue(Scanner Kbd)
{
	System.out.println("Enter the Value: ");
	int temp = Kbd.nextInt();

return temp;
}
}//end of class
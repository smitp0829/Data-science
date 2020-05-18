	.data
String: .asciiz "Enter the String: "
output: .asciiz "\nNumber of character in entered string is: "
output1: .asciiz "\nNumber in entered string is: "
output2: .asciiz "\nNumber of special character in entered string is: "
str: .space 22
strsize: .word 21
 	.text
 
 main:
  	li $v0, 4
	la $a0, String
	syscall
	
	li $v0,8
	la $a0, str
	lw $a1, strsize
	syscall
	
	la $s0, str
  	li $s1,0
  	
 
 loop:
 	lb $s2,0($s0)
 	beqz $s2,endloop
 	bge $s2,65,character
 	bge $s2,58,special
 	bge $s2,48,number
 	bge $s2,33,special
 	add $s1, $s1, 1
 	add $s0,$s0, 1
 	j loop
 
character:
    addi $t1,$t1,1
    add $s0,$s0, 1
    j loop
 
number:
	blt $s2,58,number1
	 add $s0,$s0, 1
   	 j loop

number1:
	addi $t2,$t2,1
	add $s0,$s0, 1
        j loop 
        
special:
	blt $s2,48,special1
	blt $s2,65,special1
        add $s0,$s0, 1
   	j loop
  
special1:
 	addi $t3,$t3,1
	add $s0,$s0, 1
        j loop 
 	
   	
endloop:
	li $v0,4
	la $a0, output
	syscall
	
	addi $s1,$s1,-1
		
	li $v0,1
	move $a0,$t1
	syscall
	
	li $v0,4
	la $a0, output1
	syscall
	
	
	li $v0,1
	move $a0,$t2
	syscall
	
	li $v0,4
	la $a0, output2
	syscall
	
	
	li $v0,1
	move $a0,$t3
	syscall
	
	
  	li $v0, 10
  	syscall
  	

  	
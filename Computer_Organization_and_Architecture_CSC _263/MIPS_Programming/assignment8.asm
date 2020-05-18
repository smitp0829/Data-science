	.data
String: .asciiz "Enter the String: "
output: .asciiz "\nNumber of character in entered string is: "
output1: .asciiz "\nNumber in entered string is: "
output2: .asciiz "\nNumber of special character in entered string is: "
output3: .asciiz "\nThe entered string does not have character,number, or special character"
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
	
	la $a0, str
  	li $a1,0
  	li $t0,0
  	li $v0,0
  	li $t3,0
  	
  	jal loop
  	
  	subi $sp,$sp,12
  	sw $t3,0($sp)
  	sw $v1,4($sp)
  	sw $t0,8($sp)
  	
  	
  	lw $s1,8($sp)
  	lw $s2,4($sp)
  	lw $s3,0($sp)
  	addi $sp,$sp,12
  	
	 li $v0,4
	la $a0, output
	syscall
	
		
	li $v0,1
	move $a0,$s1
	syscall
	
	li $v0,4
	la $a0, output1
	syscall
	
	
	li $v0,1
	move $a0,$s2
	syscall
	
	li $v0,4
	la $a0, output2
	syscall
	
	
	li $v0,1
	move $a0,$s3
	syscall
	
	
  	li $v0, 10
  	syscall
  	
 loop:
 	lb $a2,0($a0)
 	beqz $a2,endloop
 	bge $a2,65,character
 	bge $a2,58,special
 	bge $a2,48,number
 	bge $a2,33,special
 	add $a1, $a1, 1
 	add $a0,$a0, 1
 	jr $ra
 
character:
    addi $t0,$t0,1
    add $a0,$a0, 1
    j loop 
 
number:
	blt $a2,58,number1
	 add $a0,$a0, 1
   	j loop
   	 

number1:
	addi $v1,$v1,1
	add $a0,$a0, 1
   	j loop 
        
special:
	blt $a2,48,special1
	blt $a2,65,special1
        add $a0,$a0, 1
   	j loop
  
special1:
 	addi $t3,$t3,1
	add $a0,$a0, 1
        j loop
 	
   	
endloop:
  	
	jr $ra 

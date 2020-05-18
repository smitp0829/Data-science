	.data
String: .asciiz "Enter the String: "
output: .asciiz "Length of String is: "
str: .space 32
strsize: .word 31
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
 	add $s1, $s1, 1
 	add $s0,$s0, 1
 	j loop
 
endloop:
	li $v0,4
	la $a0, output
	syscall
	
	addi $s1,$s1,-1
	li $v0, 1
	move $a0,$s1
	syscall
	
  	li $v0, 10
  	syscall
  	

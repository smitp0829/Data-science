	.data
String: .asciiz "Enter the String: "
output: .asciiz "Reverse String: "
str: .space 32
strsize: .word 31
str1: .space 32
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
	addi $s1,$s1,-1
	
	la $s0, str
	
	li $v0, 4
	la $a0, output
	syscall
	
	add $s0,$s0,$s1
	
	j print
	
	
print:
	
	lb $s2,($s0)
	
	beqz $s2,end

	li $v0,11
	la $a0,($s2)
	syscall
	
	add $s0,$s0,-1
	j print
 
 end:
 	li $v0, 10
  	syscall 	
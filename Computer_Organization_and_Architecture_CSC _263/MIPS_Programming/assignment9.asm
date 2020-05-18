.data 
list:  .space 32
input: .asciiz "Enter the array element: "
output: .asciiz "Maximum value of Array is: "
output1: .asciiz "\nMinimum value of Array is: "
	.text

main: 
	
	la $s0,list
	li $s4,0
	li $s5,10
	
	
input1:
	beq $s4,$s5,endInput
	
	li $v0,4
	la $a0,input
	syscall 
	
	li $v0,5
	syscall 
	move $t1,$v0
	
	subi $s0,$s0,4
	sw $t1,($s0)
	
	addi $s4,$s4,1
	
	j input1
	
endInput:
	li $s4,0
	li $s5,9	
	lw $s1,($s0)
	lw $s7,($s0)
	
	j loop
	

loop: 
	beq $s4,$s5,endloop
	addi $s4,$s4,1
	addi $s0,$s0,4
	lw $s2,($s0) 
	bge $s2,$s1,swap
	ble $s2,$s7,swap1
	j loop
	

endloop:
	li $v0,4
	la $a0, output
	syscall
	
	
	li $v0, 1
	move $a0,$s1
	syscall
	
	li $v0,4
	la $a0, output1
	syscall
	

	li $v0, 1
	move $a0,$s7
	syscall
	
	
	li $v0, 10
  	syscall
  
  swap:
  	move $s1,$s2
  	j loop
  	
  swap1:
  	move $s7,$s2
  	j loop
 
 	

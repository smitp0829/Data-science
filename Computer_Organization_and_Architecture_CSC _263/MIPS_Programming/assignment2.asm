	.data 
list:  .word 2,5,3,9,22,4,7,80,10,1,12,15,98,20,8
output: .asciiz "Maximum value of Array is: "
output1: .asciiz "\nMinimum value of Array is: "
	.text

main: 
	
	la $s0,list
	li $s4,0
	li $s5,14
	ld $s1,($s0)
	ld $s7,($s0)
	
	

loop: 
	beq $s4,$s5,endloop
	addi $s4,$s4,1
	addi $s0,$s0,4
	ld $s2,($s0) 
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
 
 	
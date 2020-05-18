.data 
input: .asciiz "Enter the array element: "
output: .asciiz "Maximum value of Array is: "
output1: .asciiz "\nMinimum value of Array is: "
	.text

main: 
	
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
	
	subi $sp,$sp,4
	sw $t1,0($sp)
	
	addi $s4,$s4,1
	
	j input1
	
	
	
	
endInput:
	li $s4,0
	li $s5,9	
	lw $a0,0($sp)
	lw $a1,0($sp)
	jal loop
	
	move $t0,$a0
	move $t1,$a1
	
	li $v0,4
	la $a0, output
	syscall
	
	
	li $v0, 1
	move $a0,$t0
	syscall
	
	li $v0,4
	la $a0, output1
	syscall
	

	li $v0, 1
	move $a0,$t1
	syscall
	
	
	li $v0, 10
  	syscall
	
loop: 
	beq $s4,$s5,endloop
	addi $s4,$s4,1
	addi $sp,$sp,4
	lw $s2,($sp) 
	bge $s2,$a0,swap
	ble $s2,$a1,swap1
	j loop
	

endloop:
	jr $ra
  
  swap:
  	move $a0,$s2
  	j loop
  	
  swap1:
  	move $a1,$s2
  	j loop
 
 	

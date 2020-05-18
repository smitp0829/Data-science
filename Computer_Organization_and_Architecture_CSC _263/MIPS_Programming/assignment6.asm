	.data 
input1: .asciiz "Enter the number where you want to start from: "
input2: .asciiz "Enter the number where you want to stop: "
output: .asciiz "Addition of even number is: "
	.text 

main:
	li $v0,4
	la $a0, input1
	syscall
	
	li $v0,5
	syscall
	move $s0,$v0
	
	li $v0,4
	la $a0, input2
	syscall
	
	li $v0,5
	syscall
	move $s1,$v0
	
	li $s3,2
	li $s5,0
	addi $s1,$s1,1
loop:
	beq $s0,$s1,end
 	div $s6,$s0,$s3
 	mfhi $s4
 	beq $s4,0,addition
 	addi $s0,$s0,1
	j loop

addition: 
	add $s5,$s5,$s0
	addi $s0,$s0,1
	j loop
	
	
end:
	li $v0,4
	la $a0, output
	syscall
	
	li $v0,1
	move $a0,$s5
	syscall
	
	li $v0,10
	syscall
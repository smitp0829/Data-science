.data
Str: .asciiz "abcdeifgh "
char: .byte 'i'
out: "\nThe character is at: "	
 .text
 
 main:
	
	la $t0, str
  	li $t1,0
	
 serach:
 	lb $t2,0($t0)
 	beq $t2,'i', serach
 	beq $t2,$zero,quit
 	add $t1, $t1,1
 	add $t0,$t0, 1
 	j serach
 	
 	
quit:
	
	li $v0,4
	la $a0, search
	syscall
	
	li $v0, 1
	move $a0,$t1
	syscall
	
  	li $v0, 10
  	syscall
  	

 
 
 

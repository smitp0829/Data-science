	.data
input: .byte 60
output: .asciiz "Entered Fahrenheit value in Celsius is: "
	.text

main:
la $a0,input
lw $s0,($a0)
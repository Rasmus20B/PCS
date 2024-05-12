sum:
pushi #1
pushi #2
pushi #3
pushi #4
pushi #5
loop:
pushi $r1
addi
seti $r1
jmpneq &loop
ret
start:
pushi #0
seti $r1
call &sum
printr $r1

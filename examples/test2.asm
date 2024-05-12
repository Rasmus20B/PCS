add:
pushi #4
pushi #2
addi
pushi #5
addi
ret
check:
addi
ret
start:
pushi #3
pushi #4
call &check
print

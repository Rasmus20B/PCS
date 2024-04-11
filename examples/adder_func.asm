add:
pushi #4
print
pushi #5
print
addi
seti $r1
pushi $r1
ret
start:
call &add
print

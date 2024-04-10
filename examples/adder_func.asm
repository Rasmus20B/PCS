add:
pushi 4
print
pushi 5
print
addi
seti $tmp
pushi $tmp
ret
start:
call &add
print

shoot1:
etNew 0
etCount 0 1 3
etAim 0 1
etAngle 0 15 20
etSpeed 0 3 3
etOn 0
jmpeq &shoot1
ret
shoot2:
etNew 1
etCount 1 1 3
etAim 1 1
etAngle 1 0 15
etSpeed 1 4 8
etOn 1
pushi 0
seti $acc
pushi $acc
pushi 10
pushi 11
pushi 12
pushi 13
pushi 14
pushi 15
loop:
pushi $tmp
addi
seti $acc
etAngle 1 $acc 15
pushi $acc
etOn 1
wait 300
seti $tmp
jmpneq &loop
seti $tmp
ret
start:
movePos 100 100
movePosTime 20 0 400 400 
call &shoot2
wait 200
movePosTime 20 0 600 100
enmCreate &start 0 0 0 0 0
call &shoot2
wait 200
movePosTime 20 0 100 100
call &shoot2

shoot1:
etNew 0
etCount 0 1 3
etAim 0 1
etAngle 0 15 20
etSpeed 0 3 3
etOn 0
jmpeq shoot1
ret
shoot2:
etNew 1
etCount 1 3 8
etAim 1 2
etAngle 1 0 15
etSpeed 1 2 5
pushi 0
pushi 3
pushi 3
pushi 3
pushi 3
pushi 3
pushi 3
loop:
addi
seti 3
etOn 1
wait 300
jmpeq loop
ret
start:
movePos 100 100
movePosTime 20 0 400 400 
call shoot2
wait 20
movePosTime 20 0 600 100
call shoot2
wait 20
enmCreate start 100 100 300 0 0
movePosTime 20 0 100 100
call shoot2

shoot1:
etNew 0
etSprite 0 4 0
etCount 0 3 3
etAim 0 1
etAngle 0 15 20
etSpeed 0 2 3
etOn 0
ret
shoot2:
etNew 1
etSprite 1 2 0
etCount 1 3 3
etAim 1 1
etAngle 1 15 20
etSpeed 1 2 3
etOn 1
ret
enemy:
pushi 0
pushi 3
pushi 3
anmSetSprite 0 0
movePosTime 80 0 300 400
call shoot1
call shoot1
call shoot1
movePosTime 200 0 700 400
wait 20
call shoot2
call shoot2
call shoot2
movePosTime 100 0 800 20
delete
pushi 0
start:
pushi 1
pushi 2
enmCreate enemy 700 40 1 0 0
anmSetSprite 0 0
movePosTime 60 0 600 200
loop:
call shoot1
call shoot1
jmp loop
delete

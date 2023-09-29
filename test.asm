shoot1:
etNew 0
etSprite 0 4 0
etCount 0 3 3
etAim 0 1
etAngle 0 15 20
etSpeed 0 3 3
etOn 0
ret
shoot2:
etNew 1
etSprite 1 2 0
etCount 1 8 8
etAim 1 4
etAngle 1 0 0
etSpeed 1 2 2
etOn 1
ret
shootpat:
etNew 0
etSprite 0 4 0
etCount 0 4 3
etAim 0 1
etAngle 0 0 15
etSpeed 0 4 1
loop7:
etOn 0
wait 30
jmpeq loop7
nop
delete
enemy2:
pushi 0
pushi 3
pushi 3
pushi 3
anmSetSprite 0 0
movePosTime 80 0 300 400
call shoot1
wait 10
call shoot1
wait 10
call shoot1
wait 10
movePosTime 200 0 700 400
wait 200
call shoot2
wait 20
movePosTime 60 0 800 400
call shoot2
wait 20
call shoot2
wait 60
movePosTime 120 0 3000 400
delete
enemy1:
pushi 0
pushi 3
pushi 3
pushi 3
movePos 300 200
anmSetSprite 0 0
movePosTime 500 0 1000 400
callasync shootpat
wait 20
delete
loop1:
call shoot2
wait 30
call shoot2
wait 30
call shoot2
jmpeq loop1
movePosTime 40 0 4000 0
delete
pushi 0
start:
pushi 1
pushi 2
pushi 2
enmCreate enemy1 700 40 1 0 0
wait 10000

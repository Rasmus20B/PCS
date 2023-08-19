checking:
nop
shoot:
etNew 0
etSprite 0 2 0
etCount 0 4 4
etAim 0 2
etAngle 0 0 15
etSpeed 0 9 1
etOn 0
ret
start:
pushi 0
loop:
call shoot
wait 60
jmpneq loop
delete

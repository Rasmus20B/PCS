shoot1:
etNew #0
etCount #0 #1 #3
etAim #0 #2
etAngle #0 #15 #20
etSpeed #0 #3 #3
etOn #0
pushi #0
pushi #15
pushi #12
pushi #9
pushi #6
pushi #3
loop1:
seti $r1
etCount #0 $r1 $r1
etOn #0
wait #500
jmpneq &loop1
ret
shoot2:
etNew #1
etCount #1 #1 #3
etAim #1 #1
etAngle #1 #0 #15
etSpeed #1 #4 #8
etOn #1
pushi #0
seti $r1
pushi $r1
pushi #10
pushi #11
pushi #12
pushi #13
pushi #14
pushi #15
loop:
pushi $r2
addi
seti $r1
etAngle #1 $r1 #15
pushi $r1
etOn #1
wait #300
seti $r2
jmpneq &loop
seti $r2
ret
start:
movePos #100 #100
movePosTime #2000 #0 #400 #400 
call &shoot2
wait #100
movePosTime #2000 #0 #600 #100
callasync &shoot1
wait #100
movePosTime #2000 #0 #100 #100
wait #2000

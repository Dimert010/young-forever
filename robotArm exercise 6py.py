from RobotArm import RobotArm 

robotArm = RobotArm('exercise 6')
robotArm.speed = 4

for i in range(7):
    robotArm.moveRight()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(7):
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()

robotArm.wait()
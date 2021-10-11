from RobotArm import RobotArm 

robotArm = RobotArm('exercise 4')
robotArm.speed = 4

for y in range(2):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for y in range(2):
 robotArm.moveRight()
 robotArm.grab()
 robotArm.moveLeft()
 robotArm.drop()

robotArm.wait()
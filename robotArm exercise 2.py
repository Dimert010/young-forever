from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 4

robotArm.grab()
for o in range(9):
    robotArm.moveRight()


robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()

for o in range(5):
    robotArm.moveLeft()


robotArm.grab()

for o in range(5):
    robotArm.moveRight()

robotArm.drop()

robotArm.wait()

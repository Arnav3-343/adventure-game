import random
import time
print("Hello,welcome to the adventure game:")
time.sleep(2)
print(" you are currently in a hightech car that you stole from invent industries and the robots are chasing you, you have to reach the drop point")
time.sleep
print("you have passed the HighMen Bridge")
time.sleep(2)
print("welcome to Tech island ")
time.sleep(2)
print("loading sytems:")
totalmilesdriven=0
robots = 20
invisible=2
refills = 3
fuel= 10
distanceDriven= 10
winndistance = 100
turboboost = 1
invenobotsdistance = 10
gameOver = False
won = False
while(not gameOver and not won):
  time.sleep(1)
  print("--------------------------------")
  print("Here are your options:")
  print("---------------------------------")
  time.sleep(0.3)
  print("A. drive at full speed")
  time.sleep(0.3)
  print("B. replace gas tank")
  time.sleep(0.3)
  print("C. stop for the night")
  time.sleep(0.3)
  print("D. click this to quit the game")
  time.sleep(0.3)
  print("E. invisible")
  time.sleep(0.3)
  print("F. status check")
  time.sleep(0.3)
  print("O. You can activate turbo boost")
  print("---------------------------------")
  
  userinput = input("What is your option to escape the robots?  ")
  if(userinput=="A" or userinput == "a"):
     distanceDriven=random.randint(3,6)
     totalmilesdriven += distanceDriven
     print("you drove " + str(distanceDriven) +" miles in 5 minutes. " )
     fuel -= 2
     robotshover = random.randint(1,6)
     robots += robotshover
  elif(userinput=="B" or userinput == "b"):
    if(fuel > 0):
      refills -= 1
      print("you have one more gas tank that you can switch")
      fuel += 20
      if(refills == 0):
        print("Your out of refills")
      
  elif(userinput == "C" or userinput == "c"):
    print("you have decided to stop for the night")
    robots -= 4
  elif(userinput == "E" or userinput == "e"):
    if(invisible == 2):
     print("you have hidden from the invenobots for a short period of time,you cannot use it anymore")
    invisible -= 2
    if(invisible == 0):
        print("you can no longer go invisible")
    
  elif (userinput == "F" or userinput == "f"):
        print("You have travelled " + str(totalmilesdriven)  + " miles. You have to drive " + str(winndistance - totalmilesdriven) + " miles until you reach the checkpoint.The robots are " + str(robots) + " miles away. You have " + str(fuel) + " gallons of fuel in you tank")
  elif(userinput == "O" or userinput == "o"):
    if(turboboost == 1):
      print("you can activate turbo boost")
      totalmilesdriven += 20
      turboboost -= 1
    if(turboboost == 0):
      print(" you can no longer use this powerup")
  
  
  elif (userinput != 'q'):
          print("sorry,Invalid input")
  
  if(totalmilesdriven >= 100):
   print("you got to the check point, you win. Your")
   break
   
  if(robots <= 0):
    print("you lost, the invenobots have got you")
    break
  if(totalmilesdriven - robots <= 10 >= 2):
    print("the robots are near you! Escape them or they will capture you!")
  
  if(userinput == "D"):
    print("game over, refresh the page if you want to play again")
    break
  if(userinput == "T"):
    print("you win,don't share this cheat code to anyone:T")
    break
      
  if(fuel <= 0):
    print("YOU RAN OUT OF FUEL! \nGAME OVER!  ")
    print("\U0001F62A")
    gameOver = True
  elif(fuel < 4):
    print("you have to switch gas tanks")

   
if(userinput == "T"):
  print("you win,don't share this cheat code to anyone:T")
      




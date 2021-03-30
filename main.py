import random

print("Hello,welcome to the adventure game:")
print(" you are currently in a hightech car that you stole from invent industries and the robots are chasing you, you have to reach the drop point")
totalmilesdriven=0
robots = 20
invisible=2
refills = 2
fuel= 10
distanceDriven= 10
winndistance = 100
turboboost = 1
gameOver = False
won = False
while(not gameOver and not won):
  print("--------------------------------")
  print("Here are your options:")
  print("---------------------------------")
  print("A. drive at full speed")
  print("B. replace gas tank")
  print("C. stop for the night")
  print("D. click this to quit the game")
  print("E. invisible")
  print("F. status check")
  print("O. You can activate turbo boost")
  
  userinput = input("What is your option to escape the invenobots?  ")
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
        print("You have travelled " + str(distanceDriven) + " miles. You have to drive " + str(winndistance - distanceDriven) + " miles until you reach the checkpoint.The robots are " + str(robots) + " miles away. You have " + str(fuel) + "gallons of fuel in you tank")
  elif(userinput == "O" or userinput == "o"):
   if(turboboost == 1):
    print("you can activate turbo boost")
    distanceDriven += 20
    turboboost -= 1
  if(turboboost == 0):
    print(" you can no longer use this powerup")
  
  
  elif(userinput != "q"):
    print("Please Choose a valied option")
  
  if(totalmilesdriven >= 100):
   print("you got to the check point, you win")
   break
   
  if(robots <= 0):
    print("you lost, the invenobots have got you")
    break
  if(totalmilesdriven - robots <= 15):
    print("the invenobots are near you! Escape them or they will capture you!")
  
  if(userinput == "D"):
    print("game over, refresh the page if you want to play again")
    break
  if (fuel <= 0):
    print("YOU RAN OUT OF FUEL! \nGAME OVER!  ")
    print("\U0001F62A")
    gameOver = True
  elif(fuel < 4):
    print("you have to switch gas tanks")

  
print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the solute in bubble tea")
  print("   a) Water")
  print("   b) Milk")
  print("   c) Tea")
  print("   d) Bubble Tea")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. There is a solute present in the option you have chosen."
    score -=1
  elif answer == "c":
    output = "Wrong. There is a solute present in the option you have chosen."
    score -=1
  elif answer == "d":
    output = "Wrong. There is a solute present in the option you have chosen."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the difference between evaporation and boiling?")
  print("   a) Boiling can happen over a range of temperatures but evaporation can only happen at a fixed temperature.")
  print("   b) Boiling can only happen at 100 degrees celcius but evaporation can happen over a range of temperatures. ")
  print("   c) Boiling takes place throughout the substance but evaporation only occurs on the surface of the substance.")
  print("   d) Evaporation can occur on substances of any state but boiling can only occur on liquids.")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Boiling is the process that can happen at a fixed temperature, not evaporation!?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Different substances have different boiling points so there is no fixed temperaature for boiling to occur in all substances!"
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score -=1
    
  elif answer == "d":
    output = "Wrong. All matter can melt and boil at different substances, not only liquids!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")

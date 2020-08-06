# audreylandoy@gmail.com If I need any help.


print("Welcome to: What was that Noise?")

name = input("Hello, for who am I greeting? \n ")

print("Hmmmmm, " + name + ", sounds familiar")

print("You are in the living room of your home, you are getting ready to head to bed for the night.") 
print("Having stayed up late, everyone else in your house is fast asleep. You begin to walk up the stairs to your room when you hear...")
print("Creeeaaak")
print("You stop, frozen in place. The stair case was never this loud")
print("Creeeeeeaaaaaak")
print("Now knowing that what you heard wasnt your footsteps on the wooden staircase, you decide a plan of action for yourself.")

scene1 = input("What will you do? \n A) Look around and wait for the sound to occur again, so you can get a better understanding on the source \n B) Ignore it completely and go to bed \n C) Call out to it, as there might be a response to the strange noise")

def scene1_checkAround():
  print("")

def scene1_ignoreSound():
  print("")

def scene1_callOut():
  print("Hello! You call out")

def scene1_secretOption():
  print("You stand there, quite confused for why you are not doing anything in a circumstance like this")

if scene1 == "A":
  scene1_checkAround()
elif scene1 == "B":
  scene1_ignoreSound()
elif scene1 == "C":
  scene1_callOut()
else:
  scene1_secretOption()


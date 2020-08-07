# audreylandoy@gmail.com If I need any help.

print("Welcome to: What was that Noise?")

options = [ "A", "B", "C"]

name = input("Hello, for who am I greeting? \n ")

print("Hmmmmm, " + name + ", sounds familiar")

def start():
  print("You are in the living room of your home, you are getting ready to head to bed for the night.") 
  print("Having stayed up late, everyone else in your house is fast asleep. You begin to walk up the stairs to your room when you hear...")
  print("Creeeaaak")
  print("You stop, frozen in place. The stair case was never this loud")
  print("Creeeeeeaaaaaak")
  print("Now knowing that what you heard wasnt your footsteps on the wooden staircase, you decide a plan of action for yourself.")

  scene1 = input("What will you do? \n A) Look around and wait for the sound to occur again, so you can get a better understanding on the source \n B) Ignore it completely and go to bed \n C) Call out to it, as there might be a response to the strange noise \n")

  while scene1 not in options:
    print("Not a valid option. Please answer A, B, C")
    scene1 = input("What will you do? \n A) Look around and wait for the sound to occur again, so you can get a better understanding on the source \n B) Ignore it completely and go to bed \n C) Call out to it, as there might be a response to the strange noise \n")
  scene1_options(scene1)


def scene1_checkAround():
  print("You walk back down the stairs and start to look around for the source of the noise. You traced the noise down to 3 places:")

def scene1_ignoreSound():
  print("You continue to walk up the stairs, completely unaware of the creepy noise that you heard a second ago. Once you got to the top of the stairs,")

def scene1_callOut():
  print("Hello! You call out, hoping for an answer.")
  print("Groooaaaan!")



def scene1_options(scene1):
  if scene1 == "A":
    scene1_checkAround()
  elif scene1 == "B":
    scene1_ignoreSound()
  elif scene1 == "C":
    scene1_callOut()
  else: 
    print("That's not a valid option, pick one of the 4 options")
    start()


def main():
  start()

main()

# if_name_ == "_main_":
# main()

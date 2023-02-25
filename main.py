print('''                            ______________________________________________
                          .-'                     _                        '.
                        .'                       |-'                        |
                      .'                         |                          |
                   _.'               p         _\_/_         p              |
                _.'                  |       .'  |  '.       |              |
           __..'                     |      /    |    \      |              |
     ___..'                         .T\    ======+======    /T.             |
  ;;;\::::                        .' | \  /      |      \  / | '.           |
  ;;;|::::                      .'   |  \/       |       \/  |   '.         |
  ;;;/::::                    .'     |   \       |        \  |     '.       |
        ''.__               .'       |    \      |         \ |       '.     |
             ''._          <_________|_____>_____|__________>|_________>    |
                 '._     (___________|___________|___________|___________)  |
                    '.    \;;;Dani;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;;o;;;;/   |
                      '.~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~   |
                        '. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~  |
                          '-.______________________________________________.''')


print("Welcome to Ocean Death")
print("Your mission is to survive")

choice1 =  input("Your boat is sinking and you are surounded by sharks. Swim 'left' or swim 'right'.\n").lower()
if choice1 == "left":
  choice2 = input("You swim to a small island but it full of zombies. You have decicion to either 'fight' or 'friend' the zombies.\n ").lower()
  if choice2 == "fight":
    choice3 = input("You fought off the zombies and run in to a building there are three doors. One door say's 'Treasure' another says 'Death' the last door says 'Happiness' choose wisely.\n").lower()
    if choice3 == "treasure":
      print("Its called Ocean Death you lose...")
    elif choice3 == "death":
      print("You suck at games you lose...")
    elif choice3 == "happiness":
      print("Congrats you beat the game nerd!")
    else:
      print("that door doesnt exist you lose")
  else:
    print("Why would you try to be friends with a zombie you DIE!")  
else:
  print("Congratulations you were eaten by sharks!")
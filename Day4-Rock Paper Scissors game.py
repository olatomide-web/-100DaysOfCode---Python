import random

rock = '''

     
 ---.____    ,/k.
  ___,---'  /  ih,__,-----.___
         ,-' ,  `:7b----.__---`
     _.-/   '  /b.`.4p,
  --"  ,    ,-' ^6x, `."^=._

'''


paper = '''



 _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
              jgs    |    |



'''



scissors = '''
  _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

#0 = rock, 1 = paper, 2 = scissors
game_images = [rock, paper, scissors]

players_choice = int(input("what  do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if players_choice >=3 or players_choice < 0:
    print("You typed an invalid number, please follow the instructions")
else:
    print(game_images[players_choice])

computers_choice = random.randint(0,2)

print("You chose:")
print(game_images[players_choice])

print("Computer chose:")
print(game_images[computers_choice])



if players_choice >=3 or players_choice < 0:
    print("You typed an invalid number, please follow the instructions")

if players_choice == computers_choice:
    print("Game ends in a draw!")
elif computers_choice == 2 and players_choice == 0:
    print("you win!")
elif players_choice == 2 and computers_choice == 0:
    print("you loose!")
elif computers_choice > players_choice:
    print("you loose!")
elif players_choice > computers_choice:
    print("you win!")

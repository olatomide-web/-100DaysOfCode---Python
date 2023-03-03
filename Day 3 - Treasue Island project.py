print("""                      _
                    .(o)`---.--...__.-.__
                  .'.' '-.-..--._.--._.(o)`---...-.____
                .'.' | |   .:'     .:'| |'--._..--'-.(o)---...._____
              .'.' .'| |.:'     .:'   |.| | | |  |`---.`--..--._.-.(o)
            .'.' .' ||.|-._.-.:'_.-_-.| | | | |  ||.:'    .:'|| | |-|
          .'.' .'   || |  '     '     | | . | |  ||-._.--'._.|| | | |
        .'.'|.''    || |  '     '     | | | | |  ||  '   '   || | | |
       '.'_||| '    || |  '     '     | | | | |  ||  '   '   || | | |
           ||| '    || | _ _ _ _ _ _  | | | / |  ||  '       || | | |
           ||| '    .| || | | | | | | | |  .  '  '-----....._|' | | |
           |||    .' | || | | | | | | |.|''  ----....   ____    ' | |
           |||  .'   |>][<| | | | | | | |---  ..    --  ...   --  | |
           |||.'    .|.|| | | | | | | | |-..__    _          __ ..| |
           ||    .'  | || | | | | | | | |          '''-----. _ -- | |
           ||.'      | || | | | | | | ||| ..  -  -...          .. | |
           ||     .' | || | | | | | | | |--..____  ... ''''''''-  | |
           ||  .'    |>][<| | | | | | | |              --  __ ....| |
           ||'    .' | || | | | | | | | |---  .  .....__  ..      | |
           || .' ' .'| ||_|_|_|_|_|_| | |. ___            .-. '-' | |
           ||   .'   | |_____________/(o)__  ....  ''''  /(o) ... | |
           ||.'   .' (o)=====]======[ //(o)=============/ //==(o)='=|
           ||  .'  .'        |      |//      |   |     / //   // /.'
           ||(o)\'     \     |      |/       /  /     / //   //`/
     _ LGB || \\ \     |    =|======|=       | /     /`//   // /
      `-._.||==\\.\=====\    |      |   .'   | |====/ //===// /
          `-.   \\ \    |`-. |      |      | / /   / //   //`/ 
-._   `-.    `-. \\ \   |   =|======|=     || |   / //   //./       _.--
   `-..         `.\\`\  \    |      |     . './  /`//   .\ /  .. --'
       `..   `-.  `\\ \ |`.  |      |  .' '  |  / //   //\\-`'
          `-.       \\`\|   =|======|=       \ / // .-'   \\  .-`   .`
             `.  `.  \\/. -' |      |         / //-'    .` \\       _.-'
              `.      // \   |      |  .'  ' /`// `         \\ _..-'
                \    //.\/. =|======|=      / //       `   _.``
                 `. //  // \ |      |      / //  .-`   _.'
                   '/  // \  |      |  .' / //      _.'
                    `.//    =|======|=   / //   .-'
                     '/  `.  |      |   /.//  .'
                      `. .   |      |  /-// .'
                        `.  =|======|=/ // /
                          \  |      |/ //  |
                          |  |      |`//  /
                          \ =|======|=/ .'
                           | |    / |/  .|
                           \ |   / /|  .'\
                           |=|======|= | |
                           | |      |  | |
                           |           | |
 """)

print("welcome to treasure Island!\n Your mission is to find the hidden treasure.\n ")
option = input("You are at a crossroad. Where do you want to go?\n Type 'left' or 'right' \n")

##############################
option = option.lower()
if option == 'right':
    print("You fell into a hole, game over")
elif option == 'left':
    mode_of_transportation = input("do you want to swim or wait for a boat?\n")
    mode_of_transportation = mode_of_transportation.lower()
    if mode_of_transportation == "swim":
        print("Game over!")
    elif mode_of_transportation == "wait":
        print("the boat has arrived, enter the boat to cross the river.\n You are now at the door.")
        choose_door = input("which door do you want to enter? blue, red, yellow?\n")
        choose_door = choose_door.lower()
        if choose_door == "blue":
            print("Game Over!")
        elif choose_door == "red":
            print("Game over!")
        elif choose_door == ("yellow"):
            print("Hurray!!, you have found the treasure, it is an ancient Ruby that belongs to king Xerxes")
else:
    print("kindly read the instruction again")

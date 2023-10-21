#choose your own adventure
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 ''')

print("Welcome to Treasure Island!\nYour mission: Find the treasure.")

print("\nWalking through an enchanted wood, you reach a fork in the path.")
direction = input("Which way do you go? (type 'left' or 'right') ")
if direction.lower() != "left":
    print("\nYou have been kidnapped by a band of elves.\nGame Over")
    print('''
    ,-"=-.
     .       \
     "='"=\   '
     `@] @'|   )
     ) ` ' ),-`
      \^_,  \,  
  gpyy  ,(\,/ )`-.''')
else:
    print("\nThe path has lead you out of the forest! You see a crystal lake ahead.")
    water = input("Will you swim across or build a raft? (type 'swim' or 'raft') ")
    if water.lower() != "swim":
        print('''
                           
                          .MHMH                 X:
                          :HMMH.            .X!HMM.
                          `HMHM!            !MHMMX
                           HMHHH.            IMM!
                           XHHHHM!
     XMMM!.                IMHXHMM.                        :I.
     `HMHMMI.              :HHXXHH'                      .AMH'
       `VMHHM!              HHXIHH                      :MHH'
         `!HHHA.            XHIIIX.    .MX     .:HD    AHHV
            `HHHA.          !HI!IXI    AM:    AMHH'. :HHM!
              `XXHA.     .  `HI!:IX   :HH    AHHMV .IXHH'
               `!XIX:.  AMA:.H!::IX.  !HX   AHHHV :IIHX
                 `XIXX: :HHHHHI. .HMMMXXH: !XIHHHIIHV'
                  `X!:IXIMHHXHI.  IHHH!HX.!IIXH!.IHV
                   `H:.:!IHHXII:  .XH!!HMI::X! :XHI
                    :MI. .!!II!:  :II.!H!.:I:.IHV:
               :AMMHHII!:. :::::   ::.I: .: :IHV.                           .!!:
                   `:VMHII:. .       ..   .IHHMI                    .:IHHMMMHMM!
      ..::::.....      HHXI:.            :IXXHHMH.          .:!IXHHHHHMHHHX!'
AMMMMMMMMHHHHHHHXIIIII!!!:::.            :!!IXHHHHH:..:!!XXXHHXI!:'
              ``::!XHX:....                     .!XHHHI:'
                       II!:..           .::!IIHHI'
                  .:II::  .::        ::. .:!IHM:
            :IXXIIIIIIXHMH::!: .::  .::!II!: :H!
     .!XHHHHXHHHX!:'  .XXIXH: :III:  !XHHHHHHI!IA:.      !MA
 AHMMHMMMHI!:'      :HHHHHH:.!HHHHI: :HM:    `!XXXX::.   XMMI     .HM!
 `VI!'             !MV'  :!!IHMMMHHI. XX          `!XHHA. ..      :HMM:
                        AIIHI'   VMH: :I             `VHMMH:.      `!!
             .MMMV'    AHHH:      `HH::!    .HM:        `VMMMA
           .HV'      :MHHHI        `HI!!.                 `:HMD
          :'         IMHV'          `XII!
                      `'             :XIX.
                                      !HHI          IMMI
                                      `XHH!         IMMM:
                                       XHHH.         :I:
                                       !MHMI''')
        print("\nYou lean out of your raft to look closer at what seems to be a mermaid.\nLosing your balance, you fall into the water.\nGame Over")
    else:
        print(
            "\nWhile swimming across, a friendly group of mermaids take pity on you and help you to the other  side.\nYou arrive on a beach before a grand palace.")
        while True:
            enter = input("How will you enter:\nthrough the open window, through the servant's door or by climbing to the balcony?\n(type 'window', 'door' or 'balcony') ")
            if enter.lower() == "window":
                print('''                                 |--__
                                 |
                                 X
                        |-___   / \       |--__
                        |      =====      |
                        X      | .:|      X
                       / \     | O |     / \
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW______"""______WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _''')
                print("\nYou tumble through the window- right into a palace guard.\nGame Over")
                break
            elif enter.lower() == "balcony":
                print(
                    "\nYou enter the palace through the balcony door- where you are spotted by the princess.\nHer scream brings the palace guards running. Game Over")
                break
            elif enter.lower() == "door" or enter.lower() == "servant's door":
                print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
                print(
                    "\nDisguised as a servant, you search the rooms of the palace.\nEntering an especially decorated door, you find yourself in a room full of gold, jewellery and antiquities.\nYou win!")
                break
            else:
                print("\nCheck your spelling...")


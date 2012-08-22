# -- coding: utf-8 --
from sys import exit
from time import sleep
import os
import random

def realstart():
    os.system('clear')
    print """\033[30m\033[47m
-----------------------------------------------------------------------------
---------      _______      ________ _   _ _______ _    _ _____  ______ -----
---------/\   |  __ \ \    / /  ____| \ | |__   __| |  | |  __ \|  ____|-----
--------/  \  | |  | \ \  / /| |__  |  \| |  | |  | |  | | |__) | |__   -----
-------/ /\ \ | |  | |\ \/ / |  __| | . ` |  | |  | |  | |  _  /|  __|  -----
------/ ____ \| |__| | \  /  | |____| |\  |  | |  | |__| | | \ \| |____ -----
-----/_/    \_\_____/   \/   |______|_| \_|  |_|   \____/|_|  \_\______|-----
-----------------------------------------------------------------------------
-------------------------_____          __  __ ______ -----------------------
------------------------/ ____|   /\   |  \/  |  ____|-----------------------
-----------------------| |  __   /  \  | \  / | |__   -----------------------
-----------------------| | |_ | / /\ \ | |\/| |  __|  -----------------------
-----------------------| |__| |/ ____ \| |  | | |____ -----------------------
------------------------\_____/_/    \_\_|  |_|______|-----------------------
-----------------------------------------------------------------------------
----------------------------------START GAME---------------------------------
------------------------------Press enter to being---------------------------
-----------------------------------------------------------------------------
\033[0m
"""
    startyes()
    
def startyes():
    next = raw_input("==> ")
    startname()

def startname():
    print "Let's pick a name for you're self shall we."
    sleep(1)
    print "What do you want to be called..."
    global name
    name = raw_input("==> ")
    os.system('clear')
    if len(name) == 0:
        print "Please pick a name for yourself."
        startname()
    elif "cheat" in name:
        level_pick()
    else:
        start()
        
def start():
    print "%r you are meet with 3 doors at the begining of the castle" % name
    sleep(1)
    print "Please pick one. \033[31mred\033[0m, \033[34mblue\033[0m or \033[32mgreen\033[0m door."
    pick = raw_input("==> ")
    os.system('clear')
    if pick == "red":
        red()
    elif pick == "blue":
        blue()
    elif pick == "green":
        green()
    else:
        print "\033[1;31mYou need to pick one of the three doors\033[0m"
        start() 

def red():
    print "%r You enter the \033[31mRed\033[0m room." % name
    sleep(1)
    print "There apears to be nothing in here."
    sleep(1)
    print "Do you 'go back' or 'explore further'."
    nothing = raw_input("==> ")
    os.system('clear')
    if "explore" in nothing:
        print "There is a crack in the wall"
        sleep(1)
        print "You will need a hammer. do you want to 'go back' or 'stay'"
        hammer = raw_input("==> ")
        os.system('clear')
        if "go back" in hammer:
            print "\033[1;31mI think it was a wise choose.\033[0m"
            sleep(1)
            print "\033[1;31mYou head back to the castle enterance.\033[0m"
            sleep(1)
            start()
        elif "stay" in hammer:
            dead("You ideo you stayed and staved to death.")
        else:
            red()
    elif "go back" or "go" in nothing:
        print "\033[1;31mI think it was a wise choose.\033[0m"
        sleep(1)
        print "\033[1;31mYou head back to the castle enterance.\033[0m"
        sleep(1)
        start()
    else:
        "You need to pick one or the other"
        red()
        
def blue():
    print "%r There are 2 weapons you can choose" % name
    sleep(1)
    print "Do you want the 'sword' or the 'axe'."
    weapon = raw_input("==> ")
    os.system('clear')
    if "sword" in weapon:
        print "You picked the Sword, right on"
        sleep(1)
        startsword()
    elif "axe" in weapon:
        axe()        
    else:
        blue()

def axe():
    print """You picked the Axe, way to go.
  _________________.---.______
 (_(______________(_o o_(____()
              .___.'. .'.___.
              \ o    Y    o /
               \ \__   __/ /
                '.__'-'__.'
                    '''
    """
    sleep(1)
    print "Whoa a wild goblin appears."
    sleep(1)
    print "What do you do 'flee' or 'attack'."
    axechoose = raw_input("==> ")
    os.system('clear')
    if "flee" in axechoose:
        start()
    elif 'attack' in axechoose:
        goblin()
    else:
        axe()

def goblin():
    print "Do you attack the 'left' or 'right' arm?"
    arm = raw_input("==> ")
    os.system('clear')
    if "left" in arm:
        print "You struck the globin on his left arm"
        sleep(1)
        print "The goblin looks shocked and flees"
        sleep(1)
        axestart()
    elif "right" in arm:
        print "You struck the globin on his right arm."
        sleep(1)
        print "Whoa it looks like you killed him. Way to go."
        sleep(1)
        axestart()
    else:
        print "%r You need to pick an arm to slay with your axe." % name
        goblin()

def green():
    print "%r You open a door to a darkened room." % name
    sleep(1)
    print "What do you want to do 'step in' or 'go back'."
    pick = raw_input("==> ")
    os.system('clear')
    if "step in" in pick:
        dead("You die, curiosity killed the cat.")
    elif "go back" in pick:
        print "\033[1;31mProbily for the best.\033[0m"
        start()
    else:
        green()    
    
def startsword():
    print "Do you think you made the right choose picking the sword?"
    sleep(1)
    print """    
              (O)
              <M
   o          <M
  /| ......  /:M\------------------------------------------------,,,,,,
(O)[]XXXXXX[]I:K+}=====<{H}>================================------------>
  \| ^^^^^^  \:W/------------------------------------------------''''''
   o          <W
              <W
              (O)
    """
    sleep(1)
    print "Now you need to make another choose. Please pick the \033[33m'brown'\033[0m or \033[35m'purple'\033[0m door."
    pick = raw_input("==> ")
    os.system('clear')
    if "brown" in pick:
        swordleft()
    elif "purple" in pick:
        swordright()
    else:
        print "\033[1;31mCome on now you need to pick one to move on head.\033[0m"
        startsword()

def swordleft():
    print "Is this your lucky day?"
    sleep(1)
    print "A dark wise wizard stands befor you."
    sleep(1)
    print "Would you trade you're soul for immense wealth beyond your wildest dreams 'yes' or 'no'."
    wealth = raw_input("==> ")
    os.system('clear')
    if "yes" in wealth:
        treasurerroom()
    elif "no" in wealth:
        swordboss()
    else:
        swordleft()
    
def swordright():
    print "Ahead of you are some steping stones surrounded by lava."
    sleep(1)
    print "Do you pick the 'left' steping stone or the 'right' steping stone."
    first = raw_input("==> ")
    os.system('clear')
    if "left" in first:
        print "\033[1;31mThat's weird this stepping stone warps you back to the start of the room\033[0m"
        sleep(1)
        swordright()
    elif "right" in first:
        print "This doesn't feel to safe under foot"
        sleep(1)
        print "There are another 2 stepping stone in front of you"
        sleep(1)
        print "One on the 'left' and another to the far 'right'."
        sleep(1)
        second = raw_input("==> ")
        os.system('clear')
        if "right" in second:
            swordright1()
        elif "left" in second:
            print "\033[1;31mLooks like it was a warp stepping stone and sent you back to the start\033[0m"
            sleep(1)
            swordright()
        else:
            print "Don't take too long this stepping stone might give way"
            swordright()
    else:
        print "\033[1;31mHurry up you need to pick one.\033[0m"
        swordright()

def swordright1():
    print "I think i can see the other side and there is only 2 more stepping stones to pick 'left' or 'right'."
    sleep(1)
    first = raw_input("==> ")
    os.system('clear')
    if "right" in first:
        dead("The stepping stone gaveaway and you burnt in the lava.")
    elif "left" in first:
        print "Whoa way to go you made it to the other side alive."
        swordboss()
    else:
        print "\033[1;31mYou're really bugging me now just pick one already.\033[0m"
        swordright1()
    
    
    
def axestart():
    print "Wow that was a close shave, don't forget to close the door behind you."
    sleep(1)
    print "You are meet with two door one with flaking \033[1;34mlight blue\033[0m paint and the other is \033[1;33myellow\033[0m."
    sleep(1)
    pick = raw_input("==> ")
    os.system('clear')
    if "blue" in pick:
        print "I see the flaking \033[1;34mblue\033[0m paint didn't put you off."
        axeblue()
    elif "yellow" in pick:
        print "Is y\033[1;33mellow\033[0m you're favourite colour?"
        axeyellow()
    else:
        print "\033[1;31mYou need to pick one.\033[0m"
        axestart()

def axeblue():
    print "Looks like you have landed on your feet there is a chest in this room."
    sleep(1)
    print "There is lock on the chest and you have no key. do you want to 'break' the lock with your axe or just 'leave it'."
    sleep(1)
    pick = raw_input("==> ")
    os.system('clear')
    if "break" in pick:
        print "%r So you think you can break the lock then?" % name
        sleep(1)
        print "Here goes swing your axe."
        sleep(1)
        print "Drat you're axe broke but the chest stayed locked."
        sleep(1)
        os.system('clear')
        axeboss()
    elif "leave" in pick:
        print "I dowt there was anything in there anyway."
        os.system('clear')
        gotaxe()
    else:
        print "\033[1;31mYou need to make up you're mind about this chest.\033[0m"
        axeblue()

def axeyellow():
    print "What the hell is going on in here. Looks like a maths lesson is going on."
    sleep(1)
    print "The teacher is mumbling almost chanting some numbers to the class."
    sleep(1)
    print "He looks up over his glasses and bellows. %r you are late for you're test." % name
    sleep(1)
    print "To progress any further you must pass my math test."
    sleep(1)
    math1()
    
def math1():
    print "%r What is \033[1;36m45 + 65 =\033[0m" % name
    sleep(1)
    math = raw_input("==> ")
    os.system('clear')
    if math in "110":
        print "Currect"
        math2()
    else:
        print "\033[1;31mTry again.\033[0m"
        math1()
    
def math2():
    print "%r Im inpressed you got the first one right. Now try this on for size. \033[1;36m8 x 6 =\033[0m" % name
    sleep(1)
    math = raw_input("==> ")
    os.system('clear')
    if math in "48":
        print "Currect"
        math3()
    else:
        print "\033[1;31mTry again feeble one.\033[0m"
        math2()
        
def math3():
    print "%r Now you're just showing off. This should stump you. \033[1;36m57 ÷ 3 =\033[0m" % name
    sleep(1)
    math = raw_input("==> ")
    os.system('clear')
    if math in "19":
        print "Currect"
        math4()
    else:
        print "\033[1;31mI bet you forget to breath sometimes.\033[0m"
        math3()

def math4():
    print "%r This is a fluke i bet. This will crush your soul \033[1;36m765 - 38 =\033[0m" % name
    sleep(1)
    math = raw_input("==> ")
    os.system('clear')
    if math in "727":
        print "Currect"
        math5()
    else:
        print "\033[1;31mI knew it would crush you're soul.\033[0m"
        math4()
    
def math5():
    print "%r Last one now if you get this one right i will let you go. \033[1;36m12 x 7 =\033[0m" % name
    math = raw_input("==> ")
    os.system('clear')
    if math in "84":
        print "Drat you have excaped me for now. Watch you're back."
        gotaxe()
    else:
        print "\033[1;31mHAHAHA try again.\033[0m"
    
def gotaxe():
    print "%r I can't believe you made it this far alive" % name
    sleep(1)
    print "This looks like a very strange room, it's like there's a lake in here."
    sleep(1)
    print "%r I don't think you can swim with you're axe." % name
    sleep(1)
    print "Do you want to swim with your axe 'yes' or 'no'."
    question = raw_input("==> ")
    os.system('clear')
    if "no" in question:
        axeboss()
    elif "yes" in question:
        dead("Why didn't you take my advice and leave the Axe.")
    else:
        gotaxe()

def swordboss():
    print "%r You must be feeling really lucky because you have made it to the boss room." % name
    sleep(1)
    print "You're going to have to think on you're feet now and be quick."
    sleep(1)
    print "Holy crap it's a dragon. Are you going to 'strike first' or 'block'."
    sleep(1)
    first = raw_input("==> ")
    os.system('clear')
    if "first" in first:
        strikeboss()
    elif "block" in first:
        blockboss()
    else:
        swordboss()
        
def strikeboss():
    print "You strike the dragon's side with you're sword but it gets stuck in its scales."
    sleep(1)
    print "You strugle to get it free and the dragon blows fire in your face."
    sleep(1)
    dead("You should ask questions first then fire second excuse the pun.")
    
def blockboss():
    sleep(1)
    print "%r Good block there. You manage to get a sword swip in there." % name
    sleep(1)
    print "You got him good he looks pretty wounded."
    sleep(1)
    print "I think you killed him."
    sleep(1)
    os.system('clear')
    treasurerroom()

def treasurerroom():
    print "As you enter there room there stands 2 chests."
    sleep(1)
    print "One is all 'rusty' and the other is 'shinny'. Which do you choose."
    pick = raw_input("==> ")
    os.system('clear')
    if "shinny" in pick:
        for i in range(1):
            print random.randint(1, 100),"Pieces of \033[1;33mgold\033[0m"
            dead("That's what you get for being greedy")
    elif "rusty" in pick:
        for i in range(1):
            print random.randint(100, 1000),"Pieces of \033[1;33mgold\033[0m"
    else:
        treasurerroom()

    
def axeboss():
    print "%r You made it to the boss room." % name
    sleep(1)
    print "You're going to have to fight the goblin from befor."
    sleep(1)
    print "But this time he's found an AXE. What are you going to do 'punch' him or 'grab' the axe off him."
    pick = raw_input("==> ")
    os.system('clear')
    if "punch" in pick:
        punchboss()
    elif "grab" in pick:
        grabboss()
    else:
        "\033[1;31mYou need to pick one or the other.\033[0m"
        axeboss()
        
def punchboss():
        print "You punched him right in the face."
        sleep(1)
        print "He's that shocked he drops his AXE."
        sleep(1)
        print "Do you 'pick' up the axe or 'leave it'?"
        pick = raw_input("==> ")
        os.system('clear')
        if "pick" in pick:
            print "As you bend down to pick up the AXE the goblin claws you to death."
            dead("Why did you have to pick up the AXE.")
        elif "leave" in pick:
            print "You get a second go at the goblin, so you punch him again."
            sleep(1)
            print "This time you catch him off balance and he falls to his death."
            sleep(1)
            print "A door opens up to the treasurer room."
            os.system('clear')
            treasurerroom()
        else:
            print "\033[1;31mYou need to pick one.\033[0m"

def grabboss():
    print "%r You try and grab the axe from him but his grip is strong." % name
    sleep(1)
    print "Do you try 'harder' to pull it out or 'give' it up."
    pick = raw_input("==> ")
    os.system('clear')
    if "harder" in pick:
        print "%r You manage to get the AXE from the goblin." % name
        sleep(1)
        print "With one swipe of the AXE you behead him."
        os.system('clear')
        treasurerroom()
    elif "give" in pick:
        print "%r The goblin snatches his AXE back and with one swipe beheads you." % name
        dead("Why give up soo soon.")
    else:
        print "\033[1;31m%r What are you going to do?\033[0m" % name
        grabboss()

def dead(why):
    print why, "\033[1;31mYou're dead. Do you want to start over 'yes' or 'no'.\033[0m"
    question = raw_input("==> ")
    os.system('clear')
    if "yes" in question:
        start()
    elif "no" in question:
        exit()        
    else:
        dead(why)

def level_pick():
    while True:
        print "Pick a level number"
        print "1. Treasure room"
        print "2. Boss room sword"
        print "3. Boss room no axe"
        print "exit"
        level = raw_input("==> ")
        if level == "1":
            treasurerroom()
        elif level == "2":
            swordboss()
        elif level == "3":
            axeboss()
        elif level == "exit":
            exit()
        else:
            print "\033[1;31mPick again\033[0m."     
realstart() 

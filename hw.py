
def start():
    print("Hello welcome to our world!")
    print("You are in dark room...")
    print("please choose door #1 or #2:")

    uin = input("> ")

    if uin == "1":
        room1()
    elif uin == "2":
        room2()

def room1():
    print("welcome to room number 1!")
    print("Choose the door right or left?")

    uin = input("> ")

    if uin == "right":
        print("Going to be touch man!")
        tiger()
    elif uin == "left":
        print("You choose easy path lucky guy.")
        lion()
    else:
        print("sorry invalid input.error.")
        print("Let's start again..")
        room1()
            
def lion():
    print("o gossh! Here is deadly lion staring at you")
    print("""1. For asking chance from lion.
             2. For teasing lion""")
     
    uid = input("> ")

    if uid == "1":
        print("Only get chance to open door to escape.Solve some math's problems")
        easy()
    elif uid == "2":
        dead("You are idiot, lion smashes your face.")
    else:
        dead("Learn to type my friend.")

def dead(d):
    print(d,"Gameover>>>>")

def tiger():
    print("Welcome fock you are in hungry tiger room.")
    print("""1.Fill tiger hunger with some food.
          2.Just tease tiger.
          """)
    uid = input("> ")
    
    if uid == "1":
        print("Solve at least three math problem to feed tiger something.")
        hard()
    elif uid == "2":
        dead("Tiger ate you he was hungry")
    else:
        dead("Learn to type properly.")

def room2():
    print("Welcome to room number 2!")
    print("Choose the door right or left?")

    uin = input("> ")

    if uin == "right":
        print("Going to be tough man!")
        monster()
        
    elif uin == "left":
        print("You choosed easy path lucky guy.")
        devil_demo()

    else:
        print("sorry invalid input.error.")
        print("Let's start again.")
        room2()    

def easy():
    print("You will be asked 5 question answer at least 3.")
    qn =["Who is father of maths?","Who is father of trigonometry?","What is 2+1/2 ?","What is 7*7?","What is 5+5?"]
    a = ["","","","",""]
    
    count = 0
    for i in range(0,5):
        print(f"Qn.{i+1}",qn[i])
        a[i] = (input("> "))

    

    if a[0] == "archimedes":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    
    if a[1] == "hipparcus":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[2] == "3/2":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[3] == "49":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")
    if a[4] == "10":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")

    if count >= 3:
        print("You are winner!! you did it.")
    else:
        dead("You loose!!")

    


def hard():
    print("You will be asked 5 question answer at least 3.")
    qn =["What is the ans of lim x==>0 sinx/x",
         "What is derevative of sinx?",
         "What is calculated in interation?",
         "What is the area of curve x^3 from 0 to 3",
         "What  is general equation of circle passing origin?"]
    a = ["","","","",""]
    
    count = 0
    for i in range(0,5):
        print(f"Qn.{i+1}",qn[i])
        a[i] = (input("> "))

    

    if a[0] == "1":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    
    if a[1] == "cosx":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[2] == "area":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[3] == "81":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")
    if a[4] == "x^2+y^2=a^2":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")

    if count >= 3:
        print("You are winner!! you did it.")
    else:
        dead("You loose!!")


def monster():
    print("Welcome your entered to monster room.")
    print("""1.Monster is scientist he will ask you question to leave.
          2.Fight with monster.
          """)
    
    uin = input("> ")
    
    if uin == "1":
        print("Now time for some science quiz.")
        sc_quiz()
    elif uin == "2":
        dead("You are killed my monstor.")
    else:
        dead("Bro learn to type properly.")

def sc_quiz():
     print("You will be asked 5 question answer at least 3.")
     qn =["Who is known as father of science?",
         "Give an example of quantam particle.",
         "What is name of of our galxy?",
         "what is the speed of light?",
         "What is the famous energy equation of Elbert Einstein?"]
     a = ["","","","",""]
    
     count = 0
     for i in range(0,5):
         print(f"Qn.{i+1}",qn[i])
         a[i] = (input("> "))

    

     if a[0] == "elbert einstein":
        count+=1
        print(f"Your point is: {count}")
     else:
        print("")
    
     if a[1] == "boson" or a[1] == "hepton":
        count+=1
        print(f"Your point is: {count}")
     else:
        print("")
     if a[2] == "milkyway":
        count+=1
        print(f"Your point is: {count}")
     else:
        print("")
     if a[3] == "300000000":
        count+=1
        print(f"Your point is:{count}")
     else:
        print("")
     if a[4] == "e=mc^2":
        count+=1
        print(f"Your point is:{count}")
     else:
        print("")

     if count >= 3:
        print("You are winner!! you did it.")
     else:
        dead("You loose!!")

    

def devil_demo():
    print("hahaha !! you are in most dangerouus devil room.")
    print("""1.GO to illusion room if you can scape.
    2.Give up man.
    """)

    uin = input("> ")

    if uin == "1":
        print("Welcome you are in illuion room there are multiple door.")
        print("Try your luck to choose best door.")
        illusion_room()
    elif uin =="2":
        dead("You choosed death by your own.")
    else:
        dead("Learn to type brp!")

def illusion_room():
    print("""Choose your door....
             1.?mistery
             2.?mistery
             3.?mistery
             4.?mistery
             5.?mistery
          
          """)
    uin = input("> ")

    if uin == "1":
        tiger()
    elif uin == "2":
        lion()
    elif uin == "3":
        print("You scaped the traps you win.")
    elif uin == "4":
        monster()
    elif uin == "5":
        mistery_room()
    else:
        dead("Learn to type bro!")
    
def mistery_room():
    print("You are in danger now ! Here is all animals and demons.")
    print("Ans me the riddle question.")
    print("\n")
    print("You will be asked 5 question answer at least 3.")
    qn =["What can you catch but can't throw?",
         "What has one eye but can't see?",
         "What appears once in a minute, twice in a moment, but never in a thousand years?",
         "I can go all around the world but never leave my corner. What am I? ",
         "If you drop me, I crack. If you smile at me, I smile back. What am I? "]
    a = ["","","","",""]
    
    count = 0
    for i in range(0,5):
        print(f"Qn.{i+1}",qn[i])
        a[i] = (input("> "))

    

    if a[0] == "a cold":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    
    if a[1] == "a needle":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[2] == "a letter m":
        count+=1
        print(f"Your point is: {count}")
    else:
        print("")
    if a[3] == "a stamp":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")
    if a[4] == "a mirror":
        count+=1
        print(f"Your point is:{count}")
    else:
        print("")

    if count >= 3:
        print("You are winner!! you did it.")
    else:
        dead("You loose!!")

start()






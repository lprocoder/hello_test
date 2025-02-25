from random import randint
from textwrap import dedent

class CodeGenerator:
    def __init__(self):
        self.code1 = randint(0, 9)
        self.code2 = randint(0, 9)
        self.random_room1 = randint(1, 9)
        
        # Ensure the second room is different
        while True:
            self.random_room2 = randint(1, 9)
            if self.random_room2 != self.random_room1:
                break

    def get_code_pair(self):
        return str(self.code1) + str(self.code2) if randint(0, 1) else str(self.code2) + str(self.code1)

class Room:
    def __init__(self, room_number, code_generator):
        self.room_number = room_number
        self.code_generator = code_generator

    def check_room(self):
        if self.room_number == self.code_generator.random_room1:
            return str(self.code_generator.code1)
        elif self.room_number == self.code_generator.random_room2:
            return str(self.code_generator.code2)
        else:
            return None

class Map:
    def __init__(self, level):
        self.level = level
        self.code_generator = CodeGenerator()
        self.correct_code = self.code_generator.get_code_pair()
        self.rooms = {i: Room(i, self.code_generator) for i in range(1, 10)}
        self.play()
    
    def play(self):
        print(dedent(f"""
            Welcome to Map {self.level}! Explore the rooms to find the 2D code.
            Choose a room to search (1-9) or enter 'door' to proceed.
        """))
        
        found_codes = []
        while len(found_codes) < 2:
            choice = input("Enter room number (or 'door' if you have both codes): ")
            if choice.isdigit() and 1 <= int(choice) <= 9:
                code = self.rooms[int(choice)].check_room()
                if code and code not in found_codes:
                    found_codes.append(code)
                    print(f"You found a 1D code: {code}")
                else:
                    print("This room is empty, no code available.")
            elif choice.lower() == 'door' and len(found_codes) == 2:
                self.check_code("".join(found_codes))
                return
            else:
                print("Invalid input. Keep searching!")
        
        self.check_code("".join(found_codes))
    
    def check_code(self, entered_code):
        print("Enter the code to go to the next map:")
        #print("(Hint for debugging: Correct code is)", self.correct_code)
        user_input = input("Please enter your 2D code: ")
        if user_input == self.correct_code:
            print(f"Correct! Moving to Map {self.level + 1}.")
            if self.level < 4:
                Map(self.level + 1)
            else:
                print("Congratulations! You escaped successfully!")
        else:
            print("Incorrect code! Restarting...")
            if self.level == 4:
                Map(1)
            else:
                Map(self.level)

# Start the game
Map(1)

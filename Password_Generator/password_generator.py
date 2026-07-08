class Password_Generator:
    def __init__(self) -> None:
        self.characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "F", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%" , "&", "*", "+" , "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.characters_no_symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "F", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def password_generator(self):
        import random
        rng = random.randint(8, 16)
        self.password = ""
        for _ in range(0, rng):
            self.password += random.choice(self.characters)
        return self.password
    
    def password_generator_no_symbols(self):
        import random
        rng = random.randint(8, 16)
        self.password = ""
        for _ in range(0, rng):
            self.password += random.choice(self.characters_no_symbols)
        return self.password


'''
from random import choice, randint, shuffle

password_letters = [choice(letters) for _ range(randint(8, 16))]
password_symbols = [choice(symbols) _ range(randint(2, 6))]
password_numbers = [choice(numbers) for _ range(randint(2, 6))]

password_list = password_letters + password_symbols + password_numbers
random.shuffle.password_list
password = "".join(password_list)
'''
import random
from collections import Counter

Intents = {
    "what is your name?" : "XDEA",
    "do you like humans?" : ["No."]
}

class XDEA:
    
    def __init__(self, Intents):
        self.Intents = Intents
        self.q_keys = list(self.Intents.keys())
        
    def most_common(self, lst):
        data = Counter(lst)
        if lst != []:
            return max(lst, key=data.get)
        if lst == []:
            return "I do not know."
    
    def chat(self):
        player = ""
        while player != "q":
            print('<user> :: ',end='')
            player = input()
            if not player in self.Intents:
                print("Adding question to database...")
                self.Intents[player] = []
                self.q_keys.append(player)
            else:
                print(f'<bot> :: {self.most_common(self.Intents.get(player))}')
            question = random.choice(self.q_keys)
            print(question)
            print('<user> :: ',end='')
            player = input()
            print("Loging response into database...")
            a = self.Intents.get(question)
            a.append(player)
            self.Intents[question] = a
            print("I'm ready!")
            

XDEA(Intents=Intents).chat()
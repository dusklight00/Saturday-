import json
import random
from collections import Counter

Intents = {"what is your name?": "XDEA", "do you like humans?": ["No."]}


class XDEA:

  def __init__(self, Intents, LogFile):
    self.Intents = Intents
    self.q_keys = list(self.Intents.keys())
    self.LogFile = LogFile
    with open(LogFile, 'r') as f:
      self.Log = json.load(f)

  def most_common(self, lst):
    data = Counter(lst)
    if lst != []:
      return max(lst, key=data.get)

    if lst == []:
      return "I do not know."

  def updateLog(self):
    with open(self.LogFile, 'w') as f:
      json.dump(self.Intents, f)

  def chat(self):

    player = ""
    while player != "q":
      print('\n[you] | >_ ', end='')
      player = input()
      if player not in self.Intents:

        self.Intents[player] = []
        self.q_keys.append(player)
      else:
        print('[bot] | >_ ', {self.most_common(self.Intents.get(player))})
      question = random.choice(self.q_keys)
      print('[bot] | >_ ', question)
      print('\n[you] | >_ ', end='')
      player = input()

      a = self.Intents.get(question, [])
      if not isinstance(a, list):
        a = [a]

      a.append(player)
      self.Intents[question] = a
      self.updateLog()
      # print(Intents)


XDEA(Intents=Intents, LogFile='ChatData/intents.json').chat()

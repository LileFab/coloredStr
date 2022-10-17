import random
import time as t

from colorama import init
from termcolor import colored

init()
tab = ['red', 'green', 'yellow']
mot = "Robin = Gobeur de pioche"

while 1:
  for i in mot:
    nb = random.randrange(len(tab))
    couleur = tab[nb]
    print(colored(i, couleur), end="")
    t.sleep(0.05)
  print("")
  t.sleep(0.7)

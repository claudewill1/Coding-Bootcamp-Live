from classes.pirates import Pirate
from classes.ninjas import Ninja

michaelangelo = Ninja("MichaelAngelo")
jack_sparrow = Pirate("Jack Sparrow")

michaelangelo.show_stats()
jack_sparrow.show_stats()

nPlayers = []
pPlayers = []
nPlayers.append(michaelangelo)
pPlayers.append(jack_sparrow)



def loop(arr01, arr02):
    game = True
    while game:
        for n in arr01:
            if n.health < 0:
                arr01.remove(n)
                if len(arr01) < 1:
                    print(f"The Pirates Won")
                    game = False
                    return 0
            else:
                for p in arr02:
                    n.attack(p)
        for p in arr02:
            if p.health < 0:
                arr01.remote(p)
                if len(arr02) < 1:
                    print("Ninja's Won!")
                    game = False
                    return 0
            else:
                for n in arr01:
                    p.attack(n)

loop(nPlayers,pPlayers)
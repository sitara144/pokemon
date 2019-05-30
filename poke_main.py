from pokemon import Pokemon
from Ice import Ice
#from fire import Fire,Ghost,Flying,Fairy,Grass,Dark
from bug import Bug,Ghost,Flying,Fighting,Grass,Dark

bug =Bug("buggie",'trainer1',50)
grass=Grass("grassie","trainer2",80)
dark=Dark("D","y",100)
ghost=Ghost("ghostie","trainer3",40)


bug.attack(ghost)
ghost.attack(bug)
bug.attack(grass)
bug.attack(dark)

#print("Icy is attacking",p2.__str__())
#p2.attack(p1)'''


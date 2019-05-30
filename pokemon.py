
class Pokemon:
    basic_attack = 'tackle'
    damage =40


    def __init__(self, name, trainer,hp):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False
    def __str__(self):
        x=self.__repr__()

        y=x.index(".")
        g=x.find(" ",y)
        d=x[y+1:g]
        return d

    def speak(self):
        print(self.name + '!')

    def attack(self,other):

        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self,damage):
        print("dam",damage)
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')
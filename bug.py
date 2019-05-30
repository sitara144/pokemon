from pokemon import Pokemon


class Bug(Pokemon):
    basic_attack="Signal Beam"
    prob =0.3
    enemy_strong = ["Fighting", "Flying", "Poison", "Ghost", "Fire", "Fairy"]
    enemy_weak= ["Grass", "Psychic", "Dark"]

    def attack(self,other):
        self.speak()
        print(self.name,'used',self.basic_attack,'! on',other.name)

        if other.__str__() in self.enemy_weak:

            other.receive_damage((self.damage)//2)
        if other.__str__() in self.enemy_strong:

            other.receive_damage(self.damage*2)

        #print("here",self.__str__(),other.__str__())
      #print(isinstance(self.__class__,other.__class__))

        if other.level > self.prob and isinstance(other.__class__,self.__class__) == False:
            other.paralyzed =True
            print(other.name,'is confused')

class Fairy(Pokemon):
        basic_attack = "Blaze kick"
        prob = 1
        enemy_strong = ["poison" "Fire"]
        enemy_weak = ["Fighting","Dragon" ,"Dark"]
        def attack(self, other):
            #print(other.name)
            # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
            # 	weak-Fire, Water, Ice
            self.speak()
            print(self.name, 'used', self.basic_attack, '! on', other.name)
            #print("pokemon attacked is", other.name)

            if other.__str__() in self.enemy_weak:
                # print("weak enemy")
                other.receive_damage((self.damage) // 2)
            if other.__str__() in self.enemy_strong:
                # print("strong enemy")
                other.receive_damage(self.damage * 2)
            #print(type(other))

            #print(self, other)
            #print(isinstance(self.__class__, other.__class__))

            if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
                other.paralyzed = True
                print(other.name, 'is burned')


class Ghost(Pokemon):
    basic_attack = "lick"
    prob = 0.3
    enemy_strong = ["Dark"]
    enemy_weak = ["Ghost", "Psychic"]

    def attack(self, other):
        print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        #print("pokemon attacked is", other.name, other.__str__())
        if other.__str__() in self.enemy_weak:
            #print("weak enemy")
            other.receive_damage((self.damage) // 2)
        if other.__str__() in self.enemy_strong:
            #print("strong enemy")
            other.receive_damage(self.damage * 2)

        #print(type(other))

        #print(self, other)
        #print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Flying(Pokemon):
    basic_attack = "Bounce"
    prob = 0.3
    enemy_strong = ["Electric"]
    enemy_weak = ["Fighting","Bug" ,"Grass","Fairy"]


    def attack(self, other):
        #print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        #print("pokemon attacked is", other.name)
        other.receive_damage(self.damage)
        #print(type(other))

        #print(self, other)
        #print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Fighting(Pokemon):
    basic_attack = "Blaze kick"
    prob = 0.3
    enemy_strong = ["Dark"]
    enemy_weak = ["Ghost", "Psychic"]

    def attack(self, other):
        print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        #print("pokemon attacked is", other.name)
        other.receive_damage(self.damage)
        if other.__str__() in self.enemy_weak:
            #print("weak enemy")
            other.receive_damage((self.damage) // 2)
        if other.__str__() in self.enemy_strong:
            #print("strong enemy")
            other.receive_damage(self.damage * 2)
        #print(type(other))

        #print(self, other)
        #print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Poison(Pokemon):
    basic_attack = "Blaze kick"
    prob = 0.3
    enemy_weak = ["Grass","Fairy"]
    enemy_strong = ["Poison", "Ghost"]

    def attack(self, other):
        print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        #print("pokemon attacked is", other.name)
        other.receive_damage(self.damage)
        if other.__str__() in self.enemy_weak:
            #print("weak enemy")
            other.receive_damage((self.damage) // 2)
        if other.__str__() in self.enemy_strong:
            #print("strong enemy")
            other.receive_damage(self.damage * 2)
        #print(type(other))

        #print(self, other)
        #print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Grass(Pokemon):
    basic_attack = "lick"
    prob = 0.3
    enemy_weak = ["Dark"]
    enemy_strong = ["Ghost", "Psychic", "Dark"]

    def attack(self, other):
        print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        print("pokemon attacked is", other.name, other.__str__())
        if other.__str__() in self.enemy_weak:
            print("weak enemy")
            other.receive_damage((self.damage) // 2)
        if other.__str__() in self.enemy_strong:
            print("strong enemy")
            other.receive_damage(self.damage * 2)

        print(type(other))

        print(self, other)
        print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Dark(Pokemon):
    basic_attack = "Fling"
    prob = 1
    enemy_weak = ["Fighting", "Dark", "Fairy"]
    enemy_strong = ["Ghost", "Psychic"]

    def attack(self, other):
        print(other.name)
        # Ice	Freeze Shock	0.3	strong-Flying, Grass, Dragon\
        # 	weak-Fire, Water, Ice
        self.speak()
        print(self.name, 'used', self.basic_attack, '! on', other.name)
        print("pokemon attacked is", other.name, other.__str__())
        if other.__str__() in self.enemy_weak:
            print("weak enemy")
            other.receive_damage((self.damage) // 2)
        if other.__str__() in self.enemy_strong:
            print("strong enemy")
            other.receive_damage(self.damage * 2)

        print(type(other))

        print(self, other)
        print(isinstance(self.__class__, other.__class__))

        if other.level > self.prob and isinstance(other.__class__, self.__class__) == False:
            other.paralyzed = True
            print(other.name, 'is burned')


class Character:

    def __init__(self,name,race,clas,health):
        self.name = name
        self.race = race
        self.clas = clas
        self.skills = []
        self.inventory = []
        self.health = health
        self.level = 1
        self.experience = 0

    def setSkill(self,name,description,values,id):
        skillDict = {}
        skillDict.update({"Name":name,"Description":description,"Values":values,"ID":id})

        self.skills.append(skillDict)

        backlogString = "Character {self.name} learned the skill {name}".format(**vars())

        return backlogString

    def getSkill(self,id):

        for skill in self.skills:
            if skill.get('ID') == id:
                return skill
            else:
                return None

    def setItem(self,name,type,atribute,description,id):
        itemDict = {}
        itemDict.update({"Name":name,"Description":description,"Atribute":atribute,"ID":id,"Type":type})

        self.inventory.append(itemDict)

        backlogString = "Character {self.name} added the item {name} to inventory";format(**vars())

        return backlogString

    def getItem(self,id):

        for item in self.inventory:
            if item.get('ID') == id:
                return item
            else:
                return None

    def setHealth(self,flag,value):

        if flag == "INCREASE":
            self.health += value
            backlogString = "Character {self.name} take {value} of damage"

            return baclkogString

        elif flag == "DECREASE":
            self.health -= value
            backlogString = "Character {self.name} heals {value} of health"

            return backlogString

    def increaseXP(self,value):
        self.experience += value
        backlogString = "Character {self.name} gained {value} of experience"

        return backlogString

    def increaseLevel(self):
        self.level += 1
        self.experience = 0

        backlogString = "Character {self.name} passed to level {self.level}"

        return backlogString

    

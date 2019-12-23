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

    def getItem(self,id):

        for item in self.inventory:
            if item.get('ID') == id:
                return item
            else:
                return None

    def setHealth(self,flag,value):

        if flag == "INCREASE":
            self.health += value

        elif flag == "DECREASE":
            self.health -= value
    
    def increaseXP(self,value):
        self.experience += value
    
    def increaseLevel(self):
        self.level += 1

    

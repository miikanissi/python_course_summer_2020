class Member:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def getInfo(self):
        memberInfo = self.name + ", " + self.role
        return memberInfo

class Group:
    def __init__(self, name, member1, member2, member3):
        self.name = name
        self.member1 = member1
        self.member2 = member2
        self.member3 = member3

    def returnGroupData(self):
        groupData = "Groups name is " + str(self.name)
        groupData += "\n First member: " + self.member1.getInfo();
        groupData += "\n Second member: " + self.member2.getInfo();
        groupData += "\n Third member: " + self.member3.getInfo();
        return groupData

member1 = Member("Chris", "Leader")
member2 = Member("Thomas", "Assistant")
member3 = Member("Michael", "Accountant")
print(member2.getInfo())

group1 = Group("Startup", member1, member2, member3)
print(group1.returnGroupData())

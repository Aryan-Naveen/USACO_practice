"""
ID: Aryan Naveen
LANG: PYTHON2
TASK: gift1
"""

class friend():
    def __init__(self, name):
        self.name = name
        self.balance = 0
    
    def giving(self, amount, num):
        if(not num==0):
            gift = int(amount/num) * num
            self.balance -= gift
            return int(amount/num)
        else:
            return 0
            
    def recieving(self, amount):
        self.balance += amount

class gift():
    def __init__(self, input):
        self.giver_name = input[0]
    #    print("sad")
        self.amount = int(input[1][:input[1].find(" ")])
        # print('safd')
        self.num_friends = int(input[1][input[1].find(" ") + 1:])
        # print("dfew")
        self.friend_names = input[2:]
        # print("sfds")

    def transfer(self, friends):
        recieving_friends=[]
        for friend in friends:
            if(friend.name==self.giver_name):
                giver = friend
            if(friend.name in self.friend_names):
                recieving_friends.append(friend)
        
        gift = giver.giving(self.amount, self.num_friends)

        for friend in recieving_friends:
            friend.recieving(gift)

fin = open("gift1.in", 'r')
input = fin.read().splitlines()
fin.close()

num_friends = int(input[0])
input = input[1:]

friends = []
for i in range(num_friends):
    friends.append(friend(input[i]))

input = input[num_friends:]

while(len(input)>0):
    num_lines = int(input[1][input[1].find(" ") + 1:])
    gift(input[:num_lines+2]).transfer(friends)
    input = input[num_lines+2:]


fout = open("gift1.out", 'w')
output = ""
for friend in friends:
    output += friend.name + " " + str(friend.balance) + "\n"

fout.write(output)


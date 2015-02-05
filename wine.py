import operator, collections

class person:
    def __init__(self, n):
        self.name = n
        self.wine = []
        self.count = 0

class wine:
    def __init__(self, n):
        self.name = n
        self.person = []
        self.count = 0

def initialize():
    fp = open("person_wine_5.txt", 'r')
    people = {}
    drink = {}
    taste = {}
    for line in fp:
        per = line.strip().split("\t")
        if per[0] not in people:
            p = person(per[0]) 
            people[per[0]] = p
        if per[1] not in drink:
            w = wine(per[1])
            drink[per[1]] = w
            taste[per[1]] = 0
        if per[1] in drink and per[0] in people:
            taste[per[1]] += 1
            drink[per[1]].person.append(people[per[0]])
            people[per[0]].wine.append(drink[per[1]])
    fp.close()
    assign(taste, people, drink)

def assign(taste, people, drink): 
    bought = {}
    for y in sorted(taste.items(), key = operator.itemgetter(1)):
        n = len(drink[y[0]].person)
        p = sorted(drink[y[0]].person, key= lambda person: person.count)[0]
        if n == 1 and p.count < 3:
            bought[drink[y[0]]] = p.name
            p.count += 1
            drink[y[0]].person.append(p)
        else:
            if p.count < 3:
                bought[drink[y[0]]] = p.name
                p.count += 1
                drink[y[0]].person.append(p)
    display(bought)

def display(bought):
    out = open('output.txt', 'w')
    print>>out, len(bought)
    for x in bought.keys():
        print>>out, bought[x] + "\t" + x.name
    out.close()

initialize()

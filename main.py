import json
from agent import AgentRoute
from distance import Distance
from point import Point

def readDistances():
     f = open('distances.json')
     data = json.load(f)
     return data


def readPoints():
     f = open('points.json')
     data = json.load(f)
     return data

def getPoints():
    allPoints = []
    data = readPoints()
    for i in data:
        allPoints.append(Point(i["id"], i["address"], i["turistic"], i["qtd"]))
    return allPoints


def generatePointsMap():
    pointsFinal = {}

    for i in distances:
        points = []
        for j in distances:
            if(i.start == j.start):
                points.append(j.end[0])
        pointsFinal[i.start[0]] = points
    return pointsFinal

def generateDistances():
   data = readDistances()
   
   for i in data:
        split = i["id"].split('-')
        
        start, end = split[0], split[1]
        distances.append(Distance(start, end, i["distance"]))

def listPoints():
    for i in points:
        print(i.toString())

distances = []

generateDistances()

pointsSegment = generatePointsMap()

points = getPoints()

print("Todas as paradas possiveis:\n\n")

listPoints()

agentRoute = AgentRoute(distances, points, pointsSegment)


start = input("\n\n\nPor favor digite seu ponto de partida:\n")
end = input("Por favor digite seu ponto de destino:\n")

print(agentRoute.calculeRoute(start, end))
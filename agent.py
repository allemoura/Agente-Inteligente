from distance import Distance
from point import Point

class AgentRoute:
    def __init__(self, distances, points, pointsSegment):
        self.distances = distances,
        self.points = points
        self.pointsSegment = pointsSegment
    
    def main(self, start, end):
        print(self.calculeRoute(start, end))

    def getDistance(self, start, end):
        distance = None
        
        for i in self.distances[0]:
            if(i.start[0].upper() == start.upper() and i.end[0].upper() == end.upper()):
                distance = i
                break
        return distance

    def calculeRoute(self, start, end):
        point = start
        pointsFinal = [self.findPoint(start)]
        routes = [start.upper()]
        errorMessage = None

        while(end.upper() not in routes and errorMessage == None):
            
            points = self.pointsSegment.get(point.upper())
            distanceNew = 1000000000000
            distanceNewTotal = 100000000
            turistics = 0
            newPoint = None
            pointNewFinal = None

            for p in points:
                if(p != point.upper()):
                    distanceStart = self.getDistance(point.upper(), p)
                    distanceEnd = self.getDistance(p,end)

                    if(distanceStart == None) :break
                    
                    if(distanceEnd == None): distanceTotal = distanceStart.distance
                    else: distanceTotal = distanceStart.distance + distanceEnd.distance
                    
                    limiar = distanceTotal - distanceNew
                    pointNew = self.findPoint(p)
                    
                    if( distanceTotal >= 0 and distanceTotal <= distanceNewTotal and 
                        p.upper() not in routes or 
                        (pointNew.qtd >= turistics and limiar > 0 and limiar <= 10) ):
                        newPoint = p
                        distanceNew = distanceStart.distance
                        turistics = pointNew.qtd
                        distanceNewTotal = distanceStart.distance
                        pointNewFinal = pointNew

            if(newPoint == None):
                errorMessage = "Não foi possivel calcular esta rota"
                break
            
            point = newPoint
            routes.append(newPoint)
            pointsFinal.append(pointNewFinal)
        if(errorMessage != None):
            return errorMessage
        else:
            final = "Você vai passar pelos seguintes pontos:\n\n"

            for i in pointsFinal:
                final += i.toString()
                final += "\n"
            return final

    def findPoint(self, point):
        for i in  self.points:
            if(i.point[0] == point.upper()):
                return i

    pass


class Point:
    
    def __init__(self, point, address, turistic, qtd):
        self.point = point,
        self.address = address,
        self.turistic = turistic,
        self.qtd = qtd,

    def toString(self):
        if(self.qtd[0] == 0):
            return "Este é o ponto " + self.point[0]  + " que é a parada " + self.address[0] + " ele não tem nenhum ponto turistico."
        return "Este é o ponto " + self.point[0]  + " que é a parada " + self.address[0] +  " que tem " + str(self.qtd[0]) + " pontos turisticos: " + self.turistic[0] + ".\n"
    pass

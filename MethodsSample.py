class Cookie:
    def __init__(self, color):
        self.color=color
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
cookie1 = Cookie('Green')
cookie2 = Cookie('Blue')

print(cookie1.getColor())
cookie1.setColor('Red')
print(cookie1.getColor())
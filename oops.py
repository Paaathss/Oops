#class creation
class Person:
    def read(self):
        print('person is reading')

    def write(self):
        print('person is writing')

#object creation

obj = Person()
obj.read()
obj.write()

obj6 = Person


class House:
    def home(self,name,color,floor_material,roof_color):
        self.name = name
        self.color = color
        self.floor_material = floor_material
        self.roof_color = roof_color

    def myhome(self):
            print('person name is %s color is %s floor_material is %s roof_color %s'%(self.name,self.color,self.floor_material,self.roof_color))
raju = House()
raju.home('fathim','white','marble','blue')
raju.myhome()
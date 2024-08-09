class House:
    def __init__(self,name,color,floor_material,roof_color):



            name = input('Enter the name :')
            color = input('Enter the color :')
            floor_material = input('Enter the floor_material:')
            self.roof_color = input('Enter the roof_color :')


            self.name = name
            self.color = color
            self.floor_material = floor_material
            self.roof_color = roof_color
    def myhome(self):
         print('person name is %s color is %s floor_material is %s roof_color %s'%(self.name,self.color,self.floor_material,self.roof_color))
n = int(input('Enter how much person you want to add:'))
for i in range(n):

    raju = House('fathim', 'white', 'marble', 'blue')
    raju.myhome()







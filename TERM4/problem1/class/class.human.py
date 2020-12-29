class human:
    hair_color =None
    eye_color=None
    skin_color = None
    gender = None
    heught= None


    def call(self):
        return f"{self.name}{self.family}"

   


p = Human()
p.name = 'Alireza'
p.family= 'Tofiqi'
p.hair_color= 'black'
p.gender = 'm'
p.height = '173'
print(p.call())
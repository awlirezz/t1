class Game:
    name = None
    year = None
    mode = None 
    company=None
    
    def call(self):
        return f"{self.name}released in {self.year}"


d = Game()    
d.name='The Last of Us'
d.year='July 29 2014'
d.mode='third person'
d.company='Naughty Dog'
print(d.call())
d.call()
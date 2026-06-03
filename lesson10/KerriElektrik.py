from perseritje import Kerri

class KerriElektrik(Kerri):
    def __init__(self,name,ngjyra,viti,bateria):
        super().__init__(name,ngjyra,viti)
        self.bateria = bateria

    def rriteShpejtesi(self):
        print("Shpejtesia nuk eshte duke u rritur")
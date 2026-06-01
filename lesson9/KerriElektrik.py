from perseritje import Kerri


class KerriElektrik(Kerri):
    def __init__(self,ngjyra, vitiIProdhimit, bateria):
        super().__init__(ngjyra,vitiIProdhimit)
        self.bateria=bateria


    def mbusheBaterin(self):
        print("bateria eshte duke u mbushur")
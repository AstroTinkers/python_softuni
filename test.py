class MoiatKlas:
    __spodeleno = 10

    def __init__(self, n):
        self.nespodeleno = n

    def namali_spodeleno(self):
        MoiatKlas.__spodeleno -= 1

    def izpinti(self):
        print(f"{self.nespodeleno} {MoiatKlas.__spodeleno}")


klas1 = MoiatKlas(1)
klas2 = MoiatKlas(2)

klas1.izpinti()  # 1 10
klas2.izpinti()  # 2 10
klas1.namali_spodeleno()
MoiatKlas.klas  # 1 9
klas2.izpinti()  # 2 9
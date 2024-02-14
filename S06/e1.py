class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):   #self para acceder a las caracteristicas del objeto
        self.strbases = strbases
        bases = ["A", "C", "G", "T"]
        for i in strbases:
            if i in bases:
                solution = True
            else:
                solution = False
                break
        if solution:
            print("New sequence created")
        else:
            self.strbases = "ERROR"
            print("ERROR")
    def __str__(self):
        return self.strbases
s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")


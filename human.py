class Human:

    #built-in
    name = "Hava"

    #constructor - initialize
    def __init__(self, name, sentence):
        self.name = name
        self.sentence = sentence

    def talk(self):
        print(f"{self.name}: {self.sentence}")

    def __str__(self):   #iligili nesne print edilmek istendiginde, ne döndürsün veya ekrana ne yazsin
        return f"STR function returns: {self.name}"
    
    def walk(self):
        print(f"{self.name} is walking.")
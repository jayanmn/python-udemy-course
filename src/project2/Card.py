class Card():
    def __init__(self, name, value, shade):
        self.name = name
        self.value = value
        self.shade = shade
        self.hidden = False

    def __str__(self):
        if self.hidden is True:
            return "Hidden"
        else:
            return f"{self.name} of {self.shade}"

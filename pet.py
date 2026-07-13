class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 80

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Hunger: {self.hunger}\n"
        )

    def feed(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        print(f"{self.name} is playing")
class Manager:
    def __init__(self, name, works_at_shelter):
        self.name = name
        self.shelter = works_at_shelter

    def feed_all_pets(self):
        pets = self.shelter.get_all_pets()
        for pet in pets:
            pet.feed()

    def play_all_pets(self):
        pets = self.shelter.get_all_pets()
        for pet in pets:
            pet.play()
            print(pet)
class PetShelter:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def find_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def add_pet(self, pet):
        if self.find_pet(pet.name) is None:
            self.pets.append(pet)
        else:
            print(f"A pet with this name {pet.name} already exists.")

    def get_all_pets(self):
        return self.pets
from pet import Pet
from pet_shelter import PetShelter
from manager import Manager


def main():
    print("Pet Shelter")

    shelter = PetShelter("Happy Tails")
    manager = Manager("Alex", shelter)

    dog = Pet("Buddy", 3)
    cat = Pet("Whiskers", 2)

    shelter.add_pet(dog)
    shelter.add_pet(cat)

    print("\n--- Playing with all pets ---")
    manager.play_all_pets()

    print("--- Feeding all pets ---")
    manager.feed_all_pets()


if __name__ == "__main__":
    main()
if __name__ == "__main__":
    shelter = PetShelter("Happy Tails")
    manager = Manager("Alex", shelter)

    dog = Pet("Buddy", 3)
    cat = Pet("Whiskers", 2)

    shelter.add_pet(dog)
    shelter.add_pet(cat)
    shelter.add_pet(dog)

    print("\n--- Playing with all pets ---")
    manager.play_all_pets()

    print("--- Feeding all pets ---")
    manager.feed_all_pets()

    print("--- Checking status after feeding ---")
    for pet in shelter.get_all_pets():
        print(pet)
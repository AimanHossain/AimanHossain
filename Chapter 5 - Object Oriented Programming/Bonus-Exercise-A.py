class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

    @classmethod
    def create_from_user_input(cls):
        name = input("Enter the name of the animal: ")
        species = input("Enter the species of the animal: ")
        age = input("Enter the age of the animal: ")

        # You can add validation or error handling for user input as needed

        return cls(name, species, age)

if __name__ == "__main__":
    # Create two instances of the Animal class using user input
    animal1 = Animal.create_from_user_input()
    animal2 = Animal.create_from_user_input()

    # Display information for each animal
    print("\nAnimal 1:")
    animal1.display_info()

    print("\nAnimal 2:")
    animal2.display_info()

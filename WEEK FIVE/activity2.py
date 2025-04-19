# Derived classes and polymorphism
class Horse:
    def speak(self):
        return "Neigh!"

class Bird:
    def speak(self):
        return "Chirp!"
    
class Snake:
    def speak(self):
        return "Hiss!"
    
class Lion:
    def speak(self):
        return "Roar!"

# Polymorphism in action
for animal in [Horse(), Bird(), Snake(), Lion()]:
    print(animal.speak())
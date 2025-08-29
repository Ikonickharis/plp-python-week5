class Superhero:
    def __init__(self, name, alias, power_level):
        self.name = name
        self.alias = alias
        self._power_level = power_level  # Encapsulated (protected) attribute

    def introduce(self):
        return f"I am {self.alias}, also known as {self.name}!"

    def use_power(self):
        return f"{self.alias} uses their generic superpower!"

    def get_power_level(self):
        return self._power_level

    def set_power_level(self, new_level):
        if new_level >= 0:
            self._power_level = new_level
        else:
            print("Power level cannot be negative.")

# Subclass: Speedster
class Speedster(Superhero):
    def __init__(self, name, alias, power_level, max_speed):
        super().__init__(name, alias, power_level)
        self.max_speed = max_speed  # Additional attribute

    # Polymorphism: override use_power
    def use_power(self):
        return f"{self.alias} blazes past at {self.max_speed} mph!"

    def time_travel(self):
        if self._power_level >= 80:
            return f"{self.alias} breaks the time barrier!"
        else:
            return f"{self.alias} is too weak to time travel."


# Creating instances
hero1 = Superhero("Clark Kent", "Superman", 95)
hero2 = Speedster("Barry Allen", "The Flash", 85, 1500)

# Interactions
print(hero1.introduce())
print(hero1.use_power())
print()

print(hero2.introduce())
print(hero2.use_power())
print(hero2.time_travel())

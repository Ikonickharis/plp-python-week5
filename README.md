🦸‍♂️ Superhero Python Project

This is a simple Object-Oriented Programming (OOP) example in Python that simulates superheroes with different abilities. The code demonstrates key OOP concepts such as inheritance, polymorphism, encapsulation, and constructor overloading.

📚 Features

Create general superheroes with names, aliases, and power levels.

Specialized Speedster superheroes with additional speed and time-travel capabilities.

Encapsulated attributes using getter/setter methods.

Demonstrates polymorphism by overriding methods in subclasses.

🛠️ Technologies Used

Python 3.x

No external libraries required

🧱 Classes
Superhero

A base class representing any superhero.

Attributes:

name: Real name of the superhero

alias: Hero name

_power_level: (Protected) Integer representing power strength

Methods:

introduce(): Returns a formatted string introducing the hero

use_power(): Generic power usage message

get_power_level(): Returns the current power level

set_power_level(level): Sets the power level (cannot be negative)

Speedster (inherits from Superhero)

A specialized hero with incredible speed.

Additional Attribute:

max_speed: Maximum speed in mph

Overridden Method:

use_power(): Describes the speed power uniquely

New Method:

time_travel(): Checks if power level is high enough to time travel

🚀 Usage

Clone or copy the code and run it in any Python 3 environment:

# Zoo-Management-System
A Zoo Management System built in Python demonstrating OOP concepts such as inheritance, encapsulation, polymorphism, abstract classes, and operator overloading. Includes simulation of animals, employees, and enclosures.


📌 Project Description

This project is a Zoo Management System implemented in Python, designed as part of an Object-Oriented Programming (OOP) assignment.
The system models real-world zoo operations such as animal management, employee tasks, and enclosure handling while applying core OOP principles.

The project demonstrates:
	•	Inheritance (single, multilevel, hierarchical, multiple)
	•	Encapsulation (private attributes, property decorators)
	•	Polymorphism (method overriding, duck typing)
	•	Abstract Base Classes (ABC)
	•	Special methods like _str, __add, and __iter_
	•	Class & static methods

⸻

🎯 Features

Phase 1: Core Implementation
	•	Animal hierarchy with 5+ subclasses (Lion, Penguin, Snake, etc.)
	•	Encapsulation with protected/private attributes (health, age)
	•	Employee subclasses: Veterinarian & Zookeeper with role-specific methods
	•	Enclosure class with operator overloading (_add, __len_)

Phase 2: Advanced Features
	•	Multiple inheritance with HybridAnimal (e.g., FlyingFish)
	•	Abstract base class Animal enforcing make_sound()
	•	Class methods for handling animal births (from_birth())
	•	Duck-typed feed() function compatible with all animals

Phase 3: Simulation
	•	Zoo with 3+ enclosures
	•	10+ animals of different types
	•	Employees perform tasks:
	•	Veterinarians treat sick animals
	•	Zookeepers move animals between enclosures
	•	Daily simulation where animals:
	•	Age and lose health
	•	Employees perform duties
	•	Zoo status tracked using _str_

⸻

🛠 Technologies Used
	•	Python 3
	•	OOP concepts: Inheritance, Encapsulation, Polymorphism, ABCs
	•	Operator overloading & special methods

⸻

🚀 How to Run
	Clone the repository:

git clone https://github.com/your-username/zoo-management-system.git
cd zoo-management-system

⸻

📸 Example Output

Day 1 Simulation:
- Lion makes a roar sound
- Penguin makes a squawk sound
- Veterinarian treated a sick Snake
- Zookeeper moved Penguin to Enclosure 2
Zoo has 3 enclosures and 12 animals


⸻

📚 OOP Concepts Demonstrated
	•	Inheritance: Animal → Mammal → Lion
	•	Encapsulation: __health, __age with property setters/getters
	•	Polymorphism: make_sound() overridden in subclasses
	•	Multiple Inheritance: FlyingFish → Fish, Bird
	•	Abstract Class: Animal with @abstractmethod make_sound()
	•	Special Methods: _str, __add, __iter_

⸻

💡 This project serves as a hands-on demonstration of OOP concepts in Python while modeling real-world zoo operations.

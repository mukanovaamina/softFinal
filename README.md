# Name of your final project: Recipe master project 
# Group: SE-2215
# Team members: Guzal Mazhitova, Amina Mukanova, Aruzhan Yeleukeshova

# Project Overview: 
"Recipe master" is a Python-based application designed to assist users in mastering their culinary skills. The project incorporates various design patterns to enhance the structure, maintainability, and extensibility of the codebase.  
*Idea of the Project:*
The idea behind “Recipe master “is to create a platform for users to create, and follow cooking recipes. It offers a set of features that cover dish preparation and cooking strategies. By implementing design patterns, the project aims to demonstrate best practices in software design, ensuring adaptable solution. 
*Purpose of the Work:* 
The primary purpose of “Recipe master “is to showcase the effective implementation of software design patterns, specifically focusing on the Singleton, Factory Method, Observer, Decorator, Strategy, and Command patterns. These patterns are strategically applied to different aspects of the application, providing users with dynamic culinary experience. 
*Objectives of the Work:* 
1. Design Pattern Implementation: Implement six essential design patterns (Singleton, Factory Method, Observer, Decorator, Strategy, and Command) to enhance the overall architecture of the application.

2. User-Friendly Interface: Develop a user-friendly command-line interface (CLI) that enables users to interact intuitively with the application. The interface should facilitate recipe creation, dish preparation, and strategy selection.
   
3. SOLID Principles Adherence: Follow the principles of SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) throughout the codebase to ensure clean, modular, and maintainable code.

4. Scalability and Extensibility: Demonstrate the ability to easily extend and modify the application by allowing the addition of new dishes, cooking strategies, and decorators without major code changes.
   
"Recipe master" strives to be a versatile and educational tool for individuals passionate about cooking. The combination of design patterns and SOLID principles aims to create a robust foundation for future enhancements and improvements.

# Main body:
*Explanation*
1) Single:
Challenge: Ensure that a class has only one instance and find a global access point to that instance.
Code Application: Ensure that you only have one instance of a recipe to avoid creating duplicate data.
1.1) Recipe:
This class is used to create a single instance of a recipe, which corresponds to the Singleton pattern.
1.2)CulinaryProcess:
The class uses Singleton, represents the process of preparing a dish, and it takes an instance of the Recipe class as an argument and can be considered a piece of general information about the cooking process that can be used in various parts of the program.

2)Factory method:
Challenge: Provide an interface for instantiating our object, but allow subclasses to change the types of the instances.
Application in code: Creator classes (PlovBuilder, MantiBuilder) define factory methods for creating specific objects (Plov, Manti).
2.1)Dish, Dumplings, Plov, Manti:
The Dumplings, Plov, Manti classes represent dishes and use the factory method to create them. This allows each descendant class to decide which object to create.
2.2)DishBuilder, PlovBuilder, MantiBuilder:
The DishBuilder, PlovBuilder, MantiBuilder classes are builders for their respective dishes, using a factory method to create objects.

3)Observer:
Task: Define a one-to-many dependency between objects in such a way that when the state of one object is supplied, all details from it are transferred, deleted and updated automatically.
Code usage: Cook and Timer watch the Dumplings object and react to its changes.
3.1)Cook, Timer:
The Cook and Timer classes are observers and are used together with the Dumplings class in the Observer pattern. They are notified when the dish is completed.

4)Decorator:
Challenge: Dynamically add objects to new responsibilities without changing their code.
Code Application: SauceDecorator and CheeseDecorator add sauce and cheese functionality to the Dumplings object.
4.1)SauceDecorator, CheeseDecorator:
The SauceDecorator and CheeseDecorator classes are decorators for adding sauce and cheese to a dish (Dumplings).

5)Strategy:
Challenge: Define a family of algorithms, encapsulate each of them, and make them interchangeable.
Code Application: SteamingStrategy and BoilingStrategy provide different cooking strategies, and the CookingContext object chooses to use them.
5.1)CookingContext, SteamingStrategy, BoilingStrategy:
The CookingContext, SteamingStrategy, BoilingStrategy classes represent the cooking strategy for a dish. CookingContext uses strategies to change cooking behavior depending on the selected strategy.

6) Command:
Challenge: Encapsulate a request as an object, allow clients to parameterize different requests, organize requests into queues, and support cancellation of operations.
Code Application: SaltCommand and PepperCommand provide commands, and CulinaryExpert executes them on demand.
6.1) SaltCommand, PepperCommand, CulinaryExpert:
The classes SaltCommand, PepperCommand represent commands, and CulinaryExpert represents the command executor. This corresponds to the Command pattern.

*UML-diagram*
<image src="[https://picos/800/600sum.phot](https://www.planttext.com/api/plantuml/png/fPH1ReCm44NtFWLBgeWBiAYYa2wwg8fAB-3QqyGgsCWsKQAsTw-DiS26f5HTXSn_ypqcVx9L6alTDJL2fCPA9Iz0M0l99qgIpG7q8pS09v3UvOE4lZrQT3NZM5vAAGYOxxOdapqqXyjQd7OTgob8PquaO0rxfexMsyeZ_8IvPZVeNW-z7TPAQB7ifpq9HYF7NvXzrxJcHWTtamsczFbDWJo1JCNma2U-vBiDo8LcxnSlg7GYNJsh4EB37TErrDmifVxmV9nZrlNA6lz2_j9MuOx07eYGM0lNdoqrtfxu2A3-xsBkRQ12S0rdxKoKDevmkEHUhOQ2TLAW_TVqAZXvuyGeLu_r_92fHRJIW9kLx4wmUYLQYAR1d3e4pa0wlV1wAbphTMG9RGjo7UiNzU5iMdG03mOfSP-vdtFY4QzvbjtxxKRJhRRrVes3xRLLjwvet2zRzFiIbSEiHcAKGJERNQF0pQr8K49H_gqufZNETQYYAB3z555APyXNu30BL0_49d6K5Y4qpOSRfNz6OHgc2ef-_43R0gVsl_y7)https://www.planttext.com/api/plantuml/png/fPH1ReCm44NtFWLBgeWBiAYYa2wwg8fAB-3QqyGgsCWsKQAsTw-DiS26f5HTXSn_ypqcVx9L6alTDJL2fCPA9Iz0M0l99qgIpG7q8pS09v3UvOE4lZrQT3NZM5vAAGYOxxOdapqqXyjQd7OTgob8PquaO0rxfexMsyeZ_8IvPZVeNW-z7TPAQB7ifpq9HYF7NvXzrxJcHWTtamsczFbDWJo1JCNma2U-vBiDo8LcxnSlg7GYNJsh4EB37TErrDmifVxmV9nZrlNA6lz2_j9MuOx07eYGM0lNdoqrtfxu2A3-xsBkRQ12S0rdxKoKDevmkEHUhOQ2TLAW_TVqAZXvuyGeLu_r_92fHRJIW9kLx4wmUYLQYAR1d3e4pa0wlV1wAbphTMG9RGjo7UiNzU5iMdG03mOfSP-vdtFY4QzvbjtxxKRJhRRrVes3xRLLjwvet2zRzFiIbSEiHcAKGJERNQF0pQr8K49H_gqufZNETQYYAB3z555APyXNu30BL0_49d6K5Y4qpOSRfNz6OHgc2ef-_43R0gVsl_y7" alt="uml">

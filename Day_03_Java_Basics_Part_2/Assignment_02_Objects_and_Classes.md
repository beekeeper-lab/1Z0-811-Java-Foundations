# Day 3 Assignment: Objects and Classes in Practice

## Overview

- **Topic:** Java Basics — Creating Classes, Instantiating Objects, and Using Fields and Methods
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

In Day 2, you learned about the structure of a Java program — classes, the `main` method, and compiling/running code. Now you'll take the next step: creating your own classes that act as **blueprints** for objects.

A class can have:
- **Fields** (also called instance variables) — data that belongs to each object
- **Methods** — actions the object can perform
- **A constructor** — a special method that runs when a new object is created

Here's a quick example:

```java
public class Dog {
    String name;
    String breed;
    int age;

    public void bark() {
        System.out.println(name + " says: Woof!");
    }

    public void describe() {
        System.out.println(name + " is a " + age + "-year-old " + breed + ".");
    }
}
```

You create and use an object like this:

```java
public class DogMain {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Buddy";
        myDog.breed = "Golden Retriever";
        myDog.age = 3;

        myDog.bark();
        myDog.describe();
    }
}
```

---

## Part 1: Follow the Pattern

### Program A: `Book.java` and `BookMain.java`

Create a `Book` class with the following fields:
- `String title`
- `String author`
- `int pages`
- `int yearPublished`

Add the following methods:
- `describe()` — prints a sentence like: `"To Kill a Mockingbird by Harper Lee (1960), 281 pages."`
- `isLong()` — prints `"This is a long book."` if pages is greater than 300, otherwise prints `"This is a short read."`

Then create `BookMain.java` with a `main` method that:
1. Creates **two** different `Book` objects with different values
2. Calls `describe()` and `isLong()` on each one

### Program B: `Student.java` and `StudentMain.java`

Create a `Student` class with the following fields:
- `String name`
- `int age`
- `String major`
- `double gpa`

Add the following methods:
- `introduce()` — prints: `"Hi, I'm [name]. I'm [age] years old and studying [major]."`
- `honorsCheck()` — prints `"[name] is on the honor roll!"` if GPA is 3.5 or higher, otherwise prints `"[name] is in good standing."`

Then create `StudentMain.java` with a `main` method that:
1. Creates **three** different `Student` objects
2. Calls `introduce()` and `honorsCheck()` on each one
3. At least one student should have a GPA of 3.5 or higher and at least one below 3.5

---

## Part 2: Design Your Own

### Program C: `Vehicle.java` and `VehicleMain.java`

Design your own `Vehicle` class from scratch. Requirements:

- At least **4 fields** (you choose what they are — make, model, year, color, mileage, etc.)
- At least **3 methods** that print something meaningful about the vehicle
- At least one method should include an **if/else** decision based on one of the fields

Create `VehicleMain.java` that:
1. Creates at least **2** Vehicle objects
2. Demonstrates all of your methods

---

## Part 3: Connecting Concepts

### Program D: `OOPDemo.java`

Write a single-file program (everything in one `.java` file is fine for this one) that demonstrates the difference between a **class** and an **object** through printed output. Your program should:

1. Print a header: `"=== OOP Concepts Demo ==="`
2. Create multiple objects from the same class
3. Show that each object holds its **own data** independent of the others
4. Print a summary that explains what's happening, like:
   ```
   Both dog1 and dog2 are Dog objects, but they have different names and ages.
   The Dog class is the blueprint. Each Dog object is a unique instance.
   ```

> The goal is to show that you understand the relationship between a class and its objects.

---

## Part 4: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between a **class** and an **object**?
2. What is the difference between a **field** and a **method**?
3. In today's written assignment, you learned about the four pillars of OOP. Which pillar is most related to what you did in today's coding exercises? Why?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Objects_and_Classes.md` containing:

1. Your answers to the three reflection questions
2. A brief note about which exercise was hardest and why

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `Book` and `BookMain`: Correct fields, methods, and output | 20 |
| `Student` and `StudentMain`: Correct fields, methods, and output | 20 |
| `Vehicle` and `VehicleMain`: Original design meets requirements | 20 |
| `OOPDemo`: Clearly demonstrates class vs. object distinction | 15 |
| Reflection questions answered accurately | 15 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

# Day 2 Assignment: Anatomy of a Java Program

## Overview

- **Topic:** Java Basics — Program Structure, Classes, and the main Method
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

Every Java program is built from **classes**. A class is a blueprint that contains data and behavior. Every Java application has at least one class with a `main` method — this is where the program starts running.

The main method signature is always:

```java
public static void main(String[] args)
```

Each keyword matters:
- `public` — accessible from anywhere
- `static` — belongs to the class, not an instance
- `void` — returns nothing
- `main` — the name the JVM looks for at startup
- `String[] args` — an array of command-line arguments

---

## Part 1: Reading and Correcting Code

The following three Java programs each contain **errors**. For each one, create the `.java` file, attempt to compile it, read the error messages, fix the problems, and get it to compile and run.

### Program A: `GreetingBroken.java`

```java
public class Greeting {
    public static void main(String[] args) {
        System.out.println("Welcome to Java!")
    }
}
```

> **Hint:** There are two problems — one will cause a compiler error, and one is a naming mismatch.

### Program B: `MathDisplayBroken.java`

```java
public class MathDisplay {
    public static void Main(String[] args) {
        System.out.println("The sum of 10 + 20 is: " + (10 + 20));
        System.out.println("The product of 5 * 6 is: " + (5 * 6));
    }
}
```

> **Hint:** The program compiles but won't run. Why?

### Program C: `AboutMeBroken.java`

```java
public class AboutMe
    public static void main(String[] args) {
        System.out.println("Name: Campbell Reed");
        System.out.println("Favorite number: " + 42)
        System.out.println("Learning Java: " + true);
    }
}
```

> **Hint:** There are two syntax errors to find.

### Deliverable

For each program, save two files:
- The **fixed** version (e.g., `GreetingFixed.java`, `MathDisplayFixed.java`, `AboutMeFixed.java`)
- In your response file, write what each error was and how you identified it

---

## Part 2: Build Your Own Programs

Write each of the following programs from scratch. Each one must compile and run.

### Program D: `PersonalInfo.java`

Write a program that prints the following information, each on its own line:
- Your full name
- Your city and state
- Your favorite programming language (even if you're just starting — pick one!)
- Today's date

### Program E: `JavaFacts.java`

Write a program that prints **5 facts about Java** that you learned from today's written assignment. Format the output with numbered lines like this:

```
Fact 1: [your fact here]
Fact 2: [your fact here]
...
```

### Program F: `CommandLineGreeting.java`

Write a program that uses **command-line arguments** to print a greeting. The program should use `args[0]` to get a name passed at runtime.

Example usage:
```
javac CommandLineGreeting.java
java CommandLineGreeting Campbell
```

Expected output:
```
Hello, Campbell! Welcome to Java.
```

> **Hint:** `args` is the `String[]` parameter in the main method. `args[0]` gives you the first argument.
>
> **Bonus challenge:** What happens if you run the program without providing a name? Can you add a check using `args.length` to print a default message instead of crashing?

---

## Part 3: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When you compiled a program with errors, what kind of information did the `javac` error messages give you? Were they helpful?
2. What is the difference between a **compile-time error** and a **runtime error**? Give an example of each from today's exercises.
3. Why does Java require the file name to match the class name?

---

## Submission

Save all fixed and new `.java` files in this folder, along with a response file named `Response_02_Anatomy_of_a_Java_Program.md` containing:

1. Your error explanations for Programs A, B, and C
2. Your answers to the three reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Programs A, B, C: Errors correctly identified and fixed | 25 |
| Program D: `PersonalInfo.java` compiles, runs, and prints required info | 15 |
| Program E: `JavaFacts.java` compiles, runs, and prints 5 facts | 15 |
| Program F: `CommandLineGreeting.java` works with command-line arguments | 20 |
| Reflection questions answered accurately | 15 |
| Code is clean and properly formatted | 10 |
| **Total** | **100** |

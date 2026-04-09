# Module 2: Java Basics Part 1

> 🏷️ Start Here

> 🎯 **Teach:** What the JDK, JRE, and JVM are, how they relate, and the anatomy of a Java program including classes, the main method, and compilation
> **See:** Broken Java programs that need debugging, plus programs built from scratch using the main method and command-line arguments
> **Feel:** Comfort reading Java error messages and confidence writing simple programs independently

> 🎙️ Today you are going to look under the hood of the Java platform. You will learn what the JDK, JRE, and JVM actually are and how they work together to make Java's "write once, run anywhere" promise real. Then you will fix broken programs, write your own from scratch, and start building the instinct for reading compiler error messages.

> 🎙️ A lot of beginners skip over the JDK and JRE because they just want to write code. But understanding the platform is what separates someone who can code from someone who truly understands Java. The exam tests this, and it will make debugging much easier later.

## Research: The Java Platform

> 🎯 **Teach:** What the JDK, JRE, and JVM are, how they nest inside each other, and what role each plays in compiling and running Java programs.
> **See:** The three-layer relationship of JDK containing JRE containing JVM, and how a .java file becomes a running program.
> **Feel:** Confidence that the Java platform architecture makes sense and is not just abstract jargon.

### Overview

- **Topic:** Java Basics — The JDK, JRE, and Anatomy of a Java Program
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following questions:

1. **What is the JDK and what is the JRE?** Explain what each one is, what it contains, and how they relate to each other. Which one does a developer need? Which one does an end user need?

2. **What is the JVM?** Where does the Java Virtual Machine fit into this picture, and why is it important to Java's "write once, run anywhere" promise?

3. **What are the main components of a basic Java program?** Describe the purpose of the `class` declaration, the `main` method signature (`public static void main(String[] args)`), and how a `.java` file becomes a running program.

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Java_Platform_Research.md` in this folder.

> 💡 **Remember this one thing:** The JDK is for developers (it includes the compiler), the JRE is for running programs (it includes the JVM), and the JVM is the engine that executes your bytecode on any platform.

> 🎙️ Here is a quick way to remember the three layers. The JDK contains the JRE, and the JRE contains the JVM. Think of it like a set of nesting boxes -- the JDK is the biggest box with all the developer tools, the JRE is the middle box with everything needed to run programs, and the JVM is the innermost box that actually executes your bytecode.

## Hands-On: Anatomy of a Java Program

> 🎯 **Teach:** How to read Java compiler errors, fix broken programs, and write complete programs from scratch including ones that accept command-line arguments.
> **See:** Three broken programs with real compiler errors to diagnose, plus three new programs built from an empty file.
> **Feel:** Growing independence as a Java programmer who can debug errors and write code without hand-holding.

> 🎙️ Time to put your understanding of Java program structure into practice. You are going to fix broken programs by reading error messages, then write your own programs from scratch including one that accepts command-line arguments.

### Overview

- **Topic:** Java Basics — Program Structure, Classes, and the main Method
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

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

> 🎙️ Pay close attention to that main method signature. Every single keyword matters -- public, static, void, main, String array args. If any piece is wrong or missing, the JVM will not find your entry point and your program will not run. The exam loves to test variations of this.

---

### Part 1: Reading and Correcting Code

The following three Java programs each contain **errors**. For each one, create the `.java` file, attempt to compile it, read the error messages, fix the problems, and get it to compile and run.

#### Program A: `GreetingBroken.java`

```java
public class Greeting {
    public static void main(String[] args) {
        System.out.println("Welcome to Java!")
    }
}
```

> **Hint:** There are two problems — one will cause a compiler error, and one is a naming mismatch.

#### Program B: `MathDisplayBroken.java`

```java
public class MathDisplay {
    public static void Main(String[] args) {
        System.out.println("The sum of 10 + 20 is: " + (10 + 20));
        System.out.println("The product of 5 * 6 is: " + (5 * 6));
    }
}
```

> **Hint:** The program compiles but won't run. Why?

#### Program C: `AboutMeBroken.java`

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

> 🎙️ When you hit a compiler error, do not panic. Read the error message carefully -- it tells you the line number and what went wrong. Learning to read error messages is one of the most valuable skills you will develop as a programmer. The compiler is trying to help you.

#### Deliverable

For each program, save two files:
- The **fixed** version (e.g., `GreetingFixed.java`, `MathDisplayFixed.java`, `AboutMeFixed.java`)
- In your response file, write what each error was and how you identified it

---

### Part 2: Build Your Own Programs

Write each of the following programs from scratch. Each one must compile and run.

#### Program D: `PersonalInfo.java`

Write a program that prints the following information, each on its own line:
- Your full name
- Your city and state
- Your favorite programming language (even if you're just starting — pick one!)
- Today's date

#### Program E: `JavaFacts.java`

Write a program that prints **5 facts about Java** that you learned from today's written assignment. Format the output with numbered lines like this:

```
Fact 1: [your fact here]
Fact 2: [your fact here]
...
```

#### Program F: `CommandLineGreeting.java`

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

> 🎙️ The bonus challenge here is worth doing. Thinking about what happens when input is missing is the kind of defensive programming that separates reliable code from fragile code. Plus, checking array length before accessing an element is a pattern you will use throughout your career.

---

### Part 3: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When you compiled a program with errors, what kind of information did the `javac` error messages give you? Were they helpful?
2. What is the difference between a **compile-time error** and a **runtime error**? Give an example of each from today's exercises.
3. Why does Java require the file name to match the class name?

> 🎙️ Question two here -- the difference between compile-time and runtime errors -- is a concept that comes up over and over in Java. Get comfortable with this distinction now. Compile-time errors are caught by javac before your program runs. Runtime errors happen while the program is executing and can crash it.

---

### Submission

Save all fixed and new `.java` files in this folder, along with a response file named `Response_02_Anatomy_of_a_Java_Program.md` containing:

1. Your error explanations for Programs A, B, and C
2. Your answers to the three reflection questions

> 💡 **Remember this one thing:** Every Java program starts at `public static void main(String[] args)` — get any part of that signature wrong and the JVM will not find your entry point.

## Grading

> 🎯 **Teach:** How each assignment is evaluated so the student can self-assess before submitting.
> **See:** Detailed rubrics for the research essay and all six hands-on programs.
> **Feel:** Clarity about expectations and confidence that the criteria are straightforward to meet.

> 🔄 **Where this fits:** Day 2 deepens your understanding of the Java platform and program structure, preparing you for object-oriented concepts on Day 3 and beyond.

### Research Grading

| Criteria | Points |
|----------|--------|
| Accurately describes the JDK and JRE and their relationship | 25 |
| Explains the JVM and its role in platform independence | 25 |
| Describes the components of a basic Java program | 25 |
| Writing quality and at least 3 properly cited references | 25 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| Programs A, B, C: Errors correctly identified and fixed | 25 |
| Program D: `PersonalInfo.java` compiles, runs, and prints required info | 15 |
| Program E: `JavaFacts.java` compiles, runs, and prints 5 facts | 15 |
| Program F: `CommandLineGreeting.java` works with command-line arguments | 20 |
| Reflection questions answered accurately | 15 |
| Code is clean and properly formatted | 10 |
| **Total** | **100** |

> 🎙️ Great work today. You now understand the Java platform stack and the anatomy of a Java program. Tomorrow you are going to step into the heart of Java -- object-oriented programming. You will learn what classes and objects really are and start building your own from scratch.

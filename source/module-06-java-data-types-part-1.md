# Module 6: Java Data Types Part 1

> 🏷️ Useful Soon

> 🎯 **Teach:** What variables are in Java, all eight primitive data types with their sizes and ranges, and how the final keyword creates constants
> **See:** Programs declaring every primitive type, exploring numeric boundaries and overflow, using final constants for physics calculations, and building a budget calculator with thoughtful type choices
> **Feel:** Solid understanding of Java's type system and confidence choosing the right data type for any situation

> 🎙️ Starting today you are entering the data types block, which runs through Day 8 and is heavily tested on the certification exam. You will learn what variables are, meet all eight primitive data types, and understand when and why to use each one. You will also learn how the final keyword locks a variable's value in place.

> 🎙️ Data types are one of the most heavily tested topics on the 1Z0-811 exam. This is not a day to rush through. Understanding the difference between byte, short, int, and long -- and knowing when to use each one -- will pay off on the exam and in every program you write.

## Research: Variables and Primitive Data Types

> 🎯 **Teach:** What variables are, the difference between declaration and initialization, all eight primitive data types with their sizes and ranges, and the purpose of the final keyword.
> **See:** The complete primitive type table from byte through boolean, grouped by category, with the doubling-size pattern for integer types.
> **Feel:** Solid footing in Java's type system and awareness that this is one of the most heavily tested topics on the 1Z0-811 exam.

### Overview

- **Topic:** Working with Java Data Types — Variables, Primitives, and the `final` Keyword
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is a variable in Java?** Explain what a variable is, what it means to declare a variable versus initialize a variable, and why Java requires you to specify a data type when declaring one.

2. **What are Java's eight primitive data types?** List all eight, group them by category (integer types, floating-point types, character, boolean), and describe the size and range of each. Why does Java have multiple integer types (byte, short, int, long) instead of just one?

3. **What does the `final` keyword do when applied to a variable?** How does it differ from a regular variable? When and why would you use it?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Variables_and_Primitives_Research.md` in this folder.

> 💡 **Remember this one thing:** Java has eight primitive types — byte, short, int, long, float, double, char, and boolean — and the exam expects you to know the size and range of each one.

> 🎙️ A good trick for remembering the integer types is to think about their sizes doubling -- byte is 8 bits, short is 16, int is 32, long is 64. Each step up doubles the storage and massively increases the range. For most everyday programming, int is the default choice.

## Hands-On: Variables and Primitive Data Types in Practice

> 🎯 **Teach:** How to declare and initialize every primitive type, use the final keyword for constants, explore numeric boundaries and overflow, and choose the right type for real-world data.
> **See:** A primitive showcase, declaration style variations, physics constants with final, boundary and overflow exploration, and a budget calculator with thoughtful type choices.
> **Feel:** Confidence selecting the correct data type for any situation and understanding what happens at the edges of each type's range.

> 🎙️ Now you are going to work with every one of Java's eight primitive types, explore what happens at their boundaries, and build programs that require choosing the right type for the job.

### Overview

- **Topic:** Working with Java Data Types — Declaring, Initializing, and Using Primitive Variables
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

Java is a **statically typed** language — every variable must have a declared type before it can be used. Java has 8 primitive data types:

| Type | Size | Range / Description | Example |
|------|------|---------------------|---------|
| `byte` | 8 bits | -128 to 127 | `byte b = 100;` |
| `short` | 16 bits | -32,768 to 32,767 | `short s = 30000;` |
| `int` | 32 bits | ~-2.1 billion to ~2.1 billion | `int i = 42;` |
| `long` | 64 bits | Very large range | `long l = 999999999L;` |
| `float` | 32 bits | ~7 decimal digits precision | `float f = 3.14f;` |
| `double` | 64 bits | ~15 decimal digits precision | `double d = 3.14159;` |
| `char` | 16 bits | A single Unicode character | `char c = 'A';` |
| `boolean` | 1 bit* | `true` or `false` | `boolean b = true;` |

Key rules:
- `long` literals need an `L` suffix: `long x = 100L;`
- `float` literals need an `f` suffix: `float x = 3.14f;`
- `char` uses single quotes: `char x = 'A';`
- `String` is NOT a primitive — it's a class (covered on Day 8)

> 🎙️ Do not skip over the suffixes. Forgetting the L on a long literal or the f on a float literal is a common compiler error. Also note that char uses single quotes and String uses double quotes -- mixing those up is another classic mistake.

---

### Part 1: Declaring and Initializing Variables

#### Program A: `PrimitiveShowcase.java`

Write a program that declares and initializes **at least one variable of each of the 8 primitive types**. For each variable:

1. Declare it with a meaningful name following Java conventions
2. Print its value along with a label
3. Print the type name in a comment next to each declaration

Example output:
```
=== Primitive Data Types ===
byte:    120
short:   30000
int:     1000000
long:    9876543210
float:   3.14
double:  2.718281828
char:    J
boolean: true
```

#### Program B: `DeclarationStyles.java`

Write a program that demonstrates the **different ways to declare variables** in Java:

1. Declare and initialize on the same line
2. Declare on one line, initialize on the next
3. Declare multiple variables of the same type on one line (e.g., `int a, b, c;`)
4. Declare a `final` constant — then try to reassign it (comment out the reassignment line and add a comment explaining the error you would get)
5. Try to use a variable without initializing it (comment out the line and add a comment explaining the error)

> 🎙️ Program B is especially important -- it covers declaration patterns that the exam tests directly. Pay attention to what happens when you try to use a variable before initializing it. Java does not let you do that, and the compiler error you see is one you should recognize instantly.

---

### Part 2: Understanding `final`

#### Program C: `ConstantsDemo.java`

Write a program that models a simple physics calculation using constants. The program should:

1. Declare the following as `final` variables:
   - Speed of light: `299792458` meters per second
   - Gravitational acceleration: `9.81` m/s²
   - Pi: `3.14159265358979`

2. Declare regular (non-final) variables for:
   - A time in seconds
   - A mass in kilograms
   - A radius

3. Calculate and print:
   - Distance traveled by light in the given time (`distance = speed * time`)
   - Weight from mass (`weight = mass * gravity`)
   - Area of a circle with the given radius (`area = pi * radius * radius`)

4. Include a comment explaining why each constant should be `final` and not a regular variable

> 🎙️ The final keyword is simple but powerful -- once you assign a value to a final variable, it can never change. That is exactly what you want for constants like the speed of light or pi. If someone accidentally tries to reassign a final variable, the compiler catches it immediately.

---

### Part 3: Default Values and Boundaries

#### Program D: `BoundaryExplorer.java`

Write a program that explores the **boundaries** of Java's numeric types. This is important for the exam.

1. Print the minimum and maximum values for `byte`, `short`, `int`, and `long` using the wrapper class constants:
   ```java
   System.out.println("byte min: " + Byte.MIN_VALUE);
   System.out.println("byte max: " + Byte.MAX_VALUE);
   ```

2. Demonstrate **overflow**: What happens when you add 1 to `Byte.MAX_VALUE`? Try it:
   ```java
   byte maxByte = Byte.MAX_VALUE;
   byte overflow = (byte)(maxByte + 1);
   System.out.println("byte max + 1 = " + overflow);
   ```
   Add a comment explaining what happened and why.

3. Demonstrate the **precision difference** between `float` and `double`:
   ```java
   float f = 1.0f / 3.0f;
   double d = 1.0 / 3.0;
   System.out.println("float:  " + f);
   System.out.println("double: " + d);
   ```
   Add a comment explaining the difference in output.

4. Show what happens when you try to store a `double` value in an `int` variable without casting (comment out the line and record the error).

> 🎙️ The overflow behavior is one of the most important things you will learn today. When a byte hits 127 and you add 1, it wraps around to negative 128. Java does not warn you about this at runtime -- it just silently gives you the wrong answer. This is why knowing your type boundaries matters.

---

### Part 4: Practical Application

#### Program E: `BudgetCalculator.java`

Write a program that calculates a monthly budget. This program should demonstrate thoughtful use of the correct data types.

Requirements:
1. Use `final double` for fixed values like tax rate and savings percentage
2. Use `double` for monetary amounts (income, expenses)
3. Use `int` for quantities (number of bills, number of pay periods)
4. Use `boolean` for status flags (over budget, savings goal met)

The program should:
1. Define a monthly income
2. Define at least 5 expense categories (rent, food, utilities, transport, entertainment)
3. Calculate total expenses
4. Calculate taxes (use a `final` tax rate)
5. Calculate remaining money after expenses and taxes
6. Calculate a savings target (e.g., 20% of income) and determine if the goal is met (`boolean`)
7. Print a formatted budget summary

Example output:
```
=== Monthly Budget ===
Income:        $4000.00
Tax (22.0%):   $880.00
After tax:     $3120.00

Expenses:
  Rent:          $1200.00
  Food:          $400.00
  Utilities:     $150.00
  Transport:     $200.00
  Entertainment: $100.00
  Total:         $2050.00

Remaining:     $1070.00
Savings Goal:  $800.00
Goal Met:      true
```

---

### Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why does Java have both `int` and `long` if `long` can hold bigger numbers? Why not always use `long`?
2. What happens when an integer overflows? Is this a compile-time error or a runtime behavior?
3. Why should monetary amounts generally use `double` rather than `float`?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Variables_and_Primitives_in_Practice.md` containing:

1. Your error explanations for the commented-out lines in Part 1 and Part 3
2. Your answers to the reflection questions

> 💡 **Remember this one thing:** Integer overflow in Java does not throw an error — the value silently wraps around, which makes understanding type boundaries critical for writing correct programs.

## Grading

> 🎯 **Teach:** How each assignment is evaluated so the student can self-assess before submitting.
> **See:** Detailed rubrics for the primitives research essay and the five hands-on variable and type exercises.
> **Feel:** Clarity about expectations and readiness for type casting and promotion on Day 7.

> 🔄 **Where this fits:** Day 6 begins the data types block that runs through Day 8 — primitives, type casting, and Strings are among the most heavily tested topics on the 1Z0-811 exam.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains variables, declaration, and initialization | 25 |
| Accurately lists and describes all 8 primitive types with sizes | 30 |
| Explains the `final` keyword and when to use it | 25 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| `PrimitiveShowcase.java`: All 8 types demonstrated correctly | 15 |
| `DeclarationStyles.java`: All declaration styles shown with error explanations | 10 |
| `ConstantsDemo.java`: Correct use of `final` with calculations | 15 |
| `BoundaryExplorer.java`: Overflow, precision, and boundary values explored | 20 |
| `BudgetCalculator.java`: Correct types used, calculations work, output formatted | 20 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

> 🎙️ Solid work today. You now know all eight primitive data types, how to declare and initialize variables, and what final does. Tomorrow you will learn what happens when you need to move a value from one type to another -- type casting and promotion. Those rules are a top exam topic, so everything you learned today is the foundation for what comes next.

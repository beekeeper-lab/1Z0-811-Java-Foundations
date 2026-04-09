# Day 4 Assignment: Conventions, Comments, and Reserved Words in Practice

## Overview

- **Topic:** Basic Java Elements — Applying Naming Conventions, Using Comments, and Understanding Reserved Words
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

Java has strong conventions that the community follows to keep code readable and consistent. These aren't enforced by the compiler — your code will still compile if you name a class `my_class` — but following conventions is essential for writing professional code that others can read.

### Quick Reference: Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Class | PascalCase (uppercase start) | `StudentRecord` |
| Method | camelCase (lowercase start) | `calculateTotal()` |
| Variable | camelCase (lowercase start) | `firstName` |
| Constant | UPPER_SNAKE_CASE with `final` | `final int MAX_SIZE = 100;` |
| Package | all lowercase | `com.example.utils` |

### Quick Reference: Comment Types

```java
// This is a single-line comment

/* This is a
   multi-line comment */

/**
 * This is a Javadoc comment.
 * It documents classes and methods.
 * @param name the name to greet
 * @return a greeting string
 */
```

---

## Part 1: Fix the Conventions

The following program compiles and runs, but it **violates Java naming conventions throughout**. Rewrite it with proper naming conventions. Do not change what the program does — only fix the names.

### `BadConventions.java`

```java
public class bad_conventions {
    public static void main(String[] args) {
        String FIRST_NAME = "Alice";
        String LAST_NAME = "Smith";
        int Age = 25;
        double account_balance = 1500.75;
        final double tax_rate = 0.08;

        System.out.println("Name: " + FIRST_NAME + " " + LAST_NAME);
        System.out.println("Age: " + Age);
        System.out.println("Balance: $" + account_balance);
        System.out.println("Tax rate: " + tax_rate);

        double Tax_Amount = account_balance * tax_rate;
        System.out.println("Tax owed: $" + Tax_Amount);
    }
}
```

### Deliverable

Save the corrected version as `GoodConventions.java`. In your response file, list every naming violation you found and what you changed it to.

---

## Part 2: Add Comments to Existing Code

The following program works but has **zero comments**. Add appropriate comments throughout:

- A **Javadoc comment** above the class describing what the program does
- A **multi-line comment** at the top explaining the purpose and author
- **Single-line comments** explaining at least 5 key lines of code
- Do **not** over-comment obvious lines (e.g., don't comment `int x = 5;` with `// set x to 5`)

### `GradeCalculator.java`

```java
public class GradeCalculator {
    public static void main(String[] args) {
        int exam1 = 88;
        int exam2 = 92;
        int exam3 = 76;
        int homework = 95;

        double examWeight = 0.70;
        double homeworkWeight = 0.30;

        double examAverage = (exam1 + exam2 + exam3) / 3.0;
        double finalGrade = (examAverage * examWeight) + (homework * homeworkWeight);

        System.out.println("Exam Average: " + examAverage);
        System.out.println("Final Grade: " + finalGrade);

        if (finalGrade >= 90) {
            System.out.println("Letter Grade: A");
        } else if (finalGrade >= 80) {
            System.out.println("Letter Grade: B");
        } else if (finalGrade >= 70) {
            System.out.println("Letter Grade: C");
        } else {
            System.out.println("Letter Grade: F");
        }
    }
}
```

### Deliverable

Save your commented version as `GradeCalculatorCommented.java` in this folder.

---

## Part 3: Reserved Words Exploration

### Program A: `ReservedWordErrors.java`

Try to compile the following program. It uses **Java reserved words as identifiers** in several places. The compiler will reject it.

```java
public class ReservedWordErrors {
    public static void main(String[] args) {
        int class = 10;
        String return = "hello";
        double static = 3.14;
        boolean if = true;
    }
}
```

1. Attempt to compile it and record the error messages.
2. Fix the program by replacing each reserved word with a valid variable name that describes what the variable might represent.
3. Save the fixed version as `ReservedWordFixed.java`.

### Program B: `ReservedWordReference.java`

Write a program that demonstrates the correct use of **at least 10 different reserved words**. The program should compile and run, and each reserved word should be used appropriately in context.

Use comments to label each reserved word as you use it. For example:

```java
// "public" - access modifier making this class accessible everywhere
public class ReservedWordReference {
    // "static" - belongs to the class, not an instance
    // "final" - value cannot be changed after assignment
    static final int MAX_VALUE = 100;

    // ...continue demonstrating more reserved words...
}
```

### Deliverable

Save as `ReservedWordReference.java`. Aim for at least **10 reserved words** clearly labeled with comments.

---

## Part 4: Bring It All Together

### `RecipeCard.java`

Write a complete, well-structured program that models a recipe card. This program should be a **showcase of everything you learned today**:

- **Proper naming conventions** for the class, all variables, and any constants
- **All three comment types** used appropriately (Javadoc, multi-line, single-line)
- **At least one constant** using `final`
- **Clean, readable formatting**

The program should:
1. Store a recipe name, number of servings, prep time in minutes, and at least 4 ingredients
2. Print a formatted recipe card to the terminal, for example:

```
=============================
  Recipe: Chocolate Chip Cookies
  Servings: 24
  Prep Time: 45 minutes
=============================
  Ingredients:
  - Flour
  - Sugar
  - Butter
  - Chocolate Chips
=============================
```

3. Calculate and print the **prep time per serving** (prep time divided by servings)
4. Print whether the recipe is "Quick" (under 30 minutes) or "Takes some time" (30 minutes or more)

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why do naming conventions matter if the compiler doesn't enforce them?
2. What's the difference between a useful comment and a useless comment? Give an example of each.
3. Were there any reserved words you found surprising — words you might have wanted to use as variable names?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Conventions_in_Practice.md` containing:

1. Your list of naming violations from Part 1
2. The compiler errors from Part 3A
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `GoodConventions.java`: All naming violations identified and fixed | 15 |
| `GradeCalculatorCommented.java`: Appropriate use of all three comment types | 15 |
| `ReservedWordFixed.java`: Errors recorded and program corrected | 10 |
| `ReservedWordReference.java`: At least 10 reserved words correctly demonstrated | 15 |
| `RecipeCard.java`: Meets all requirements with proper conventions and comments | 25 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

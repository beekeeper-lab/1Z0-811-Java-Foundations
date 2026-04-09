# Day 15 Assignment: The Switch Statement in Practice

## Overview

- **Topic:** Using Decision Statements — switch, case, break, default, and fall-through
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Basic switch syntax

```java
switch (expression) {
    case value1:
        // code for value1
        break;
    case value2:
        // code for value2
        break;
    default:
        // code if no case matches
        break;
}
```

### Supported types for switch expression
- `int`, `byte`, `short`, `char`
- `String` (since Java 7)
- `enum` types
- **NOT** supported: `long`, `float`, `double`, `boolean`

### Fall-through

```java
switch (day) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        System.out.println("Weekday");
        break;  // Without this break, execution falls into case 6
    case 6:
    case 7:
        System.out.println("Weekend");
        break;
}
```

---

## Part 1: Switch Basics

### Program A: `SwitchBasics.java`

Write a program that demonstrates the basic forms of switch statements:

1. **Switch on int — Day of the week:** Use `Scanner` to read a number 1-7 and print the day name:
   ```
   Enter day number (1-7): 3
   Wednesday
   ```
   Include a `default` case for invalid numbers.

2. **Switch on char — Grade feedback:** Read a character (A-F) and print feedback:
   - A: "Excellent work!"
   - B: "Good job!"
   - C: "Satisfactory."
   - D: "Needs improvement."
   - F: "Please see the instructor."
   - default: "Invalid grade."

3. **Switch on String — Month to season:** Read a month name and print the season:
   - "December", "January", "February" → "Winter"
   - "March", "April", "May" → "Spring"
   - "June", "July", "August" → "Summer"
   - "September", "October", "November" → "Fall"

   Use `.toLowerCase()` on the input so that "MARCH", "March", and "march" all work. Use fall-through to group months that share a season.

---

## Part 2: Fall-Through Behavior

### Program B: `FallThroughDemo.java`

Write a program that demonstrates fall-through — both accidental and intentional:

1. **Accidental fall-through (the bug):** Write a switch that is MISSING break statements. Predict the output before running:
   ```java
   int choice = 2;
   switch (choice) {
       case 1:
           System.out.println("One");
       case 2:
           System.out.println("Two");
       case 3:
           System.out.println("Three");
       case 4:
           System.out.println("Four");
       default:
           System.out.println("Default");
   }
   ```
   Add a comment explaining why multiple lines printed.

2. **Fixed version:** Add break statements and show the corrected output.

3. **Intentional fall-through — grouping cases:** Write a switch that tells you how many days are in a month:
   ```java
   switch (month) {
       case 4: case 6: case 9: case 11:
           days = 30;
           break;
       case 2:
           days = 28; // simplified, ignoring leap years
           break;
       default:
           days = 31;
           break;
   }
   ```
   Read the month number from input and print the number of days. Add a comment explaining why fall-through is useful here.

4. **Intentional fall-through — cumulative behavior:** Write a switch that prints preparation steps. Entry at any step includes all steps below it:
   ```java
   int startStep = 2; // Start from step 2
   switch (startStep) {
       case 1:
           System.out.println("Step 1: Preheat oven");
       case 2:
           System.out.println("Step 2: Mix ingredients");
       case 3:
           System.out.println("Step 3: Pour into pan");
       case 4:
           System.out.println("Step 4: Bake for 30 minutes");
       case 5:
           System.out.println("Step 5: Let cool and serve");
   }
   ```
   Run it with `startStep = 1`, then `startStep = 3`. Add a comment explaining why no breaks are needed here.

---

## Part 3: Switch vs. If-Else-If

### Program C: `SwitchVsIfElse.java`

Write a program that solves the same problems using both switch and if-else-if, so Campbell can see when each is better:

1. **Calculator — good for switch:** Read two numbers and an operator (`+`, `-`, `*`, `/`). Implement once with switch, once with if-else-if:
   ```
   Enter first number: 10
   Enter operator (+, -, *, /): *
   Enter second number: 5
   Result: 10 * 5 = 50
   ```
   Add a comment: which version is cleaner for this problem?

2. **Range classification — bad for switch:** Classify a score into a grade (0-59: F, 60-69: D, 70-79: C, 80-89: B, 90-100: A). Implement with if-else-if. Add a comment explaining why switch can't easily handle ranges.

3. **Menu selection — good for switch:** Display a menu with 5 options and execute the chosen one. Add a comment explaining why switch is natural for menus.

4. **Complex conditions — bad for switch:** Determine if a person can board a flight (has ticket AND valid ID AND arrives 30+ minutes early). Add a comment explaining why switch can't handle compound boolean logic.

---

## Part 4: Practical Application

### Program D: `VendingMachine.java`

Build a vending machine simulator using switch statements, Scanner, and printf:

1. Display a product menu:
   ```
   ╔═══════════════════════════════════╗
   ║       VENDING MACHINE            ║
   ╠═══════════════════════════════════╣
   ║  A1 - Cola           $1.50      ║
   ║  A2 - Diet Cola      $1.50      ║
   ║  A3 - Lemon-Lime     $1.50      ║
   ║  B1 - Water          $1.00      ║
   ║  B2 - Orange Juice   $2.00      ║
   ║  B3 - Iced Tea       $1.75      ║
   ║  C1 - Chips          $1.25      ║
   ║  C2 - Candy Bar      $1.50      ║
   ║  C3 - Trail Mix      $2.25      ║
   ╚═══════════════════════════════════╝
   ```

2. Ask the user to enter a product code (use `String` switch).

3. Use a switch to look up the product name and price. Use `default` for invalid codes.

4. Ask the user how much money they are inserting.

5. Use if-else to determine:
   - If the money is enough: print the product, the change, and "Enjoy!"
   - If the money is not enough: print how much more is needed

6. Format all currency with `printf` to 2 decimal places.

7. Handle the input case-insensitively (`toUpperCase()`) so "a1", "A1", and "a1" all work.

---

## Part 5: Exam-Style Tricky Questions

### Program E: `SwitchExamPrep.java`

These patterns appear frequently on the 1Z0-811 exam. For each one, **predict the output** as a comment before running:

1. **What prints?**
   ```java
   String color = "RED";
   switch (color) {
       case "red":
           System.out.println("Lowercase red");
           break;
       case "RED":
           System.out.println("Uppercase RED");
           break;
       case "Red":
           System.out.println("Mixed case Red");
           break;
   }
   ```
   Add a comment: is String switch case-sensitive?

2. **What prints?**
   ```java
   int x = 3;
   switch (x) {
       case 1:
           System.out.println("A");
       case 2:
           System.out.println("B");
       case 3:
           System.out.println("C");
       case 4:
           System.out.println("D");
           break;
       case 5:
           System.out.println("E");
   }
   ```

3. **What prints?**
   ```java
   int num = 10;
   switch (num) {
       default:
           System.out.println("Default");
       case 1:
           System.out.println("One");
           break;
       case 2:
           System.out.println("Two");
   }
   ```
   Add a comment: can `default` appear anywhere in the switch? Does it affect fall-through?

4. **Does this compile?**
   ```java
   int value = 5;
   final int CONSTANT = 5;
   int variable = 5;
   switch (value) {
       case CONSTANT:
           System.out.println("Constant match");
           break;
       case variable:  // Does this compile?
           System.out.println("Variable match");
           break;
   }
   ```
   Add a comment explaining why case labels must be compile-time constants.

5. **Write your own** tricky switch question with at least one fall-through, a default in an unusual position, and a String comparison. Include the predicted output and actual output.

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When is a switch statement a better choice than if-else-if? Give a specific example.
2. Why must case labels be compile-time constants (literals or `final` variables)?
3. Is String comparison in a switch case-sensitive? How should you handle user input to account for this?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Switch_Statement_in_Practice.md` containing:

1. Your predictions vs. actual results for Part 2 (fall-through) and Part 5 (exam prep)
2. Your comparisons from Part 3
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `SwitchBasics.java`: All 3 switch types (int, char, String) working | 15 |
| `FallThroughDemo.java`: All 4 fall-through scenarios with explanations | 15 |
| `SwitchVsIfElse.java`: All 4 comparisons with accurate commentary | 15 |
| `VendingMachine.java`: Full simulator with switch, validation, and formatting | 20 |
| `SwitchExamPrep.java`: All 5 questions with correct predictions and explanations | 20 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

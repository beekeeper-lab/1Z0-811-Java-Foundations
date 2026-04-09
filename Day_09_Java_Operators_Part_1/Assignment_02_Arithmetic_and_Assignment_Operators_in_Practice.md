# Day 9 Assignment: Arithmetic and Assignment Operators in Practice

## Overview

- **Topic:** Working with Java Operators — Arithmetic, Increment/Decrement, and Compound Assignment
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3` (integer!) |
| `%` | Modulo (remainder) | `10 % 3` | `1` |

### Increment / Decrement

| Expression | Name | Behavior |
|------------|------|----------|
| `++x` | Pre-increment | Increments **before** the value is used |
| `x++` | Post-increment | Uses the value **then** increments |
| `--x` | Pre-decrement | Decrements **before** the value is used |
| `x--` | Post-decrement | Uses the value **then** decrements |

### Compound Assignment

| Operator | Equivalent | Bonus |
|----------|-----------|-------|
| `x += 5` | `x = x + 5` | Includes implicit cast |
| `x -= 5` | `x = x - 5` | Includes implicit cast |
| `x *= 5` | `x = x * 5` | Includes implicit cast |
| `x /= 5` | `x = x / 5` | Includes implicit cast |
| `x %= 5` | `x = x % 5` | Includes implicit cast |

---

## Part 1: Arithmetic Fundamentals

### Program A: `ArithmeticDemo.java`

Write a program that demonstrates every arithmetic operator with clear output:

1. **Addition, Subtraction, Multiplication** — straightforward, one example each
2. **Integer Division** — demonstrate that `10 / 3` yields `3`, not `3.333...`
3. **Floating-point Division** — demonstrate that `10.0 / 3.0` yields `3.333...`
4. **Mixed Division** — show what happens with `10 / 3.0` and `10.0 / 3`
5. **Division by zero:**
   - What happens with `10 / 0`? (Wrap in try/catch and print the exception)
   - What happens with `10.0 / 0.0`? (This does NOT crash — print the result and explain)
6. **Modulo:** Show examples for each:
   - `10 % 3` → remainder is 1
   - `15 % 5` → remainder is 0
   - `7 % 2` → remainder is 1 (odd number check)
   - A negative number: `-7 % 3` — what is the result?

---

## Part 2: Modulo in Action

### Program B: `ModuloApplications.java`

The modulo operator is more useful than it first appears. Write a program that demonstrates these practical uses:

1. **Even/Odd checker:** Given an array of integers `{12, 7, 24, 3, 18, 9, 42}`, loop through and print whether each is even or odd. (Use `number % 2 == 0`)

2. **Clock arithmetic:** Given a value of `250` total minutes, calculate the hours and remaining minutes:
   ```
   250 minutes = 4 hours and 10 minutes
   ```

3. **Making change:** Given an amount in cents (e.g., `487`), break it down into quarters, dimes, nickels, and pennies using `/` and `%`:
   ```
   487 cents = 19 quarters, 1 dime, 0 nickels, 2 pennies
   ```

4. **Cycle detection:** Given a counter that goes from 0 to 20, print "BUZZ" every 5th number using `%`:
   ```
   0: BUZZ
   1:
   2:
   3:
   4:
   5: BUZZ
   ...
   ```

---

## Part 3: Increment and Decrement

### Program C: `IncrementDecrement.java`

This is a **heavy exam topic**. Write a program that explores prefix vs. postfix behavior:

1. **Simple standalone usage** — show that on their own line, `x++` and `++x` have the same effect:
   ```java
   int a = 5;
   a++;
   System.out.println("After a++: " + a);  // 6

   int b = 5;
   ++b;
   System.out.println("After ++b: " + b);  // 6
   ```

2. **Inside an expression** — this is where they differ. Predict the output FIRST (write your prediction as a comment), then run:
   ```java
   int x = 10;
   int y = x++;
   System.out.println("x = " + x + ", y = " + y);

   int m = 10;
   int n = ++m;
   System.out.println("m = " + m + ", n = " + n);
   ```

3. **Inside a print statement:**
   ```java
   int counter = 5;
   System.out.println(counter++);  // What prints?
   System.out.println(counter);    // What prints now?

   int counter2 = 5;
   System.out.println(++counter2); // What prints?
   System.out.println(counter2);   // What prints now?
   ```

4. **Tricky exam-style questions** — predict the output before running:
   ```java
   int a = 3;
   int result = a++ + ++a;
   System.out.println("a = " + a + ", result = " + result);

   int b = 5;
   int result2 = --b + b-- + b;
   System.out.println("b = " + b + ", result2 = " + result2);
   ```

For each tricky question, write a **step-by-step explanation** as comments showing how you worked out the answer.

---

## Part 4: Compound Assignment Operators

### Program D: `CompoundAssignment.java`

Write a program that demonstrates all five compound assignment operators:

1. **Basic usage:** Start with `int score = 100;` and apply each operator:
   ```
   score += 10  → 110
   score -= 25  → 85
   score *= 2   → 170
   score /= 5   → 34
   score %= 10  → 4
   ```
   Print the value after each step.

2. **The implicit cast trick** (important for the exam):
   ```java
   byte b = 10;
   // b = b + 5;    // ERROR! b + 5 is an int
   b += 5;          // WORKS! Compound assignment includes implicit cast
   ```
   Demonstrate this with `byte`, `short`, and `char`. Comment out the failing line and explain the error, then show the compound assignment working.

3. **String concatenation with `+=`:**
   ```java
   String message = "Hello";
   message += " ";
   message += "World";
   message += "!";
   System.out.println(message);  // "Hello World!"
   ```
   Build a sentence word by word using `+=`.

---

## Part 5: Practical Application

### Program E: `ScoreTracker.java`

Write a program that simulates tracking a player's score in a game. This should use all the operator types from today:

1. Start with a `score` of `0` and a `lives` of `3`
2. Simulate a series of game events using print statements and operators:
   - Player collects a coin: `score += 10`
   - Player defeats an enemy: `score += 25`
   - Player gets hit: `lives--` (use post-decrement and print the value change)
   - Player finds a multiplier: `score *= 2`
   - Player pays for a power-up: `score -= 15`
   - Player splits score with a teammate: `score /= 2`
   - Calculate bonus coins: `score % 100` (remainder becomes bonus)
3. After each event, print the current state:
   ```
   Event: Collected a coin
   Score: 10 | Lives: 3
   ---
   Event: Defeated an enemy
   Score: 35 | Lives: 3
   ---
   Event: Got hit!
   Lives were 3, now 2
   Score: 35 | Lives: 2
   ---
   ```
4. At the end, determine if the player survived (`lives > 0`) and print a final summary

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the result of `7 / 2` in Java? How do you get `3.5` instead?
2. In the expression `int y = x++;`, why does `y` get the OLD value of `x`?
3. Why does `b += 5` compile for a `byte` variable but `b = b + 5` does not?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Arithmetic_and_Assignment_Operators_in_Practice.md` containing:

1. Your predictions vs. actual results from Part 3
2. Your step-by-step explanations of the tricky increment/decrement questions
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `ArithmeticDemo.java`: All operators demonstrated including division edge cases | 15 |
| `ModuloApplications.java`: All 4 practical applications correct | 15 |
| `IncrementDecrement.java`: All scenarios with predictions and explanations | 20 |
| `CompoundAssignment.java`: All operators shown, implicit cast demonstrated | 15 |
| `ScoreTracker.java`: Complete game simulation using all operator types | 15 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

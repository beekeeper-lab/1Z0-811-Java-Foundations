# Day 7 Assignment: Type Casting and Promotion in Practice

## Overview

- **Topic:** Working with Java Data Types — Widening, Narrowing, and Automatic Promotion
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

Java automatically **widens** values when assigning a smaller type to a larger type — this is safe because no data is lost:

```java
int myInt = 42;
double myDouble = myInt;  // Automatic widening: int → double
```

Java requires an explicit **narrowing cast** when going from a larger type to a smaller type — this may lose data:

```java
double myDouble = 9.99;
int myInt = (int) myDouble;  // Manual cast: double → int (loses .99)
```

### The Promotion Hierarchy

```
byte → short → int → long → float → double
```

Any type on the left can be automatically promoted to any type on the right.

### Automatic Promotion in Expressions

When you mix types in an expression, Java automatically promotes the smaller type:

```java
int a = 5;
double b = 2.0;
double result = a + b;  // a is promoted to double before addition
```

**Important exam rule:** When `byte`, `short`, or `char` values are used in arithmetic, they are **always promoted to `int`** first:

```java
byte a = 10;
byte b = 20;
// byte c = a + b;  // ERROR! a + b becomes an int
int c = a + b;       // Correct
byte d = (byte)(a + b);  // Also correct — explicit cast back
```

---

## Part 1: Widening Conversions

### Program A: `WideningDemo.java`

Write a program that demonstrates the **entire widening chain**. Start with a `byte` value and assign it step by step through every widening conversion:

1. `byte` → `short`
2. `short` → `int`
3. `int` → `long`
4. `long` → `float`
5. `float` → `double`

At each step, print the value and the type. Example:

```
byte value:   42
short value:  42
int value:    42
long value:   42
float value:  42.0
double value: 42.0
```

Then try the reverse direction — start with a `double` and attempt to assign it to a `float` without casting. Comment out the line and record the compiler error.

---

## Part 2: Narrowing Conversions

### Program B: `NarrowingDemo.java`

Write a program that demonstrates narrowing casts and the data loss that can occur:

1. Cast `double 9.99` to `int` — what happens to the decimal?
2. Cast `int 130` to `byte` — what happens when the value exceeds the byte range?
3. Cast `int 65` to `char` — what character does it produce?
4. Cast `double 1_000_000.75` to `float` — does precision change?
5. Cast `long 3_000_000_000L` to `int` — what value do you get?

For each cast, print:
- The original value and type
- The cast value and type
- A comment explaining what happened

Example:
```
double 9.99 → int 9 (decimal truncated, not rounded)
int 130 → byte -126 (overflow — wraps around)
```

---

## Part 3: Automatic Promotion in Expressions

### Program C: `PromotionRules.java`

Write a program that demonstrates Java's automatic promotion rules. For each scenario below, predict the result type, then verify:

1. **int + double:**
   ```java
   int a = 10;
   double b = 3.0;
   // What type is the result of a + b?
   ```

2. **byte + byte:**
   ```java
   byte x = 50;
   byte y = 60;
   // What type is x + y? Can you store it in a byte?
   ```

3. **int / int (integer division):**
   ```java
   int p = 7;
   int q = 2;
   // What is p / q? Is it 3 or 3.5?
   ```

4. **Forcing floating-point division:**
   ```java
   int p = 7;
   int q = 2;
   // How do you get 3.5 instead of 3? Show two different ways.
   ```

5. **char arithmetic:**
   ```java
   char letter = 'A';
   // What is letter + 1? What type is the result?
   // How do you get 'B' from letter + 1?
   ```

6. **Mixed expression:**
   ```java
   byte a = 10;
   short b = 20;
   long c = 30L;
   // What type is a + b + c?
   ```

For each scenario, print:
- The expression
- Your prediction (as a comment)
- The actual result
- An explanation of the promotion rule that applies

---

## Part 4: Practical Application

### Program D: `TemperatureConverter.java`

Write a temperature conversion program that demonstrates casting and type considerations:

1. Declare temperatures as different types:
   - A `double` for Fahrenheit input (e.g., `98.6`)
   - Convert to Celsius using: `C = (F - 32) * 5.0 / 9.0`
   - Store the result as a `double` (precise) and also cast it to an `int` (rounded down)

2. Show conversions for at least 5 different temperatures:
   - Freezing point of water (32°F)
   - Body temperature (98.6°F)
   - Boiling point of water (212°F)
   - A cold day (0°F)
   - A hot day (105°F)

3. For each conversion, print both the precise and truncated values:
   ```
   98.6°F = 37.0°C (precise) = 37°C (truncated)
   ```

4. **Demonstrate a casting pitfall:** Show what happens if you use integer division instead of floating-point division in the formula:
   ```java
   // Wrong: (F - 32) * 5 / 9     ← integer division!
   // Right: (F - 32) * 5.0 / 9.0  ← floating-point division
   ```

### Program E: `GradeRounder.java`

Write a program that takes a set of exam scores as `double` values and:

1. Calculates the average (as a `double`)
2. Casts the average to an `int` to show truncation
3. Uses `Math.round()` to show proper rounding
4. Demonstrates the difference between truncation and rounding with at least 3 different averages (e.g., 89.4, 89.5, 89.9)
5. Assigns a letter grade based on the rounded value

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why does Java automatically promote `byte` and `short` to `int` in arithmetic expressions?
2. What is the difference between truncation and rounding? Why does casting to `int` truncate instead of round?
3. A common exam question: what is the result of `10 / 3` in Java? What about `10 / 3.0`? Explain why they differ.

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Type_Casting_in_Practice.md` containing:

1. Your predictions vs. actual results from Part 3
2. Your casting pitfall demonstration from Part 4
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `WideningDemo.java`: Complete widening chain demonstrated | 15 |
| `NarrowingDemo.java`: All 5 narrowing scenarios with explanations | 15 |
| `PromotionRules.java`: All 6 scenarios with predictions and explanations | 20 |
| `TemperatureConverter.java`: Correct conversions and casting pitfall shown | 15 |
| `GradeRounder.java`: Truncation vs. rounding clearly demonstrated | 15 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

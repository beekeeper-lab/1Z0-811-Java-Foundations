# Day 13 Assignment: Random and Math Classes in Practice

## Overview

- **Topic:** Working with the Random and Math Classes
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### The Math Class (java.lang — no import needed)

All methods are `static` — you call them on the class itself, not on an object:

```java
double result = Math.sqrt(25);   // 5.0
int bigger = Math.max(10, 20);   // 20
```

| Method | Returns | Description | Example |
|--------|---------|-------------|---------|
| `Math.abs(x)` | same type | Absolute value | `Math.abs(-7)` → `7` |
| `Math.max(a, b)` | same type | Larger of two values | `Math.max(3, 9)` → `9` |
| `Math.min(a, b)` | same type | Smaller of two values | `Math.min(3, 9)` → `3` |
| `Math.pow(base, exp)` | `double` | Exponentiation | `Math.pow(2, 8)` → `256.0` |
| `Math.sqrt(x)` | `double` | Square root | `Math.sqrt(144)` → `12.0` |
| `Math.round(x)` | `long`/`int` | Round to nearest integer | `Math.round(3.6)` → `4` |
| `Math.floor(x)` | `double` | Round down | `Math.floor(3.9)` → `3.0` |
| `Math.ceil(x)` | `double` | Round up | `Math.ceil(3.1)` → `4.0` |
| `Math.random()` | `double` | Random value [0.0, 1.0) | `Math.random()` → `0.7362...` |
| `Math.PI` | `double` | Constant: 3.14159... | `Math.PI` → `3.141592653...` |
| `Math.E` | `double` | Constant: 2.71828... | `Math.E` → `2.718281828...` |

### The Random Class (java.util — must import)

```java
import java.util.Random;
Random rand = new Random();
int n = rand.nextInt(10);   // 0 through 9
```

| Method | Returns | Description |
|--------|---------|-------------|
| `nextInt()` | `int` | Any random integer |
| `nextInt(bound)` | `int` | 0 (inclusive) to bound (exclusive) |
| `nextDouble()` | `double` | 0.0 (inclusive) to 1.0 (exclusive) |
| `nextBoolean()` | `boolean` | `true` or `false` randomly |
| `nextLong()` | `long` | Any random long |

### Generating a random number in a range

```java
// Random int between min and max (inclusive)
int result = rand.nextInt(max - min + 1) + min;

// Example: random number between 5 and 15
int roll = rand.nextInt(11) + 5;
```

---

## Part 1: Math Method Explorer

### Program A: `MathExplorer.java`

Write a program that demonstrates every `Math` method and constant from the table above:

1. **Absolute value:** Show `Math.abs()` with a positive number, a negative number, and zero. Show it with both `int` and `double`.

2. **Max and Min:** Compare pairs of numbers using `Math.max()` and `Math.min()`. Include a three-way maximum using nested calls:
   ```java
   int biggest = Math.max(Math.max(a, b), c);
   ```

3. **Power and Square Root:**
   - Calculate 2^10 (1024)
   - Calculate the square root of 225 (15)
   - Show that `Math.sqrt(Math.pow(x, 2))` gives back `x`

4. **Rounding — round vs. floor vs. ceil:** For each of these values, show all three results: `3.2`, `3.5`, `3.8`, `-3.2`, `-3.5`, `-3.8`
   ```
   Value    round()  floor()  ceil()
   3.2      3        3.0      4.0
   3.5      4        3.0      4.0
   3.8      4        3.0      4.0
   -3.2     -3       -4.0     -3.0
   -3.5     -3       -4.0     -3.0
   -3.8     -4       -4.0     -3.0
   ```
   Use `printf` to format this as a clean table. Add a comment noting the surprising behavior of `round()` with negative numbers.

5. **Constants:** Use `Math.PI` and `Math.E` in calculations:
   - Area and circumference of a circle with radius 7
   - Volume of a sphere with radius 5: `(4.0/3.0) * Math.PI * Math.pow(r, 3)`

---

## Part 2: Random Number Generation

### Program B: `RandomExplorer.java`

Write a program that demonstrates the `Random` class:

1. **Basic generation:** Create a `Random` object and generate and print:
   - 5 random integers (any range)
   - 5 random integers between 0 and 99
   - 5 random doubles between 0.0 and 1.0
   - 5 random booleans

2. **Custom ranges:** Generate random numbers in specific ranges:
   - A random number between 1 and 6 (dice roll)
   - A random number between 1 and 100
   - A random number between -50 and 50
   - A random number between 10 and 20

3. **Math.random() comparison:** Show how to accomplish the same ranges using `Math.random()` instead of the `Random` class:
   ```java
   // Dice roll with Math.random()
   int roll = (int)(Math.random() * 6) + 1;
   ```

4. **Seeds and reproducibility:** Create two `Random` objects with the same seed and show they produce the same sequence:
   ```java
   Random rand1 = new Random(12345);
   Random rand2 = new Random(12345);
   // Print 5 numbers from each — they should match
   ```

---

## Part 3: Practical Applications

### Program C: `DiceSimulator.java`

Write a program that simulates rolling two six-sided dice 1,000 times and tracks the results:

1. Roll two dice and sum them for each roll
2. Track how many times each sum (2 through 12) appears using an array of counters
3. After all rolls, print a frequency table:
   ```
   Sum   Count   Percentage   Bar
   2     28      2.8%         ***
   3     54      5.4%         *****
   4     85      8.5%         *********
   5     112     11.2%        ***********
   6     138     13.8%        **************
   7     167     16.7%        *****************
   8     142     14.2%        **************
   9     109     10.9%        ***********
   10    82      8.2%         ********
   11    55      5.5%         ******
   12    28      2.8%         ***
   ```
4. Use `printf` for clean column alignment
5. Print which sum occurred most and least often using `Math.max()` logic
6. Add a comment: does the distribution roughly match what probability theory predicts? (7 should be the most common)

### Program D: `GeometryCalculator.java`

Write a program that uses the `Math` class to perform geometry calculations. Use `Scanner` for input and `printf` for output.

Implement a menu-driven calculator:
```
=== Geometry Calculator ===
1. Circle (area, circumference)
2. Triangle (area, hypotenuse)
3. Rectangle (area, diagonal)
4. Sphere (volume, surface area)
5. Distance between two points
Choose an option:
```

For each option:
1. **Circle:** Given radius, calculate area (`PI * r^2`) and circumference (`2 * PI * r`)
2. **Triangle:** Given two sides, calculate area (`0.5 * base * height`) and hypotenuse (`sqrt(a^2 + b^2)`)
3. **Rectangle:** Given width and height, calculate area and diagonal (`sqrt(w^2 + h^2)`)
4. **Sphere:** Given radius, calculate volume (`(4/3) * PI * r^3`) and surface area (`4 * PI * r^2`)
5. **Distance:** Given (x1, y1) and (x2, y2), calculate distance (`sqrt((x2-x1)^2 + (y2-y1)^2)`)

Format all output to 2 decimal places using `printf`.

---

## Part 4: Mini-Game

### Program E: `NumberGuessingGame.java`

Build a number guessing game that combines `Random`, `Math`, `Scanner`, String methods, and `printf`:

1. Generate a random number between 1 and 100
2. Give the player 7 attempts to guess it
3. After each guess, tell them if they are too high, too low, or correct
4. Track the number of guesses used
5. After a correct guess, calculate how far off their first guess was using `Math.abs()`
6. Print a formatted summary:
   ```
   ╔══════════════════════════════════╗
   ║      NUMBER GUESSING GAME       ║
   ╠══════════════════════════════════╣
   ║  The number was: 42             ║
   ║  You guessed it in: 4 attempts  ║
   ║  First guess was off by: 23     ║
   ║  Rating: Good!                  ║
   ╚══════════════════════════════════╝
   ```
7. Assign a rating using the ternary operator:
   - 1 guess: "Incredible!"
   - 2-3 guesses: "Excellent!"
   - 4-5 guesses: "Good!"
   - 6-7 guesses: "Keep practicing!"
   - Ran out of guesses: "Better luck next time!"

8. After the game, ask if they want to play again (use `Scanner` and `String` methods to accept "yes", "YES", "y", etc.)

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why are all `Math` methods `static`? What would it mean if they weren't?
2. What is the difference between `Math.round()`, `Math.floor()`, and `Math.ceil()`? When would you use each?
3. Why does `rand.nextInt(6)` give you 0-5 instead of 1-6? How do you shift the range?
4. When would you use a seeded `Random` instead of an unseeded one?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Random_and_Math_in_Practice.md` containing:

1. Your observations about the dice distribution from Part 3
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `MathExplorer.java`: All methods demonstrated, rounding table formatted | 15 |
| `RandomExplorer.java`: All generation types shown, seeds demonstrated | 15 |
| `DiceSimulator.java`: 1000 rolls, frequency table, distribution analysis | 20 |
| `GeometryCalculator.java`: All 5 options working with formatted output | 20 |
| `NumberGuessingGame.java`: Full game with all features working | 15 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

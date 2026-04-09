# Module 7: Java Data Types Part 2

> 🏷️ Useful Soon

> 🎯 **Teach:** How type casting works in Java, the difference between widening and narrowing conversions, and how automatic promotion affects arithmetic expressions
> **See:** The full widening chain from byte to double, narrowing casts that lose data, promotion rules in mixed-type expressions, and a temperature converter that demonstrates casting pitfalls
> **Feel:** Clarity about when Java handles type conversion automatically and when you need an explicit cast, plus awareness of the data loss traps the exam loves to test

> 🎙️ Yesterday you learned about Java's eight primitive types. Today you are going to learn what happens when you need to move a value from one type to another. Java has strict rules about this, and the certification exam tests them heavily. You will see which conversions happen automatically, which ones require a cast, and what can go wrong when data does not fit.

> 🎙️ Think of it this way -- pouring water from a small cup into a big bucket is safe, that is widening. Pouring from a big bucket into a small cup will spill, that is narrowing. Java lets the safe direction happen automatically but makes you explicitly say "I know this might spill" for the dangerous direction.

## Research: Type Casting and Promotion

> 🎯 **Teach:** What type casting is, the widening promotion hierarchy from byte to double, why narrowing requires an explicit cast, and the risks of data loss when narrowing.
> **See:** The full widening chain (byte -> short -> int -> long -> float -> double) and examples of truncation and overflow during narrowing casts.
> **Feel:** Clarity about when Java handles conversion automatically and when you must intervene with a cast.

### Overview

- **Topic:** Working with Java Data Types — Casting and Automatic Promotion
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is type casting in Java?** Explain what it means to cast a value from one data type to another. Why is casting sometimes necessary?

2. **What is the difference between widening (automatic) and narrowing (manual) conversions?** Describe Java's promotion hierarchy (byte → short → int → long → float → double). Why does Java allow widening automatically but require explicit casting for narrowing?

3. **What are the risks of narrowing casts?** What can go wrong when you cast a `double` to an `int`, or a `long` to a `byte`? Explain with examples of data loss or unexpected results.

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Type_Casting_Research.md` in this folder.

> 💡 **Remember this one thing:** Java automatically widens from smaller to larger types (byte to int to double) but requires an explicit cast to narrow, because narrowing can lose data.

> 🎙️ When you research the widening chain, memorize this order -- byte, short, int, long, float, double. Any type can automatically become any type to its right. Going left requires a cast. The exam will absolutely test whether you know which direction is automatic and which is not.

## Hands-On: Type Casting and Promotion in Practice

> 🎯 **Teach:** How to perform widening and narrowing conversions, predict the result type of mixed-type expressions, and avoid the integer-division and byte-promotion pitfalls the exam tests.
> **See:** The full widening chain in code, five narrowing scenarios with data loss, six promotion rule puzzles, and a temperature converter demonstrating casting traps.
> **Feel:** Readiness to predict the outcome of any casting or promotion question on the certification exam.

> 🎙️ Now you are going to see casting and promotion in action. You will walk through the entire widening chain, deliberately lose data with narrowing casts, and discover the promotion rules that catch many students off guard on the exam.

### Overview

- **Topic:** Working with Java Data Types — Widening, Narrowing, and Automatic Promotion
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

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

#### The Promotion Hierarchy

```
byte → short → int → long → float → double
```

Any type on the left can be automatically promoted to any type on the right.

#### Automatic Promotion in Expressions

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

> 🎙️ That automatic promotion rule is the one that catches the most students. Even though both a and b are bytes, the moment you add them together Java promotes the result to int. You cannot store it back in a byte without a cast. This is a top exam question -- do not skip over it.

---

### Part 1: Widening Conversions

#### Program A: `WideningDemo.java`

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

> 🎙️ As you walk through each widening step, notice that the value stays the same. That is the whole point of widening -- no data is lost. The value 42 as a byte is the same 42 as an int, the same 42 as a long. It just gets a bigger container.

---

### Part 2: Narrowing Conversions

#### Program B: `NarrowingDemo.java`

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

> 🎙️ Narrowing is where things get dangerous and interesting. Casting double 9.99 to int does not round -- it truncates, dropping the decimal entirely. And casting 130 to byte gives you negative 126 because of overflow. These are exactly the traps the exam sets for you.

---

### Part 3: Automatic Promotion in Expressions

#### Program C: `PromotionRules.java`

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

> 🎙️ For the promotion rules exercise, write your prediction as a comment before you run each scenario. This practice of predicting first and then verifying is exactly what the exam requires. If your prediction is wrong, figure out why before moving on -- that is where the real learning happens.

---

### Part 4: Practical Application

#### Program D: `TemperatureConverter.java`

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

#### Program E: `GradeRounder.java`

Write a program that takes a set of exam scores as `double` values and:

1. Calculates the average (as a `double`)
2. Casts the average to an `int` to show truncation
3. Uses `Math.round()` to show proper rounding
4. Demonstrates the difference between truncation and rounding with at least 3 different averages (e.g., 89.4, 89.5, 89.9)
5. Assigns a letter grade based on the rounded value

---

### Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why does Java automatically promote `byte` and `short` to `int` in arithmetic expressions?
2. What is the difference between truncation and rounding? Why does casting to `int` truncate instead of round?
3. A common exam question: what is the result of `10 / 3` in Java? What about `10 / 3.0`? Explain why they differ.

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Type_Casting_in_Practice.md` containing:

1. Your predictions vs. actual results from Part 3
2. Your casting pitfall demonstration from Part 4
3. Your answers to the reflection questions

> 💡 **Remember this one thing:** When byte, short, or char values are used in arithmetic, Java always promotes them to int first — this is the source of many exam questions and subtle bugs.

## Grading

> 🎯 **Teach:** How each assignment is evaluated so the student can self-assess before submitting.
> **See:** Detailed rubrics for the casting research essay and the five hands-on widening, narrowing, and promotion exercises.
> **Feel:** Clarity about expectations and momentum heading into the Strings capstone on Day 8.

> 🔄 **Where this fits:** Day 7 builds directly on Day 6's primitive types by teaching how values move between types — casting and promotion rules are a top exam topic and essential for writing correct calculations.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains what type casting is and why it is needed | 25 |
| Accurately describes widening vs. narrowing with the promotion hierarchy | 30 |
| Explains risks of narrowing casts with examples of data loss | 25 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

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

> 🎙️ You now understand how Java moves values between types -- widening, narrowing, and automatic promotion. Tomorrow you complete the data types block with Strings, which are the most commonly used type in Java and one of the most heavily tested topics on the exam. Everything from today connects directly to what comes next.

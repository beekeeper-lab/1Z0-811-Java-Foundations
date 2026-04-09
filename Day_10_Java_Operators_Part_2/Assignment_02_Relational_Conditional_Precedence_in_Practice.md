# Day 10 Assignment: Relational, Conditional, and Precedence in Practice

## Overview

- **Topic:** Working with Java Operators — Relational, Logical, Ternary, and Operator Precedence
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Relational Operators (return `boolean`)

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `true` |
| `!=` | Not equal to | `5 != 3` | `true` |
| `>` | Greater than | `5 > 3` | `true` |
| `>=` | Greater than or equal | `5 >= 5` | `true` |
| `<` | Less than | `3 < 5` | `true` |
| `<=` | Less than or equal | `5 <= 5` | `true` |

### Conditional (Logical) Operators

| Operator | Meaning | Behavior |
|----------|---------|----------|
| `&&` | AND | `true` only if BOTH sides are `true` |
| `\|\|` | OR | `true` if EITHER side is `true` |
| `!` | NOT | Flips `true` to `false` and vice versa |

### The Ternary Operator

```java
String result = (score >= 60) ? "Pass" : "Fail";
// Equivalent to:
// if (score >= 60) { result = "Pass"; } else { result = "Fail"; }
```

### Operator Precedence (highest to lowest, simplified)

```
1. () — parentheses (highest)
2. ++ -- ! — unary operators
3. * / % — multiplication, division, modulo
4. + - — addition, subtraction
5. < > <= >= — relational
6. == != — equality
7. && — logical AND
8. || — logical OR
9. ? : — ternary
10. = += -= *= /= %= — assignment (lowest)
```

---

## Part 1: Relational Operators

### Program A: `RelationalDemo.java`

Write a program that demonstrates all six relational operators:

1. **Numeric comparisons:** Declare two `int` variables and print the result of every relational operator between them:
   ```
   a = 10, b = 20
   a == b: false
   a != b: true
   a > b:  false
   a >= b: false
   a < b:  true
   a <= b: true
   ```

2. **Comparing equal values:** Repeat with `a = 15, b = 15` — note which operators return `true` now.

3. **Double comparison trap:** Demonstrate why comparing `double` values with `==` can be unreliable:
   ```java
   double x = 0.1 + 0.2;
   double y = 0.3;
   System.out.println(x == y);  // What does this print? Why?
   System.out.println(Math.abs(x - y) < 0.0001);  // Better approach
   ```
   Add a comment explaining floating-point precision.

4. **char comparisons:** Characters can be compared because they have numeric Unicode values:
   ```java
   char a = 'A';  // Unicode 65
   char b = 'Z';  // Unicode 90
   System.out.println(a < b);   // true
   System.out.println(a == 65); // true
   ```
   Compare a few characters and explain the results.

---

## Part 2: Conditional (Logical) Operators

### Program B: `LogicalOperators.java`

Write a program that demonstrates `&&`, `||`, and `!`:

1. **Truth table for AND:** Print all four combinations:
   ```
   true  && true  = true
   true  && false = false
   false && true  = false
   false && false = false
   ```

2. **Truth table for OR:** Print all four combinations.

3. **NOT:** Demonstrate `!true` and `!false`.

4. **Practical examples using variables:**
   ```java
   int age = 20;
   boolean hasLicense = true;
   boolean hasInsurance = false;

   // Can they drive?
   boolean canDrive = (age >= 16) && hasLicense && hasInsurance;
   System.out.println("Can drive: " + canDrive);  // false — no insurance
   ```

5. **Short-circuit evaluation:** This is important for the exam. Demonstrate that Java stops evaluating as soon as the result is known:
   ```java
   int x = 0;

   // With &&: if the left side is false, the right side is NEVER evaluated
   boolean result1 = (x != 0) && (10 / x > 2);
   System.out.println("result1: " + result1);  // false — no crash!

   // Without short-circuit, 10 / 0 would crash. Prove it:
   // boolean crash = (10 / x > 2);  // Uncomment to see ArithmeticException
   ```

   ```java
   // With ||: if the left side is true, the right side is NEVER evaluated
   boolean result2 = (x == 0) || (10 / x > 2);
   System.out.println("result2: " + result2);  // true — right side skipped
   ```

6. **Side effects with short-circuit:** Predict the output before running:
   ```java
   int a = 5;
   boolean test = (a > 10) && (++a > 5);
   System.out.println("a = " + a);  // Is a still 5 or 6?

   int b = 5;
   boolean test2 = (b < 10) || (++b > 5);
   System.out.println("b = " + b);  // Is b still 5 or 6?
   ```
   Add comments explaining why the increment did or didn't happen.

---

## Part 3: The Ternary Operator

### Program C: `TernaryDemo.java`

Write a program that demonstrates the ternary operator in various situations:

1. **Basic usage:**
   ```java
   int score = 75;
   String result = (score >= 60) ? "Pass" : "Fail";
   System.out.println(result);
   ```

2. **Assigning a number:**
   ```java
   int a = 10, b = 20;
   int max = (a > b) ? a : b;
   System.out.println("Max: " + max);
   ```

3. **Inside a print statement:**
   ```java
   int temperature = 35;
   System.out.println("It is " + ((temperature > 30) ? "hot" : "not hot") + " today.");
   ```

4. **Nested ternary** (for awareness — show that it works but can be hard to read):
   ```java
   int grade = 85;
   String letter = (grade >= 90) ? "A"
                 : (grade >= 80) ? "B"
                 : (grade >= 70) ? "C"
                 : "F";
   ```
   Add a comment that nested ternaries are generally discouraged in favor of if/else chains for readability.

5. **Converting 5 simple if/else blocks to ternary:** Write 5 different scenarios as if/else first, then convert each to a ternary expression. Examples:
   - Determine if a number is positive or negative
   - Determine if a year is a leap year (divisible by 4)
   - Set a discount rate based on membership status
   - Choose singular vs. plural wording (e.g., "1 item" vs. "3 items")
   - Determine AM or PM from a 24-hour value

---

## Part 4: Operator Precedence

### Program D: `PrecedenceExplorer.java`

Write a program that demonstrates why precedence matters. For each expression below:
- Write your **prediction** as a comment
- Print the actual result
- Add the expression **with parentheses** showing the order Java evaluates it

1. **Arithmetic precedence:**
   ```java
   int a = 2 + 3 * 4;        // Is this 20 or 14?
   int b = (2 + 3) * 4;      // What about now?
   ```

2. **Mixed arithmetic and relational:**
   ```java
   boolean c = 10 > 5 + 3;   // Is 5 + 3 evaluated first?
   boolean d = 10 > (5 + 3); // Same or different?
   ```

3. **Logical operator precedence — && before ||:**
   ```java
   boolean e = true || false && false;
   // Is this (true || false) && false → false?
   // Or true || (false && false) → true?
   ```

4. **Complex expression:**
   ```java
   int x = 5;
   boolean f = x > 3 && x < 10 || x == 20;
   // Add parentheses to show the actual evaluation order
   ```

5. **Assignment is last:**
   ```java
   int g = 2;
   g += 3 * 2;  // Is this (g + 3) * 2 or g + (3 * 2)?
   ```

6. **The parentheses fix:** Rewrite each expression above with explicit parentheses, and add a comment: *"When in doubt, use parentheses to make your intent clear."*

---

## Part 5: Operators Capstone

### Program E: `EligibilityChecker.java`

Build a program that determines eligibility for various programs using **every operator type** from Days 9 and 10. Use `Scanner` to read input from the user.

Collect the following information:
- Name (`String`)
- Age (`int`)
- Annual income (`double`)
- Years of experience (`int`)
- Has a degree (`boolean` — accept `true` or `false`)
- Credit score (`int`)

Determine eligibility for each of the following using compound boolean expressions:

1. **Voting:** Age >= 18
2. **Car rental:** Age >= 21 AND has a degree OR age >= 25
3. **Loan approval:** Credit score >= 700 AND income >= 30000 AND age >= 18
4. **Senior discount:** Age >= 65 OR (age >= 60 AND income < 25000)
5. **Job posting:** (Has degree AND experience >= 2) OR (experience >= 5)
6. **Premium membership:** Income >= 50000 AND credit score >= 750 AND age >= 21

For each check:
- Use the ternary operator to assign "Eligible" or "Not Eligible"
- Print the result with the criteria shown
- Use `&&`, `||`, and `!` appropriately
- Use parentheses to make the logic clear

Print a final summary:
```
=== Eligibility Report for Campbell Reed ===
Voting:             Eligible
Car Rental:         Eligible
Loan Approval:      Not Eligible
Senior Discount:    Not Eligible
Job Posting:        Eligible
Premium Membership: Not Eligible
---
Eligible for 3 out of 6 programs.
```

Use a counter variable with `++` to count how many programs the user is eligible for, and use `%` to determine if that count is odd or even (just for practice).

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is short-circuit evaluation, and how could it prevent a runtime error?
2. Why does `&&` have higher precedence than `||`? Can you think of a real-world analogy?
3. When is a ternary operator better than an if/else, and when is it worse?
4. Looking back at Days 9 and 10 together — which operator concept do you think will appear most on the exam, and why?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Relational_Conditional_Precedence_in_Practice.md` containing:

1. Your predictions vs. actual results from Parts 2 and 4
2. Your short-circuit evaluation explanations
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `RelationalDemo.java`: All 6 operators demonstrated, double comparison trap shown | 10 |
| `LogicalOperators.java`: Truth tables, short-circuit demonstrated and explained | 20 |
| `TernaryDemo.java`: All scenarios shown, 5 if/else conversions completed | 15 |
| `PrecedenceExplorer.java`: All expressions with predictions and parenthesized versions | 15 |
| `EligibilityChecker.java`: All operator types used, user input, correct logic | 20 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

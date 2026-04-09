# Day 16 Assignment: Equality, Comparison, and Decision Statements Capstone

## Overview

- **Topic:** Using Decision Statements — == vs .equals(), compareTo(), and a comprehensive capstone
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### == with primitives vs. objects

```java
// Primitives — == compares VALUES
int a = 5;
int b = 5;
System.out.println(a == b);  // true

// Objects — == compares REFERENCES (memory addresses)
String s1 = new String("Hello");
String s2 = new String("Hello");
System.out.println(s1 == s2);      // false — different objects
System.out.println(s1.equals(s2)); // true — same content
```

### compareTo()

`compareTo()` returns an `int` for lexicographic (alphabetical) comparison:

```java
String a = "Apple";
String b = "Banana";
String c = "Apple";

a.compareTo(b);  // negative — "Apple" comes BEFORE "Banana"
b.compareTo(a);  // positive — "Banana" comes AFTER "Apple"
a.compareTo(c);  // 0 — they are equal
```

**Rule of thumb:** Think of `a.compareTo(b)` as `a - b`:
- Negative → a comes first
- Zero → they're equal
- Positive → b comes first

---

## Part 1: == vs .equals() Deep Dive

### Program A: `EqualityExplorer.java`

Write a program that covers every scenario tested on the exam:

1. **Primitives with ==:**
   ```java
   int a = 10, b = 10;
   double c = 10.0;
   System.out.println("int == int: " + (a == b));       // true
   System.out.println("int == double: " + (a == c));     // true (widening)
   ```

2. **String literals with ==:**
   ```java
   String s1 = "Java";
   String s2 = "Java";
   String s3 = "Ja" + "va";  // Compile-time constant
   System.out.println("literal == literal: " + (s1 == s2));  // true — same pool object
   System.out.println("literal == concat literal: " + (s1 == s3));  // true — compiler optimizes
   ```

3. **String objects with ==:**
   ```java
   String s4 = new String("Java");
   String s5 = new String("Java");
   System.out.println("new == new: " + (s4 == s5));          // false
   System.out.println("literal == new: " + (s1 == s4));      // false
   System.out.println("new .equals(new): " + (s4.equals(s5))); // true
   ```

4. **Runtime concatenation:**
   ```java
   String part = "Ja";
   String s6 = part + "va";  // Runtime concatenation — NOT a compile-time constant
   System.out.println("literal == runtime concat: " + (s1 == s6));  // false!
   ```
   Add a comment explaining why this differs from `"Ja" + "va"`.

5. **The null trap:**
   ```java
   String nullStr = null;
   // System.out.println(nullStr.equals("test"));  // NullPointerException!
   System.out.println("test".equals(nullStr));      // false — safe!
   ```
   Add a comment explaining why you should put the literal on the LEFT side of `.equals()`.

6. For each scenario, add a comment explaining the result.

---

## Part 2: compareTo() in Action

### Program B: `CompareToExplorer.java`

Write a program that demonstrates `compareTo()`:

1. **Basic comparisons:**
   ```java
   String a = "Apple";
   String b = "Banana";
   String c = "Cherry";
   String d = "Apple";
   ```
   Print `a.compareTo(b)`, `b.compareTo(a)`, `a.compareTo(d)`, and `c.compareTo(a)`. For each, state whether the result is negative, zero, or positive and what that means.

2. **Case sensitivity:**
   ```java
   String upper = "HELLO";
   String lower = "hello";
   System.out.println(upper.compareTo(lower));  // negative — uppercase comes first in Unicode
   ```
   Add a comment explaining that uppercase letters have lower Unicode values than lowercase.

3. **Using compareTo() for sorting decisions:**
   Given three names entered by the user, determine which comes first and last alphabetically using `compareTo()` and if statements:
   ```
   Enter name 1: Charlie
   Enter name 2: Alice
   Enter name 3: Bob

   Alphabetical order:
   1. Alice
   2. Bob
   3. Charlie
   ```
   Use `compareTo()` in if-else logic to sort them (no arrays needed — just compare pairs).

4. **Using compareTo() for range checks:**
   Read a word from the user and determine if it falls in the first half of the alphabet (A-M) or the second half (N-Z):
   ```java
   if (word.toUpperCase().compareTo("N") < 0) {
       System.out.println("First half of the alphabet");
   }
   ```

---

## Part 3: Choosing the Right Structure

### Program C: `DecisionChooser.java`

For each scenario below, implement the solution using the **most appropriate** decision structure. Add a comment above each solution explaining WHY you chose that structure.

1. **Check if a number is even** — (Which structure: single if, if-else, ternary, or switch?)

2. **Map a numeric month (1-12) to its name** — (Which structure is cleanest?)

3. **Determine shipping cost based on weight:**
   - Under 1 lb: $3.00
   - 1-5 lbs: $5.00
   - 5-20 lbs: $10.00
   - Over 20 lbs: $20.00

4. **Set a greeting based on time of day:**
   - 5-11: "Good morning"
   - 12-16: "Good afternoon"
   - 17-20: "Good evening"
   - 21-4: "Good night"

5. **Validate a password** — must be at least 8 characters, contain at least one digit, and not contain the word "password" (multiple independent checks)

6. **Assign a label from a single character:**
   - 'R' → "Red", 'G' → "Green", 'B' → "Blue"

7. **Determine maximum of three numbers** — (Can you do this with ternary? With Math.max? With if-else?)

8. **Print whether a year is a leap year** — Leap year rules: divisible by 4, EXCEPT if divisible by 100, UNLESS also divisible by 400

For each one, implement the solution and add a brief comment explaining your structure choice.

---

## Part 4: Decision Statements Capstone

### Program D: `BankAccountSimulator.java`

Build an interactive bank account simulator that combines **everything from Days 14, 15, and 16**. This is the capstone for the entire Decision Statements section.

The program should:

1. **Start with account setup** using if-else validation:
   - Ask for account holder name (validate not empty with `trim().isEmpty()`)
   - Ask for account type: "checking" or "savings" (validate with `equalsIgnoreCase()`)
   - Ask for initial deposit (validate it's positive)

2. **Display a menu using switch:**
   ```
   === Bank Account: Campbell Reed (Checking) ===
   Balance: $1,000.00
   ─────────────────────────────
   1. Deposit
   2. Withdraw
   3. Check Balance
   4. Transfer (checking ↔ savings)
   5. Account Summary
   6. Exit
   Choose an option:
   ```

3. **Implement each menu option:**
   - **Deposit:** Read amount, validate > 0, add to balance
   - **Withdraw:** Read amount, validate > 0, check sufficient funds using if-else:
     - If checking: allow overdraft up to -$100 but charge $35 fee
     - If savings: do not allow overdraft
   - **Check Balance:** Print formatted balance with account type
   - **Transfer:** Simulate a transfer — ask for amount, subtract from current, add to "other" account (just track two balances)
   - **Account Summary:** Print a formatted summary including:
     - Account holder, account type
     - Current balance
     - Number of transactions (track with a counter)
     - Number of overdraft fees charged
     - Total fees paid
   - **Exit:** Print goodbye message

4. **Use these decision structures throughout:**
   - `switch` for the menu
   - `if-else` for validation and business rules
   - `else-if` chains for multi-condition checks
   - Ternary operator for inline formatting (e.g., showing "Overdrawn" or "Good standing")
   - `compareTo()` or `equals()` for String comparisons
   - `==` for numeric comparisons

5. **Loop the menu** until the user chooses Exit (use a `while` loop — we'll cover these formally on Days 17-19, but you've seen loops in examples. A simple `while (running)` is fine here).

6. **Format all output** with `printf` and proper currency formatting.

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the most common mistake beginners make with `==` and Strings? How do you avoid it?
2. What does `compareTo()` return, and how do you remember what negative, zero, and positive mean?
3. Looking back at Days 14, 15, and 16 — which decision structure do you think you'll use most often in real programs? Why?
4. Why should you put the literal on the left side of `.equals()` (e.g., `"admin".equals(input)` instead of `input.equals("admin")`)?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Equality_Comparison_and_Decisions_Capstone.md` containing:

1. Your structure choice explanations from Part 3
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `EqualityExplorer.java`: All == vs .equals() scenarios with explanations | 15 |
| `CompareToExplorer.java`: All compareTo scenarios, sorting, and range check | 15 |
| `DecisionChooser.java`: All 8 scenarios with correct structure choices | 15 |
| `BankAccountSimulator.java`: Full simulator with all menu options and validation | 35 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

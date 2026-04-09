# Day 8 Assignment: Strings and Type Conversions in Practice

## Overview

- **Topic:** Working with Java Data Types — Strings, String Initialization, and Converting Between Types
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

Strings are one of the most-used types in Java, and the exam tests them heavily. Key things to know:

```java
// String literals — stored in the String Pool
String a = "Hello";
String b = "Hello";
// a and b point to the SAME object in the pool

// Using new — creates a separate object
String c = new String("Hello");
// c is a different object, even though it has the same value

// This is why:
System.out.println(a == b);      // true  (same pool object)
System.out.println(a == c);      // false (different objects)
System.out.println(a.equals(c)); // true  (same content)
```

### Converting Between Strings and Primitives

```java
// Primitive → String
String s1 = String.valueOf(42);        // "42"
String s2 = Integer.toString(42);      // "42"
String s3 = "" + 42;                   // "42" (concatenation trick)

// String → Primitive
int i = Integer.parseInt("42");
double d = Double.parseDouble("3.14");
boolean b = Boolean.parseBoolean("true");
```

---

## Part 1: String Declaration and Initialization

### Program A: `StringBasics.java`

Write a program that demonstrates the different ways to create and work with strings:

1. Create a string using a literal: `String greeting = "Hello";`
2. Create a string using `new`: `String greeting2 = new String("Hello");`
3. Create an empty string: `String empty = "";`
4. Create a `null` string: `String nothing = null;`
5. Concatenate strings using `+`
6. Concatenate strings using `.concat()`

Print each one and demonstrate:
- The difference between an **empty string** and a **null string** (print the length of the empty string; what happens if you try to get the length of null? Comment out the crashing line and explain the error)
- That `+` can concatenate strings with non-string types:
  ```java
  int age = 20;
  String message = "I am " + age + " years old.";
  ```

---

## Part 2: String Immutability

### Program B: `ImmutabilityDemo.java`

Write a program that proves strings are immutable:

1. Create a string variable: `String original = "Hello";`
2. Call `original.toUpperCase();` on its own line (without assigning the result)
3. Print `original` — has it changed?
4. Now assign the result: `String upper = original.toUpperCase();`
5. Print both `original` and `upper` — show that `original` is unchanged

6. Demonstrate the same concept with `replace()`:
   ```java
   String phrase = "I like cats";
   phrase.replace("cats", "dogs");  // Does this change phrase?
   System.out.println(phrase);       // What prints?
   ```

7. Show the correct way:
   ```java
   String newPhrase = phrase.replace("cats", "dogs");
   System.out.println(newPhrase);
   ```

8. Add comments explaining **why** this happens — strings are immutable, so every method returns a NEW string.

---

## Part 3: == vs .equals()

### Program C: `StringEquality.java`

This is a **critical exam topic**. Write a program that demonstrates the difference between `==` and `.equals()` for strings:

1. **Scenario 1 — Two literals:**
   ```java
   String a = "Java";
   String b = "Java";
   ```
   Print `a == b` and `a.equals(b)`. Explain why both are `true`.

2. **Scenario 2 — Literal vs. new:**
   ```java
   String a = "Java";
   String c = new String("Java");
   ```
   Print `a == c` and `a.equals(c)`. Explain why `==` is `false` but `.equals()` is `true`.

3. **Scenario 3 — Concatenation:**
   ```java
   String a = "Java";
   String d = "Ja" + "va";
   String e = "Ja";
   String f = e + "va";
   ```
   Print `a == d` and `a == f`. Explain why the results differ. (Hint: compile-time constants vs. runtime concatenation)

4. **The rule for the exam:** Add a summary comment stating: *"Always use `.equals()` to compare string content. Use `==` only when you intentionally want to compare object references."*

---

## Part 4: Converting Between Strings and Primitives

### Program D: `TypeConversions.java`

Write a program that demonstrates all common conversions between strings and primitives:

**String → Primitive:**
1. Parse `"42"` to `int` using `Integer.parseInt()`
2. Parse `"3.14"` to `double` using `Double.parseDouble()`
3. Parse `"true"` to `boolean` using `Boolean.parseBoolean()`
4. Parse `"A"` to `char` using `.charAt(0)`

**Primitive → String:**
5. Convert `int 100` to String using `String.valueOf()`
6. Convert `double 9.99` to String using `Double.toString()`
7. Convert `boolean true` to String using `String.valueOf()`
8. Convert using concatenation: `"" + 42`

**Error handling:**
9. What happens when you try `Integer.parseInt("hello")`? Wrap it in a try/catch and print the exception message. (We'll cover exceptions more on Day 20, but this is a good preview.)
10. What happens with `Integer.parseInt("3.14")`? Try it and explain.

---

## Part 5: Data Types Capstone

### Program E: `StudentRecordBuilder.java`

Build a program that ties together everything from Days 6, 7, and 8. The program should:

1. Use `Scanner` to read the following input from the user as **Strings**:
   - Student name
   - Age (entered as text, e.g., `"20"`)
   - GPA (entered as text, e.g., `"3.75"`)
   - Credits completed (entered as text, e.g., `"64"`)
   - Is full-time? (entered as text, e.g., `"true"`)

2. **Parse** each string input into the appropriate primitive type:
   - `int age = Integer.parseInt(ageInput);`
   - `double gpa = Double.parseDouble(gpaInput);`
   - etc.

3. Use `final` constants for:
   - Credits required for graduation (e.g., `120`)
   - GPA threshold for honors (e.g., `3.5`)
   - GPA threshold for Dean's List (e.g., `3.8`)

4. Calculate and display:
   - Credits remaining (cast to `int` if needed)
   - Percentage of degree completed (as `double`, formatted to 1 decimal place)
   - Whether the student qualifies for honors or Dean's List (`boolean`)
   - Estimated semesters remaining (use integer division and casting)

5. Print a formatted summary:
   ```
   === Student Record ===
   Name:               Campbell Reed
   Age:                20
   GPA:                3.75
   Credits Completed:  64 of 120
   Progress:           53.3%
   Full-Time:          true
   Honors:             true
   Dean's List:        false
   Semesters Remaining: 4
   ```

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between `==` and `.equals()` when comparing strings? When should you use each?
2. Why does `"Hello".toUpperCase()` not change the original string?
3. What is the String Pool, and why does Java use it?
4. Looking back at Days 6, 7, and 8 together — what is the relationship between primitive types, wrapper classes (like `Integer`), and `String`?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Strings_in_Practice.md` containing:

1. Your explanations for the `==` vs `.equals()` scenarios in Part 3
2. Your error explanations from Part 4
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `StringBasics.java`: All declaration styles and null/empty demonstrated | 10 |
| `ImmutabilityDemo.java`: Immutability clearly proven with explanations | 15 |
| `StringEquality.java`: All scenarios correct with accurate explanations | 20 |
| `TypeConversions.java`: All conversions demonstrated, errors explained | 15 |
| `StudentRecordBuilder.java`: Full capstone with parsing, constants, casting, and output | 20 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

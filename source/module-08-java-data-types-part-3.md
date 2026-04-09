# Module 8: Java Data Types Part 3

> 🏷️ Useful Soon

> 🎯 **Teach:** That String is a class not a primitive, what immutability means, the difference between == and .equals() for strings, and how to convert between strings and primitives
> **See:** Programs proving string immutability, the String Pool in action, == versus .equals() producing different results, and a capstone student record builder using Scanner, parsing, and casting
> **Feel:** Deep confidence with strings and type conversions, which are among the most heavily tested topics on the 1Z0-811 exam

> 🎙️ Today you are completing the data types block with the most-used type in Java -- String. Even though you have been using strings since Day 1, there is a lot more going on under the hood than you might expect. Strings are not primitives, they are immutable objects, and the exam tests the differences intensely. You will also tie together everything from Days 6, 7, and 8 in a capstone exercise.

> 🎙️ You have been using strings since Day 1, but here is what most beginners do not realize -- String is not a primitive type like int or double. It is a full class from java.lang. That distinction matters because strings behave differently from primitives in ways the exam specifically tests.

## Research: Strings in Java

> 🎯 **Teach:** Why String is a class and not a primitive, what immutability means for every string operation, and how the String Pool optimizes memory for string literals.
> **See:** The distinction between string literals and new String(), the mechanics of immutability, and how the String Pool reuses identical string objects.
> **Feel:** A deeper respect for strings as objects with behaviors that differ fundamentally from primitive types.

### Overview

- **Topic:** Working with Java Data Types — Strings as Objects, Not Primitives
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **Why is `String` not a primitive data type?** Explain how `String` is actually a class (from `java.lang`) and what it means that strings are objects. How does declaring a `String` differ from declaring an `int` or `double`?

2. **What does it mean that strings are immutable?** Explain what immutability means in the context of Java strings. When you "change" a string, what is actually happening in memory?

3. **What are the different ways to create strings in Java?** Describe the difference between string literals (`"hello"`) and using the `new` keyword (`new String("hello")`). What is the **String Pool**, and how does it relate to string creation?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Strings_Research.md` in this folder.

> 💡 **Remember this one thing:** Strings in Java are immutable — every method that appears to modify a string actually creates and returns a new String object, leaving the original unchanged.

> 🎙️ Immutability is the single most important concept about strings in Java. When you call toUpperCase on a string, the original string does not change. A brand new string is created and returned. If you do not capture that return value, the uppercase version is lost. This trips up beginners constantly.

## Hands-On: Strings and Type Conversions in Practice

> 🎯 **Teach:** How to prove string immutability in code, the critical difference between == and .equals() for string comparison, and how to convert between strings and primitives using parse and valueOf methods.
> **See:** Immutability experiments, three == vs .equals() scenarios with different results, type conversion methods, and a capstone student record builder combining all data type concepts.
> **Feel:** Deep confidence with strings and type conversions -- the most heavily tested topics on the 1Z0-811 exam.

> 🎙️ Now you are going to put strings through their paces. You will prove immutability with your own code, master the critical difference between == and .equals(), and build a capstone program that ties together primitives, casting, and strings from the entire data types block.

### Overview

- **Topic:** Working with Java Data Types — Strings, String Initialization, and Converting Between Types
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

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

> 🎙️ This is the trap -- the double equals operator checks whether two variables point to the same object in memory. The equals method checks whether the content is the same. For strings, you almost always want equals. Get this wrong on the exam and you lose easy points.

#### Converting Between Strings and Primitives

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

### Part 1: String Declaration and Initialization

#### Program A: `StringBasics.java`

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

> 🎙️ Pay attention to the difference between an empty string and null. An empty string is a real String object that just happens to contain zero characters -- you can call methods on it. A null string is not an object at all -- calling any method on it crashes your program with a NullPointerException.

---

### Part 2: String Immutability

#### Program B: `ImmutabilityDemo.java`

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

### Part 3: == vs .equals()

#### Program C: `StringEquality.java`

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

> 🎙️ Scenario 3 in the equality exercise is the trickiest one. When Java concatenates two string literals at compile time, it puts the result in the String Pool. But when one part is a variable, the concatenation happens at runtime and creates a new object outside the pool. That is why the double equals results differ even though the content is identical.

---

### Part 4: Converting Between Strings and Primitives

#### Program D: `TypeConversions.java`

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

> 🎙️ The type conversion methods you are learning here -- parseInt, parseDouble, valueOf -- are the bridge between strings and primitives. You will use them constantly whenever you read user input, because Scanner gives you strings and your program needs numbers. Knowing which method to call for which type is an essential skill.

---

### Part 5: Data Types Capstone

#### Program E: `StudentRecordBuilder.java`

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

### Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between `==` and `.equals()` when comparing strings? When should you use each?
2. Why does `"Hello".toUpperCase()` not change the original string?
3. What is the String Pool, and why does Java use it?
4. Looking back at Days 6, 7, and 8 together — what is the relationship between primitive types, wrapper classes (like `Integer`), and `String`?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Strings_in_Practice.md` containing:

1. Your explanations for the `==` vs `.equals()` scenarios in Part 3
2. Your error explanations from Part 4
3. Your answers to the reflection questions

> 💡 **Remember this one thing:** Always use `.equals()` to compare string content — the `==` operator compares object references, not the characters in the string, and this distinction is one of the most commonly tested concepts on the exam.

## Grading

> 🎯 **Teach:** How each assignment is evaluated so the student can self-assess before submitting.
> **See:** Detailed rubrics for the Strings research essay and the five hands-on string and conversion exercises including the capstone.
> **Feel:** Satisfaction at completing the entire data types block and readiness to move into operators.

> 🔄 **Where this fits:** Day 8 completes the data types block — primitives, casting, and Strings form the foundation that operators, control flow, and every other topic in the curriculum build upon.

### Research Grading

| Criteria | Points |
|----------|--------|
| Explains why String is a class, not a primitive, and what that means | 30 |
| Accurately describes string immutability and its implications | 30 |
| Covers string literals vs. `new String()` and the String Pool | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

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

> 🎙️ Congratulations -- you have completed the entire data types block. Over the last three days you covered primitives, type casting, and Strings, which together form one of the biggest sections on the certification exam. Starting tomorrow, you enter the operators block, where you will learn how to do math, make comparisons, and combine conditions in Java.

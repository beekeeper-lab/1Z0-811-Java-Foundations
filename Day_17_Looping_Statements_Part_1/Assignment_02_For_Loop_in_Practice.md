# Day 17 Assignment: The for Loop in Practice

## Overview

- **Topic:** Using Looping Statements — Standard for Loop and Enhanced for Loop
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Standard for loop

```java
for (initialization; condition; update) {
    // body — runs each iteration
}
```

Execution order:
1. **Initialization** runs once at the start
2. **Condition** is checked BEFORE each iteration — if false, loop ends
3. **Body** executes
4. **Update** runs AFTER the body
5. Go back to step 2

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);  // Prints 0, 1, 2, 3, 4
}
```

### Enhanced for loop (for-each)

```java
String[] names = {"Alice", "Bob", "Charlie"};
for (String name : names) {
    System.out.println(name);  // Prints each name
}
```

Read as: "for each `name` in `names`." No index variable, no bounds checking — Java handles it.

---

## Part 1: for Loop Fundamentals

### Program A: `ForLoopBasics.java`

Write a program that demonstrates the basic forms of for loops:

1. **Count up:** Print numbers 1 through 10
2. **Count down:** Print numbers 10 through 1
3. **Count by twos:** Print even numbers from 2 through 20
4. **Count by fives:** Print multiples of 5 from 5 through 100
5. **Negative range:** Print numbers from -5 to 5
6. **Character loop:** Print all uppercase letters A through Z using a `char` loop variable:
   ```java
   for (char c = 'A'; c <= 'Z'; c++) {
       System.out.print(c + " ");
   }
   ```

For each loop, print a label before the output so it's clear which is which.

---

## Part 2: Loop Execution Tracing

### Program B: `ForLoopTracing.java`

Understanding exactly when each part of the for loop executes is critical for the exam. Predict the output FIRST, then run.

1. **Off-by-one exploration:**
   ```java
   // How many times does each loop run?
   for (int i = 0; i < 5; i++)    // a) starts at 0, less than 5
   for (int i = 0; i <= 5; i++)   // b) starts at 0, less than or equal to 5
   for (int i = 1; i < 5; i++)    // c) starts at 1, less than 5
   for (int i = 1; i <= 5; i++)   // d) starts at 1, less than or equal to 5
   ```
   For each, print the iteration count and add a comment with your prediction.

2. **Unusual for loops (exam favorites):**
   ```java
   // Empty body — what does this do?
   int sum = 0;
   for (int i = 1; i <= 10; sum += i, i++) ;
   System.out.println("Sum: " + sum);
   ```

   ```java
   // Multiple variables
   for (int i = 0, j = 10; i < j; i++, j--) {
       System.out.println("i=" + i + " j=" + j);
   }
   ```

   ```java
   // All parts optional — infinite loop (runs 3 times then breaks)
   int count = 0;
   for (;;) {
       if (count >= 3) break;
       System.out.println("Iteration " + count);
       count++;
   }
   ```

3. **Variable scope:** What happens if you try to use the loop variable after the loop?
   ```java
   for (int i = 0; i < 5; i++) {
       System.out.println(i);
   }
   // System.out.println(i);  // Does this compile?
   ```
   Comment out the error line and explain why.

For each tricky example, write your prediction as a comment BEFORE the code, then verify.

---

## Part 3: Enhanced for Loop

### Program C: `EnhancedForLoop.java`

Write a program that demonstrates the enhanced for loop:

1. **Iterate over an int array:**
   ```java
   int[] scores = {88, 92, 76, 95, 83, 91, 87};
   ```
   - Print each score
   - Calculate and print the sum and average

2. **Iterate over a String array:**
   ```java
   String[] languages = {"Java", "Python", "TypeScript", "Flutter", "C++"};
   ```
   - Print each language
   - Print each language with its length: `"Java (4 characters)"`
   - Find and print the longest language name

3. **Iterate over characters in a String** using `toCharArray()`:
   ```java
   String message = "Hello, World!";
   for (char c : message.toCharArray()) {
       // process each character
   }
   ```
   - Count the number of vowels in the string
   - Count the number of uppercase and lowercase letters

4. **Limitation demonstration:** Show that you CANNOT modify array elements with an enhanced for loop:
   ```java
   int[] numbers = {1, 2, 3, 4, 5};
   for (int n : numbers) {
       n = n * 2;  // Does this change the array?
   }
   // Print the array — it's unchanged!
   ```
   Then show how to do it with a standard for loop. Add a comment explaining why.

---

## Part 4: Loop Patterns

### Program D: `LoopPatterns.java`

Write a program that uses for loops to generate text-based patterns. These exercises build strong loop-control skills.

1. **Right triangle:**
   ```
   *
   **
   ***
   ****
   *****
   ```

2. **Inverted triangle:**
   ```
   *****
   ****
   ***
   **
   *
   ```

3. **Number triangle:**
   ```
   1
   12
   123
   1234
   12345
   ```

4. **Multiplication table (nested loops):** Print a 10x10 multiplication table:
   ```
        1    2    3    4    5    6    7    8    9   10
    ─────────────────────────────────────────────────
   1|   1    2    3    4    5    6    7    8    9   10
   2|   2    4    6    8   10   12   14   16   18   20
   3|   3    6    9   12   15   18   21   24   27   30
   ...
   ```
   Use `printf` with width specifiers for alignment.

5. **Diamond (challenge):**
   ```
       *
      ***
     *****
    *******
   *********
    *******
     *****
      ***
       *
   ```
   Use a variable for the size so the diamond can be made larger or smaller.

---

## Part 5: Practical Application

### Program E: `ForLoopApplications.java`

Write a program with several practical uses of for loops:

1. **Factorial calculator:** Calculate `n!` for a user-provided number. Example: `5! = 120`

2. **Fibonacci sequence:** Print the first 20 Fibonacci numbers:
   ```
   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
   ```

3. **Prime number checker:** Ask for a number and determine if it's prime by checking divisibility from 2 to the square root of the number using `Math.sqrt()`.

4. **FizzBuzz:** Print numbers 1 to 50. For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for multiples of both print "FizzBuzz":
   ```
   1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, ...
   ```

5. **Simple bar chart:** Given an array of values, print a horizontal bar chart:
   ```java
   int[] data = {3, 7, 2, 9, 5};
   String[] labels = {"Mon", "Tue", "Wed", "Thu", "Fri"};
   ```
   Output:
   ```
   Mon | ***
   Tue | *******
   Wed | **
   Thu | *********
   Fri | *****
   ```

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What are the three parts of a for loop header, and in what order do they execute?
2. When would you choose an enhanced for loop over a standard for loop? When can you NOT use the enhanced version?
3. What is an "off-by-one" error, and how do you avoid it?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_For_Loop_in_Practice.md` containing:

1. Your predictions vs. actual results from Part 2
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `ForLoopBasics.java`: All 6 counting patterns correct | 10 |
| `ForLoopTracing.java`: All tricky loops with predictions and explanations | 15 |
| `EnhancedForLoop.java`: All 4 demonstrations including limitation | 15 |
| `LoopPatterns.java`: All 5 patterns rendered correctly | 20 |
| `ForLoopApplications.java`: All 5 practical applications working | 25 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

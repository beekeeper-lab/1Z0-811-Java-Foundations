# Day 21 Assignment: Exception Handling in Practice

## Overview

- **Topic:** Debugging and Exception Handling — try, catch, finally, and Common Exceptions
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### try-catch syntax

```java
try {
    // Code that might throw an exception
    int result = 10 / 0;
} catch (ArithmeticException e) {
    // Code that runs if the exception occurs
    System.out.println("Error: " + e.getMessage());
}
// Execution continues here after the catch
```

### Multiple catch blocks

```java
try {
    // risky code
} catch (ArithmeticException e) {
    System.out.println("Math error: " + e.getMessage());
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Array error: " + e.getMessage());
} catch (Exception e) {
    System.out.println("Some other error: " + e.getMessage());
}
```

**Order matters:** Catch more specific exceptions FIRST. The general `Exception` catch must be last — the compiler enforces this.

### finally block

```java
try {
    // risky code
} catch (Exception e) {
    // handle error
} finally {
    // ALWAYS runs — whether or not an exception occurred
    // Used for cleanup (closing files, releasing resources)
}
```

### Common exam exceptions

| Exception | Cause |
|-----------|-------|
| `ArithmeticException` | Division by zero (integers only) |
| `NullPointerException` | Calling a method on `null` |
| `ArrayIndexOutOfBoundsException` | Accessing an invalid array index |
| `StringIndexOutOfBoundsException` | Invalid `charAt()` or `substring()` index |
| `NumberFormatException` | `Integer.parseInt("abc")` |
| `ClassCastException` | Invalid type cast on objects |

---

## Part 1: Triggering and Catching Every Common Exception

### Program A: `ExceptionCatalog.java`

Write a program that **intentionally triggers** each of the 6 common exceptions, catches them, and prints useful information. For each one:

1. Print a header: `"=== ArithmeticException ==="`
2. Write the triggering code inside a try block
3. Catch the specific exception type
4. Print:
   - The exception class name: `e.getClass().getSimpleName()`
   - The message: `e.getMessage()`
   - A plain-English explanation of what went wrong
5. Continue to the next exception

Structure:
```
=== ArithmeticException ===
Trigger: 10 / 0
Exception: ArithmeticException
Message: / by zero
Explanation: Cannot divide an integer by zero.

=== NullPointerException ===
Trigger: null.length()
Exception: NullPointerException
Message: ...
Explanation: Tried to call a method on a null reference.

...and so on for all 6...
```

After all 6, print: `"Program completed — all exceptions were handled!"` to prove the program didn't crash.

---

## Part 2: try-catch Flow of Execution

### Program B: `FlowOfExecution.java`

Understanding what runs and what gets skipped is critical for the exam. For each scenario, **predict the output** before running:

1. **Exception in try — catch handles it:**
   ```java
   System.out.println("Before try");
   try {
       System.out.println("In try — before error");
       int x = 10 / 0;
       System.out.println("In try — after error");  // Does this print?
   } catch (ArithmeticException e) {
       System.out.println("In catch");
   }
   System.out.println("After try-catch");
   ```

2. **No exception — catch is skipped:**
   ```java
   try {
       System.out.println("In try — no error here");
       int x = 10 / 2;
       System.out.println("Result: " + x);
   } catch (ArithmeticException e) {
       System.out.println("In catch");  // Does this print?
   }
   System.out.println("After try-catch");
   ```

3. **finally always runs — with exception:**
   ```java
   try {
       System.out.println("In try");
       int[] arr = new int[3];
       arr[5] = 10;
       System.out.println("After error");
   } catch (ArrayIndexOutOfBoundsException e) {
       System.out.println("In catch");
   } finally {
       System.out.println("In finally");  // Always prints
   }
   System.out.println("After everything");
   ```

4. **finally always runs — without exception:**
   ```java
   try {
       System.out.println("In try — no error");
   } catch (Exception e) {
       System.out.println("In catch");
   } finally {
       System.out.println("In finally");
   }
   ```

5. **Wrong exception type — not caught:**
   ```java
   try {
       int[] arr = new int[3];
       arr[5] = 10;  // ArrayIndexOutOfBoundsException
   } catch (ArithmeticException e) {  // Wrong type!
       System.out.println("Caught it");
   }
   System.out.println("After try-catch");  // Does this print?
   ```
   Wrap this entire block in ANOTHER try-catch to prevent the program from crashing.

6. **Multiple catch blocks — which one runs?**
   ```java
   try {
       String s = null;
       s.length();
   } catch (ArithmeticException e) {
       System.out.println("ArithmeticException");
   } catch (NullPointerException e) {
       System.out.println("NullPointerException");
   } catch (Exception e) {
       System.out.println("Generic Exception");
   }
   ```

For each scenario, write your prediction as a comment BEFORE the code.

---

## Part 3: Multiple Catch Blocks

### Program C: `MultiCatchDemo.java`

Write a program that demonstrates handling different exceptions differently:

1. **Calculator with error handling:** Use Scanner to read two numbers and an operator. Handle each possible error:
   ```java
   try {
       System.out.print("Enter first number: ");
       int a = Integer.parseInt(scanner.nextLine());  // Could throw NumberFormatException

       System.out.print("Enter operator (+,-,*,/): ");
       String op = scanner.nextLine();

       System.out.print("Enter second number: ");
       int b = Integer.parseInt(scanner.nextLine());  // Could throw NumberFormatException

       int result;
       switch (op) {
           case "/":
               result = a / b;  // Could throw ArithmeticException
               break;
           // ... other cases
       }
       System.out.println("Result: " + result);
   } catch (NumberFormatException e) {
       System.out.println("Error: Please enter valid numbers.");
   } catch (ArithmeticException e) {
       System.out.println("Error: Cannot divide by zero.");
   }
   ```

2. **Array processor with multiple risks:** Write code that:
   - Reads an index from the user
   - Accesses an array at that index
   - Converts the element to a String and parses it
   Handle `ArrayIndexOutOfBoundsException`, `NumberFormatException`, and `NullPointerException` separately with helpful messages.

3. **Catch ordering test:** Try putting `catch (Exception e)` BEFORE a more specific catch. What does the compiler say? Comment out the broken version and add a comment explaining the rule.

---

## Part 4: Practical Application

### Program D: `RobustInputReader.java`

Write a utility program that demonstrates how exception handling makes programs **robust** — they handle bad input gracefully instead of crashing.

Build methods that safely read different types of input:

1. **`readInt(Scanner, String prompt)`:** Keep asking until the user enters a valid integer:
   ```
   Enter your age: abc
   Invalid — please enter a whole number.
   Enter your age: 12.5
   Invalid — please enter a whole number.
   Enter your age: 25
   ```
   Use a while loop with try-catch inside.

2. **`readDouble(Scanner, String prompt)`:** Same pattern for doubles.

3. **`readIntInRange(Scanner, String prompt, int min, int max)`:** Read an integer that must be within a range:
   ```
   Enter month (1-12): 0
   Must be between 1 and 12.
   Enter month (1-12): abc
   Invalid — please enter a whole number.
   Enter month (1-12): 7
   ```

4. **Use these methods** to build a profile builder that collects:
   - Name (String — no parsing needed, but validate not empty)
   - Age (int, between 1 and 120)
   - GPA (double, between 0.0 and 4.0)
   - Graduation year (int, between 2020 and 2035)

   Print a formatted profile at the end. The program should be **impossible to crash** with bad input.

---

## Part 5: Debugging and Exception Handling Capstone

### Program E: `SafeGradebook.java`

Build a gradebook application that combines debugging skills from Day 20 with exception handling from Day 21. The program should be completely crash-proof.

Requirements:

1. **Student data entry with full validation:**
   - Number of students (int, 1-30) — handle non-numeric input
   - For each student: name and 3 exam scores (0-100)
   - Handle every possible bad input with try-catch and loops

2. **Calculations with error prevention:**
   - Calculate each student's average
   - Calculate the class average
   - Find the highest and lowest averages
   - Handle edge cases (what if all scores are 0? what if there's only 1 student?)

3. **Report generation with formatted output:**
   ```
   ╔════════════════════════════════════════════════════════╗
   ║                   CLASS GRADEBOOK                     ║
   ╠════════════════════════════════════════════════════════╣
   ║  Student         Exam1  Exam2  Exam3   Avg   Grade   ║
   ║  ────────────────────────────────────────────────────  ║
   ║  Alice             88     92     85   88.3   B       ║
   ║  Bob               95     91     97   94.3   A       ║
   ║  Charlie           72     68     75   71.7   C       ║
   ╠════════════════════════════════════════════════════════╣
   ║  Class Average: 84.8                                  ║
   ║  Highest: Bob (94.3)                                  ║
   ║  Lowest: Charlie (71.7)                               ║
   ╚════════════════════════════════════════════════════════╝
   ```

4. **Use these specific constructs:**
   - `try-catch` with `NumberFormatException` for all numeric input
   - `try-catch` with `ArrayIndexOutOfBoundsException` as a safety net
   - `finally` block for printing a footer message ("Report generated successfully" or "Report generated with errors")
   - Multiple catch blocks in at least one location
   - Input validation loops (do-while with try-catch inside)

5. **Intentionally handle these edge cases:**
   - User enters "abc" for a score → re-prompt
   - User enters -5 for a score → re-prompt (not an exception, but a validation check)
   - User enters 150 for a score → re-prompt
   - Empty string for a name → re-prompt

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between **preventing** an error (e.g., checking `if (x != 0)` before dividing) and **handling** an error (e.g., catching `ArithmeticException`)? When should you use each approach?
2. Why must more specific catch blocks come before more general ones?
3. When does the `finally` block run? Can you think of a situation where `finally` is essential?
4. Looking at Days 20 and 21 together — how does exception handling change the way you think about writing code?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Exception_Handling_in_Practice.md` containing:

1. Your flow-of-execution predictions from Part 2
2. Your catch ordering findings from Part 3
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `ExceptionCatalog.java`: All 6 exceptions triggered, caught, and explained | 15 |
| `FlowOfExecution.java`: All 6 scenarios with correct predictions | 15 |
| `MultiCatchDemo.java`: Calculator, array processor, and ordering test | 15 |
| `RobustInputReader.java`: All 3 methods plus crash-proof profile builder | 20 |
| `SafeGradebook.java`: Full capstone — crash-proof with formatted output | 20 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

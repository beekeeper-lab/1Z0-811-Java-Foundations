# Day 20 Assignment: Identifying and Fixing Errors in Practice

## Overview

- **Topic:** Debugging and Exception Handling — Finding Syntax Errors, Logic Errors, and Runtime Errors
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Three types of errors

| Type | When Detected | Example |
|------|--------------|---------|
| **Syntax error** | Compile time — `javac` refuses to compile | Missing semicolon, mismatched braces |
| **Runtime error** | During execution — program crashes | Division by zero, ArrayIndexOutOfBoundsException |
| **Logic error** | Never detected automatically — wrong output | Using `>` instead of `>=`, off-by-one errors |

### Reading a stack trace

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
    at MyProgram.processData(MyProgram.java:15)
    at MyProgram.main(MyProgram.java:8)
```

Read from bottom to top:
1. `main` called `processData` (line 8)
2. `processData` crashed at line 15
3. The exception is `ArrayIndexOutOfBoundsException` — you tried to access index 5 in a 5-element array (valid indices are 0-4)

---

## Part 1: Syntax Error Hunt

### Program A: `SyntaxErrors.java`

The following program has **10 syntax errors**. Find and fix every one. **Do not change what the program is supposed to do** — only fix the syntax.

```java
public class SyntaxErrors {
    public static void main(String[] args) {
        // Calculate and display student information
        String name = "Campbell"
        int age = 20;
        double gpa = 3.75

        System.out.println("Student: " + Name);
        System.out.println("Age: " + age)
        System.out.println("GPA: " + gpa);

        if (gpa >= 3.5) {
            System.out.println("Honor roll!");
        else {
            System.out.println("Keep working hard!");
        }

        for (int i = 0; i <= 3, i++) {
            System.out.println("Semester " + (i + 1));
        }

        int[] scores = {88, 92, 76, 95};
        int total = 0;
        for (int score ; scores) {
            total += score
        }
        double average = total / scores.length();
        System.out.println("Average: " + average);
    }
}
```

### Deliverable

Save the fixed version as `SyntaxErrorsFixed.java`. In your response file, list every error you found with:
- Line number
- What was wrong
- How you fixed it

---

## Part 2: Logic Error Hunt

### Program B: `LogicErrors.java`

The following program **compiles and runs without crashing**, but it produces **wrong results**. There are **7 logic errors**. Find and fix every one.

```java
public class LogicErrors {
    public static void main(String[] args) {
        // 1. Calculate average of three numbers
        int a = 80, b = 90, c = 85;
        double average = a + b + c / 3;
        System.out.println("Average of 80, 90, 85: " + average);
        // Expected: 85.0

        // 2. Check if a number is between 10 and 20 (inclusive)
        int number = 15;
        if (number > 10 && number > 20) {
            System.out.println(number + " is between 10 and 20");
        } else {
            System.out.println(number + " is NOT between 10 and 20");
        }
        // Expected: "15 is between 10 and 20"

        // 3. Count down from 5 to 1
        System.out.print("Countdown: ");
        for (int i = 5; i >= 1; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        // Expected: "Countdown: 5 4 3 2 1"
        // WARNING: This one will run forever — comment it out after identifying the bug

        // 4. Find the maximum value
        int[] values = {34, 67, 23, 89, 12, 56};
        int max = values[0];
        for (int i = 0; i < values.length; i++) {
            if (values[i] < max) {
                max = values[i];
            }
        }
        System.out.println("Maximum: " + max);
        // Expected: 89

        // 5. Calculate factorial of 5 (5! = 120)
        int n = 5;
        int factorial = 0;
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        System.out.println("5! = " + factorial);
        // Expected: 120

        // 6. Determine if a year is a leap year
        int year = 2024;
        boolean isLeapYear = (year % 4 == 0) || (year % 100 != 0) && (year % 400 == 0);
        System.out.println(year + " is a leap year: " + isLeapYear);
        // Expected: true (2024 IS a leap year)
        // Test also with 1900 (should be false) and 2000 (should be true)

        // 7. Build a greeting string
        String firstName = "Campbell";
        String lastName = "Reed";
        String greeting = "Hello, " + firstName + ". " + lastName + "!";
        System.out.println(greeting);
        // Expected: "Hello, Campbell Reed!"
    }
}
```

### Deliverable

Save the fixed version as `LogicErrorsFixed.java`. In your response file, for each error explain:
- What the code was doing wrong
- What the correct logic should be
- How you identified the bug (did you trace it mentally, use print statements, or test with known values?)

---

## Part 3: Runtime Error Hunt

### Program C: `RuntimeErrors.java`

The following program compiles successfully but **crashes at runtime**. There are **5 runtime errors** at different points. Find each one, explain why it crashes, and fix it.

**Strategy:** Run the program. It will crash at the first error. Fix that one, run again, and find the next. Record the stack trace for each crash.

```java
import java.util.Scanner;

public class RuntimeErrors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Error 1: Array access
        int[] numbers = {10, 20, 30, 40, 50};
        for (int i = 0; i <= numbers.length; i++) {
            System.out.println("Element " + i + ": " + numbers[i]);
        }

        // Error 2: Division
        int total = 100;
        int count = 0;
        int avg = total / count;
        System.out.println("Average: " + avg);

        // Error 3: String operations
        String text = null;
        System.out.println("Length: " + text.length());

        // Error 4: Number parsing
        String input = "twelve";
        int parsed = Integer.parseInt(input);
        System.out.println("Parsed: " + parsed);

        // Error 5: Stack overflow (recursive)
        System.out.println("Result: " + badMethod(5));

        scanner.close();
    }

    public static int badMethod(int n) {
        return n + badMethod(n - 1);  // No base case!
    }
}
```

### Deliverable

Save the fixed version as `RuntimeErrorsFixed.java`. In your response file, for each error record:
- The exception type (e.g., `ArrayIndexOutOfBoundsException`)
- The stack trace (first 2-3 lines)
- Why the error occurred
- How you fixed it

---

## Part 4: Debugging with Print Statements

### Program D: `DebugWithPrints.java`

The following program is supposed to find all prime numbers between 1 and 50, but it's producing wrong results. **Do not just look at it and fix it** — use the debugging process:

1. Run the program and observe the incorrect output
2. Add `System.out.println()` debugging statements at key points to trace execution
3. Identify the bug(s) by reading the trace output
4. Fix the bug(s)
5. Remove the debug print statements (or comment them out)

```java
public class DebugWithPrints {
    public static void main(String[] args) {
        System.out.println("Prime numbers between 1 and 50:");
        for (int num = 1; num <= 50; num++) {
            boolean isPrime = true;
            for (int i = 2; i < num; i++) {
                if (num % i == 0) {
                    isPrime = true;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(num + " ");
            }
        }
        System.out.println();
        // Expected: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
    }
}
```

### Deliverable

Save THREE versions:
- `DebugWithPrintsOriginal.java` — the broken version
- `DebugWithPrintsTrace.java` — the version with your debug print statements (showing your debugging process)
- `DebugWithPrintsFixed.java` — the corrected version

In your response file, describe the step-by-step debugging process you followed.

---

## Part 5: Mixed Error Challenge

### Program E: `MixedErrors.java`

The following program has **3 syntax errors, 3 logic errors, and 2 runtime errors** (8 total). Fix them all. Classify each error by type.

```java
import java.util.Scanner

public class MixedErrors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Build a simple gradebook
        String[] names = {"Alice", "Bob", "Charlie", "Diana"};
        int[] grades = {88, 95, 72, 91, 85};  // Mismatched length — runtime risk

        // Print all students and grades
        for (int i = 0; i < grades.length; i++) {
            System.out.printf("%-10s: %d%n" names[i], grades[i]);
        }

        // Calculate class average
        int sum = 0;
        for (int i = 1; i <= grades.length; i++) {
            sum += grades[i];
        }
        double classAverage = sum / grades.length;
        System.out.println("Class average: " + classAverage);
        // Expected: should be a decimal, not integer division

        // Find students above average
        int aboveAverage = 0;
        for (int i = 0; i < names.length; i++) {
            if (grades[i] > classAverage); {
                aboveAverage++;
                System.out.println(names[i] + " is above average");
            }
        }
        System.out.println(aboveAverage + " students above average");

        // Determine highest grade
        int highest = 0;
        for (int grade : grades) {
            if (grade < highest) {
                highest = grade;
            }
        }
        System.out.println("Highest grade: " + highest)

        scanner.close();
    }
}
```

### Deliverable

Save the fixed version as `MixedErrorsFixed.java`. In your response file, list each error with:
- Error number (1-8)
- Error type (syntax, logic, or runtime)
- Description of the error
- How you fixed it

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Which type of error is easiest to find — syntax, logic, or runtime? Which is hardest? Why?
2. How do you read a Java stack trace? What should you look at first?
3. Describe your debugging process — what steps do you follow when a program doesn't work as expected?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Errors_and_Debugging_in_Practice.md` containing:

1. Your error lists with classifications for Parts 1, 2, 3, and 5
2. Your debugging process description from Part 4
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `SyntaxErrorsFixed.java`: All 10 syntax errors found and fixed | 15 |
| `LogicErrorsFixed.java`: All 7 logic errors found, fixed, and explained | 20 |
| `RuntimeErrorsFixed.java`: All 5 runtime errors with stack traces and fixes | 15 |
| `DebugWithPrints`: Debugging process shown with trace, 3 versions saved | 15 |
| `MixedErrorsFixed.java`: All 8 errors classified and fixed | 20 |
| Reflection questions answered accurately | 5 |
| All fixed programs compile and run without errors | 10 |
| **Total** | **100** |

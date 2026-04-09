# Module 20: Debugging and Exceptions Part 1

> 🏷️ When You're Ready

> 🎯 **Teach:** How to identify, classify, and fix syntax errors, logic errors, and runtime errors using systematic debugging strategies
> **See:** Programs with intentional bugs that you must find and fix, stack traces that you must read, and a step-by-step debugging process using print statements
> **Feel:** Unafraid of error messages, viewing them as helpful clues rather than obstacles, and equipped with a reliable process for tracking down bugs

> 🎙️ Today is different from every day before it. Instead of writing new programs from scratch, you will fix broken ones. Every programmer spends a huge amount of time debugging, so learning to read error messages, trace through logic, and systematically find bugs is just as important as writing code in the first place. You will work with syntax errors the compiler catches, logic errors that produce wrong answers, and runtime errors that crash your program.

> 🎙️ Every programmer, no matter how experienced, writes bugs. The difference between a beginner and a professional is not that the professional writes perfect code -- it is that the professional knows how to find and fix problems quickly. That is what today is all about.

## Research: Syntax Errors, Logic Errors, and Debugging

> 🎯 **Teach:** How to distinguish syntax errors, logic errors, and runtime errors, and what debugging strategies work best for each type.
> **See:** A research assignment covering error classification, stack trace reading, and at least four debugging techniques.
> **Feel:** Prepared to approach bugs systematically rather than guessing.

### Overview

- **Topic:** Debugging and Exception Handling — Identifying Syntax and Logic Errors
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is the difference between a syntax error and a logic error?** Define each type, explain when each is detected (compile-time vs. runtime vs. wrong output), and give an example of each. Which type is harder to find and fix? Why?

2. **What is a runtime error?** How does it differ from a syntax error and a logic error? Explain what happens when a Java program encounters a runtime error — what does the JVM do? What is a stack trace, and how do you read one?

3. **What are common debugging strategies?** Describe at least four techniques a programmer can use to find and fix bugs:
   - Reading compiler error messages carefully
   - Using print statements to trace execution
   - Rubber duck debugging (explaining code out loud)
   - Testing with edge cases and boundary values
   - Using a debugger tool

   Which techniques work best for syntax errors vs. logic errors?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Errors_and_Debugging_Research.md` in this folder.

### Grading Criteria

| Criteria | Points |
|----------|--------|
| Clearly defines syntax vs. logic errors with examples | 30 |
| Explains runtime errors, JVM behavior, and stack traces | 30 |
| Describes at least 4 debugging strategies with applicability | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

> 🎙️ Here is a helpful way to think about the three error types. Syntax errors are like spelling mistakes in an essay -- the teacher catches them before grading. Runtime errors are like a car breaking down during a road trip -- everything seemed fine until it was not. Logic errors are like driving to the wrong city -- the car runs perfectly but you end up in the wrong place.

> 💡 **Remember this one thing:** Syntax errors are caught by the compiler and are the easiest to fix. Logic errors produce wrong output but no error message, making them the hardest to find. Runtime errors crash the program and produce a stack trace that tells you exactly where the crash happened.

## Hands-On: Identifying and Fixing Errors in Practice

> 🎯 **Teach:** How to find and fix syntax errors, logic errors, and runtime errors in broken programs using systematic debugging.
> **See:** Ten syntax errors, seven logic errors, five runtime errors, a print-statement debugging exercise, and a mixed-error challenge.
> **Feel:** Unafraid of error messages, viewing them as helpful clues that guide you straight to the fix.

> 🎙️ Now you become a detective. You will hunt down ten syntax errors, seven logic errors, five runtime errors, and eight mixed errors across several broken programs. You will also practice the debugging process by adding print statements to trace through a buggy prime number finder.

### Overview

- **Topic:** Debugging and Exception Handling — Finding Syntax Errors, Logic Errors, and Runtime Errors
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

#### Three types of errors

| Type | When Detected | Example |
|------|--------------|---------|
| **Syntax error** | Compile time — `javac` refuses to compile | Missing semicolon, mismatched braces |
| **Runtime error** | During execution — program crashes | Division by zero, ArrayIndexOutOfBoundsException |
| **Logic error** | Never detected automatically — wrong output | Using `>` instead of `>=`, off-by-one errors |

#### Reading a stack trace

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
    at MyProgram.processData(MyProgram.java:15)
    at MyProgram.main(MyProgram.java:8)
```

Read from bottom to top:
1. `main` called `processData` (line 8)
2. `processData` crashed at line 15
3. The exception is `ArrayIndexOutOfBoundsException` — you tried to access index 5 in a 5-element array (valid indices are 0-4)

> 🎙️ Reading stack traces from bottom to top is a skill that will save you hours of frustration. The bottom line tells you where the chain started, and each line above shows the next method call until you reach the line that actually crashed. Once you get comfortable reading these, error messages become helpful friends instead of scary walls of text.

---

### Part 1: Syntax Error Hunt

#### Program A: `SyntaxErrors.java`

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

#### Deliverable

Save the fixed version as `SyntaxErrorsFixed.java`. In your response file, list every error you found with:
- Line number
- What was wrong
- How you fixed it

> 🎙️ Syntax errors are the easiest to fix because the compiler tells you exactly what is wrong and where. Look at the line number in the error message, read the description, and the fix is usually obvious -- a missing semicolon, a mismatched brace, or a typo in a variable name.

---

### Part 2: Logic Error Hunt

#### Program B: `LogicErrors.java`

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

#### Deliverable

Save the fixed version as `LogicErrorsFixed.java`. In your response file, for each error explain:
- What the code was doing wrong
- What the correct logic should be
- How you identified the bug (did you trace it mentally, use print statements, or test with known values?)

> 🎙️ Logic errors are the hardest because the program runs without crashing -- it just gives you the wrong answer. The factorial bug is a perfect example. Setting the initial value to zero instead of one means every multiplication produces zero. The program runs fine, but five factorial comes out as zero instead of 120. You have to reason about what the code is actually doing versus what you intended.

---

### Part 3: Runtime Error Hunt

#### Program C: `RuntimeErrors.java`

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

#### Deliverable

Save the fixed version as `RuntimeErrorsFixed.java`. In your response file, for each error record:
- The exception type (e.g., `ArrayIndexOutOfBoundsException`)
- The stack trace (first 2-3 lines)
- Why the error occurred
- How you fixed it

> 🎙️ Runtime errors give you a stack trace, which is actually a gift -- it tells you exactly what went wrong and where. The strategy here is simple: run the program, read the stack trace, fix the first crash, and run again. Each fix reveals the next error. Work through them one at a time.

---

### Part 4: Debugging with Print Statements

#### Program D: `DebugWithPrints.java`

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

#### Deliverable

Save THREE versions:
- `DebugWithPrintsOriginal.java` — the broken version
- `DebugWithPrintsTrace.java` — the version with your debug print statements (showing your debugging process)
- `DebugWithPrintsFixed.java` — the corrected version

In your response file, describe the step-by-step debugging process you followed.

> 🎙️ Resist the urge to just eyeball the bug and fix it. The point of this exercise is to practice the debugging process -- add print statements, observe the trace, and let the evidence guide you to the fix. This process works on programs that are a thousand lines long where you cannot just read through the whole thing.

---

### Part 5: Mixed Error Challenge

#### Program E: `MixedErrors.java`

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

#### Deliverable

Save the fixed version as `MixedErrorsFixed.java`. In your response file, list each error with:
- Error number (1-8)
- Error type (syntax, logic, or runtime)
- Description of the error
- How you fixed it

> 🎙️ The mixed error challenge is the closest thing to real-world debugging. In practice, bugs do not come neatly labeled as syntax, logic, or runtime. You have to figure out which type you are dealing with and then apply the right strategy. Start by trying to compile -- if it fails, you have syntax errors. If it compiles but crashes, you have runtime errors. If it runs but gives wrong answers, you have logic errors.

---

### Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Which type of error is easiest to find — syntax, logic, or runtime? Which is hardest? Why?
2. How do you read a Java stack trace? What should you look at first?
3. Describe your debugging process — what steps do you follow when a program doesn't work as expected?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Errors_and_Debugging_in_Practice.md` containing:

1. Your error lists with classifications for Parts 1, 2, 3, and 5
2. Your debugging process description from Part 4
3. Your answers to the reflection questions

> 💡 **Remember this one thing:** Read stack traces from bottom to top. The bottom shows where your code started, and each line above shows the chain of method calls that led to the crash. The top line tells you the exception type and the exact line number where it happened.

> 🎙️ Today was different from every other day in this course, and that was intentional. Debugging is a skill that you develop separately from coding, and it is just as important. From here on out, when your programs do not work, you have a systematic process to follow instead of staring at the screen hoping the answer appears. Next up, you will learn about exception handling, which lets you write code that anticipates and gracefully handles errors instead of crashing.

## Grading

> 🎯 **Teach:** How your research and hands-on work will be evaluated for the debugging and error identification module.
> **See:** Rubrics for the research essay and the five hands-on error-hunting programs.
> **Feel:** Clear on grading expectations so you can double-check each deliverable before submitting.

> 🔄 **Where this fits:** Day 20 shifts from writing code to fixing code, building the debugging skills you will need for every remaining project in this course and for the error-identification questions on the 1Z0-811 exam.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly defines syntax vs. logic errors with examples | 30 |
| Explains runtime errors, JVM behavior, and stack traces | 30 |
| Describes at least 4 debugging strategies with applicability | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

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

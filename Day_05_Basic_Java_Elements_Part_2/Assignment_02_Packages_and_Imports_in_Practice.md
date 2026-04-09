# Day 5 Assignment: Packages and Imports in Practice

## Overview

- **Topic:** Basic Java Elements — Using Packages, Import Statements, and java.lang Classes
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

So far, all of your programs have lived in the "default" package — just `.java` files in a directory with no `package` statement. In real Java projects, code is organized into packages, which map to folder structures on disk.

### How Packages Work

```
myproject/
  com/
    example/
      utils/
        MathHelper.java    ← package com.example.utils;
      app/
        Main.java          ← package com.example.app;
```

The first line of `MathHelper.java` would be:
```java
package com.example.utils;
```

And `Main.java` would import it with:
```java
package com.example.app;
import com.example.utils.MathHelper;
```

### Compiling and Running with Packages

From the `myproject/` root directory:
```
javac com/example/utils/MathHelper.java
javac com/example/app/Main.java
java com.example.app.Main
```

> Notice: you compile with file paths (using `/`) but run with package names (using `.`).

---

## Part 1: Exploring java.lang

The `java.lang` package is automatically imported into every Java program. You've already been using classes from it without knowing it.

### Program A: `LangExplorer.java`

Write a program that demonstrates **at least 5 classes from `java.lang`** by using methods from each one. For each class, use a comment to label it.

Use the following classes:

1. **`String`** — Use at least 2 String methods (e.g., `length()`, `toUpperCase()`, `charAt()`)
2. **`Integer`** — Use `Integer.parseInt()` to convert a String to an int, and `Integer.MAX_VALUE` to print the largest possible int
3. **`Double`** — Use `Double.parseDouble()` to convert a String to a double
4. **`Math`** — Use at least 2 Math methods (e.g., `Math.abs()`, `Math.max()`, `Math.sqrt()`)
5. **`System`** — You already use `System.out.println()`. Also use `System.currentTimeMillis()` to print the current time in milliseconds

Example output format:
```
=== String ===
"Hello World" has 11 characters
Uppercase: HELLO WORLD

=== Integer ===
Parsed "42" to integer: 42
Max integer value: 2147483647

...and so on for each class...
```

---

## Part 2: Using Imports

### Program B: `ScannerDemo.java`

The `Scanner` class lives in `java.util` — it is NOT auto-imported. Write a program that:

1. Imports `java.util.Scanner`
2. Asks the user for their name, age, and favorite number
3. Prints a summary of their input
4. Uses `scanner.close()` when done

Example interaction:
```
What is your name? Campbell
How old are you? 20
What is your favorite number? 7
Hello, Campbell! You are 20 years old and your favorite number is 7.
```

> **Hint:** Use `scanner.nextLine()` for strings, `scanner.nextInt()` for integers.
> **Watch out:** Mixing `nextInt()` and `nextLine()` can cause issues. Call `scanner.nextLine()` after `nextInt()` to consume the leftover newline.

### Program C: `DateTimeInfo.java`

Write a program that imports and uses classes from `java.time` to display:

1. Today's date (use `java.time.LocalDate`)
2. The current time (use `java.time.LocalTime`)
3. The current date and time combined (use `java.time.LocalDateTime`)
4. What day of the week it is
5. What month it is

You can use individual imports or a wildcard import — try both and note the difference in your response file.

---

## Part 3: Creating Your Own Packages

### Setting Up a Package Structure

For this exercise, you will create a small multi-file project with packages. Work inside a new directory called `packagedemo` within this Day_05 folder.

Create the following folder and file structure:

```
packagedemo/
  com/
    internship/
      models/
        Employee.java
      app/
        EmployeeApp.java
```

### `Employee.java`

```java
package com.internship.models;
```

This class should have:
- Fields: `String name`, `String department`, `double salary`
- A method `displayInfo()` that prints all the employee's information
- A method `calculateBonus()` that returns 10% of the salary and prints the bonus amount

### `EmployeeApp.java`

```java
package com.internship.app;
import com.internship.models.Employee;
```

This class should have a `main` method that:
1. Creates at least 2 `Employee` objects with different data
2. Calls `displayInfo()` and `calculateBonus()` on each

### Compiling and Running

From the `packagedemo/` directory, compile and run using:
```
javac com/internship/models/Employee.java
javac com/internship/app/EmployeeApp.java
java com.internship.app.EmployeeApp
```

### Deliverable

Save all files in the package structure described above. Record the exact compile and run commands you used in your response file.

---

## Part 4: Import Detective

### Program D: `ImportDetective.java`

The following program is missing its import statements. Figure out which imports are needed, add them, and get the program to compile and run.

```java
// TODO: Add the correct import statements here

public class ImportDetective {
    public static void main(String[] args) {
        // Uses ArrayList from java.util
        ArrayList<String> colors = new ArrayList<>();
        colors.add("Red");
        colors.add("Green");
        colors.add("Blue");
        System.out.println("Colors: " + colors);

        // Uses Random from java.util
        Random random = new Random();
        int randomNumber = random.nextInt(100);
        System.out.println("Random number: " + randomNumber);

        // Uses LocalDate from java.time
        LocalDate today = LocalDate.now();
        System.out.println("Today's date: " + today);

        // Uses DecimalFormat from java.text
        DecimalFormat formatter = new DecimalFormat("#,###.00");
        double bigNumber = 1234567.891;
        System.out.println("Formatted: " + formatter.format(bigNumber));
    }
}
```

### Deliverable

Save the working version as `ImportDetective.java`. In your response file, list every import you added and which package each class comes from.

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What happens if you try to use `Scanner` without importing it? What error do you get?
2. What is the difference between `import java.util.Scanner;` and `import java.util.*;`? When might you prefer one over the other?
3. Why do you think Java auto-imports `java.lang` but not `java.util`?
4. When compiling a class in a package, why do you compile using the file path (`com/internship/models/Employee.java`) but run using the package name (`com.internship.app.EmployeeApp`)?

---

## Submission

Save all `.java` files and the `packagedemo/` directory in this folder, along with a response file named `Response_02_Packages_and_Imports_in_Practice.md` containing:

1. The imports you added to `ImportDetective.java` with explanations
2. The compile/run commands for the package exercise
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `LangExplorer.java`: Demonstrates 5 java.lang classes correctly | 15 |
| `ScannerDemo.java`: Correctly imports and uses Scanner for user input | 15 |
| `DateTimeInfo.java`: Correctly imports and uses java.time classes | 15 |
| Package exercise: Correct structure, compiles and runs with packages | 20 |
| `ImportDetective.java`: All imports identified and program runs | 15 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

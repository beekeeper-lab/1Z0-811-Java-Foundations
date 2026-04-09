# Day 12 Assignment: String Formatting and Escape Sequences in Practice

## Overview

- **Topic:** Working with the String Class — printf, String.format(), and Escape Sequences
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### printf Format Specifiers

`System.out.printf()` uses format strings with specifiers that are replaced by values:

```java
String name = "Campbell";
int age = 20;
double gpa = 3.75;
System.out.printf("Name: %s, Age: %d, GPA: %.2f%n", name, age, gpa);
// Output: Name: Campbell, Age: 20, GPA: 3.75
```

| Specifier | Type | Example | Output |
|-----------|------|---------|--------|
| `%d` | Integer | `printf("%d", 42)` | `42` |
| `%f` | Float/Double | `printf("%f", 3.14)` | `3.140000` |
| `%.2f` | Float with precision | `printf("%.2f", 3.14159)` | `3.14` |
| `%s` | String | `printf("%s", "Hi")` | `Hi` |
| `%c` | Character | `printf("%c", 'A')` | `A` |
| `%b` | Boolean | `printf("%b", true)` | `true` |
| `%n` | Newline | `printf("line1%nline2")` | line1\nline2 |
| `%10d` | Right-aligned, width 10 | `printf("%10d", 42)` | `        42` |
| `%-10s` | Left-aligned, width 10 | `printf("%-10s!", "Hi")` | `Hi        !` |
| `%05d` | Zero-padded, width 5 | `printf("%05d", 42)` | `00042` |

### String.format()

Works exactly like `printf` but **returns a String** instead of printing:

```java
String formatted = String.format("Hello, %s!", name);
```

### Escape Sequences

| Sequence | Meaning |
|----------|---------|
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\"` | Literal double quote |
| `\'` | Literal single quote |

---

## Part 1: Format Specifier Basics

### Program A: `FormatSpecifiers.java`

Write a program that demonstrates every format specifier from the table above:

1. **Basic specifiers:** Print each type with its specifier:
   ```
   Integer (%d):    42
   Float (%f):      3.141593
   Precise (%.2f):  3.14
   String (%s):     Hello
   Char (%c):       A
   Boolean (%b):    true
   ```

2. **Width and alignment:** Print the same value with different widths:
   ```
   Right-aligned: [        42]
   Left-aligned:  [42        ]
   Zero-padded:   [0000000042]
   ```
   Use `[` and `]` to make the padding visible.

3. **Multiple values in one format string:**
   ```java
   System.out.printf("%-15s %3d %8.2f%n", "Alice", 95, 92.50);
   System.out.printf("%-15s %3d %8.2f%n", "Bob", 87, 88.75);
   System.out.printf("%-15s %3d %8.2f%n", "Campbell", 91, 95.25);
   ```

4. **printf vs. String.format():** Show the same output produced both ways and explain in a comment when you would use each.

---

## Part 2: Escape Sequences

### Program B: `EscapeSequences.java`

Write a program that demonstrates every common escape sequence:

1. **Newline (`\n`):** Print three lines using a single `println` statement:
   ```
   Line 1
   Line 2
   Line 3
   ```

2. **Tab (`\t`):** Print a simple table using tabs:
   ```
   Name		Age	City
   Alice		25	Seattle
   Bob		30	Portland
   Campbell	20	Denver
   ```

3. **Backslash (`\\`):** Print a Windows-style file path:
   ```
   C:\Users\Campbell\Documents\Java
   ```

4. **Double quote (`\"`):** Print a sentence with quoted words:
   ```
   She said "Hello, World!" to the class.
   ```

5. **Single quote (`\'`):** Print:
   ```
   It's a beautiful day.
   ```

6. **Combining escapes:** Print a formatted block that uses multiple escape sequences together:
   ```
   File: "report.txt"
   Path: C:\Users\Documents\
   Status:	Complete
   Notes:	Line 1
   	Line 2
   	Line 3
   ```

---

## Part 3: Formatted Tables

### Program C: `FormattedReport.java`

Write a program that prints a well-formatted product inventory report using `printf`. This is where formatting becomes genuinely useful.

Hardcode data for at least 6 products with:
- Product name (`String`)
- Quantity in stock (`int`)
- Price per unit (`double`)
- Total value (quantity * price, calculated)

Print a formatted table:
```
================================================================
                    INVENTORY REPORT
================================================================
Product              Qty    Price/Unit     Total Value
----------------------------------------------------------------
Laptop               15      $999.99      $14,999.85
Mouse                142       $24.99       $3,548.58
Keyboard              87       $49.99       $4,349.13
Monitor               23      $349.99       $8,049.77
USB Cable            350        $9.99       $3,496.50
Headphones            64       $79.99       $5,119.36
----------------------------------------------------------------
TOTAL                681                   $39,563.19
================================================================
```

Requirements:
- Use `printf` with width specifiers to align columns
- Left-align product names with `%-20s`
- Right-align numbers with `%6d` and `%12.2f`
- Calculate and print the totals at the bottom
- Use `String.format()` for at least one value (e.g., formatting the currency)

---

## Part 4: printf vs. Concatenation

### Program D: `FormatComparison.java`

Write a program that shows the same output produced three different ways, so Campbell can see when each approach is best:

**Scenario 1: Simple student record**
```
Name: Campbell Reed | Age: 20 | GPA: 3.75
```
- Version A: String concatenation with `+`
- Version B: `System.out.printf()`
- Version C: `String.format()` stored in a variable, then printed

**Scenario 2: A table row**
```
  42    Campbell         3.75    true
```
- Version A: Concatenation (show how awkward the spacing is)
- Version B: `printf` with width specifiers (show how clean it is)

**Scenario 3: Currency display**
```
$1,234.56
```
- Version A: Manual formatting with concatenation
- Version B: `printf` with `%,.2f`

Add comments explaining which approach is clearest and most maintainable for each scenario.

---

## Part 5: String Class Capstone

### Program E: `ReportCardGenerator.java`

Build a complete report card generator that combines String methods from Day 11 with formatting from Day 12. Use `Scanner` for input.

The program should:

1. **Collect student information:**
   - Full name (clean it with `trim()` and proper capitalization)
   - Student ID (validate it's exactly 8 characters using `length()`)
   - 5 course names and their grades (as doubles)

2. **Process the data using String methods:**
   - Capitalize the first letter of each word in the name
   - Ensure the student ID is uppercase
   - Determine letter grades from numeric grades

3. **Print a formatted report card using printf:**

```
╔══════════════════════════════════════════════╗
║              REPORT CARD                     ║
╠══════════════════════════════════════════════╣
║  Student: CAMPBELL REED                      ║
║  ID:      STU12345                           ║
╠══════════════════════════════════════════════╣
║  Course               Grade    Letter        ║
║  ──────────────────────────────────────      ║
║  Mathematics           92.50   A             ║
║  English               88.00   B             ║
║  Computer Science      95.75   A             ║
║  History               78.30   C             ║
║  Physics               84.60   B             ║
║  ──────────────────────────────────────      ║
║  GPA:                  87.83                  ║
║  Status:               PASS                  ║
╠══════════════════════════════════════════════╣
║  Honors:    No                               ║
║  Dean's List: No                             ║
╚══════════════════════════════════════════════╝
```

4. **Use these String methods from Day 11:**
   - `trim()`, `toUpperCase()`, `substring()`, `length()`, `charAt()`
   - Use `contains()` or `equals()` for comparisons

5. **Use these formatting techniques from Day 12:**
   - `printf` with `%-20s`, `%8.2f`, `%-6s` for aligned columns
   - `String.format()` for building at least one computed string
   - `%n` for newlines within format strings

6. **Use the ternary operator** (Day 10) for Honors and Dean's List determination

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When would you choose `printf` over string concatenation? Give a specific example.
2. What is the difference between `\n` and `%n` in a format string? When does the distinction matter?
3. What does `String.format()` return, and why is it sometimes more useful than `printf`?
4. Looking at Days 11 and 12 together — how do String methods and String formatting complement each other in real programs?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_String_Formatting_in_Practice.md` containing:

1. Your comparison notes from Part 4
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `FormatSpecifiers.java`: All specifiers demonstrated with width/alignment | 10 |
| `EscapeSequences.java`: All escape sequences demonstrated correctly | 10 |
| `FormattedReport.java`: Clean aligned table with calculated totals | 20 |
| `FormatComparison.java`: All 3 scenarios shown 3 ways with clear commentary | 15 |
| `ReportCardGenerator.java`: Full capstone using Day 11 + Day 12 skills | 25 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

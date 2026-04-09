# Day 30 Assignment: Method Overloading and Final Capstone

## Overview

- **Topic:** Java Methods — Overloaded Methods and Comprehensive 1Z0-811 Capstone
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Method overloading

Same name, different parameter lists:

```java
public static int add(int a, int b) {
    return a + b;
}

public static double add(double a, double b) {
    return a + b;
}

public static int add(int a, int b, int c) {
    return a + b + c;
}
```

Java picks the right one based on the arguments you pass:

```java
add(3, 5);       // Calls int version
add(3.0, 5.0);   // Calls double version
add(1, 2, 3);    // Calls three-arg version
```

### What counts as overloading

| Change | Valid overload? |
|--------|----------------|
| Different number of parameters | Yes |
| Different parameter types | Yes |
| Different parameter order (of types) | Yes |
| Different return type only | **No** — won't compile |
| Different parameter names only | **No** — not a different signature |

### Type promotion in overloading

If there's no exact match, Java promotes the type:

```java
public static void print(double d) { System.out.println("double: " + d); }

print(5);  // No int version exists → int promoted to double
```

---

## Part 1: Method Overloading Fundamentals

### Program A: `OverloadingBasics.java`

Write a program that demonstrates overloading with multiple examples:

1. **Overloaded `display()` method:**
   ```java
   public static void display(int x) { ... }
   public static void display(double x) { ... }
   public static void display(String x) { ... }
   public static void display(int x, int y) { ... }
   public static void display(String label, int value) { ... }
   ```
   Call each from main and print which version was called.

2. **Overloaded `calculate()` method:**
   - `calculate(double radius)` — returns area of a circle
   - `calculate(double length, double width)` — returns area of a rectangle
   - `calculate(double base, double height, boolean isTriangle)` — returns area of a triangle
   - `calculate(int side)` — returns area of a square

   Call each and print the results with labels.

3. **Type promotion demonstration:** Write only a `double` version of a method, then call it with `int`, `float`, and `long` arguments. Print what happens:
   ```java
   public static void showValue(double d) {
       System.out.println("Received: " + d);
   }
   showValue(5);       // int → double
   showValue(5.0f);    // float → double
   showValue(5L);      // long → double
   ```

4. **What does NOT work:** Comment out examples that won't compile:
   ```java
   // These are NOT valid overloads — explain in comments why:
   // public static int process(int x) { return x; }
   // public static double process(int x) { return x; }  // Same params, different return only
   ```

---

## Part 2: Practical Overloading

### Create `Formatter.java` and `FormatterMain.java`

**`Formatter.java`**

Build a utility class with heavily overloaded methods (like Java's own `println`):

**Overloaded `formatCurrency()`:**
1. `formatCurrency(double amount)` — returns `"$1,234.56"`
2. `formatCurrency(double amount, String currencySymbol)` — returns `"€1,234.56"`
3. `formatCurrency(double amount, String currencySymbol, int decimalPlaces)` — returns `"€1,234.6"`

**Overloaded `repeat()`:**
1. `repeat(String text, int times)` — repeats the text: `"Ha"` × 3 → `"HaHaHa"`
2. `repeat(char c, int times)` — repeats the character: `'*'` × 5 → `"*****"`
3. `repeat(String text, int times, String separator)` — repeats with separator: `"Hey"` × 3 with `", "` → `"Hey, Hey, Hey"`

**Overloaded `max()`:**
1. `max(int a, int b)` — returns larger of two ints
2. `max(double a, double b)` — returns larger of two doubles
3. `max(int a, int b, int c)` — returns largest of three ints
4. `max(int[] arr)` — returns largest in an array

**Overloaded `contains()`:**
1. `contains(String text, String target)` — case-sensitive search
2. `contains(String text, String target, boolean ignoreCase)` — optional case sensitivity
3. `contains(int[] arr, int target)` — searches an int array
4. `contains(String[] arr, String target)` — searches a String array

All methods should be static. Include a private constructor.

**`FormatterMain.java`**

Demonstrate every overloaded version of every method. Print results showing which version was called:
```
=== formatCurrency ===
formatCurrency(1234.56):                    $1,234.56
formatCurrency(1234.56, "€"):              €1,234.56
formatCurrency(1234.56, "€", 1):           €1,234.6

=== max ===
max(10, 20):                               20
max(3.14, 2.71):                           3.14
max(5, 12, 8):                             12
max([3, 7, 2, 9, 1]):                      9
```

---

## Part 3: Exam-Style Method Questions

### Program C: `MethodExamPrep.java`

These patterns appear on the 1Z0-811 exam. Predict the output BEFORE running:

1. **Which overload is called?**
   ```java
   public static void test(int x) { System.out.println("int: " + x); }
   public static void test(double x) { System.out.println("double: " + x); }
   public static void test(String x) { System.out.println("String: " + x); }

   test(5);
   test(5.0);
   test("5");
   test(5L);      // long — which version?
   test(5.0f);    // float — which version?
   test('A');     // char — which version?
   ```

2. **Return type is NOT part of the signature:**
   ```java
   // Does this compile?
   // public static int getValue() { return 5; }
   // public static double getValue() { return 5.0; }
   ```
   Comment out and explain.

3. **Overloading with autoboxing:**
   ```java
   public static void process(int x) { System.out.println("int"); }
   public static void process(Integer x) { System.out.println("Integer"); }

   process(5);                    // Which one?
   process(Integer.valueOf(5));   // Which one?
   ```

4. **Static method scope:**
   ```java
   public class Scope {
       private int x = 10;
       private static int y = 20;

       public static void staticMethod() {
           // System.out.println(x);  // Does this compile?
           System.out.println(y);     // Does this compile?
       }

       public void instanceMethod() {
           System.out.println(x);     // Does this compile?
           System.out.println(y);     // Does this compile?
       }
   }
   ```

5. **Accessor/mutator pattern:**
   ```java
   public class Box {
       private int width;
       public int getWidth() { return width; }
       public void setWidth(int width) { this.width = width; }
   }
   // In main:
   Box b = new Box();
   b.setWidth(10);
   System.out.println(b.getWidth());
   // b.width = 20;  // Does this compile?
   ```

6. **Write your own** overloading exam question with at least 3 versions of the same method name, including one that involves type promotion. Include the prediction and explanation.

---

## Part 4: Final Capstone — Student Management System

### Create a multi-file application that serves as the capstone for the ENTIRE 1Z0-811 course.

This project should demonstrate EVERY major topic from Days 1-30. Build a Student Management System with the following files:

**`Student.java`**

- **Private fields** (Day 25): name, studentId (auto-assigned, static counter), age, email, major, gpa, enrollmentYear, ArrayList of course names
- **Multiple constructors** with chaining (Day 26): full, partial, name-only
- **Getters and setters** with validation (Day 29):
  - Name: not empty, trim whitespace (Day 11 String methods)
  - Email: must contain "@" (Day 11)
  - Age: 16-100 (Day 14 if-else)
  - GPA: 0.0-4.0 (Day 14)
- **Instance methods** (Day 28):
  - `addCourse(String course)` — adds to ArrayList (Day 23)
  - `removeCourse(String course)` — removes from ArrayList
  - `isEnrolledIn(String course)` — checks with contains()
  - `getAcademicStanding()` — returns "Honor Roll"/"Good Standing"/"Probation" based on GPA (Day 14/15 switch or if-else)
  - `getYearsEnrolled()` — calculates from current year (Day 5 java.time)
- **Overloaded methods** (Day 30):
  - `displayInfo()` — full details
  - `displayInfo(boolean brief)` — short or full based on flag
  - `displayInfo(String format)` — "table", "card", or "csv" format
- **Static methods** (Day 29):
  - `getTotalStudents()`
  - `getNextId()`
- **toString()** (Day 27)

**`Course.java`**

- Private fields: name, code, instructor, maxCapacity, ArrayList of enrolled student names
- Constructors with chaining
- Getters/setters with validation
- Overloaded `enroll()`:
  - `enroll(Student s)` — enroll one student
  - `enroll(Student[] students)` — enroll from an array (Day 22)
  - `enroll(ArrayList<Student> students)` — enroll from an ArrayList (Day 23)
- `isFull()`, `getAvailableSeats()`, `displayRoster()`

**`GradeBook.java`**

- Manages grades for students using parallel arrays or an ArrayList of formatted strings
- **Static utility methods:**
  - `calculateAverage(double[] grades)` — uses arrays (Day 22)
  - `calculateAverage(ArrayList<Double> grades)` — overloaded for ArrayList (Day 23/30)
  - `getLetterGrade(double average)` — uses if-else or switch (Day 14/15)
  - `calculateGPA(String letterGrade)` — converts letter to GPA points
- **Instance methods:**
  - `addGrade(String studentName, double grade)` — with validation (Day 21 try-catch)
  - `getStudentGrades(String studentName)` — search and return
  - `displayGradeReport()` — formatted with printf (Day 12)

**`StudentManagementSystem.java`** (the main class)

Interactive menu-driven application:

```
╔══════════════════════════════════════════╗
║     STUDENT MANAGEMENT SYSTEM           ║
╠══════════════════════════════════════════╣
║  1.  Add Student                        ║
║  2.  Remove Student                     ║
║  3.  Search Student                     ║
║  4.  View All Students                  ║
║  5.  Add Course                         ║
║  6.  Enroll Student in Course           ║
║  7.  Record Grade                       ║
║  8.  View Grade Report                  ║
║  9.  View Course Roster                 ║
║  10. System Statistics                  ║
║  11. Sort Students                      ║
║  0.  Exit                               ║
╚══════════════════════════════════════════╝
```

This program must use:
- **do-while** for the menu loop (Day 18)
- **switch** for menu selection (Day 15)
- **for loops** for iterating arrays (Day 17)
- **enhanced for loops** for iterating ArrayLists (Day 17/23)
- **while loops** for input validation (Day 18)
- **break and continue** where appropriate (Day 19)
- **try-catch** for all user input (Day 21)
- **Scanner** for input (Day 5)
- **printf** for formatted output (Day 12)
- **String methods** for input processing (Day 11)
- **Math/Random** for generating sample data (Day 13)
- **Arrays and ArrayLists** together (Day 24)
- **Private fields, getters, setters** (Days 25, 29)
- **Constructors with chaining** (Day 26)
- **Composition** (Day 27)
- **Static and instance methods** (Day 29)
- **Overloaded methods** (Day 30)

**System Statistics** should display:
- Total students registered
- Total courses offered
- Average GPA across all students
- Student with highest GPA
- Most popular course (most enrollments)
- Grade distribution across all recorded grades

---

## Part 5: Reflection Questions

Answer these briefly (2-3 sentences each — this is the final reflection):

1. What is method overloading, and how does it make code more user-friendly?
2. Looking at the entire 30-day curriculum, which topic was the most challenging for you? Which was the most interesting?
3. How do all the topics connect — data types, operators, strings, decisions, loops, arrays, classes, and methods? Can you describe a mental model of how a Java program is built from these pieces?
4. What topics do you feel most confident about going into the 1Z0-811 exam? Which topics do you want to review more?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Method_Overloading_and_Final_Capstone.md` containing:

1. Your predictions from Part 3
2. A list of which Day's topic each part of the capstone demonstrates
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `OverloadingBasics.java`: All overloading forms with type promotion | 10 |
| `Formatter.java/Main`: All overloaded utility methods demonstrated | 10 |
| `MethodExamPrep.java`: All 6 questions with correct predictions | 10 |
| Final Capstone — `Student.java`: Fields, constructors, getters/setters, overloaded methods | 15 |
| Final Capstone — `Course.java`: Overloaded enroll, validation, composition | 10 |
| Final Capstone — `GradeBook.java`: Static utilities, grade calculations | 10 |
| Final Capstone — `StudentManagementSystem.java`: Full menu, all topics integrated | 15 |
| Reflection questions answered thoughtfully | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

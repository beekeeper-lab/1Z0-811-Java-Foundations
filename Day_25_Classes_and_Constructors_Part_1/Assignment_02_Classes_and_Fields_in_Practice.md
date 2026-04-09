# Day 25 Assignment: Classes, Objects, and Fields in Practice

## Overview

- **Topic:** Classes and Constructors — Creating Classes, Using private, and Understanding Variable Scope
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### A complete class with private fields

```java
public class Person {
    // Instance variables (belong to each object)
    private String name;
    private int age;

    // Class variable (belongs to the class, shared by all objects)
    private static int personCount = 0;

    // Local variable example (inside a method)
    public void greet() {
        String greeting = "Hello!";  // local variable — only exists in this method
        System.out.println(greeting + " I'm " + name);
    }
}
```

### The three variable types

| Type | Declared | Scope | Default Value | Lifetime |
|------|----------|-------|---------------|----------|
| Instance variable | Inside class, outside methods | Entire class | Yes (0, null, false) | Lives as long as the object |
| Class variable (`static`) | Inside class with `static` | Entire class + shared | Yes (0, null, false) | Lives as long as the program |
| Local variable | Inside a method | Only that method | **None** — must initialize | Lives until method ends |

### Access with private

```java
public class BankAccount {
    private double balance;  // Cannot be accessed directly from outside

    // Must use methods to interact with private fields
    public double getBalance() {
        return balance;
    }
}
```

```java
BankAccount acct = new BankAccount();
// acct.balance = 1000;     // ERROR — balance is private
// double b = acct.balance;  // ERROR — balance is private
double b = acct.getBalance(); // OK — using the public method
```

---

## Part 1: Building Classes with Fields

### Program A: Create the following three classes as separate `.java` files, plus `ClassDemoMain.java` to test them.

**`Product.java`**

Create a class with these fields (all `private`):
- `String name`
- `String category`
- `double price`
- `int quantityInStock`

Add a `displayInfo()` method that prints all fields in a formatted way.

For now, set fields directly in the constructor or use a temporary workaround (we'll add proper constructors on Day 26). You can make fields `public` temporarily and add a comment: `// TODO: make private, add getters/setters`.

**`Movie.java`**

Create a class with these fields:
- `String title`
- `String director`
- `int year`
- `double rating`
- `String genre`

Add methods:
- `displayInfo()` — prints movie details
- `isClassic()` — returns `true` if the movie is more than 25 years old
- `isHighlyRated()` — returns `true` if rating is 8.0 or above

**`Rectangle.java`**

Create a class with these fields:
- `double width`
- `double height`

Add methods:
- `getArea()` — returns width * height
- `getPerimeter()` — returns 2 * (width + height)
- `isSquare()` — returns true if width equals height
- `displayInfo()` — prints dimensions, area, perimeter, and whether it's a square

**`ClassDemoMain.java`**

In main, create at least 2 objects from each class, set their fields, and call all methods.

---

## Part 2: Variable Scope and Lifetime

### Program B: `VariableScope.java`

Write a single-file program that demonstrates all three variable types and their scope:

1. **Instance variables:** Create a class `Counter` with an instance variable `int count`. Create two `Counter` objects and modify each independently to prove they have separate copies:
   ```java
   Counter c1 = new Counter();
   Counter c2 = new Counter();
   c1.count = 10;
   c2.count = 20;
   // c1.count is still 10 — each object has its own
   ```

2. **Class (static) variable:** Add a `static int totalCounters` that increments every time a Counter is used. Show that ALL Counter objects share this single variable:
   ```java
   System.out.println(Counter.totalCounters);  // Shared across all objects
   ```

3. **Local variables:** Show that local variables only exist inside their method:
   ```java
   public void calculate() {
       int temp = 42;  // Only exists here
       System.out.println(temp);
   }
   // temp does not exist outside calculate()
   ```

4. **Local variable must be initialized:** Demonstrate the compiler error:
   ```java
   public void broken() {
       int x;
       // System.out.println(x);  // ERROR: variable x might not have been initialized
   }
   ```
   Comment it out and explain in a comment why instance variables get defaults but locals don't.

5. **Variable shadowing:** Show what happens when a local variable has the same name as an instance variable:
   ```java
   private int value = 10;

   public void confusing() {
       int value = 20;  // Local shadows the instance variable
       System.out.println(value);       // Prints 20 (local)
       System.out.println(this.value);  // Prints 10 (instance)
   }
   ```

---

## Part 3: The private Modifier

### Program C: Create `BankAccount.java` and `BankAccountMain.java`

**`BankAccount.java`**

Create a class with ALL private fields:
- `private String accountHolder`
- `private String accountNumber`
- `private double balance`
- `private int transactionCount`

Since the fields are private, the ONLY way to interact with them is through methods. Add these public methods:

1. `setAccountHolder(String name)` — sets the name (validate not empty)
2. `getAccountHolder()` — returns the name
3. `setAccountNumber(String number)` — sets it (validate exactly 10 characters)
4. `getAccountNumber()` — returns the number, but masked: `"******7890"` (only show last 4)
5. `getBalance()` — returns the balance
6. `deposit(double amount)` — adds to balance (validate positive), increments transaction count
7. `withdraw(double amount)` — subtracts from balance (validate positive and sufficient funds), increments transaction count
8. `getTransactionCount()` — returns the count
9. `displayStatement()` — prints a formatted account summary

**`BankAccountMain.java`**

In main:
1. Create a BankAccount and set it up using the setter methods
2. Perform several deposits and withdrawals
3. Show that you CANNOT access `balance` directly — try it, comment out the error, and explain
4. Show that validation prevents negative deposits and overdrafts
5. Display the final statement

Add a comment block explaining why `private` fields with public methods is better than public fields — even though it's more code.

---

## Part 4: Multiple Objects from One Class

### Program D: Create `Student.java` and `ClassroomMain.java`

**`Student.java`**

Create a class with private fields:
- `private String name`
- `private int id`
- `private double[] grades` (an array of 5 grades)
- `private static int nextId = 1000` (auto-incrementing ID)

Add methods:
- `setName(String name)` — set the name
- `getName()` — get the name
- `getId()` — get the ID
- `setGrade(int index, double grade)` — set a specific grade (validate index 0-4 and grade 0-100)
- `getGrade(int index)` — get a specific grade
- `getAverage()` — calculate and return the average of all grades
- `getLetterGrade()` — return a letter grade based on the average
- `displayReport()` — print a formatted student report

The ID should be auto-assigned — each new Student gets the next ID automatically using the static `nextId` field. This demonstrates a practical use of class variables.

**`ClassroomMain.java`**

In main:
1. Create an array of 5 Students (or an ArrayList)
2. Set names and grades for each
3. Print each student's report
4. Find and print the student with the highest average
5. Find and print the class average across all students
6. Print a formatted class roster table using `printf`

Show that each Student has:
- Its own copy of name, grades (instance variables)
- A unique auto-assigned ID
- A shared counter for total students created (class variable)

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between an instance variable and a local variable? Why do instance variables get default values but locals do not?
2. Why should fields generally be `private`? What is the benefit of forcing access through methods?
3. What is a `static` variable, and why is it useful for things like counters and IDs?
4. How does Day 25 build on the OOP concepts you learned on Day 3?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Classes_and_Fields_in_Practice.md` containing:

1. Your explanation of why private fields with public methods is preferred
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Three classes with fields and methods, tested in main | 20 |
| `VariableScope.java`: All 5 scope demonstrations with explanations | 15 |
| `BankAccount.java/Main`: Private fields, validation, and access control | 25 |
| `Student.java/ClassroomMain`: Auto-ID, array of objects, class statistics | 25 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

# Day 26 Assignment: Constructors in Practice

## Overview

- **Topic:** Classes and Constructors — Default, Parameterized, and Overloaded Constructors
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Default constructor

When you write NO constructors, Java provides a default one that takes no arguments and sets fields to defaults:

```java
public class Dog {
    String name;
    int age;
    // Java provides: public Dog() { }  — implicitly
}
Dog d = new Dog();  // name = null, age = 0
```

**Once you write ANY constructor, Java stops providing the default:**

```java
public class Dog {
    String name;
    int age;

    public Dog(String name, int age) {  // parameterized constructor
        this.name = name;
        this.age = age;
    }
}
Dog d1 = new Dog("Buddy", 3);  // Works
// Dog d2 = new Dog();          // ERROR — no default constructor anymore!
```

### The `this` keyword

Inside a constructor or method, `this` refers to the current object:

```java
public Dog(String name, int age) {
    this.name = name;   // this.name = instance variable, name = parameter
    this.age = age;
}
```

### Constructor overloading

Multiple constructors with different parameter lists:

```java
public class Dog {
    private String name;
    private int age;

    // No-arg constructor
    public Dog() {
        this("Unknown", 0);  // Calls the two-arg constructor
    }

    // One-arg constructor
    public Dog(String name) {
        this(name, 0);  // Calls the two-arg constructor
    }

    // Two-arg constructor (the "primary" one)
    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

**Rule:** `this()` must be the FIRST statement in the constructor.

---

## Part 1: Default Constructor Behavior

### Program A: Create `DefaultConstructorDemo.java` and `DefaultMain.java`

**`DefaultConstructorDemo.java`**

1. Create a class `Widget` with fields: `String label`, `int count`, `double price`, `boolean active`. Do NOT write any constructor.

2. In `DefaultMain.java`, create a Widget and print all its fields to show the defaults.

3. Now add a parameterized constructor to Widget:
   ```java
   public Widget(String label, int count, double price) { ... }
   ```

4. Try to create a Widget with no arguments: `new Widget()`. Comment out the error and explain: *"Once I added a parameterized constructor, the default constructor disappeared."*

5. Fix it by adding an explicit no-arg constructor:
   ```java
   public Widget() {
       this("Default Widget", 0, 0.0);
   }
   ```

6. Now both work — test and print both.

---

## Part 2: Parameterized Constructors and `this`

### Program B: Create `Book.java` and `BookMain.java`

**`Book.java`**

Create a class with private fields:
- `private String title`
- `private String author`
- `private int pages`
- `private double price`
- `private boolean isHardcover`

Write a parameterized constructor that:
1. Accepts all five fields as parameters
2. Uses `this.field = field` for every assignment
3. Validates: title and author not empty, pages > 0, price >= 0

Add methods:
- Getters for all fields
- `displayInfo()` — formatted output
- `getPricePerPage()` — returns price / pages

**`BookMain.java`**

Create at least 4 Book objects with different values. Display each one and its price per page. Try to create a book with invalid data (empty title, negative pages) and show how your validation handles it.

**Demonstrate `this`:** Add a method that returns the object itself:
```java
public Book applyDiscount(double percent) {
    this.price -= this.price * (percent / 100);
    return this;  // Returns the same object — enables chaining
}
```

Show method chaining in main:
```java
Book b = new Book("Java", "Author", 500, 49.99, true);
b.applyDiscount(10).displayInfo();
```

---

## Part 3: Constructor Overloading

### Program C: Create `Employee.java` and `EmployeeMain.java`

**`Employee.java`**

Create a class with private fields:
- `private String name`
- `private String department`
- `private double salary`
- `private String email`
- `private static int nextId = 1000`
- `private int id`

Write **four overloaded constructors** using constructor chaining with `this()`:

1. **Full constructor** (all fields): The "primary" constructor that all others delegate to
   ```java
   public Employee(String name, String department, double salary, String email) {
       this.id = nextId++;
       this.name = name;
       this.department = department;
       this.salary = salary;
       this.email = email;
   }
   ```

2. **Three-arg constructor** (no email): Calls the full constructor with a generated email
   ```java
   public Employee(String name, String department, double salary) {
       this(name, department, salary, name.toLowerCase().replace(" ", ".") + "@company.com");
   }
   ```

3. **Two-arg constructor** (name and department only): Calls the three-arg with a default salary
   ```java
   public Employee(String name, String department) {
       this(name, department, 50000.0);
   }
   ```

4. **No-arg constructor**: Calls the two-arg with defaults
   ```java
   public Employee() {
       this("New Employee", "Unassigned");
   }
   ```

Add getters, setters, and a `displayInfo()` method.

**`EmployeeMain.java`**

Create one employee using EACH constructor:
```java
Employee e1 = new Employee("Alice Johnson", "Engineering", 95000, "alice@company.com");
Employee e2 = new Employee("Bob Smith", "Marketing", 72000);
Employee e3 = new Employee("Charlie Brown", "Sales");
Employee e4 = new Employee();
```

Print all four to show that defaults were applied correctly and IDs auto-incremented. Show the constructor chaining by adding print statements inside each constructor:
```java
public Employee() {
    this("New Employee", "Unassigned");
    System.out.println("No-arg constructor called");
}
```

This reveals the call chain: no-arg → two-arg → three-arg → full.

---

## Part 4: Constructors and Validation

### Program D: Create `Temperature.java` and `TemperatureMain.java`

**`Temperature.java`**

Create a class that represents a temperature with validation built into the constructor:

Private fields:
- `private double degrees`
- `private char scale` ('C', 'F', or 'K')

Constructors:
1. **Two-arg constructor** (degrees and scale):
   - Validate scale is 'C', 'F', or 'K' (throw `IllegalArgumentException` if not)
   - Validate Kelvin is not below 0 (absolute zero)
   - Validate Celsius is not below -273.15
   - Validate Fahrenheit is not below -459.67

2. **One-arg constructor** (degrees only): Defaults to Celsius
   ```java
   public Temperature(double degrees) {
       this(degrees, 'C');
   }
   ```

3. **No-arg constructor**: Defaults to 0°C
   ```java
   public Temperature() {
       this(0.0, 'C');
   }
   ```

Methods:
- `toCelsius()` — converts and returns the value in Celsius
- `toFahrenheit()` — converts and returns the value in Fahrenheit
- `toKelvin()` — converts and returns the value in Kelvin
- `displayAll()` — prints the temperature in all three scales using `printf`

**`TemperatureMain.java`**

1. Create temperatures using each constructor
2. Display all conversions
3. Try to create an invalid temperature (negative Kelvin) — wrap in try-catch and show the error
4. Create an array of Temperature objects and find the hottest and coldest

---

## Part 5: Exam-Style Constructor Questions

### Program E: `ConstructorExamPrep.java`

These patterns appear on the 1Z0-811 exam. Predict the output BEFORE running:

1. **Which constructor runs?**
   ```java
   public class Gadget {
       public Gadget() { System.out.println("No-arg"); }
       public Gadget(String name) { System.out.println("String: " + name); }
       public Gadget(int count) { System.out.println("Int: " + count); }
   }
   // In main:
   Gadget g1 = new Gadget();
   Gadget g2 = new Gadget("Widget");
   Gadget g3 = new Gadget(5);
   ```

2. **Constructor chaining order:**
   ```java
   public class Chain {
       public Chain() {
           this(10);
           System.out.println("A");
       }
       public Chain(int x) {
           this(x, 20);
           System.out.println("B");
       }
       public Chain(int x, int y) {
           System.out.println("C: " + x + ", " + y);
       }
   }
   // In main:
   Chain c = new Chain();
   ```
   What order do A, B, C print?

3. **Does this compile?**
   ```java
   public class Broken {
       private int value;
       public Broken(int value) {
           this.value = value;
       }
   }
   // In main:
   Broken b = new Broken();  // No no-arg constructor!
   ```

4. **Does this compile?**
   ```java
   public class AlsoBroken {
       public AlsoBroken() {
           System.out.println("Hello");
           this(10);  // this() not first statement!
       }
       public AlsoBroken(int x) {
           System.out.println("x = " + x);
       }
   }
   ```

5. **this vs. parameter:**
   ```java
   public class Confusing {
       private int x = 10;
       public Confusing(int x) {
           System.out.println("x = " + x);
           System.out.println("this.x = " + this.x);
           this.x = x;
           System.out.println("this.x after = " + this.x);
       }
   }
   // In main:
   Confusing c = new Confusing(99);
   ```

For each, write your prediction as a comment, then verify.

---

## Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What happens to the default constructor when you write your own? Why is this important to remember?
2. Why is `this` necessary when constructor parameters have the same name as instance variables?
3. What is constructor chaining with `this()`, and why is it useful?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Constructors_in_Practice.md` containing:

1. Your constructor chaining trace from Part 3
2. Your predictions from Part 5
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Part 1: Default constructor behavior demonstrated with explanation | 10 |
| `Book.java/Main`: Parameterized constructor with validation and this | 15 |
| `Employee.java/Main`: Four overloaded constructors with chaining | 25 |
| `Temperature.java/Main`: Constructors with validation and conversions | 20 |
| `ConstructorExamPrep.java`: All 5 questions with correct predictions | 15 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

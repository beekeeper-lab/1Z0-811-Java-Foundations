# Module 25: Classes and Constructors Part 1

> 🏷️ Advanced

> 🎯 **Teach:** How to create your own classes with private fields, understand the three types of variables (instance, class, and local), and use the private access modifier to enforce encapsulation
> **See:** Custom Product, Movie, Rectangle, BankAccount, and Student classes that demonstrate field access control, variable scope, and auto-incrementing IDs
> **Feel:** A deeper understanding of object-oriented programming, moving from using classes to designing them yourself

> 🎙️ Back on Day 3 you learned the idea that a class is a blueprint and an object is an instance of that blueprint. Today you put that theory into practice by building your own classes from scratch. You will create private fields, understand why access control matters, and see how instance variables, class variables, and local variables each have their own scope and lifetime. This is the beginning of truly thinking like an object-oriented programmer.

> 🎙️ This is a big milestone in the course. Up until now you have been using classes that other people wrote -- String, Scanner, ArrayList. Starting today, you design your own. This is where programming shifts from following recipes to actually creating things, and it is the largest topic area on the 1Z0-811 exam.

![Architect with class blueprints](../images/module-25/blueprint-architect.png)

## Research: Classes, Objects, and Fields

> 🎯 **Teach:** The relationship between classes and objects, the three variable types (instance, class, local), and why the private modifier matters.
> **See:** A research assignment exploring instantiation, variable scope and lifetime, and the connection between private fields and encapsulation.
> **Feel:** Ready to articulate core OOP concepts before designing your own classes from scratch.

### Overview

- **Topic:** Classes and Constructors — Creating Classes, Instance Variables, and the private Modifier
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is the relationship between a class and an object?** Expand on what you learned on Day 3 — now with deeper understanding. Explain that a class is a blueprint and an object is an instance. What does it mean to "instantiate" an object with `new`? What happens in memory when you create an object?

2. **What are instance variables, class variables, and local variables?** Define each type, explain where each is declared (inside a method, inside a class but outside methods, with `static`), and describe their scope and lifetime. What are the default values for instance variables vs. local variables? (Hint: local variables have NO default — they must be initialized before use.)

3. **What is the `private` access modifier and why is it important?** Explain what `private` does — it restricts access to within the class only. Why is this useful? Connect this to the OOP concept of **encapsulation** from Day 3. What happens if you try to access a private field from outside the class?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Classes_and_Fields_Research.md` in this folder.

> 💡 **Remember this one thing:** Instance variables get default values (0, null, false) and live as long as the object. Local variables get no defaults and must be initialized before use -- the compiler will reject your code if you try to read an uninitialized local variable. This difference is a frequent exam topic.

## Hands-On: Classes, Objects, and Fields in Practice

> 🎯 **Teach:** How to create classes with private fields, demonstrate variable scope differences, and enforce encapsulation through access control.
> **See:** Custom Product, Movie, Rectangle, BankAccount, and Student classes with private fields, getters and setters, and auto-incrementing IDs.
> **Feel:** The shift from using other people's classes to designing your own, understanding that you are now building the blueprints.

> 🎙️ Now you will build your own classes from the ground up, starting with simple ones and working up to a fully encapsulated BankAccount with private fields and public methods that control all access to the data.

### Overview

- **Topic:** Classes and Constructors — Creating Classes, Using private, and Understanding Variable Scope
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

#### A complete class with private fields

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

#### The three variable types

| Type | Declared | Scope | Default Value | Lifetime |
|------|----------|-------|---------------|----------|
| Instance variable | Inside class, outside methods | Entire class | Yes (0, null, false) | Lives as long as the object |
| Class variable (`static`) | Inside class with `static` | Entire class + shared | Yes (0, null, false) | Lives as long as the program |
| Local variable | Inside a method | Only that method | **None** — must initialize | Lives until method ends |

> 🎙️ That table is worth memorizing. The exam will give you code with variables declared in different places and ask about their scope, defaults, or lifetime. The biggest trap is local variables having no default value -- if you try to use one before assigning it, the compiler rejects your code. Instance variables do not have this problem because Java initializes them automatically.

![Three variable types: instance, class, and local](../images/module-25/three-variable-types.png)

#### Access with private

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

![Encapsulation as a vault protecting private fields](../images/module-25/encapsulation-vault.png)

---

### Part 1: Building Classes with Fields

#### Program A: Create the following three classes as separate `.java` files, plus `ClassDemoMain.java` to test them.

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

> 🎙️ Building your own classes with fields and methods is the first step. Do not worry about making them perfect yet -- constructors and proper encapsulation come in the next two days. Right now, focus on understanding that each object you create gets its own separate copy of the instance variables.

---

### Part 2: Variable Scope and Lifetime

#### Program B: `VariableScope.java`

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

> 🎙️ Variable shadowing in Part 2 is a subtle topic that the exam loves. When a local variable has the same name as an instance variable, the local one wins inside that method. You have to use this dot to reach the instance variable. This is not just a trick question -- it is the reason the this keyword exists, and you will use it constantly in constructors starting tomorrow.

---

### Part 3: The private Modifier

#### Program C: Create `BankAccount.java` and `BankAccountMain.java`

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

> 🎙️ The BankAccount is the clearest example of why private matters. Imagine if balance were public -- any code anywhere could set it to a million dollars or negative infinity. By making it private and providing deposit and withdraw methods with validation, you control every possible interaction with that field. This is encapsulation in action, and the exam expects you to understand why it is the right design.

---

### Part 4: Multiple Objects from One Class

#### Program D: Create `Student.java` and `ClassroomMain.java`

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

![Static ID counter shared across all Student objects](../images/module-25/static-id-counter.png)

> 🎙️ The auto-incrementing ID is a perfect example of why static variables exist. Every Student needs a unique ID, and the static nextId field keeps track of the next one to assign. Since it is shared across all Student objects, each new Student gets the next number in sequence without any coordination. This pattern is used constantly in real applications -- databases, user accounts, order numbers.

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

### Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between an instance variable and a local variable? Why do instance variables get default values but locals do not?
2. Why should fields generally be `private`? What is the benefit of forcing access through methods?
3. What is a `static` variable, and why is it useful for things like counters and IDs?
4. How does Day 25 build on the OOP concepts you learned on Day 3?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Classes_and_Fields_in_Practice.md` containing:

1. Your explanation of why private fields with public methods is preferred
2. Your answers to the reflection questions

> 💡 **Remember this one thing:** Making fields `private` and providing public getter and setter methods is the foundation of encapsulation. It lets you add validation, control access, and change the internal implementation without breaking code that uses your class -- this is why every well-designed Java class follows this pattern.

## Grading

> 🎯 **Teach:** How your research and hands-on work are evaluated across class design and encapsulation concepts.
> **See:** Rubrics for the research essay, all four program sets, and the reflection questions.
> **Feel:** Clear about what constitutes a complete, high-quality submission for this module.

> 🔄 **Where this fits:** Day 25 begins the classes and constructors section, moving you from using Java's built-in classes to designing your own -- a major step toward the object-oriented programming skills tested on the 1Z0-811 exam.

> 🎙️ Today you took the first big step into object-oriented programming -- creating your own classes, understanding variable scope, and using private to protect your data. Tomorrow you will learn constructors, which let you initialize objects properly at the moment they are created instead of calling setters one by one. The pieces are coming together.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains the class-object relationship with instantiation | 25 |
| Accurately defines instance, class, and local variables with scope and defaults | 35 |
| Explains private modifier and connects it to encapsulation | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| Part 1: Three classes with fields and methods, tested in main | 20 |
| `VariableScope.java`: All 5 scope demonstrations with explanations | 15 |
| `BankAccount.java/Main`: Private fields, validation, and access control | 25 |
| `Student.java/ClassroomMain`: Auto-ID, array of objects, class statistics | 25 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

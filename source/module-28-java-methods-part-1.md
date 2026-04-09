# Module 28: Java Methods Part 1

> 🏷️ Advanced

> 🎯 **Teach:** How to define methods with parameters and return types, understand pass-by-value semantics for both primitives and objects, and compose methods that call other methods
> **See:** Programs that build reusable method libraries, prove Java's pass-by-value behavior, compose character-analysis methods, and create a menu-driven math toolkit
> **Feel:** Confident breaking problems into small, reusable methods and understanding exactly what happens to data when it is passed to a method

> 🎙️ You have been calling methods all along -- `System.out.println()`, `scanner.nextLine()`, `Math.sqrt()`. Today you learn how to write your own. A method is a named block of code that performs a specific task, and learning to design good methods is what separates code that works from code that is clean, reusable, and maintainable. You will also learn one of the most important concepts in Java: pass-by-value, which determines what happens to your data when you hand it to a method.

> 🎙️ Methods are what make your code reusable. Without methods, you would have to copy and paste the same logic everywhere it is needed. With methods, you write it once, name it clearly, and call it wherever you need it. The exam tests method signatures, return types, and pass-by-value heavily, so today is directly exam-relevant.

## Research: Describing and Creating Methods

> 🎯 **Teach:** What methods are, how parameters and return types work, and what pass-by-value means for primitives versus objects.
> **See:** A research assignment covering method signatures, the difference between parameters and arguments, and method design best practices.
> **Feel:** Ready to explain method fundamentals in your own words before writing reusable methods yourself.

### Overview

- **Topic:** Java Methods — Defining Methods, Parameters, and Return Types
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is a method in Java?** Explain what a method is, what problem it solves (code reuse, organization, abstraction), and describe each part of a method signature: access modifier, return type, method name, and parameter list. What does `void` mean as a return type? What does the `return` statement do?

2. **What are parameters and arguments?** Explain the difference between a parameter (the variable in the method definition) and an argument (the value passed when calling the method). How does Java handle parameter passing — is it pass-by-value or pass-by-reference? What does this mean for primitives vs. objects?

3. **What makes a good method?** Describe best practices for method design: a method should do one thing, have a descriptive name, be a reasonable length, and have clear inputs and outputs. Why is breaking code into methods better than writing everything in main?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_Methods_Research.md` in this folder.

> 💡 **Remember this one thing:** Java is always pass-by-value. For primitives, a copy of the value is passed, so the original cannot change. For objects, a copy of the reference is passed -- you can modify the object's contents through that reference, but you cannot make the caller's variable point to a different object.

## Hands-On: Describing and Creating Methods in Practice

> 🎯 **Teach:** How to define methods with parameters and return types, prove Java's pass-by-value behavior, and compose methods that call other methods.
> **See:** A method library with ten utility functions, pass-by-value demonstrations with primitives and arrays, and a menu-driven math toolkit.
> **Feel:** Confident breaking problems into small, reusable methods and understanding exactly what happens to data when passed to a method.

> 🎙️ Now you will write methods of every shape and size -- void methods, methods that return values, methods that take parameters, and methods that call other methods. Then you will prove to yourself exactly how pass-by-value works in Java.

### Overview

- **Topic:** Java Methods — Defining Methods, Parameters, Return Types, and Pass-by-Value
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

#### Method anatomy

```java
public static int add(int a, int b) {
//│      │      │   │    └─ parameters
//│      │      │   └────── method name
//│      │      └────────── return type
//│      └───────────────── static (belongs to class, not object)
//└──────────────────────── access modifier
    return a + b;  // return statement sends a value back
}
```

#### void vs. return type

```java
// void — performs an action, returns nothing
public static void greet(String name) {
    System.out.println("Hello, " + name);
}

// Return type — performs a calculation, returns a result
public static double average(int a, int b) {
    return (a + b) / 2.0;
}
```

#### Calling methods

```java
greet("Campbell");               // void — just call it
double avg = average(85, 92);    // return type — store the result
System.out.println(average(85, 92)); // or use it directly
```

#### Pass-by-value

Java ALWAYS passes by value. For primitives, a copy is passed — the original can't change. For objects, a copy of the *reference* is passed — you can modify the object's contents but can't reassign the reference.

```java
public static void tryToChange(int x) {
    x = 999;  // Only changes the local copy
}

int num = 5;
tryToChange(num);
System.out.println(num);  // Still 5!
```

> 🎙️ Pass-by-value is one of the trickiest concepts in Java. The key insight is that Java always copies the value being passed. For a primitive, that is the actual data, so the method cannot change the original. For an object reference, it is a copy of the address, so the method can modify the object but cannot make the caller's variable point to a different object. Study the examples carefully.

---

### Part 1: Method Fundamentals

#### Program A: `MethodBasics.java`

Write a program with a variety of methods to demonstrate the fundamentals. All methods should be `static` (since they're called from `main`).

1. **void with no parameters:**
   ```java
   public static void printSeparator() {
       System.out.println("════════════════════════════════");
   }
   ```

2. **void with parameters:**
   ```java
   public static void printGreeting(String name, int times) {
       for (int i = 0; i < times; i++) {
           System.out.println("Hello, " + name + "!");
       }
   }
   ```

3. **Returns a value:**
   ```java
   public static int square(int n) {
       return n * n;
   }
   ```

4. **Returns a boolean:**
   ```java
   public static boolean isEven(int n) {
       return n % 2 == 0;
   }
   ```

5. **Write 6 more methods on your own:**
   - `max(int a, int b)` → returns the larger value
   - `absoluteValue(int n)` → returns the absolute value without using `Math.abs()`
   - `celsiusToFahrenheit(double celsius)` → returns the converted temperature
   - `isPalindrome(String text)` → returns true if the string reads the same forwards and backwards
   - `countVowels(String text)` → returns the number of vowels
   - `repeatString(String text, int times)` → returns the text repeated (e.g., `repeatString("Ha", 3)` → `"HaHaHa"`)

6. **Call every method from main** and print the results. Show that methods with return values can be used inside expressions:
   ```java
   System.out.println("Max of squares: " + max(square(3), square(4)));
   ```

> 🎙️ When you are writing your own methods, pay attention to the return type. A void method performs an action but gives nothing back. A method with a return type computes a result and hands it to the caller. The exam will show you methods and ask what they return, or whether they compile. If the return type says int but the method returns a String, that is a compiler error.

---

### Part 2: Pass-by-Value

#### Program B: `PassByValueDemo.java`

Write a program that proves Java is pass-by-value:

1. **Primitive pass-by-value:** Show that modifying a primitive parameter does NOT affect the original:
   ```java
   public static void tryToModify(int x) {
       x = x * 10;
       System.out.println("Inside method: x = " + x);
   }

   // In main:
   int original = 5;
   tryToModify(original);
   System.out.println("After method: original = " + original);  // Still 5
   ```

2. **String pass-by-value:** Strings are objects but immutable — reassignment inside a method doesn't affect the original:
   ```java
   public static void tryToModify(String s) {
       s = s.toUpperCase();
       System.out.println("Inside method: s = " + s);
   }

   // In main:
   String greeting = "hello";
   tryToModify(greeting);
   System.out.println("After method: greeting = " + greeting);  // Still "hello"
   ```

3. **Array pass-by-value (of the reference):** The reference is copied, but both copies point to the SAME array — so modifications ARE visible:
   ```java
   public static void doubleAll(int[] arr) {
       for (int i = 0; i < arr.length; i++) {
           arr[i] *= 2;
       }
   }

   // In main:
   int[] nums = {1, 2, 3, 4, 5};
   doubleAll(nums);
   // nums is now {2, 4, 6, 8, 10} — the original IS changed!
   ```

4. **But reassigning the reference doesn't work:**
   ```java
   public static void tryToReplace(int[] arr) {
       arr = new int[]{99, 99, 99};  // Points local copy to a new array
       System.out.println("Inside: " + Arrays.toString(arr));
   }

   // In main:
   int[] nums = {1, 2, 3};
   tryToReplace(nums);
   System.out.println("After: " + Arrays.toString(nums));  // Still {1, 2, 3}
   ```

5. Add summary comments explaining the rule: *"Java passes a copy of the value. For primitives, it's a copy of the data. For objects, it's a copy of the reference — so you can modify the object through it, but you can't make the original variable point somewhere else."*

> 🎙️ The array pass-by-value demo is the most important one. Primitives cannot be changed by a method, but arrays can because the method receives a copy of the reference that points to the same array. This is why doubleAll modifies the original but tryToReplace does not. If you can explain the difference between those two, you understand Java's parameter passing.

---

### Part 3: Methods That Call Methods

#### Program C: `MethodComposition.java`

Write a program that demonstrates methods calling other methods to build more complex behavior:

1. **Basic building blocks:**
   ```java
   public static boolean isLetter(char c) { ... }
   public static boolean isDigit(char c) { ... }
   public static boolean isUpperCase(char c) { ... }
   public static boolean isLowerCase(char c) { ... }
   ```

2. **Methods that use the building blocks:**
   ```java
   public static boolean isAlphanumeric(char c) {
       return isLetter(c) || isDigit(c);
   }

   public static int countDigits(String text) {
       int count = 0;
       for (char c : text.toCharArray()) {
           if (isDigit(c)) count++;
       }
       return count;
   }

   public static int countUpperCase(String text) { ... }
   public static int countLowerCase(String text) { ... }
   ```

3. **A high-level method that composes everything:**
   ```java
   public static void analyzeString(String text) {
       System.out.println("Text: \"" + text + "\"");
       System.out.println("Length: " + text.length());
       System.out.println("Letters: " + countLetters(text));
       System.out.println("Digits: " + countDigits(text));
       System.out.println("Uppercase: " + countUpperCase(text));
       System.out.println("Lowercase: " + countLowerCase(text));
       System.out.println("Is alphanumeric only: " + isAllAlphanumeric(text));
   }
   ```

4. **Test with varied inputs:** Analyze `"Hello World 123"`, `"ABC"`, `"12345"`, `"Hello123!"`, and `""`.

Add a comment explaining how breaking logic into small methods makes code readable, testable, and reusable.

> 🎙️ Method composition is a powerful design technique. Notice how analyzeString calls countDigits, which calls isDigit. Each method does one small thing, and the higher-level methods combine them into something more complex. This layered approach makes your code easy to read, easy to test, and easy to change.

---

### Part 4: Practical Application

#### Program D: `MathToolkit.java`

Build a collection of math utility methods that demonstrate method design best practices:

1. `factorial(int n)` — returns n! as a long
2. `isPrime(int n)` — returns true if prime
3. `gcd(int a, int b)` — returns greatest common divisor (use the Euclidean algorithm)
4. `lcm(int a, int b)` — returns least common multiple (uses `gcd`)
5. `fibonacci(int n)` — returns the nth Fibonacci number
6. `power(double base, int exponent)` — returns base^exponent without using `Math.pow()`
7. `sumOfDigits(int n)` — returns the sum of all digits (e.g., 1234 → 10)
8. `reverseNumber(int n)` — returns the number reversed (e.g., 1234 → 4321)
9. `isArmstrong(int n)` — returns true if it's an Armstrong number (sum of cubes of digits equals the number, e.g., 153 = 1³ + 5³ + 3³)
10. `nthPrime(int n)` — returns the nth prime number (uses `isPrime`)

Create a menu-driven main method that lets the user pick which function to run:
```
=== Math Toolkit ===
1. Factorial
2. Prime Check
3. GCD
4. LCM
5. Fibonacci
6. Power
7. Sum of Digits
8. Reverse Number
9. Armstrong Check
10. Nth Prime
0. Exit
```

Use exception handling for all input. Format output with `printf`.

> 🎙️ The MathToolkit is a great study resource beyond just this course. Algorithms like factorial, Fibonacci, and prime checking show up in coding interviews and competitions. Build them all from scratch without looking up solutions -- the struggle of figuring out the logic is what makes you a stronger programmer.

---

### Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between a parameter and an argument?
2. Why does Java use pass-by-value? What would be different if it used pass-by-reference?
3. Why is it better to write many small methods that each do one thing than one large method that does everything?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Methods_in_Practice.md` containing:

1. Your pass-by-value observations from Part 2
2. Your answers to the reflection questions

> 💡 **Remember this one thing:** A well-designed method does exactly one thing, has a descriptive name that tells you what it does, and keeps its logic short enough to understand at a glance. When you find yourself writing a method that does multiple things, split it into smaller methods that each handle one piece -- this is how professional developers write maintainable code.

## Grading

> 🎯 **Teach:** How your research and hands-on work are evaluated across method fundamentals.
> **See:** Rubrics for the research essay, all four Java programs, and the reflection questions.
> **Feel:** Clear about what constitutes a complete, high-quality submission for this module.

> 🔄 **Where this fits:** Day 28 begins the methods section, teaching you how to write reusable, well-designed methods with proper parameters and return types -- the building blocks that make your classes and programs functional for the 1Z0-811 exam.

> 🎙️ You now know how to write methods with parameters and return types, you understand pass-by-value, and you can compose methods that call other methods. Tomorrow you will dive into getters and setters with validation, and static versus instance methods. Those concepts build directly on what you learned today, so make sure your method fundamentals are solid.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains what methods are with all parts of the signature | 30 |
| Accurately describes parameters vs. arguments and pass-by-value | 30 |
| Discusses method design best practices | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| `MethodBasics.java`: All 10 methods correct with demonstration | 20 |
| `PassByValueDemo.java`: All 4 scenarios with clear explanations | 20 |
| `MethodComposition.java`: Methods calling methods, string analysis | 15 |
| `MathToolkit.java`: All 10 functions with menu system | 25 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

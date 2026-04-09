# Day 28 Assignment: Describing and Creating Methods in Practice

## Overview

- **Topic:** Java Methods — Defining Methods, Parameters, Return Types, and Pass-by-Value
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Method anatomy

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

### void vs. return type

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

### Calling methods

```java
greet("Campbell");               // void — just call it
double avg = average(85, 92);    // return type — store the result
System.out.println(average(85, 92)); // or use it directly
```

### Pass-by-value

Java ALWAYS passes by value. For primitives, a copy is passed — the original can't change. For objects, a copy of the *reference* is passed — you can modify the object's contents but can't reassign the reference.

```java
public static void tryToChange(int x) {
    x = 999;  // Only changes the local copy
}

int num = 5;
tryToChange(num);
System.out.println(num);  // Still 5!
```

---

## Part 1: Method Fundamentals

### Program A: `MethodBasics.java`

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

---

## Part 2: Pass-by-Value

### Program B: `PassByValueDemo.java`

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

---

## Part 3: Methods That Call Methods

### Program C: `MethodComposition.java`

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

---

## Part 4: Practical Application

### Program D: `MathToolkit.java`

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

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between a parameter and an argument?
2. Why does Java use pass-by-value? What would be different if it used pass-by-reference?
3. Why is it better to write many small methods that each do one thing than one large method that does everything?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Methods_in_Practice.md` containing:

1. Your pass-by-value observations from Part 2
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `MethodBasics.java`: All 10 methods correct with demonstration | 20 |
| `PassByValueDemo.java`: All 4 scenarios with clear explanations | 20 |
| `MethodComposition.java`: Methods calling methods, string analysis | 15 |
| `MathToolkit.java`: All 10 functions with menu system | 25 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

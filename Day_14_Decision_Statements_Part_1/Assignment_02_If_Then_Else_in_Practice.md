# Day 14 Assignment: If-Then and If-Then-Else in Practice

## Overview

- **Topic:** Using Decision Statements — if, if-else, else-if chains, and nested ifs
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Basic if-then

```java
if (condition) {
    // runs only when condition is true
}
```

### if-then-else

```java
if (condition) {
    // runs when true
} else {
    // runs when false
}
```

### else-if chain

```java
if (condition1) {
    // first match wins
} else if (condition2) {
    // checked only if condition1 was false
} else if (condition3) {
    // checked only if condition1 and condition2 were false
} else {
    // default — none of the above matched
}
```

### Nested if

```java
if (outerCondition) {
    if (innerCondition) {
        // both conditions are true
    }
}
// Often equivalent to: if (outerCondition && innerCondition)
```

### Common Pitfall — the "dangling else"

```java
// Without braces, the else belongs to the NEAREST if
if (x > 0)
    if (x > 100)
        System.out.println("Big");
else
    System.out.println("This else belongs to the INNER if, not the outer!");
```

**Rule of thumb:** Always use braces, even for single-statement bodies.

---

## Part 1: Basic If-Else

### Program A: `BasicDecisions.java`

Write a program that demonstrates the fundamental forms of if statements. Use `Scanner` for input.

1. **Simple if:** Ask for a temperature. If it's above 100, print a heat warning.

2. **if-else:** Ask for a number. Print whether it's positive or negative. (Consider: what about zero?)

3. **if-else-if chain:** Ask for a test score (0-100) and assign a letter grade:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - Below 60: F
   Print the score and letter grade.

4. **Multiple independent ifs:** Ask for a person's age and print ALL that apply (not just the first match):
   - Under 13: "Child"
   - 13-17: "Teenager"
   - 18 or older: "Can vote"
   - 21 or older: "Can rent a car"
   - 65 or older: "Senior citizen"

   Add a comment explaining why these must be separate `if` statements (not else-if) since a 65-year-old should see "Can vote", "Can rent a car", AND "Senior citizen".

---

## Part 2: The Braces Trap

### Program B: `BracesDemo.java`

Write a program that demonstrates why omitting braces is dangerous:

1. **The dangling else problem:** Write this exact code and predict what it prints for `x = 5`:
   ```java
   int x = 5;
   if (x > 10)
       if (x > 20)
           System.out.println("Greater than 20");
   else
       System.out.println("What does this print?");
   ```
   Add a comment explaining which `if` the `else` actually belongs to, and why the output might surprise you.

2. **The accidental semicolon:** Predict what this prints:
   ```java
   int score = 85;
   if (score > 90);  // Notice the semicolon!
   {
       System.out.println("Excellent!");
   }
   ```
   Add a comment explaining why "Excellent!" prints even though 85 is not greater than 90.

3. **The multi-statement trap:** Predict the output:
   ```java
   int age = 15;
   if (age >= 18)
       System.out.println("You can vote.");
       System.out.println("Welcome to adulthood.");  // Is this inside the if?
   ```
   Add a comment explaining why the second line always prints.

4. **Rewrite all three** with proper braces so they behave as the programmer likely intended.

---

## Part 3: Nested Decisions

### Program C: `NestedDecisions.java`

Write a program that uses nested if statements for multi-level decision making. Use `Scanner` for input.

1. **Login simulator:** Ask for a username and password.
   - First check if the username is "admin"
     - If yes, check if the password is "secret123"
       - If yes: "Login successful! Welcome, administrator."
       - If no: "Incorrect password."
     - Else check if the username is "guest"
       - If yes: "Welcome, guest! Limited access granted."
     - Else: "Unknown user."

2. **Ticket pricing:** Ask for age and whether it's a weekday or weekend.
   - Children (under 12):
     - Weekday: $5
     - Weekend: $8
   - Adults (12-64):
     - Weekday: $10
     - Weekend: $15
   - Seniors (65+):
     - Weekday: $7
     - Weekend: $10
   Print the ticket price using `printf`.

3. **Refactored version:** Rewrite the ticket pricing using `&&` in else-if chains instead of nesting. Add a comment discussing which version is more readable.

---

## Part 4: Practical Application

### Program D: `TaxCalculator.java`

Write a simplified US tax bracket calculator using else-if chains. Use `Scanner` to get the filing status and income.

Filing statuses:
- Single
- Married

Tax brackets for Single:
| Income Range | Tax Rate |
|-------------|----------|
| $0 - $10,275 | 10% |
| $10,276 - $41,775 | 12% |
| $41,776 - $89,075 | 22% |
| $89,076 - $170,050 | 24% |
| Over $170,050 | 32% |

Tax brackets for Married:
| Income Range | Tax Rate |
|-------------|----------|
| $0 - $20,550 | 10% |
| $20,551 - $83,550 | 12% |
| $83,551 - $178,150 | 22% |
| $178,151 - $340,100 | 24% |
| Over $340,100 | 32% |

**Note:** This is a simplified version — real taxes use marginal rates. For this exercise, just apply the single rate for the bracket.

The program should:
1. Ask for filing status (validate using `equalsIgnoreCase()`)
2. Ask for annual income
3. Use nested logic: outer if for filing status, inner else-if chain for brackets
4. Calculate the tax amount
5. Print a formatted summary:
   ```
   === Tax Calculation ===
   Filing Status: Single
   Annual Income:  $75,000.00
   Tax Bracket:    22%
   Tax Owed:       $16,500.00
   After Tax:      $58,500.00
   ```

### Program E: `SeasonAndActivity.java`

Write a program that recommends activities based on multiple conditions. Use `Scanner` for input.

Collect:
- Month (1-12)
- Temperature (as an integer)
- Is it raining? (boolean)

Determine the season from the month:
- 12, 1, 2: Winter
- 3, 4, 5: Spring
- 6, 7, 8: Summer
- 9, 10, 11: Fall

Then use nested decisions to recommend an activity:
- **Winter:**
  - Below 32°F and not raining: "Go skiing!"
  - Below 32°F and raining/sleeting: "Stay inside with hot cocoa."
  - 32°F or above: "Take a winter walk."
- **Spring:**
  - Raining: "Visit a museum."
  - Not raining and above 60°F: "Go for a hike!"
  - Not raining and 60°F or below: "Explore a local coffee shop."
- **Summer:**
  - Above 90°F: "Go swimming!"
  - 70-90°F and not raining: "Have a picnic in the park."
  - Raining: "Catch a movie."
  - Below 70°F: "Perfect weather for a bike ride."
- **Fall:**
  - Not raining and above 50°F: "Go apple picking!"
  - Not raining and 50°F or below: "Visit a pumpkin patch."
  - Raining: "Cozy up with a good book."

Print the season, conditions, and recommendation using `printf`.

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between an `else if` chain and multiple separate `if` statements? When would you use each?
2. Why is it considered best practice to always use curly braces with if statements, even for single-line bodies?
3. When is nesting if statements better than using `&&` to combine conditions, and vice versa?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_If_Then_Else_in_Practice.md` containing:

1. Your predictions and explanations for the braces traps in Part 2
2. Your comparison of nested vs. flattened ticket pricing in Part 3
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `BasicDecisions.java`: All 4 scenarios working with proper logic | 15 |
| `BracesDemo.java`: All 3 traps identified with rewrites | 15 |
| `NestedDecisions.java`: Login, ticket pricing, and refactored version | 20 |
| `TaxCalculator.java`: Correct brackets, formatted output | 20 |
| `SeasonAndActivity.java`: All seasons and conditions handled | 15 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

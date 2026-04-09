# Module 18: Looping Statements Part 2

> 🏷️ When You're Ready

> 🎯 **Teach:** How to use while loops for condition-based repetition and do-while loops for guaranteed-first-execution patterns like input validation
> **See:** Sentinel-controlled loops, menu-driven programs, password limiters, and an ATM simulator using both loop types
> **Feel:** Clear on when to use while vs do-while and confident you can build interactive programs that loop until the user is done

> 🎙️ Today you learn the other two loop types in Java. While the for loop is perfect when you know how many times to repeat, the while loop handles situations where you keep going until a condition changes, and the do-while loop guarantees the body runs at least once before checking. These are the loops you use for input validation, menu systems, and processing data until a sentinel value signals stop.

> 🎙️ The for loop is perfect when you know you need exactly ten iterations. But what about a login screen where you keep asking until the password is correct? You have no idea how many attempts it will take. That is where while and do-while loops come in -- they repeat based on conditions, not counts.

## Research: while and do-while Loops

> 🎯 **Teach:** How while loops check conditions before executing and do-while loops guarantee at least one execution, plus how sentinel values control termination.
> **See:** A research assignment comparing while vs. do-while syntax, infinite loop risks, and sentinel-controlled patterns.
> **Feel:** Ready to explain when each loop type is the right choice before applying them in programs.

### Overview

- **Topic:** Using Looping Statements — while and do-while Loops
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is a while loop?** Explain its syntax and how it differs from a for loop. When is a while loop the better choice — specifically, when you don't know in advance how many times the loop should run? Walk through an example step by step.

2. **What is a do-while loop?** Explain its syntax and how it differs from a while loop. What does it mean that a do-while loop is "guaranteed to execute at least once"? When is this behavior useful?

3. **What are the risks of while and do-while loops?** Explain infinite loops — what causes them, how to recognize them, and how to prevent them. What is a sentinel value, and how is it used to control loop termination?

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_While_and_Do_While_Research.md` in this folder.

### Grading Criteria

| Criteria | Points |
|----------|--------|
| Clearly explains while loop syntax and when to use it over for | 30 |
| Accurately describes do-while and its "at least once" guarantee | 30 |
| Explains infinite loops, prevention, and sentinel values | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

> 🎙️ The key distinction to nail in your research is when the condition gets checked. While checks before the body runs, so it can skip entirely. Do-while checks after the body runs, so it always executes at least once. This one difference determines which loop you should use for any given problem.

> 💡 **Remember this one thing:** A while loop checks its condition before executing the body, so it can run zero times. A do-while loop checks its condition after executing the body, so it always runs at least once. This distinction is heavily tested on the exam.

## Hands-On: while and do-while Loops in Practice

> 🎯 **Teach:** How to use while loops for condition-based repetition and do-while loops for input validation, menus, and guaranteed-first-execution patterns.
> **See:** While and do-while fundamentals, sentinel-controlled data entry, loop type comparisons, and a full ATM simulator.
> **Feel:** Confident you can build interactive programs that loop until the user is done.

> 🎙️ Now you will build programs that use while and do-while loops for real tasks. You will see exactly when each loop type shines, use sentinel values to control data entry, and build a full ATM simulator that puts both loop types to work.

### Overview

- **Topic:** Using Looping Statements — while Loops, do-while Loops, and Sentinel-Controlled Loops
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

#### while loop

Checks the condition BEFORE each iteration — may run zero times:

```java
while (condition) {
    // body
}
```

#### do-while loop

Checks the condition AFTER each iteration — always runs at least once:

```java
do {
    // body
} while (condition);  // Note the semicolon!
```

#### When to use which

| Loop | Use when... |
|------|-------------|
| `for` | You know how many iterations in advance |
| `while` | You don't know how many iterations; condition checked first |
| `do-while` | You need at least one iteration before checking the condition |

#### Sentinel values

A **sentinel** is a special input value that signals the loop to stop:

```java
Scanner scanner = new Scanner(System.in);
int sum = 0;
System.out.println("Enter numbers (-1 to stop):");
int number = scanner.nextInt();
while (number != -1) {   // -1 is the sentinel
    sum += number;
    number = scanner.nextInt();
}
```

> 🎙️ That table comparing when to use each loop type is your decision guide. For loops when you know the count, while loops when you do not, and do-while when you need at least one execution. Keep this mental model and you will always pick the right loop.

---

### Part 1: while Loop Fundamentals

#### Program A: `WhileBasics.java`

Write a program that demonstrates the while loop in various forms:

1. **Count up with while:** Print numbers 1 through 10 using a while loop. Compare this side-by-side (in comments) with the equivalent for loop.

2. **Count down with while:** Print 10 through 1, then "Liftoff!"

3. **Condition-based termination:** Start with `int value = 1000;` and repeatedly divide by 2, printing each value, until the value reaches 0:
   ```
   1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0
   ```

4. **String processing with while:** Given a string, use a while loop and `indexOf()` to count and print the position of every space character:
   ```java
   String text = "The quick brown fox jumps over the lazy dog";
   ```
   ```
   Space found at index 3
   Space found at index 9
   Space found at index 15
   ...
   ```

5. **Zero iterations:** Demonstrate that a while loop can run zero times:
   ```java
   int x = 10;
   while (x < 5) {
       System.out.println("This never prints");
   }
   System.out.println("Loop skipped because condition was false from the start");
   ```

> 🎙️ The string processing exercise in item four is a clever use of while loops. You use indexOf to find each space, process it, then search for the next one starting after the last position. This search-and-advance pattern shows up constantly in real text processing.

---

### Part 2: do-while Loop Fundamentals

#### Program B: `DoWhileBasics.java`

Write a program that demonstrates the do-while loop:

1. **Guaranteed execution:** Show that do-while runs at least once even when the condition is immediately false:
   ```java
   int x = 10;
   do {
       System.out.println("This prints once even though x > 5");
   } while (x < 5);
   ```
   Contrast this with the equivalent while loop from Part 1 that runs zero times.

2. **Menu-driven input:** Display a menu and keep asking until the user makes a valid choice:
   ```java
   int choice;
   do {
       System.out.println("1. Play");
       System.out.println("2. Settings");
       System.out.println("3. Quit");
       System.out.print("Enter choice (1-3): ");
       choice = scanner.nextInt();
       if (choice < 1 || choice > 3) {
           System.out.println("Invalid! Try again.");
       }
   } while (choice < 1 || choice > 3);
   ```
   Add a comment explaining why do-while is perfect for input validation.

3. **Password attempt limiter:** Ask for a password (correct password is "java123"). Allow up to 3 attempts:
   ```
   Enter password: wrong
   Incorrect. 2 attempts remaining.
   Enter password: nope
   Incorrect. 1 attempt remaining.
   Enter password: java123
   Access granted!
   ```
   Use a do-while loop with TWO conditions: wrong password AND attempts remaining.

4. **Number guessing with do-while:** Generate a random number 1-20 and let the user guess until correct, using a do-while loop. Print how many guesses it took.

> 🎙️ Do-while is the natural choice for input validation and menus because you always need to show the menu or ask for input at least once before you can check whether the response is valid. If you tried to do this with a regular while loop, you would have to duplicate the prompt or initialize with a dummy value.

---

### Part 3: Sentinel-Controlled Loops

#### Program C: `SentinelLoops.java`

Write a program that uses sentinel values to control loop termination:

1. **Grade calculator:** Ask the user to enter exam scores one at a time. Enter `-1` to stop. Calculate and print:
   - Number of scores entered
   - Sum of all scores
   - Average score
   - Highest and lowest scores
   ```
   Enter score (-1 to stop): 88
   Enter score (-1 to stop): 92
   Enter score (-1 to stop): 76
   Enter score (-1 to stop): 95
   Enter score (-1 to stop): -1

   Scores entered: 4
   Sum: 351
   Average: 87.75
   Highest: 95
   Lowest: 76
   ```

2. **Word collector:** Ask the user to enter words one at a time. Enter "quit" to stop. Print:
   - Total number of words entered
   - The longest word
   - The shortest word
   - All words concatenated with spaces
   Use `equalsIgnoreCase()` to check the sentinel so "QUIT", "Quit", and "quit" all work.

3. **Running total calculator:** Ask the user for numbers continuously. After each number, print the running total. Enter `0` to stop:
   ```
   Enter number (0 to stop): 10
   Running total: 10
   Enter number (0 to stop): 25
   Running total: 35
   Enter number (0 to stop): -5
   Running total: 30
   Enter number (0 to stop): 0
   Final total: 30
   ```

> 🎙️ Sentinel values are a clean way to end a loop without knowing in advance how many items there will be. The key rule is that your sentinel must be a value that could never be valid data. Using negative one as a sentinel for test scores works because no real score is negative one. Choosing a bad sentinel leads to confusing bugs.

---

### Part 4: while vs. do-while Comparison

#### Program D: `WhileVsDoWhile.java`

Write the SAME program implemented both ways, to clearly show when the behavior differs:

1. **Input validation — getting a number between 1 and 10:**
   - Version A (while): Must initialize the variable to an invalid value first
   - Version B (do-while): Naturally asks at least once
   Add a comment explaining why do-while is cleaner for this pattern.

2. **Processing a counter from 5 down to 1:**
   - Version A (while)
   - Version B (do-while)
   Add a comment: do they produce the same output?

3. **When start condition is false — counter starts at 10, condition is < 5:**
   - Version A (while): How many times does the body execute?
   - Version B (do-while): How many times does the body execute?
   Add a comment explaining the critical difference.

4. **Exam-style prediction:** Predict the output of each before running:
   ```java
   // Version A
   int a = 5;
   while (a < 5) {
       System.out.println("while: " + a);
       a++;
   }
   System.out.println("a = " + a);

   // Version B
   int b = 5;
   do {
       System.out.println("do-while: " + b);
       b++;
   } while (b < 5);
   System.out.println("b = " + b);
   ```

> 🎙️ The comparison in item three is the most important one here. When the starting condition is false, the while loop runs zero times but the do-while loop still runs once. This is the exam question you will see -- they show you both loops with a condition that is already false and ask for the output. Now you know the answer.

---

### Part 5: Practical Application

#### Program E: `ATMSimulator.java`

Build an ATM simulator that uses both while and do-while loops appropriately:

1. **Login with do-while:** Ask for a 4-digit PIN. Allow up to 3 attempts. Lock the account after 3 failures.

2. **Main menu with do-while:** Show the menu and process choices until the user selects Exit:
   ```
   === ATM Menu ===
   1. Check Balance
   2. Deposit
   3. Withdraw
   4. Transaction History
   5. Exit
   ```

3. **Deposit with while validation:** Keep asking for a valid amount (positive, not exceeding $10,000 per transaction) using a while loop.

4. **Withdraw with while validation:** Keep asking for a valid amount (positive, not exceeding balance, must be a multiple of 20) using a while loop.

5. **Transaction history:** Track the last 10 transactions in a String array. Print them when requested.

6. **Exit confirmation with do-while:** "Are you sure? (yes/no)" — keep asking until valid input received.

Use `printf` for all currency formatting. Use String methods from Day 11 for input processing.

---

### Part 6: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the key difference between a while loop and a do-while loop? Give a real-world analogy.
2. What is a sentinel value? Why is it important to choose a sentinel that cannot be confused with valid data?
3. How do you prevent an infinite loop? What should you always check before writing a while loop?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_While_and_Do_While_in_Practice.md` containing:

1. Your predictions from Part 4
2. Your answers to the reflection questions

> 💡 **Remember this one thing:** Do-while is the natural choice for input validation and menu systems because you always need to ask the user at least once before you can check whether their input is valid.

> 🎙️ You now have all three loop types in your toolkit -- for, while, and do-while. Tomorrow you will complete the looping section by learning break and continue for fine-grained loop control, comparing all three loop types side by side, and building a text adventure game as the grand finale.

## Grading

> 🎯 **Teach:** How your research and hands-on work will be evaluated for the while and do-while module.
> **See:** Rubrics for the research essay and the five hands-on programs including the ATM simulator.
> **Feel:** Assured you understand the scoring criteria so you can polish your work before submitting.

> 🔄 **Where this fits:** Day 18 adds while and do-while loops to your toolkit, giving you all three loop types tested on the 1Z0-811 exam and preparing you for the loop comparison and capstone on Day 19.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains while loop syntax and when to use it over for | 30 |
| Accurately describes do-while and its "at least once" guarantee | 30 |
| Explains infinite loops, prevention, and sentinel values | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| `WhileBasics.java`: All 5 while loop demonstrations | 10 |
| `DoWhileBasics.java`: All 4 do-while demonstrations with input validation | 15 |
| `SentinelLoops.java`: All 3 sentinel patterns with correct tracking | 15 |
| `WhileVsDoWhile.java`: All 4 comparisons with predictions and explanations | 15 |
| `ATMSimulator.java`: Full simulator with appropriate loop types | 25 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

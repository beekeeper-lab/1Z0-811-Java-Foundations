# Module 23: Arrays and ArrayLists Part 2

> 🏷️ When You're Ready

> 🎯 **Teach:** How to use the ArrayList class to create dynamic, resizable collections, including all core methods, autoboxing with wrapper classes, and safe iteration patterns
> **See:** Programs that build interactive shopping lists, student rosters, and demonstrate the critical differences between ArrayList and array behavior
> **Feel:** Empowered by ArrayList's flexibility compared to fixed-size arrays, and aware of the key gotchas like the remove trap and concurrent modification

> 🎙️ Yesterday you learned that arrays are powerful but have one major limitation: their size is fixed at creation. Today you meet ArrayList, a class from the Java collections framework that grows and shrinks automatically as you add and remove elements. You will learn its essential methods, understand autoboxing with wrapper classes, and build real interactive applications with dynamic data.

> 🎙️ ArrayList is one of the most heavily tested topics on the 1Z0-811 exam. You need to know every method, the autoboxing rules, and the gotchas around removing elements. Today is packed, but every piece of it is directly useful for the exam.

## Research: The ArrayList Class

> 🎯 **Teach:** What ArrayList is, how it differs from arrays, and how autoboxing with wrapper classes works.
> **See:** A research assignment covering all core ArrayList methods, generic type syntax, and the objects-only limitation.
> **Feel:** Confident you can describe dynamic collections before building interactive applications with them.

### Overview

- **Topic:** Arrays and ArrayLists — Creating and Manipulating ArrayLists
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

### Instructions

Write a short research essay addressing the following:

1. **What is an ArrayList and how does it differ from an array?** Explain that ArrayList is a resizable, dynamic collection class from `java.util`. How does it solve the fixed-size limitation of arrays? What does it mean that ArrayList can only hold objects, not primitives — and what are wrapper classes (`Integer`, `Double`, `Boolean`) and autoboxing?

2. **What are the most important ArrayList methods?** Describe each of the following and what it returns:
   - `add(element)` — adds to the end
   - `add(index, element)` — inserts at a position
   - `get(index)` — retrieves an element
   - `set(index, element)` — replaces an element
   - `remove(index)` — removes by position
   - `remove(object)` — removes by value
   - `size()` — number of elements
   - `contains(object)` — checks for presence
   - `isEmpty()` — checks if empty
   - `clear()` — removes all elements

3. **What is the generic type syntax `<E>` (angle brackets)?** Explain why you write `ArrayList<String>` instead of just `ArrayList`, what type safety it provides, and what happens if you use a raw `ArrayList` without specifying a type.

### Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

### Submission

Save your completed essay as `Response_01_ArrayList_Research.md` in this folder.

> 💡 **Remember this one thing:** ArrayList can only hold objects, not primitives. When you write `ArrayList<Integer>` and add an `int`, Java automatically converts it to an `Integer` object through autoboxing. This is seamless but important to understand, especially when using `remove()` on an Integer list where index-based and value-based removal can be ambiguous.

## Hands-On: ArrayList in Practice

> 🎯 **Teach:** How to use every core ArrayList method, navigate autoboxing traps, and safely iterate while removing elements.
> **See:** Programs that build interactive shopping lists, student rosters, and demonstrate the remove-by-index versus remove-by-value ambiguity.
> **Feel:** Empowered by ArrayList's flexibility and aware of the key gotchas that appear on the exam.

> 🎙️ Time to put ArrayList through its paces. You will use every method, explore the autoboxing traps that show up on the exam, and build a fully interactive shopping list manager.

### Overview

- **Topic:** Arrays and ArrayLists — Creating, Manipulating, and Iterating ArrayLists
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

### Background

#### Creating an ArrayList

```java
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<>();   // Empty list of Strings
ArrayList<Integer> numbers = new ArrayList<>(); // Empty list of Integers (not int!)
```

#### Key methods

```java
names.add("Alice");           // Add to end → [Alice]
names.add("Bob");             // Add to end → [Alice, Bob]
names.add(1, "Charlie");      // Insert at index 1 → [Alice, Charlie, Bob]
names.get(0);                 // Returns "Alice"
names.set(0, "Anna");         // Replace → [Anna, Charlie, Bob]
names.remove(0);              // Remove by index → [Charlie, Bob]
names.remove("Bob");          // Remove by value → [Charlie]
names.size();                 // Returns 1
names.contains("Charlie");    // Returns true
names.isEmpty();              // Returns false
names.clear();                // Empty the list → []
```

> 🎙️ Notice how ArrayList methods use names like get, set, add, and remove instead of bracket notation. This is because ArrayList is a class with methods, not a built-in language feature like arrays. The exam will test whether you mix up the syntaxes -- remember, brackets are for arrays and method calls are for ArrayLists.

#### Autoboxing

ArrayList can't hold primitives — it uses wrapper classes. Java automatically converts between them:

```java
ArrayList<Integer> nums = new ArrayList<>();
nums.add(42);       // Autoboxing: int 42 → Integer.valueOf(42)
int val = nums.get(0); // Unboxing: Integer → int
```

#### Iterating

```java
// Standard for loop
for (int i = 0; i < names.size(); i++) {
    System.out.println(names.get(i));
}

// Enhanced for loop
for (String name : names) {
    System.out.println(name);
}
```

---

### Part 1: ArrayList Fundamentals

#### Program A: `ArrayListBasics.java`

Write a program that demonstrates every core ArrayList method:

1. **Create and populate:** Create an `ArrayList<String>` of fruit names. Add at least 6 fruits using `add()`.

2. **Print the list:** Print the entire list using `System.out.println(fruits)` — ArrayList has a built-in `toString()`. Then print each element individually using a for loop with indices.

3. **Access and modify:**
   - Get and print the first and last elements using `get()`
   - Replace the third element using `set()`
   - Print the size using `size()`

4. **Insert and remove:**
   - Insert a fruit at index 2 using `add(index, element)`
   - Print the list — notice everything shifts right
   - Remove a fruit by index using `remove(index)`
   - Remove a fruit by value using `remove(value)`
   - Print the list after each operation

5. **Search:**
   - Check if the list contains "Mango" using `contains()`
   - Find the index of a fruit using `indexOf()`
   - Check if the list is empty using `isEmpty()`

6. **Clear and check:** Clear the list and confirm it's empty.

> 🎙️ Take your time with Part 1 and make sure you try every method. The best way to remember what get, set, add, remove, contains, and size do is to call each one yourself and see the output. Do not just read the examples -- type them out and run them.

---

### Part 2: Autoboxing and Wrapper Classes

#### Program B: `AutoboxingDemo.java`

Write a program that demonstrates autoboxing, unboxing, and the wrapper classes:

1. **Autoboxing in action:** Add primitive values to ArrayLists of wrapper types:
   ```java
   ArrayList<Integer> ints = new ArrayList<>();
   ints.add(42);       // int → Integer (autoboxing)

   ArrayList<Double> doubles = new ArrayList<>();
   doubles.add(3.14);  // double → Double

   ArrayList<Boolean> bools = new ArrayList<>();
   bools.add(true);    // boolean → Boolean
   ```

2. **Unboxing in action:** Retrieve values and use them as primitives:
   ```java
   int value = ints.get(0);        // Integer → int (unboxing)
   double pi = doubles.get(0);     // Double → double
   boolean flag = bools.get(0);    // Boolean → boolean
   ```

3. **The `remove()` trap with Integer lists:** This is an exam topic:
   ```java
   ArrayList<Integer> nums = new ArrayList<>();
   nums.add(10);
   nums.add(20);
   nums.add(30);

   nums.remove(1);              // Removes element at INDEX 1 (removes 20)
   // nums.remove(Integer.valueOf(10)); // Removes the VALUE 10
   ```
   Demonstrate both forms and add comments explaining the ambiguity. Show how `Integer.valueOf()` forces removal by value.

4. **Null in an ArrayList:** Unlike arrays of primitives (which have default values), an ArrayList can hold `null`:
   ```java
   ArrayList<String> list = new ArrayList<>();
   list.add("Hello");
   list.add(null);
   list.add("World");
   System.out.println(list);        // [Hello, null, World]
   System.out.println(list.get(1)); // null
   // list.get(1).length();         // NullPointerException!
   ```

> 🎙️ The remove trap with Integer lists is a classic exam question. When you call remove(1) on an ArrayList of Integers, Java treats 1 as an index, not as the Integer value 1. To remove the value, you need to write remove(Integer.valueOf(1)). Make sure you understand why this ambiguity exists -- it is because remove is overloaded with both an int index version and an Object value version.

---

### Part 3: Iterating and Processing ArrayLists

#### Program C: `ArrayListIteration.java`

Write a program that demonstrates all the ways to iterate over an ArrayList:

1. **Standard for loop with index:**
   ```java
   ArrayList<String> colors = new ArrayList<>();
   // add colors...
   for (int i = 0; i < colors.size(); i++) {
       System.out.println(i + ": " + colors.get(i));
   }
   ```

2. **Enhanced for loop:**
   ```java
   for (String color : colors) {
       System.out.println(color);
   }
   ```

3. **Processing while iterating — the removal trap:** Demonstrate the problem of removing elements while iterating with an enhanced for loop:
   ```java
   // This will throw ConcurrentModificationException!
   ArrayList<Integer> nums = new ArrayList<>();
   nums.add(1); nums.add(2); nums.add(3); nums.add(4); nums.add(5);

   // BROKEN — uncomment to see the error:
   // for (int n : nums) {
   //     if (n % 2 == 0) {
   //         nums.remove(Integer.valueOf(n));
   //     }
   // }
   ```
   Show the fix — iterate backwards with a standard for loop:
   ```java
   for (int i = nums.size() - 1; i >= 0; i--) {
       if (nums.get(i) % 2 == 0) {
           nums.remove(i);
       }
   }
   ```
   Add a comment explaining why backwards iteration avoids index shifting problems.

4. **Building a new list from an old one:** Filter an ArrayList of integers to create a new ArrayList containing only even numbers. Use an enhanced for loop to read, and `add()` to build the new list.

5. **String processing:** Given an `ArrayList<String>` of mixed-case names, create a new list with all names converted to uppercase. Then create another with only names longer than 5 characters.

> 🎙️ The backwards iteration trick for removing elements is important to internalize. When you remove an element, everything after it shifts left. If you are going forwards, you skip the next element because it moved into the slot you just processed. Going backwards avoids this entirely because the shifting only affects indices you have already visited.

---

### Part 4: Practical Application

#### Program D: `ShoppingList.java`

Build an interactive shopping list manager using ArrayList and Scanner:

1. **Menu:**
   ```
   === Shopping List Manager ===
   1. Add item
   2. Remove item
   3. View list
   4. Check if item is on the list
   5. Sort list alphabetically
   6. Clear list
   7. Exit
   ```

2. **Add item:** Ask for the item name. Check if it's already in the list using `contains()` (case-insensitive — convert both to lowercase before comparing). If it is, warn the user; if not, add it.

3. **Remove item:** Ask for the item name. If it exists (case-insensitive search), remove it. Otherwise, print "Item not found."

4. **View list:** Print the list with numbering:
   ```
   Shopping List (5 items):
   1. Milk
   2. Bread
   3. Eggs
   4. Cheese
   5. Apples
   ```

5. **Check item:** Ask for an item and report if it's on the list.

6. **Sort alphabetically:** Use `java.util.Collections.sort(list)` to sort the list, then display it.

7. **Clear list:** Confirm before clearing ("Are you sure? yes/no").

Use a do-while loop for the menu and try-catch for input validation. Use String methods (`trim()`, `equalsIgnoreCase()`) for input processing.

#### Program E: `StudentRoster.java`

Build a student roster manager that stores students as formatted strings and demonstrates ArrayList processing:

1. **Add students:** Collect name and grade, store as formatted string: `"Campbell Reed: 92"`

2. **Display roster:** Print all students with numbering and `printf` formatting.

3. **Find student by name:** Search the ArrayList using a loop and `contains()` or `startsWith()`.

4. **Calculate class average:** Parse the grade from each string using `substring()` and `Integer.parseInt()`.

5. **Find honor roll:** Filter students with grades >= 90 into a new ArrayList and display them.

6. **Remove student:** Search by name, confirm, and remove.

Use exception handling for all user input. Format all output with `printf`.

> 🎙️ The ShoppingList and StudentRoster are the kind of programs that make ArrayList feel real. You are not just calling methods in isolation anymore -- you are building interactive applications where users add, remove, and search data. This is exactly how ArrayList is used in production Java applications.

---

### Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When would you choose an ArrayList over an array? When would an array be the better choice?
2. What is autoboxing, and why is it necessary for ArrayList?
3. Why can you remove elements while iterating backwards but not forwards?

---

### Submission

Save all `.java` files in this folder, along with a response file named `Response_02_ArrayList_in_Practice.md` containing:

1. Your observations on the `remove()` trap with Integers from Part 2
2. Your iteration trap findings from Part 3
3. Your answers to the reflection questions

> 💡 **Remember this one thing:** Never remove elements from an ArrayList while iterating forward with an enhanced for loop -- it throws a ConcurrentModificationException. Instead, iterate backwards with a standard for loop so that removing an element does not shift the indices of the elements you have not yet visited.

## Grading

> 🎯 **Teach:** How your research and hands-on work are evaluated across ArrayList concepts.
> **See:** Rubrics for the research essay, all five Java programs, and the reflection questions.
> **Feel:** Clear about what constitutes a complete, high-quality submission for this module.

> 🔄 **Where this fits:** Day 23 introduces ArrayList, the dynamic counterpart to arrays, completing your understanding of Java's two primary ways to store collections of data -- both are tested extensively on the 1Z0-811 exam.

> 🎙️ You now have two powerful tools for storing collections -- arrays and ArrayLists. Tomorrow you will compare them side by side, learn to convert between them, and build a capstone project that uses both. Knowing when to pick one over the other is a skill the exam tests, so get ready to put that decision-making into practice.

### Research Grading

| Criteria | Points |
|----------|--------|
| Clearly explains ArrayList vs. array, including wrapper classes and autoboxing | 30 |
| Accurately describes all listed ArrayList methods | 30 |
| Explains generic type syntax and type safety | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

### Hands-On Grading

| Criteria | Points |
|----------|--------|
| `ArrayListBasics.java`: All methods demonstrated with output | 10 |
| `AutoboxingDemo.java`: Autoboxing, unboxing, remove trap, and null shown | 15 |
| `ArrayListIteration.java`: All iteration styles and the removal trap | 20 |
| `ShoppingList.java`: Full interactive manager with all 7 menu options | 25 |
| `StudentRoster.java`: Roster with search, average, filtering, and removal | 15 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

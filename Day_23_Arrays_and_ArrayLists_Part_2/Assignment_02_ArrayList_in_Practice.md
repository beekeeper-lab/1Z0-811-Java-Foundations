# Day 23 Assignment: ArrayList in Practice

## Overview

- **Topic:** Arrays and ArrayLists — Creating, Manipulating, and Iterating ArrayLists
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Creating an ArrayList

```java
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<>();   // Empty list of Strings
ArrayList<Integer> numbers = new ArrayList<>(); // Empty list of Integers (not int!)
```

### Key methods

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

### Autoboxing

ArrayList can't hold primitives — it uses wrapper classes. Java automatically converts between them:

```java
ArrayList<Integer> nums = new ArrayList<>();
nums.add(42);       // Autoboxing: int 42 → Integer.valueOf(42)
int val = nums.get(0); // Unboxing: Integer → int
```

### Iterating

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

## Part 1: ArrayList Fundamentals

### Program A: `ArrayListBasics.java`

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

---

## Part 2: Autoboxing and Wrapper Classes

### Program B: `AutoboxingDemo.java`

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

---

## Part 3: Iterating and Processing ArrayLists

### Program C: `ArrayListIteration.java`

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

---

## Part 4: Practical Application

### Program D: `ShoppingList.java`

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

### Program E: `StudentRoster.java`

Build a student roster manager that stores students as formatted strings and demonstrates ArrayList processing:

1. **Add students:** Collect name and grade, store as formatted string: `"Campbell Reed: 92"`

2. **Display roster:** Print all students with numbering and `printf` formatting.

3. **Find student by name:** Search the ArrayList using a loop and `contains()` or `startsWith()`.

4. **Calculate class average:** Parse the grade from each string using `substring()` and `Integer.parseInt()`.

5. **Find honor roll:** Filter students with grades >= 90 into a new ArrayList and display them.

6. **Remove student:** Search by name, confirm, and remove.

Use exception handling for all user input. Format all output with `printf`.

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. When would you choose an ArrayList over an array? When would an array be the better choice?
2. What is autoboxing, and why is it necessary for ArrayList?
3. Why can you remove elements while iterating backwards but not forwards?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_ArrayList_in_Practice.md` containing:

1. Your observations on the `remove()` trap with Integers from Part 2
2. Your iteration trap findings from Part 3
3. Your answers to the reflection questions

## Grading Criteria

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

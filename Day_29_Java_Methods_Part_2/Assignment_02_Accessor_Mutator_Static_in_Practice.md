# Day 29 Assignment: Accessor, Mutator, and Static Methods in Practice

## Overview

- **Topic:** Java Methods — Getters, Setters, Static Methods, and Static vs. Instance
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Accessor (getter) and Mutator (setter)

```java
public class Product {
    private String name;
    private double price;

    // Accessor — returns the value
    public String getName() {
        return name;
    }

    // Mutator — sets the value with validation
    public void setPrice(double price) {
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative");
        }
        this.price = price;
    }
}
```

### Static methods

```java
public class MathUtils {
    // Static — belongs to the class, called with MathUtils.add()
    public static int add(int a, int b) {
        return a + b;
    }
}

// Called with the CLASS name, not an object:
int sum = MathUtils.add(5, 3);
```

### Static vs. instance rules

| | Static method | Instance method |
|---|---|---|
| Access static fields? | Yes | Yes |
| Access instance fields? | **No** | Yes |
| Use `this`? | **No** | Yes |
| How to call? | `ClassName.method()` | `object.method()` |
| Needs an object? | No | Yes |

---

## Part 1: Getters and Setters with Validation

### Create `UserAccount.java` and `UserAccountMain.java`

**`UserAccount.java`**

Private fields:
- `String username`
- `String email`
- `String password`
- `int age`
- `double accountBalance`
- `boolean isActive`

Write getters and setters for ALL fields with the following validation rules:

1. **`setUsername(String username)`:**
   - Must be 3-20 characters
   - Must start with a letter
   - Cannot contain spaces
   - If invalid, throw `IllegalArgumentException` with a descriptive message

2. **`setEmail(String email)`:**
   - Must contain exactly one "@"
   - Must contain at least one "." after the "@"
   - Cannot be empty

3. **`setPassword(String password)`:**
   - Must be at least 8 characters
   - Must contain at least one digit (loop through with `Character.isDigit()`)
   - Must contain at least one uppercase letter

4. **`getPassword()`:**
   - Should NOT return the actual password
   - Return a masked version: `"********"` (same length as the password)

5. **`setAge(int age)`:**
   - Must be between 13 and 120

6. **`setAccountBalance(double balance)`:**
   - Cannot be negative

7. **`setActive(boolean active)`:**
   - Simple setter, no validation needed

8. **Read-only field demonstration:** Add a `private final String accountId` that is set in the constructor and has a getter but NO setter. Explain in a comment why `final` fields shouldn't have setters.

**`UserAccountMain.java`**

1. Create a UserAccount with valid data — set every field
2. Print all fields using getters
3. Try setting invalid values for each validated field — wrap each in try-catch and show the error messages:
   ```
   Testing username "ab": IllegalArgumentException: Username must be 3-20 characters
   Testing email "invalid": IllegalArgumentException: Email must contain @
   Testing password "short": IllegalArgumentException: Password must be at least 8 characters
   ...
   ```
4. Show that `getPassword()` returns a masked version

---

## Part 2: Static Methods

### Create `StringUtils.java` and `ArrayUtils.java` and `UtilsMain.java`

**`StringUtils.java`** — a utility class with ONLY static methods:

1. `public static String capitalize(String s)` — capitalizes the first letter: `"hello"` → `"Hello"`
2. `public static String reverse(String s)` — reverses the string
3. `public static int wordCount(String s)` — counts words (split by spaces)
4. `public static String truncate(String s, int maxLength)` — truncates to maxLength and adds "..." if it was longer
5. `public static boolean isPalindrome(String s)` — checks if it reads the same forwards and backwards (ignore case)
6. `public static String repeat(String s, int times)` — repeats the string
7. `public static String mask(String s, int visibleChars)` — masks all but the last N characters: `mask("1234567890", 4)` → `"******7890"`

Add a **private constructor** to prevent instantiation:
```java
private StringUtils() {
    // Utility class — should not be instantiated
}
```
Add a comment explaining why utility classes have private constructors.

**`ArrayUtils.java`** — another static utility class:

1. `public static int sum(int[] arr)` — returns the sum
2. `public static double average(int[] arr)` — returns the average
3. `public static int max(int[] arr)` — returns the maximum
4. `public static int min(int[] arr)` — returns the minimum
5. `public static int[] reverse(int[] arr)` — returns a new reversed array
6. `public static boolean contains(int[] arr, int target)` — searches for a value
7. `public static String toString(int[] arr)` — returns `"[1, 2, 3]"` format

All methods should handle edge cases (null arrays, empty arrays) with validation.

**`UtilsMain.java`**

Demonstrate every method from both utility classes. Call them all using the CLASS name:
```java
String reversed = StringUtils.reverse("Hello");
int total = ArrayUtils.sum(new int[]{1, 2, 3, 4, 5});
```

Show that you CANNOT create an instance: `// new StringUtils()` → error.

---

## Part 3: Static vs. Instance

### Create `GameCharacter.java` and `GameMain.java`

**`GameCharacter.java`**

A class that uses BOTH static and instance members to demonstrate the difference:

**Instance fields (unique per character):**
- `private String name`
- `private int health`
- `private int attackPower`
- `private int level`
- `private int experiencePoints`

**Static fields (shared by ALL characters):**
- `private static int totalCharacters = 0`
- `private static int totalBattles = 0`
- `private static String gameVersion = "1.0"`

**Instance methods (operate on this character):**
- Getters and setters with validation
- `attack(GameCharacter target)` — reduces target's health by this character's attack power, increments `totalBattles`
- `heal(int amount)` — restores health up to a maximum
- `gainExperience(int xp)` — adds XP, levels up every 100 XP
- `isAlive()` — returns true if health > 0
- `displayStats()` — prints this character's stats

**Static methods (class-level operations):**
- `getTotalCharacters()` — returns how many characters exist
- `getTotalBattles()` — returns total battles fought across all characters
- `getGameVersion()` — returns the version
- `resetBattleCount()` — resets the battle counter
- `printGameStats()` — prints all static statistics

**Demonstrate the compile error:** Add a comment showing that a static method cannot access `this` or instance fields:
```java
// public static void broken() {
//     System.out.println(this.name);  // ERROR: cannot use 'this' in static context
//     System.out.println(name);       // ERROR: non-static field from static context
// }
```

**`GameMain.java`**

1. Create 4 characters with different stats
2. Show that static fields are shared:
   ```java
   System.out.println("Total characters: " + GameCharacter.getTotalCharacters());
   ```
3. Simulate several battles between characters
4. Show that `totalBattles` increases regardless of which characters fight
5. Level up characters through experience
6. Print individual stats AND game-wide stats
7. Show static methods called on the CLASS vs instance methods called on OBJECTS

---

## Part 4: Practical Application

### Create `Inventory.java` and `InventoryItem.java` and `InventoryMain.java`

**`InventoryItem.java`**

Well-encapsulated class with:
- Private fields: `name`, `category`, `quantity`, `price`, `reorderThreshold`
- Constructor with validation
- Getters and setters with validation (quantity >= 0, price >= 0)
- `getTotalValue()` — returns quantity * price
- `needsReorder()` — returns true if quantity <= reorderThreshold
- `toString()` — formatted summary

**`Inventory.java`**

Manages a collection of InventoryItems:
- Private field: `ArrayList<InventoryItem> items`
- Static field: `static int totalInventoriesCreated`

**Instance methods:**
- `addItem(InventoryItem item)` — adds with duplicate name check
- `removeItem(String name)` — removes by name
- `findItem(String name)` — returns the item or null
- `updateQuantity(String name, int newQuantity)` — uses setter validation
- `getItemsByCategory(String category)` — returns filtered ArrayList
- `getReorderList()` — returns ArrayList of items needing reorder
- `getTotalValue()` — sum of all items' total values
- `displayInventory()` — formatted table:
   ```
   ═══════════════════════════════════════════════════════════════
   Item                Category       Qty    Price      Total
   ───────────────────────────────────────────────────────────────
   Laptop              Electronics     15   $999.99   $14,999.85
   Mouse               Electronics    142    $24.99    $3,548.58  ⚠ REORDER
   Coffee Beans        Food            50     $12.99     $649.50
   ═══════════════════════════════════════════════════════════════
   Total Inventory Value: $19,197.93
   Items Needing Reorder: 1
   ```

**Static methods:**
- `getInventoriesCreated()` — returns count
- `compareInventories(Inventory a, Inventory b)` — prints which has more items and higher total value

**`InventoryMain.java`**

1. Create two Inventories (e.g., "Warehouse A" and "Warehouse B")
2. Add items to each
3. Display both inventories
4. Show reorder lists
5. Update quantities and show changes
6. Compare the two inventories using the static method
7. Demonstrate using both instance methods (on objects) and static methods (on the class)

---

## Part 5: Reflection Questions

Answer these briefly (1-2 sentences each):

1. Why should setters include validation instead of just directly assigning the value?
2. When should a method be static? Give a real-world example of a class that should only have static methods.
3. Why can't a static method access instance variables? What would go wrong if it could?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Accessor_Mutator_Static_in_Practice.md` containing:

1. Your validation test results from Part 1
2. Your static vs. instance observations from Part 3
3. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| `UserAccount`: All fields with validated getters/setters, masked password | 20 |
| `StringUtils` and `ArrayUtils`: All static methods with private constructor | 20 |
| `GameCharacter`: Static vs. instance clearly demonstrated, battles working | 20 |
| `Inventory/InventoryItem`: Full system with instance and static methods | 20 |
| Reflection questions answered accurately | 10 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

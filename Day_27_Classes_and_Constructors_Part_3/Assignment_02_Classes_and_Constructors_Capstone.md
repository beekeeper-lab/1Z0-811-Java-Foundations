# Day 27 Assignment: Classes and Constructors Capstone

## Overview

- **Topic:** Classes and Constructors — Composition, Full Class Design, and Comprehensive Capstone
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Background

### Composition — objects inside objects

A class can have fields that are other objects, creating a "has-a" relationship:

```java
public class Address {
    private String street;
    private String city;
    private String state;
    private String zip;
    // constructor, getters, toString...
}

public class Person {
    private String name;
    private Address homeAddress;  // Person "has an" Address

    public Person(String name, Address homeAddress) {
        this.name = name;
        this.homeAddress = homeAddress;
    }
}

// Usage:
Address addr = new Address("123 Main St", "Denver", "CO", "80202");
Person p = new Person("Campbell", addr);
```

### Overriding toString()

Every class can override `toString()` so `System.out.println(object)` prints something useful:

```java
@Override
public String toString() {
    return name + " (Age: " + age + ")";
}
```

---

## Part 1: Composition — Objects Inside Objects

### Create the following files: `Address.java`, `ContactInfo.java`, `Person.java`, `CompositionMain.java`

**`Address.java`**

Private fields:
- `String street`
- `String city`
- `String state`
- `String zipCode`

Constructors:
- Full constructor (all four fields)
- Two-arg constructor (city, state) — defaults street to "Unknown" and zip to "00000"

Methods:
- Getters and setters for all fields
- `getFullAddress()` — returns formatted string: `"123 Main St, Denver, CO 80202"`
- `toString()` — returns the same as `getFullAddress()`

**`ContactInfo.java`**

Private fields:
- `String phone`
- `String email`

Constructors:
- Full constructor (both fields with validation — phone not empty, email must contain "@")
- One-arg constructor (phone only) — defaults email to "not provided"

Methods:
- Getters and setters with validation
- `toString()` — returns formatted contact info

**`Person.java`**

Private fields:
- `String name`
- `int age`
- `Address homeAddress`   ← composition
- `ContactInfo contact`   ← composition

Constructors:
- Full constructor (all four fields)
- Three-arg constructor (name, age, address) — creates default ContactInfo
- Two-arg constructor (name, age) — creates default Address and ContactInfo

Methods:
- Getters and setters
- `displayFullProfile()` — prints name, age, full address, and contact info using the composed objects' methods
- `toString()` — summary line

**`CompositionMain.java`**

1. Create Address and ContactInfo objects separately
2. Pass them to Person constructors
3. Create Persons using each constructor overload
4. Call `displayFullProfile()` on each
5. Modify a Person's address through the getter: `person.getAddress().setCity("Seattle")` — show that changes propagate
6. Demonstrate that two Persons can share the same Address object (roommates) — change the address and show both are affected. Then discuss in a comment whether this is desirable.

---

## Part 2: Full Class Design from Scratch

### Create `MusicTrack.java` and `Playlist.java` and `MusicMain.java`

**`MusicTrack.java`**

Design a complete, well-encapsulated class from scratch. Private fields:
- `String title`
- `String artist`
- `String album`
- `int durationSeconds`
- `int playCount`
- `double rating` (0.0 to 5.0)

Constructors:
- Full constructor (title, artist, album, duration, rating) — validates all fields
- Three-arg constructor (title, artist, duration) — defaults album to "Single", rating to 0.0
- No-arg constructor — defaults to placeholder values

Methods:
- Getters for all fields
- Setters with validation for rating (0.0-5.0) and duration (> 0)
- `play()` — increments playCount by 1 and prints "Now playing: [title] by [artist]"
- `getDurationFormatted()` — returns duration as "M:SS" format (e.g., 215 seconds → "3:35")
- `isPopular()` — returns true if playCount > 100 or rating >= 4.0
- `toString()` — returns a formatted summary

**`Playlist.java`**

A class that CONTAINS MusicTracks — composition with a collection:

Private fields:
- `String name`
- `ArrayList<MusicTrack> tracks`
- `static int totalPlaylists = 0`

Constructors:
- Constructor with name — initializes an empty ArrayList
- Constructor with name and initial track array

Methods:
- `addTrack(MusicTrack track)` — adds if not already present (check by title and artist)
- `removeTrack(String title)` — searches and removes by title
- `getTrack(int index)` — returns the track at the index (with bounds checking)
- `getTotalDuration()` — sums all track durations and returns formatted string
- `getAverageRating()` — average rating across all tracks
- `getMostPlayed()` — returns the track with the highest play count
- `displayPlaylist()` — prints a formatted playlist:
   ```
   ╔══════════════════════════════════════════════════════════╗
   ║  Playlist: My Favorites (5 tracks)                      ║
   ╠══════════════════════════════════════════════════════════╣
   ║  #  Title                Artist          Duration  ★    ║
   ║  ─────────────────────────────────────────────────────  ║
   ║  1  Shape of You        Ed Sheeran       3:53    4.5   ║
   ║  2  Blinding Lights     The Weeknd       3:20    4.8   ║
   ║  ...                                                    ║
   ╠══════════════════════════════════════════════════════════╣
   ║  Total Duration: 18:45  |  Avg Rating: 4.3             ║
   ╚══════════════════════════════════════════════════════════╝
   ```
- `sortByRating()` — sorts tracks by rating (highest first). Implement a simple sort since MusicTrack doesn't implement Comparable.

**`MusicMain.java`**

1. Create at least 8 MusicTrack objects using different constructors
2. Simulate plays on several tracks (call `play()` multiple times)
3. Rate some tracks
4. Create two Playlists and add different tracks to each
5. Display both playlists
6. Find and display the most played track across all tracks
7. Show the total playlists created using the static counter

---

## Part 3: Classes and Constructors Capstone

### Create a multi-file application: `LibraryCatalog`

Build a library catalog system that is the capstone for the entire Classes and Constructors section (Days 25-27). This project uses EVERY concept from these three days.

**Create the following files:**

**`Author.java`**
- Private fields: `String name`, `String nationality`, `int birthYear`
- Two constructors: full and name-only
- Getters, `toString()`

**`LibraryBook.java`**
- Private fields: `String title`, `Author author` (composition), `String isbn`, `int yearPublished`, `int totalCopies`, `int availableCopies`, `String genre`
- Private static field: `static int totalBooksInSystem = 0`
- Three constructors with chaining:
  - Full constructor (all fields, validates ISBN is 13 characters)
  - Without available copies (defaults to totalCopies)
  - Title, author, and genre only (defaults for other fields)
- Methods:
  - `checkOut()` — decreases availableCopies (validates > 0)
  - `returnBook()` — increases availableCopies (validates not exceeding total)
  - `isAvailable()` — returns true if copies available
  - `getAvailabilityStatus()` — returns "Available (3 of 5)" or "All Checked Out"
  - Getters, `toString()`, `displayInfo()`

**`LibraryMember.java`**
- Private fields: `String name`, `int memberId` (auto-assigned from static counter), `ArrayList<LibraryBook> checkedOutBooks`, `int maxBooks` (default 5)
- Constructors: full constructor and name-only
- Methods:
  - `checkOutBook(LibraryBook book)` — validates member hasn't exceeded max, book is available
  - `returnBook(LibraryBook book)` — removes from member's list, updates book
  - `getCheckedOutCount()` — returns number of books currently checked out
  - `displayMemberInfo()` — formatted member card with checked-out book list

**`Library.java`**
- Private fields: `String name`, `ArrayList<LibraryBook> catalog`, `ArrayList<LibraryMember> members`
- Constructor: name only, initializes empty lists
- Methods:
  - `addBook(LibraryBook book)` — adds to catalog
  - `registerMember(LibraryMember member)` — adds to members
  - `searchByTitle(String keyword)` — returns ArrayList of matches
  - `searchByAuthor(String authorName)` — returns ArrayList of matches
  - `searchByGenre(String genre)` — returns ArrayList of matches
  - `displayCatalog()` — formatted table of all books with availability
  - `displayMembers()` — formatted table of all members
  - `getStatistics()` — prints total books, total members, most popular genre, books checked out vs. available

**`LibraryMain.java`**

1. Create the Library
2. Create at least 4 Authors
3. Create at least 10 LibraryBooks using different constructors
4. Add all books to the library
5. Create at least 3 LibraryMembers
6. Register all members
7. Simulate a series of checkouts and returns
8. Search by title, author, and genre
9. Display the full catalog
10. Display member info for each member
11. Print library statistics
12. Demonstrate error handling (try to check out an unavailable book, try to exceed member's max)

All output should be formatted with `printf`. All input validation should prevent crashes. Use every concept from Days 25-27:
- Private fields with getters/setters (Day 25)
- Instance, class, and local variables (Day 25)
- Multiple overloaded constructors with chaining (Day 26)
- `this` keyword (Day 26)
- Constructor validation (Day 26)
- Composition — objects containing objects (Day 27)
- Static fields for counters and totals (Days 25-26)
- ArrayList for collections of objects (Day 24 callback)

---

## Part 4: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is composition (the "has-a" relationship)? Give an example from your capstone project.
2. Why is it important for constructors to initialize objects to a valid state?
3. What happens if two objects share a reference to the same composed object? Is this always a problem?
4. Looking at Days 25, 26, and 27 — how has your understanding of classes and OOP changed since Day 3?

---

## Submission

Save all `.java` files in this folder, along with a response file named `Response_02_Classes_and_Constructors_Capstone.md` containing:

1. Your design decisions for the library catalog (why you organized the classes the way you did)
2. Your answers to the reflection questions

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Composition demo: Address, ContactInfo, Person working together | 10 |
| MusicTrack and Playlist: Full design with formatting and sorting | 20 |
| LibraryCatalog capstone: All 5 classes working together | 40 |
| Capstone uses all required concepts (private, constructors, chaining, composition, static, ArrayList) | 15 |
| Reflection questions answered accurately | 5 |
| All programs compile and run without errors | 10 |
| **Total** | **100** |

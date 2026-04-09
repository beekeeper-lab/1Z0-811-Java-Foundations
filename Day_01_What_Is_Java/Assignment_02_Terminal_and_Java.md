# Day 1 Assignment: Terminal Basics and Running Your First Java Program

## Overview

- **Topic:** Terminal Navigation and Compiling Java
- **Type:** Technical / Hands-On
- **Estimated Time:** 1.5 hours

## Part 1: Terminal Command Reference

Before you begin the exercises, familiarize yourself with the following terminal commands. These work on macOS, Linux, and Windows (via WSL or PowerShell).

| # | Command | Description | Example |
|---|---------|-------------|---------|
| 1 | `pwd` | Print the current working directory | `pwd` |
| 2 | `ls` | List files and folders in the current directory | `ls` or `ls -la` |
| 3 | `cd` | Change directory (move into a folder) | `cd my_folder` |
| 4 | `cd ..` | Move up one directory | `cd ..` |
| 5 | `mkdir` | Create a new directory | `mkdir projects` |
| 6 | `rmdir` | Remove an empty directory | `rmdir old_folder` |
| 7 | `rm` | Remove a file | `rm myfile.txt` |
| 8 | `rm -r` | Remove a directory and its contents | `rm -r old_project` |
| 9 | `touch` | Create an empty file | `touch notes.txt` |
| 10 | `nano` | Open a simple text editor in the terminal | `nano HelloWorld.java` |
| 11 | `cat` | Display the contents of a file | `cat HelloWorld.java` |
| 12 | `cp` | Copy a file | `cp file.txt backup.txt` |
| 13 | `mv` | Move or rename a file | `mv file.txt new_location/` |
| 14 | `clear` | Clear the terminal screen | `clear` |
| 15 | `javac` | Compile a Java source file | `javac HelloWorld.java` |
| 16 | `java` | Run a compiled Java program | `java HelloWorld` |

> **Note for Windows users:** If you are on Windows, use WSL (Windows Subsystem for Linux) or Git Bash. These commands work the same way. PowerShell equivalents exist but differ slightly.

---

## Part 2: Guided Exercises

Complete each step below **in order**. After each step, write down the command you used in the **Submission Log** at the end of this assignment.

### Exercise A: Setting Up Your Workspace

1. Open your terminal.
2. Use `pwd` to confirm your current location.
3. Navigate to your home directory using `cd ~`.
4. Create a new directory called `java_projects`.
5. Move into the `java_projects` directory.
6. Inside `java_projects`, create a subdirectory called `day_01`.
7. Move into the `day_01` directory.
8. Use `pwd` to confirm you are in `~/java_projects/day_01`.

### Exercise B: Creating Your First Java Program

9. Using `nano`, create a new file called `HelloWorld.java`.
10. Type the following program into nano exactly as shown:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("My name is Campbell Reed.");
        System.out.println("I am learning Java!");
    }
}
```

11. Save the file in nano (`Ctrl+O`, then `Enter`) and exit (`Ctrl+X`).
12. Use `cat` to display the contents of `HelloWorld.java` and verify it looks correct.
13. Compile the program using `javac HelloWorld.java`.
14. Use `ls` to confirm that a file called `HelloWorld.class` now exists. This is the compiled bytecode.
15. Run the program using `java HelloWorld`.

> You should see three lines of output printed to the terminal.

### Exercise C: Moving Files Around

16. Navigate up one directory (back to `java_projects`).
17. Create a new directory called `completed`.
18. Copy `day_01/HelloWorld.java` into the `completed` directory.
19. Navigate into `completed` and use `ls` to confirm the file is there.
20. Use `cat` to display the file contents and verify the copy.

### Exercise D: Cleanup

21. Navigate back to `java_projects`.
22. Create a temporary directory called `scratch`.
23. Move into `scratch` and create an empty file called `temp.txt` using `touch`.
24. Navigate back up to `java_projects`.
25. Remove the `scratch` directory and its contents using `rm -r`.
26. Use `ls` to confirm `scratch` is gone.

---

## Part 3: Reflection Questions

Answer these briefly (1-2 sentences each):

1. What is the difference between `javac` and `java`? Why are there two separate commands?
2. What file extension does Java source code use? What file extension does compiled Java bytecode use?
3. Why does the class name (`HelloWorld`) need to match the file name (`HelloWorld.java`)?

---

## Submission

### Command Log

Record every command you ran for each numbered step. Use the format below and save this file as `Response_02_Terminal_and_Java.md` in this folder.

```
Step 1:  [your command here]
Step 2:  pwd
Step 3:  cd ~
Step 4:  ...
...
Step 26: ...
```

### Reflection Answers

Include your answers to the three reflection questions at the bottom of your response file.

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct commands logged for all 26 steps | 40 |
| HelloWorld.java compiles and runs successfully | 25 |
| File copy and directory cleanup completed correctly | 15 |
| Reflection questions answered accurately | 20 |
| **Total** | **100** |

# Day 16 Assignment: Equality, Comparison, and Choosing the Right Decision Structure

## Overview

- **Topic:** Using Decision Statements — == vs .equals(), compareTo(), and Decision-Making Strategies
- **Type:** Written Research Assignment
- **Estimated Time:** 30 minutes
- **Target Length:** Approximately 3/4 page (300-400 words)

## Instructions

Write a short research essay addressing the following:

1. **How does `==` differ between primitives and objects?** Explain that `==` compares values for primitives but compares memory references for objects. Why does `==` sometimes return `true` for two String literals with the same content but `false` when one is created with `new`? Connect this to the String Pool concept from Day 8.

2. **What are `equals()` and `compareTo()` for Strings?** Explain what each method does:
   - `equals()` — returns `boolean`, checks if content is identical
   - `equalsIgnoreCase()` — same but case-insensitive
   - `compareTo()` — returns `int`, compares lexicographically (what do negative, zero, and positive return values mean?)

   When should you use each method?

3. **How do you choose the right decision structure?** Summarize when to use each:
   - A single `if` — one condition, one action
   - `if-else` — two mutually exclusive paths
   - `else-if` chain — multiple mutually exclusive conditions
   - `switch` — matching a single value against discrete options
   - Nested ifs — multi-level decision trees
   - Ternary operator — simple inline choice

## Requirements

- Your response should be approximately **3/4 of a page** (300-400 words).
- Write in your own words. Do not copy and paste from your sources.
- Include at least **3 references** to third-party sources (articles, documentation, books, etc.). List them at the end of your essay in a "References" section.
- Use proper grammar and complete sentences.

## Submission

Save your completed essay as `Response_01_Equality_and_Comparison_Research.md` in this folder.

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Accurately explains == for primitives vs. objects with String Pool connection | 30 |
| Describes equals(), equalsIgnoreCase(), and compareTo() with return values | 30 |
| Provides a clear guide for choosing the right decision structure | 20 |
| Writing quality and at least 3 properly cited references | 20 |
| **Total** | **100** |

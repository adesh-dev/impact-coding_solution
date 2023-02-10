# impact-coding_solution

Solution for finding the probability of missing your graduation day [Coding Problem Solution]

Problem Statement:

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

The number of ways to attend classes over N days.
The probability that you will miss your graduation ceremony. Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal.
Test cases:

for 5 days: 14/29 for 10 days: 372/773

Solution (Approach)

The approach is to find all the combinations for attending the classes and then subtracting the number of invalid ways to the total number of ways to attend the classes.

The probability to miss graduation is calculate by subtracting the invalid graduation days missed from the total number of graduation days missed divided by the total number of ways of attending classes over N days.

Test Case Output of the Code:

for 5 days: 14/29 for 10 days: 372/773 for 20 days: 263384/547337 for 25 days: 7008598/14564533

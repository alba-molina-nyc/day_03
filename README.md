# Day 03 - conditional statements, code blocks, scope, global, local

**a simple if else statement using comparison operators**

```python
height = int(input('please enter your height in cm'))
if height >= 120:
    print('you can ride the rollercoaster')
else:
    print('you cannot ride the rollercoaster')
```

**solution**
[roller_coaster](exercises/01_roller_coaster.py)

| Operator    | Meaning    |
| ------------- | ------------- |
| >         | greater than         |
| <           | less than        |
| >=          | greater than or equal to |
| <=          | less than or equal to |
| ==          | equal to |
| !=          | not equal to |

---

## Odd or Even Exercise

### Instructions

Write a program that works out whether if a given number is an odd or even number.

Even numbers can be divided by 2 with no remainder.

`e.g. 86 is even because 86 ÷ 2 = 43`

- 43 does not have any decimal places. Therefore the division is clean.

`e.g. 59 is odd because 59 ÷ 2 = 29.5`

- 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

The `modulo` is written as a `percentage sign (%) in Python`. It gives you the remainder after a division.

e.g.

6 ÷ 2 = 3 with no remainder.

6 % 2 = 0
5 ÷ 2 = 2 x 2 + 1, remainder is 1.

5 % 2 = 1
14 ÷ 4 = 3 x 4 + 2, remainder is 2.

14 % 4 = 2
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

**Example Input 1**
43
**Example Output 1**
This is an odd number.
**Example Input 2**
94
**Example Output 2**
This is an even number.
e.g. When you hit run, this is what should happen:



_Hint_
All even numbers can be divided by 2 with 0 remainder.
Try some using the modulo with some odd numbers e.g.

```3 % 2
5 % 2
7 % 2

Then try using the modulo with some even numbers e.g.

4 % 2
6 % 2
8 % 2
See what's in common each time.
```

**Test Your Code**
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-1-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

**Solution**
[odd_or_even](exercises/02_odd_or_even.py)

---

## Nested if /else

```python
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
```

**elif**

```python
if condition1:
    do A
elif condition2:
    do B
else:
    do this
```

[03_roller_coaster_2.0.py](exercises/03_roller_coaster_2.0.py)

[04_bmi_2.0.py](exercises/04_bmi_2.0.py)

---

### 💪This is a Difficult Challenge 💪

**Instructions**
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

```e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷ 4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)
```
Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

Example Input 1
2400
Example Output 1
Leap year.
Example Input 2
1989
Example Output 2
Not leap year.
e.g. When you hit run, this is what should happen:



**Hint**
Try to visualise the rules by creating a flow chart on www.draw.io
If you really get stuck, you can see the flow chart I created:
https://bit.ly/36BjS2D

**Test Your Code**
Before checking the solution, try copy-pasting your code into this repl:

https://repl.it/@appbrewery/day-3-3-test-your-code

This repl includes my testing code that will check if your code meets this assignment's objectives.

**Solution**

[leap_year](exercises/05_leap_year.py)

---

### Check multiple conditions in the same line of code 

and combining different conditions all in the same line of code

```python



```

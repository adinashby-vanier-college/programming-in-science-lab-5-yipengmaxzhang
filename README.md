[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IAZFwPPG)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18367460)
# Programming in Science - Lab 5

This template repository is the starter project for Programming in Science Lab 5. Written in Python, and tested with Pytest.

### Question(s) 

1. Write a function `hollow_square(n)` that returns a string representing a hollow square pattern of stars (`*`) with side length `n`.

#### Example (n = 5):
```
*****
*   *
*   *
*   *
*****
```
✅ **Hints:** Use a `while` loop and construct each line, appending them to a result string.

2. Write a function `number_pattern(n)` that returns a string representing a number pattern of height `n` **without using a `for` loop inside the print statement**.

#### Example (n = 4):
```
1
12
123
1234
```
✅ **Hints:** Use nested `while` loops to build the pattern.

3. Write a function `sum_of_natural_numbers(n)` that **returns the sum** of the first `n` natural numbers using a `while` loop.

#### Example:
For `n = 5`:
```
Sum = 1 + 2 + 3 + 4 + 5 = 15
```
✅ **Hints:** Use a counter variable and accumulate the total.

4. Write a function `centered_star_pyramid(n)` that returns a string representing a centered pyramid of stars (`*`) with height `n`.

#### Example (n = 4):
```
   *
  ***
 *****
*******
```
✅ **Hints:** Use spaces before stars to center the pyramid.

### Run Command

`pytest`
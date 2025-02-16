# Test Plan: Quadratic Equation Solver

## Overview

This document contains information about the unit testing course that I am covering at university. Outlined below are the tests with their expected results. 

## Test Cases

| ID | Description                     | Input (a, b, c) | Expected Output                       |  Status  |
|----|---------------------------------|-----------------|---------------------------------------|----------|
| 1  | Two distinct real roots         | (1, -3, 2)      | (2.0, 1.0)                            | positive |
| 2  | One real root                   | (1, 2, 1)       | (-1.0,)                               | positive |
| 3  | Complex roots                   | (1, 1, 1)       | (-0.5 ± 0.866j)                       | positive |
| 4  | Invalid input: a = 0            | (0, 2, 1)       | ValueError raised                     | positive |

## Question
A primary school teacher wants a computer program to test the basic arithmetic skills of her students. The program should generate a quiz consisting of random series of questions, using in each case any two numbers and addition, subtraction and multiplication. the system should ask the student's name, then ask 10 questions, output if the answer to each question is correct or not and produce a final score out of 10.

## Solution
Very simple solution. One function to ask a question which can then be used multiple times. There is a loop which calls the `generateQuestion` function the required number of times.

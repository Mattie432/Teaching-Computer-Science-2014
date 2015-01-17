## Question
The teacher wants to use the results from students taking these quizzes to log their performance. The systems shroud store the last three scores for each student. The teacher would like to be able to output the results of the quiz for a particular class, sorted:
1. in alphabetical order with each students highest score for the tests
2. by the highest score, highest to lowest
3. by the average score, highest to lowest

## Solution
The save result function was changed to only store the last 3 results of the pupil. It also appends the results to any existing ones and so keeps all of the results for a pupil on one line in the file.

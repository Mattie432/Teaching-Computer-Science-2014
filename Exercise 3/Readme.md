## Question
The teacher wants to use the results from students taking these quizzes to log their performance. The systems shroud store the last three scores for each student. The teacher would like to be able to output the results of the quiz for a particular class, sorted:
1. in alphabetical order with each students highest score for the tests
2. by the highest score, highest to lowest
3. by the average score, highest to lowest

## Solution
The save result function was changed to only store the last 3 results of the pupil. It also appends the results to any existing ones and so keeps all of the results for a pupil on one line in the file.

The results parser works by first asking for a class to display the results for. The file is then read and parsed into a list of tuples. Each tuple contains the pupils name, three test scores, the highest of the three scores and an average of their scores. This data is held in a global list for continued use.

The manipulation of the data can be done in the three ways expected. they all sort the data in situ and then print it out. This is using the inbuilt python list sort method with an anonymous lambda function to tell it which column to sort by.

The print method is generic and can be applied to any of the sorted data sets.

## Possible Additions
* could check that files exist before trying to open them `[easy]`
* could format the printed results with borders `[medium]`
* could implement own sorting algorithm `[hard]`

## Question
The teacher wants to keep track of the scores each member of the class obtains in the quiz. There are three classes in the school and the data should be kept separately for each class.

## Solution
The question does not say anything about the program having to read the file back so my solution only adds the save functionality.

Only addition was the `saveResults` method which takes the pupils name, class and score and appends it to a file. This means there are multiple entries for repeat students however this could be addressed by the pupils as an extension?

Possibly useful for pupils to know about global vars (for pupil name & class) though is not strictly necessary.

## Possible Additions
* check that the class entered is valid against previous records (e.g. 1,2 or 3) `[easy]`
* check that the name is a valid string (e.g. no numbers) `[medium]`
* append future scores to existing pupils rather than new line for each result `[hard]`

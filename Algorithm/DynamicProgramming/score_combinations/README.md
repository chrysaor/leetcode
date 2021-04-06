# Score Combinations

```
Given an array scoreEvents of possible score point amounts in a sports match and an integer amount finalScore (the final score of the game), 
return the total of possible unique score event arrangements that would result in the value of finalScore.
```

```
Example 1:

Input:
scoreEvents = [2,3,7]
finalScore = 12

Output: 4
Explanation:
There are 4 possible ways that the game ended with a final score of 12:
1.) [2, 2, 2, 2, 2, 2]
2.) [3, 3, 3, 3]
3.) [2, 2, 2, 3, 3]
4.) [2, 3, 7]


Example 2:

Input:
scoreEvents = [2,4,5]
finalScore = 9

Output: 2

Explanation:
There are 2 possible ways that the game ended with a final score of 9:
1.) [2, 2, 5]
2.) [4, 5]


Example 3:

Input:
scoreEvents = [4,5]
finalScore = 11

Output: 0
```
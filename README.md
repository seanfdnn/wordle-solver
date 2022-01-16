# A Python-Based Wordle Solver
This small Python application will solve Wordle puzzles.

To run:
```
python main.py
```

Example usage:
```

    Sean's Wordle Bot

    Respond reply with unmatched letters with an asterisk, "*",
    letters matched, but not in the correct position as lowercase,
    letters matched and in the correct position as uppercase.

    I.e.
        Guess:    PANIC
        Response  *anI*


 Next best guesses: ['LATER', 'ALTER', 'ALERT', 'AROSE', 'IRATE']

Guess:    LATER
Response: ***er

 Next best guesses: ['PROSE', 'SPORE', 'ROUSE', 'SCORE', 'SNORE']

Guess:    PROSE
Response: *r*sE

 Next best guesses: ['SHIRE', 'SURGE', 'SERVE']

Guess:    SHIRE
Response: SHIRE
Congratulations!
```
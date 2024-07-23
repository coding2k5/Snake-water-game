# Snake-water-gun game
Its a game in which you will play with computer. One input is given by you and other will be given by computer.

let s = snake, w = water and g = gun in comments.
Then use while loop and import random.
Take a variable named computer which will choice random from list of 0,1,-1.
Take another variable named youstr to input choice from user. Note - input must be s,w or g.
Take a dictionary named youdict assign s to 0, w to 1 and g to -1.
Take another dictionary named reversedict to reverse the input dictionary assign 0 to snake, 1 to water and -1 to gun.
Take a new variable named you which is equals to youdict of list youstr.
Print your's choice and computer's choice.
Now make the logic of the game.
If computer choose same as you then its draw. Otherwise use nested if else inside else.
elif comupter choose snake and you choose water, print you lose.
elif computer choose snake and you choose gun, print you won.
elif computer choose water and you choose snake, print you won.
elif computer choose water and you choose gun, print you lose.
elif computer choose gun and you choose snake, print you lose.
elif computer choose gun and you choose water, print you won.
Now in the last print "Invalid input" inside the else statement.



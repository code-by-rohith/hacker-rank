# Game Rules
#
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string .
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Sample Input
# BANANA
# Sample Output
# Stuart 12
# Note :
# Vowels are only defined as . In this problem,  is not considered a vowel.


def minion_game(s):
    n=len(s)
    count_of_starut=0
    count_of_kevin=0

    for i in range(n):
        if s[i] in 'AEIOU':
            count_of_kevin=count_of_kevin+(n-i)
        else:
            count_of_starut = count_of_starut + (n-i)

    if count_of_starut > count_of_kevin:
        print("stuart  "+str(count_of_starut))
    elif count_of_kevin < count_of_starut :
        print("kevin  "+str(count_of_kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)




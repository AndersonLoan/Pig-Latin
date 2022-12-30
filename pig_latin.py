# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 7-1
# Date: 1 10 22
#
word = input("Enter word(s) to convert to Pig Latin:\n")#acquires user's word(s)
y = word
word = word.split()#makes user input into a list
word3 = []
x = 0
vowels = ["a","e","i","o","u","y"]
print(f'In Pig Latin," {y}" is:',end = ' ')
for i in range(len(word)):#repeats for every word or phrase
    word2 = word[i]
    word3 = []
    for j in range(len(word2)):#checks every letter in the iterating word
                    for p in range(len(vowels)):#checks if the indiivdual letter is a vowel
                        if word2[j] == vowels[p]:
                            if word2[j] == word2[0]:#if the letter is a vowel and it's the first letter outputs said word with yay at the end
                                if(len(word3) <1):
                                    word3.append(word2[j])
                                    print(word2+ "yay",end = ' ')
                            elif word2[j] != word2[0]:#if the letter is a vowel but it isnt the first letter then it'll move all the previousletters behind the word and attach ay
                                if(len(word3) <1):
                                    x = j
                                    word3.append(word2[j])
                                    print(word2[x:len(word2)]+ word2[0:x] + "ay",end = ' ')
                
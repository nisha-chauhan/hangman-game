# from replit import clear
import random
from word_list import word_list
choosen_word=random.choice(word_list)
import logo
#cheeting
print(f"the random word is:{(choosen_word)}")
from logo import logo 
print(logo )
blank=[]
len= len(choosen_word)
for _ in range(len):
  blank+="_"
print(blank)
end_of_game=False
lives=6

while end_of_game!=True:
      
  guess=input("Guess a letter:\n").lower()
  
  if guess in blank:
    print(f"you already guessed this({guess})")
  for position in range(len):
    letter= choosen_word[position]
    if letter==guess:
      blank[position]=letter
  print(blank)
  if '_'not in blank:
    end_of_game=True
    print("you win")
    
  if guess not in choosen_word:
    print(f"you guesses({guess}) that's not in the word so loose a life")
    lives-=1
    if lives==0:
      end_of_game=True
      print("YOU LOOSE") 
      #Join all the elements in the list and turn it into a String.
  print(f"{''.join(blank)}")  
  
  from logo import stages
  print(stages[lives])       
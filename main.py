print('''
Key Details:
--------------
1) Rock: R
2) Paper: P
3) Scissor: S
----------0_0-------''')
import random

options = ['r','p','s']
options_inOBj = {'r':"Rock",'p':'Paper','s':'Scissor'}
score_file = open('score.txt','r+w')
score = score_file.read()
shoot = input("Enter a KEY: ").lower();

samantha = random.choice(options);

print(f'Your shoot {options_inOBj.get(shoot)} and samantha shoot {options_inOBj.get(samantha)}',end=": ")

if shoot == samantha:
    print("Ooo!! this is draw 😅");
else:
    if shoot == 'r' and samantha == 'p':
        print('Samantha win 🥳')
    elif shoot=='p' and samantha == 'r':
        score += 1;
        print('You Win 🥳 🚀');
    elif shoot == 's' and samantha == 'p':
        score += 1;
        print("You win 🥳🚀");
    elif shoot == 'p' and samantha == 's':
         print('Samantha win 🥳');
    elif shoot == 'r' and samantha == 's':
        score += 1;
        print("You win 🥳🚀");
    elif shoot=='s' and samantha == 'r':
        print('Samantha win 🥳');
    else:
        print("Someone did bad something 🪨  📜 ✂️")
        
print(score)
score_file.write(score)
score_file.close()
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
score_store = open('score.txt','r+')
shoot = input("Enter a KEY: ").lower();
pre_socre = int(score_store.read());
samantha = random.choice(options)

print(f"Your shoot {options_inOBj.get(shoot)} and samantha shoot {options_inOBj.get(samantha)} \n{f'Your higest score: {pre_socre}' if pre_socre != 0 else ''}",end='' if pre_socre == 0 else " ") # if {} else is same as JS -> ?:

if shoot == samantha:
    print("Ooo!! this is draw 😅");
else:
    if shoot == 'r' and samantha == 'p':
        print('Samantha win 🥳')
    elif shoot=='p' and samantha == 'r':
        pre_socre += 1;
        print('You Win 🥳 🚀');
    elif shoot == 's' and samantha == 'p':
        pre_socre += 1;
        print("You win 🥳🚀");
    elif shoot == 'p' and samantha == 's':
         print('Samantha win 🥳');
    elif shoot == 'r' and samantha == 's':
        pre_socre += 1;
        print("You win 🥳🚀");
    elif shoot=='s' and samantha == 'r':
        print('Samantha win 🥳');
    else:
        print("Someone did bad something 🪨  📜 ✂️")


score_store.seek(0) #Cursor move into beginning
score_store.write(str(pre_socre))

score_store.close()

print('''
Key Details:
--------------
1) Rock: R
2) Paper: P
3) Scissor: S
----------0_0-------''')

shoot = input("Enter a KEY: ").lower();

samantha = 'p'.lower()



if shoot == samantha:
    print("Ooo!! this is draw 😅");
else:
    if shoot == 'r' and samantha == 'p':
        print('Samantha win 🥳')
    elif shoot=='p' and samantha == 'r':
        print('You Win 🥳🚀');
    elif shoot == 's' and samantha == 'p':
        print("You win 🥳🚀");
    elif shoot == 'p' and samantha == 's':
         print('Samantha win 🥳');
    elif shoot == 'r' and samantha == 's':
        print("You win 🥳🚀");
    elif shoot=='s' and samantha == 'r':
        print('Samantha win 🥳');
    else:
        print("Someone did bad something 🐍🐍")
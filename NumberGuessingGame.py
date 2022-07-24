print("welcome to number guessing game");

number = 15
count=0

while count<7:
    guess_num=int(input('enter the number: '));
    if 0<guess_num<15:
        print('number is short');
    if guess_num>15:
        print('number is large');
    if guess_num%3==0 and guess_num<15:
        print(' the number is a multiple of 3 and  greater than 10');
    if guess_num==15:
        print('Hurrah! you won.');
        break;
    count+=1
    print("used", count, "chance and left with", 7-count , "chances");
    if count==6:
        print("You used all your chances and now game is over");
    continue    
                    
    
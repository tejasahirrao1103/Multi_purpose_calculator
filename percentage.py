def persent():

    note="""
hello!!!.. users your welcome to my percentage calculator guys.. :)
    """
    
    #print(art)
    print(note)

    while True:
        print("press enter to start")
        stop=input().lower().strip()
        if stop== 'q':
            print("thank you !!! ")
            break
        menu= """
seclect format from below

1.what is  X % of Y = ?
ex. 5% of 500 = 25

2. Y is X % of ? 
ex. 25 is 5% of 500

3. Y increase X % = ?
ex. 500 increase 5 % = 525

4. Y Decrese X % = ?
ex. 500 decrese 5 % = 475

NOTE :- 'x' --> is always '%' while input dont use '%' sign
        'Y' --> is non percentage value
 """
        
        print(menu)
        menusel=input()
        
        if menusel== '1':
            X=float(input("what is X % (enter persentage value e without '%'): "))
            Y=float(input("of Y : "))

        if menusel== '2':
            Y=float(input("Y is : "))
            X=float(input("X % of (enter persentage value e without '%') : "))

        if menusel== '3':
            Y=float(input(" Y increase : "))
            X=float(input("X % (enter persentage value e without '%'): "))

        if menusel== '4':
            Y=float(input("Y decrese : "))
            X=float(input("X % (enter persentage value e without '%'): "))


        def tone(x,y):
            c=(x/100)*y
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        def ttwo(x,y):
            c=y/x*100
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return
        
        def tthree(x,y):
            c=y*(1+x/100)
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return
            
        def tfour(x,y):
            c=y*(1-x/100)
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return
        
        if menusel == '1':
            tone(X,Y)

        if menusel == '2':
            ttwo(X,Y)

        if menusel == '3':
            tthree(X,Y) 

        if menusel == '4':
            tfour(X,Y)

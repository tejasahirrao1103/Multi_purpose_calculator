def arth():

    note="""
    hello!!!.. users your welcome to my arethmatic calculator guys.. :)

    instruction:

    for addition use -->> "+"
    for substraction use -->> "-"
    for multiplication use -->> "*"
    for division use -->> "/"
    """

    #print(art)
    print(note)

    while True:
        print("press enter to start")
        stop=input().lower().strip()
        if stop== 'q':
            print("thank you !!! ")
            break

        x=float((input("enter first no: "))) #num 1 = x
        oprator= (input("enter oprator: "))
        y=float(input("enter second no: ")) # num 2 = y


        def addition(a,b):
            c=a+b
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        def substraction(a,b):
            c=a-b
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        def multiplication(a,b):
            c=a*b
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        def division(a,b):
            c=a/b
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        if (oprator == '+'):
            addition(x,y)

        elif (oprator == '-'):
            substraction(x,y)

        elif(oprator == '*'):
            multiplication(x,y)

        else:
            division(x,y)
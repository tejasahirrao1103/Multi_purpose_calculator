def sqr():

    note="""
hello!!!.. users your welcome to my squre/squreroot calculator guys.. :)
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
seclect option from below

1. press 1 for squring
2. press 2 for squre root"""
        print(menu)
        menusel=input()
        z=float((input("enter first no: ")))


        def squreroot(a):
            c=a**0.5
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        def squre(a):
            c=a*a
            print("your ans is",c,"\n")
            print("for stop calculator press 'Q' ")
            return

        if menusel== '1':
            squre(z)
        else:
            squreroot(z)

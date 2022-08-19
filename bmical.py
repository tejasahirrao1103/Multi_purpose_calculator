def bmi():

    note="""
hello!!!.. users your welcome to my bmi calculator guys.. Let's Check Your helth :) 
    """
    
    #print(art)
    print(note)

    while True:
        print("press enter to start")
        stop=input().lower().strip()
        if stop== 'q':
            print("thank you !!! ")
            break
        
        hight= float(input("what is you hight buddy in cm: "))
        weight= float (input("Let's move toward your weight what is it: "))


        def bmio(w,h):
            bmi=w/h**2

            print("your BMI is: ", bmi,"\n")
            if bmi<18.5:
                print("Gain some.. You are Underweight")
            elif bmi>=18.5 and bmi<25:
                print('You are Normal')
            elif bmi>=25 and bmi< 30:
                print("ohh.. YOU are Overweight")
            else:
                print("You need to loos it.. You are Obesity")
                print("for stop calculator press 'Q' ")
            
            return
        
        bmio(weight,hight)

        
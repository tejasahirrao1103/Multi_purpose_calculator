import arithmatic
import sqr_t 
import percentage
import bmical

art = """
._ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _.
|                                 |
|     WELCOM TO MY CALCULATOR     |
|        BY TEJAS AHIRRAO         |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
"""

print(art)

menu= """
select option from below
1. Normal arithhmatic calculator (+,-,*,/)
2. Percentage calculator
3. squre and squre root clalculator
4. BMI Calculator
"""

print(menu)

menusel=int(input("please select calulator by index number: "))

if menusel == 1:
    arithmatic.arth()
if menusel== 2:
    percentage.persent()
if menusel == 3:
    sqr_t.sqr()
if menusel == 4:
    bmical.bmi()
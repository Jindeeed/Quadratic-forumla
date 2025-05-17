#Ask for equation
#Find each a,b and c
#Do quadratic formula
# ^2 for a square number


#split equation
#handle each 3 parts seperately and find coeffiecint
#combine them all together through quadratic formula to get answer

import re 


def main():
    equation = input("Please enter the equation \nUse ^2 for square:: ")
    
    equation_sect = equation.split()
    collect_equation(equation_sect)



def combine(equation_sect):
    combined_list = []
    i = 0
    while i < len(equation_sect):
        if equation_sect[i] in ['+','-'] and i + 1 < len(equation_sect):
                combine = equation_sect[i] + equation_sect[i+1]
                combined_list.append(combine)
                i += 2
        else:
            combined_list.append(equation_sect[i])
            i += 1
            
    return(combined_list)


def collect_equation(equation_sect):
    print(equation_sect)
    combined_list = combine(equation_sect)
    print(combined_list)

    a = combined_list[0]
    b = combined_list[1]
    c = combined_list[2]

    
    coeff_a  = find_coefficientXsqr(a)
    coeff_b = find_coefficientX(b)
    coeff_c = c

    print(coeff_a)
    print(coeff_b)
    print(coeff_c)

    calulcate(coeff_a,coeff_b,coeff_c)



def calulcate(coeff_a,coeff_b,coeff_c):
    a = float(coeff_a)
    b = float(coeff_b)
    c = float(coeff_c)

    x1 = ((-1*b) + (b.__pow__(2)-4*(a*c)).__pow__(1/2))/(2*a)
    x2 = ((-1*b) - (b.__pow__(2)-4*(a*c)).__pow__(1/2))/(2*a)

    print(f"X = {x1}\nX = {x2}")
   





def find_coefficientXsqr(a):
    search = re.match(r'^(-?\d*)x\^2',a)
    search = search.group(1)
    if search == "" or search == "+":
        coefficient = 1
    elif search == "-":
        coefficient = -1
    else:
         coefficient = int(search)
         
    return coefficient


def find_coefficientX(b):
    search = re.search(r"(-?\d+)(?=x)",b)
    search = search.group(1)
    if search == "" or search == "+":
        coefficient = 1
    elif search ==  "-":
        coefficient = -1
    else:
        coefficient = int(search)
    
    return coefficient




main()
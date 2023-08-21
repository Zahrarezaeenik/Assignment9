def add(frac_1, frac_2) :
    return {'s':(frac_1["s"] * frac_2["m"]) + (frac_2["s"] * frac_1["m"]) , 'm':frac_1["m"] * frac_2["m"]}

def multiply(frac_1,frac_2):
    return {'s':frac_1["s"] * frac_2["s"] , 'm':frac_1["m"] * frac_2["m"] }

def subtract(frac_1,frac_2):
    return {'s': (frac_1["s"] * frac_2["m"]) - (frac_2["s"] * frac_1["m"]) , 'm': frac_1["m"] * frac_2["m"]}

def divide(frac_1, frac_2) :
    return {'s':frac_1["s"] * frac_2["m"] , 'm':frac_1["m"] * frac_2["s"] }

def show(frac):
    print(f"{frac['s']}/{frac['m']} = {(frac['s'] / frac['m']):.4f}")

def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return int(input("Enter menu: "))

def frac_input(text,Condition=None):
    m=float(input(text))
    if m!=Condition:
        return m
    else:
        print("denominator cannot be zero.")
    return frac_input(text,Condition)

def main():
    print("fraction 1")
    frac_1={'s':frac_input("Enter num5erator of fraction:"),
            'm':frac_input("Enter denominator of fraction:",0)
    }
    print("fraction 2")
    frac_2={'s':frac_input("Enter numerator of fraction:"),
            'm':frac_input("Enter denominator of fraction:",0)
    }
    while True:
        print("=============")
        choice=menu()
        print("=============")
        if choice == 1:
            show(add(frac_1,frac_2))
        elif choice == 2:
            show(subtract(frac_1,frac_2))
        elif choice == 3:
            show(multiply(frac_1,frac_2))
        elif choice == 4:
            show(divide(frac_1,frac_2))
        elif choice==5:
            break
        else:
            print("input invalid!")

if __name__ == "__main__":
    main()
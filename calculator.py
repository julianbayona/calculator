number_one = int(input("digite el numero: "))
number_two = int(input("digite el numero: "))
option = int(input("1. sumar\n2. restar\n3. multiplicar\n4. dividir\n"))

if option==1:
    print(f"el resultado de la suma es: {number_one + number_two}" )
elif option == 2:
    print(f"el resultado de la resta es: {number_one - number_two}" )
elif option == 3:
    print(f"el resultado de la multiplicacion es: {number_one * number_two}" )

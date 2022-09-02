def divisors(num):
    assert num > 0, "Debes ingresar un numero positivo"
    divisors = [i for i in range(1,num+1) if num % i == 0]
    return divisors
  
    
    # try:
    #     if num <= 0:
    #         raise TypeError("Debes ingresar un numero positivo")
    # except TypeError as ve:
    #     print(ve)
    # return "escribie otro numero"  

    
def run():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
    except ValueError:
        print("Debes ingresar un numero")

    # assert num.isnumeric() and int(num)>0, 'Ingresa solo numeros positivos'
  
if __name__ == '__main__':
    run()
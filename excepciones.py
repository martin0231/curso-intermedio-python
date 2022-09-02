def palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    try:
        if len(string) == 0 or len(string) == 1:
            raise ValueError("La cadena tiene que ser de mas de 1 caracter")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
        


try:
    print(palindrome())
except TypeError:
    print("Solo se pueden ingresar strings")
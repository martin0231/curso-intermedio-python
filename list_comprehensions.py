import math

def run():

    list = []
    # for i in range(1, 101):
    #     a = i**2
    #     list.append(a)
    
    # print(list)

    # for i in range(1, 101):
    #     a = i**2
    #     if a % 3 != 0:
    #         list.append(a)
    # print(list)

    # list2 = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    # print(list2)


    dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(dict)

    dict2 = {i: round(math.sqrt(i), 2) for i in range(1, 1001)}
    print(dict2)

    array = [1,2,3,4,5]
    list = [i**2 for i in array if i % 2 == 0]
    print(list)

    def divisors(num):
        divisors = [i for i in range(1,num+1) if num % i == 1]
    
    print(divisors(6))

if __name__ == '__main__':
    run()
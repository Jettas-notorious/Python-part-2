def generator(n):
    list=[1,2,3,4,5]
    fibinacci_numbers=[1,1]# first two represent 1 and 2's fibonacci number

    for i in range(3,n+1):
        x=list[1+1]+list[i-2]
        fibinacci_numbers.append(x)
    print(list)#prints the list of numbers used
    print(fibinacci_numbers)#prints a list of each fibinacci number equavalent to its list[] number

generator(5)
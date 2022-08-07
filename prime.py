user_input = int(input("Enter a number: "))
print("--------------------------")
print(f"Prime numbers below {user_input} are")
def prime_num():
    num_of_prime=0
    sum = 0
    for a in range(2,user_input):
            for i in range(2,a):
                if a % i == 0:
                    break
            else:
                print(a)
                num_of_prime+=1
                sum += a
    average=sum/num_of_prime
    print("------------------------------------------")
    print(f"The number of prime numbers below {user_input} are {num_of_prime}")
    print("------------------------------------------")
    print("The sum of the prime numbers printed is",sum)
    print("------------------------------------------")
    print("The average of the prime numbers is",average)
    
prime_num()
    
        
    
                
        
                
                

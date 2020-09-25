from PrimeGenerator import PrimeNumberGenerator as p

def check_prime():
    print("========")
    x = input("input a number to check: ")
    if p.is_Prime(p,int(x)):
        print(x," is prime")
    else:
        print(x," is not prime")
    print("========")

def gen_primes():
    print("========")
    print("finding primes in range of..")
    x = input("input a number ")
    y = input("input another number ")
    vals = p.generate(p, int(x),int(y))
    print("the primes between ", x," and ",y, "are:")
    print(vals)
    print("========")

def console():
    while True:
        choice = input("Choose between:\n 1) check if a value is prime \n 2) generate all primes between 2 values \n choice: ")
        if choice == "1":
            check_prime()
        elif choice == "2":
            gen_primes()
        else: 
            print("error choose better please" )

console()
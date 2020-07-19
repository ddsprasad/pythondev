import pdb
#Method 1
def fact(num):
    # pdb.set_trace()
    result = 1
    for i in range(1,num+1):
        result *= i
    print(f"factorial of {num} is {result}")

fact(10)

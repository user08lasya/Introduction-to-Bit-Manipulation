def numberOfBits(n):
    count=0
    while(n):
        count += 1
        n >>= 1
    return count
number = int(input("Enter yor number : "))
print("Total bits: ",numberOfBits(number))

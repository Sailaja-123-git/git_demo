import random #for taking up the random module to the execution environment
input("press any key to generate otp/ secret code:")
secret_code = random.randrange(100000,999999)
otp = secret_code
print ("your otp is :",otp)
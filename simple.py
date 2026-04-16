def simple_interest(p,t,r):
  si = (p*t*r) / 100
  return si

principal=int(input("Enter the principal amount: "))
time=int(input("Enter the time period in years: "))
rate=int(input("Enter the rate of interest: "))

interest = simple_interest(principal,time,rate)
print("The simple interest is:", interest)
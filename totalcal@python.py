'''
wap to input thr yarly salary of a employ and hence calculate the income tax payable as per the given table
Salary                               Rate of tax
upto 2.5L                              nil      
2.5-5L                                 5% OF  AMT exceeding 2.5L   
5-10L                                  10% of AMT exceeding  5l+24000
10-15L                                 15% of amt exceeding 10L+94000 
>15L                                   20% OF amt EXCEEDING 15l + 1.5l
'''
sals = float(input("ENTER THE YEARLY SALARY:"))
amt = 0 

if sals<=250000:
    amt = 0 
elif sals<=500000:
    amt= 0.05 * (sals - 250000)
elif sals<=100000:    
    amt= .010* (sals - 500000) +24000 
elif sals<=150000:
    amt= 0.15* (sals-1000000)+94000
else:
    amt= 0.20* (sals - 1500000)+150000
print("INCOME TAX +" amt + 'on' + sals)

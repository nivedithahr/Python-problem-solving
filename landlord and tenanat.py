bill=input("Enter all bills to be shared separated with a comma\n")
a1=bill.split(",")
a2=[]
sum=0
n=int(input("Enter no. of tenants "))
n+=1
for i in range(len(a1)):
    print("Enter total amount for",a1[i],"bill ")
    a2.append(float(input()))
for i in range(len(a1)):
    sum+=round(a2[i]/n,2)
print("The",a1[i],"bill is split as",round(a2[i]/n,2),"per head")
print("\nThe total per head is",sum)
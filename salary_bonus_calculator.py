''' Salary Bonus Calculator:
Write a program that asks the user for their salary and years of service:

If the years of service are more than 5, give the user a bonus of 10% of their salary and print the new salary.
If the years of service are 5 or less, print the current salary with no bonus.
'''


salary = int(input("Enter your salary : "))
service = int(input("Enter your years of service : "))
if service > 5:
    bonus = salary *0.10
    new_salary = salary + bonus
    print(f"your bonus is 10 % of your salary. Your new salary is:{new_salary}")
else:
    print(f"No bonus. Your current salary is same :{salary}")


'''
Enter your salary : 5000
Enter your years of service : 7
your bonus is 10 % of your salary. Your new salary is:5500.0
PS D:\
Enter your salary : 3000
Enter your years of service : 3
No bonus. Your current salary is same :3000
'''
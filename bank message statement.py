savings_acct_balance=50000
print("welcome to hdfc bank")
print("insert your card")
name = "Nivetha shanmugam"
bank_acct_num ="XXXXXXXXXX4990"
withdrawelAmt =(int(input("enter the amt :")))
balance=savings_acct_balance - withdrawelAmt
branch_name=input("enter the branch name :")
import pytz
import datetime
ctime=pytz.timezone("asia/kolkata")
time=datetime.datetime.now(ctime)
statement = "Hi {1} you have withdrawn INR{0} from {3} hdfc branch and your current balance {4} in your bank account :{5} as of {2}"
print(statement.format(withdrawelAmt,name,time,branch_name,balance,bank_acct_num))
print("                                              Thank You                                                                                ")

# this program will keep track of the stocks
# Sam Cole
from Stack import Stack
from Queue import Queue
print("Are you using LIFO or FIFO for your stock portfolio?"
      "please type LIFO or FIFO exactly how you see them")
choice = input()

if choice == "LIFO":
    # this is the menu
    totalstock = Stack()
    totalmoney = Stack()
    profit = 0
    answer = 0
    allstocks = 0
    while answer != 5:
        print("""Please type the number to select what you would like to do
                1.buy stock
                2.sell stock
                3.see your profit
                4.see how many stocks
                5.close program""")
        answer = int(input())
        if answer == 1:
            print("How many stocks did you buy?")
            stock = int(input())
            allstocks = stock + allstocks
            print("How much was it per stock? please only the number")
            money = int(input())
            totalstock.push(stock)
            totalmoney.push(money)

        elif answer == 2:
            print("How much are you selling?")
            reqstock = int(input())
            allstocks = allstocks - reqstock
            print("For how much per stock? please only the number")
            money = int(input())
            oldstock = int(totalstock.pop())
            oldmoney = int(totalmoney.pop())
            profit = (money - oldmoney) * reqstock
            while reqstock > oldstock:
                reqstock = reqstock - oldstock
                oldstock = totalstock.pop()
            if reqstock < oldstock:
                oldstock = oldstock - reqstock
                totalstock.push(oldstock)
                totalmoney.push(oldmoney)

        elif answer == 3:
            print("Your profit is:")
            print("$" + str(profit))

        elif answer == 4:
            print(f"You have {allstocks} stocks in your portfolio")
if choice == "FIFO":
    # this is the menu
    totalstock = Queue()
    totalmoney = Queue()
    profit = 0
    answer = 0
    allstocks = 0
    while answer != 5:
        print("""Please type the number to select what you would like to do
                1.buy stock
                2.sell stock
                3.see your profit
                4.see how many stocks
                5.close program""")
        answer = int(input())
        if answer == 1:
            print("How many stocks did you buy?")
            stock = int(input())
            allstocks = allstocks + stock
            print("How much was it per stock? please only the number")
            money = int(input())
            totalstock.push(stock)
            totalmoney.push(money)

        elif answer == 2:
            print("How much are you selling?")
            reqstock = int(input())
            allstocks = allstocks - reqstock
            print("For how much per stock? please only the number")
            money = int(input())
            oldstock = int(totalstock.pop())
            oldmoney = int(totalmoney.pop())
            profit = (money - oldmoney) * reqstock
            while reqstock > oldstock:
                reqstock = reqstock - oldstock
                oldstock = totalstock.pop()
            if reqstock < oldstock:
                oldstock = oldstock - reqstock
                totalstock.push(oldstock)
                totalmoney.push(oldmoney)

        elif answer == 3:
            print("Your profit is:")
            print("$" + str(profit))

        elif answer == 4:
            print(f"You have {allstocks} stocks in your portfolio")

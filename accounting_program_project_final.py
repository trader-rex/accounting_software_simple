import xtry
import sqlite3


conn = sqlite3.connect('Balance sheet.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Balance_sheet(class, name, amount, description, date);")
cursor.execute("CREATE TABLE IF NOT EXISTS Profits_Expenses(class, name, amount, description, date);")
assets = {}
capital = {}
liabilities = {}
expenses = {}
profits = {}
Balance = True
print('Welcome to this simple accounting software which main purpose was to exercise coding skills.')
while Balance:
    answer = input('Would you like to propose an accounting event? Answer with " Yes" or " No": ')
    answer_affirmative = [' Yes', 'Yes', 'yes', ' yes', 'YES', ' YES']
    answer_negative = [' No', 'No', 'no', ' no', 'NO', ' NO']
    if answer in answer_affirmative:
        print('What kind of accounting event would you like to do? Choose from the Options menu.')
        balance_sheet = ['Assets', 'Capital', 'Liabilities']
        rdg = ['Profits', 'Expenses']
        balance_sheet_and_rdg = balance_sheet + rdg
        for i, element in enumerate(balance_sheet_and_rdg):
            print(i + 1, element)
        decision = int(input('Enter the number of your decision: ')) - 1
        if decision == 0:
            resultA = xtry.assets()
            print(resultA)
            for Key_Item, Value_ItemA in resultA.items():
                key_one = Key_Item[0]
                key_two = Key_Item[1]
                item_one = Value_ItemA[0]
                item_two = Value_ItemA[1]
                item_three = Value_ItemA[2]
                cursor.execute("""
                INSERT INTO Balance_sheet VALUES(?,?,?,?,?)
                """, (key_one, key_two, item_one, item_two, item_three))
                conn.commit()
                if Key_Item in assets.keys():
                    assets[Key_Item] += Value_ItemA
                else:
                    assets.update(resultA)
            print('All assets: ', assets)

        elif decision == 1:
            resultC = xtry.capital()
            print(resultC)
            for Key_Item, Value_ItemC in resultC.items():
                key_one = Key_Item[0]
                key_two = Key_Item[1]
                item_one = Value_ItemC[0]
                item_two = Value_ItemC[1]
                item_three = Value_ItemC[2]
                cursor.execute("""
                INSERT INTO Balance_sheet VALUES(?,?,?,?,?)
                """, (key_one, key_two, item_one, item_two, item_three))
                conn.commit()
                if Key_Item in capital.keys():
                    capital[Key_Item] += Value_ItemC
                else:
                    capital.update(resultC)
            print('All capital: ', capital)

        elif decision == 2:
            resultL = xtry.liabilities()
            print(resultL)
            for Key_Item, Value_ItemL in resultL.items():
                key_one = Key_Item[0]
                key_two = Key_Item[1]
                item_one = Value_ItemL[0]
                item_two = Value_ItemL[1]
                item_three = Value_ItemL[2]
                cursor.execute("""
                INSERT INTO Balance_sheet VALUES(?,?,?,?,?)
                """, (key_one, key_two, item_one, item_two, item_three))
                conn.commit()
                if Key_Item in liabilities.keys():
                    liabilities[Key_Item] += Value_ItemL
                else:
                    liabilities.update(resultL)
            print('All liabilities: ', liabilities)

        elif decision == 3:
            resultP = xtry.profits()
            print(resultP)
            for Key_Item, Value_ItemP in resultP.items():
                key_one = Key_Item[0]
                key_two = Key_Item[1]
                item_one = Value_ItemP[0]
                item_two = Value_ItemP[1]
                item_three = Value_ItemP[2]
                cursor.execute("""
                INSERT INTO Profits_Expenses VALUES(?,?,?,?,?)
                """, (key_one, key_two, item_one, item_two, item_three))
                conn.commit()
                if Key_Item in profits.keys():
                    profits[Key_Item] += Value_ItemP
                else:
                    profits.update(resultP)
            print('All profits: ', profits)

        elif decision == 4:
            resultE = xtry.expenses()
            print(resultE)
            for Key_Item, Value_ItemE in resultE.items():
                key_one = Key_Item[0]
                key_two = Key_Item[1]
                item_one = Value_ItemE[0]
                item_two = Value_ItemE[1]
                item_three = Value_ItemE[2]
                cursor.execute("""
                INSERT INTO Profits_Expenses VALUES(?,?,?,?,?)
                """, (key_one, key_two, item_one, item_two, item_three))
                conn.commit()
                if Key_Item in expenses.keys():
                    expenses[Key_Item] += Value_ItemE
                else:
                    expenses.update(resultE)
            print('All expenses', expenses)

    elif answer_negative:
        print('What do you want to do next?')
        choice = ['Terminate the program', 'Check the stats']
        for q, c in enumerate(choice):
            print(q + 1, c)
        choice_of_yours = int(input('Chose one number from the options above: '))
        if choice_of_yours == 1:
            conn.close()
            Balance = False
        elif choice_of_yours == 2:
            choice_2 = ['Balance sheet', 'Profits and expenses']
            for q, c in enumerate(choice_2):
                print(q + 1, c)
            choice_two = int(input('What do you want to check; Balance sheet or Profits and Expenses: '))
            if choice_two == 1:
                cursor.execute("select * from Balance_sheet;")
                conn.commit()
                rows = cursor.fetchall()
                print('Current state of balance sheet\n ')
                for row in rows:
                    print(row)
            elif choice_two == 2:
                cursor.execute("select * from Profits_Expenses;")
                conn.commit()
                rows = cursor.fetchall()
                print('Current state of profits and expenses\n ')
                for row in rows:
                    print(row)

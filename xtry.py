def assets():
    Assets = {}
    A_dict = {}
    keys_for_data = [('1', 'Current assets'), ('10', 'Cash'), ('12', 'Accounts receivable'), ('3', 'Inventory')]
    for k_options in keys_for_data:
        print(keys_for_data.index(k_options) + 1, k_options)
    k_dec = int(input('Choose from the options above: ')) - 1
    k = keys_for_data[k_dec]
    amount = int(input('Enter the amount: '))
    desc = input('Enter the description: ')
    date = input('Enter Today`s date: ')
    data = [amount, desc, date]
    value_data = []
    for element in data:
        value_data.append(element)
        if len(value_data) == 3:
            A_dict[k] = value_data
        Assets.update(A_dict)
    return Assets


def capital():
    Capital = {}
    C_dict = {}
    keys_for_data = [('9', 'Capital'), ('9', 'Retained Earnings')]
    for k_options in keys_for_data:
        print(keys_for_data.index(k_options) + 1, k_options)
    k_dec = int(input('Choose from the options above: ')) - 1
    k = keys_for_data[k_dec]
    amount = int(input('Enter the amount: '))
    desc = input('Enter the description: ')
    date = input('Enter Today`s date: ')
    data = [amount, desc, date]
    value_data = []
    for element in data:
        value_data.append(element)
        if len(value_data) == 3:
            C_dict[k] = value_data
        Capital.update(C_dict)
    return Capital


def liabilities():
    Liabilities = {}
    L_dict = {}
    keys_for_data = [('2', 'Short-Term Debt'), ('2','Long-Term Debt')]
    for k_options in keys_for_data:
        print(keys_for_data.index(k_options) + 1, k_options)
    k_dec = int(input('Choose from the options above: ')) - 1
    k = keys_for_data[k_dec]
    amount = int(input('Enter the amount: '))
    desc = input('Enter the description: ')
    date = input('Enter Today`s date: ')
    data = [amount, desc, date]
    value_data = []
    for element in data:
        value_data.append(element)
        if len(value_data) == 3:
            L_dict[k] = value_data
        Liabilities.update(L_dict)
    return Liabilities

def profits():
    Profits = {}
    P_dict = {}
    keys_for_data = [('7', 'Bussiness profits')]
    for k_options in keys_for_data:
        print(keys_for_data.index(k_options) + 1, k_options)
    k_dec = int(input('Choose from the options above: ')) - 1
    k = keys_for_data[k_dec]
    amount = int(input('Enter the amount: '))
    desc = input('Enter the description: ')
    date = input('Enter Today`s date: ')
    data = [amount, desc, date]
    value_data = []
    for element in data:
        value_data.append(element)
        if len(value_data) == 3:
            P_dict[k] = value_data
        Profits.update(P_dict)
    return Profits

def expenses():
    Expenses = {}
    E_dict = {}
    keys_for_data = [('7', 'Bussiness profits')]
    for k_options in keys_for_data:
        print(keys_for_data.index(k_options) + 1, k_options)
    k_dec = int(input('Choose from the options above: ')) - 1
    k = keys_for_data[k_dec]
    amount = int(input('Enter the amount: '))
    desc = input('Enter the description: ')
    date = input('Enter Today`s date: ')
    data = [amount, desc, date]
    value_data = []
    for element in data:
        value_data.append(element)
        if len(value_data) == 3:
            E_dict[k] = value_data
        Expenses.update(E_dict)
    return Expenses

def max_joltage(bank_number):
    bank = str(bank_number)
    first_pos = bank.index(max(bank[:-1]))
    second_pos = bank.index(max(bank[first_pos + 1 :]), first_pos + 1)
    return int(str(bank)[first_pos] + str(bank)[second_pos])

from collections import Counter

def lottery(table, number):
    freq_dict = Counter(table)
    return [key for key, value in freq_dict.items() if value == number]


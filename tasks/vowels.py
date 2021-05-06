# посчитать гласные в слове

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)  # если буквы нет в словаре то она инициализируется как ключ
        found[letter] += 1

for k, v in sorted(found.items()): # Цыкл перебора ключа и значения в отсортированом списке
    print(k, 'was found', v, 'time(s).')

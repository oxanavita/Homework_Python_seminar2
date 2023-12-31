# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input("Введите количество монет, лежащих на столе: "))
coins = input("Введите последовательность монеток (используйте 'T' для решки, 'H' для герба): ")
heads = 0
tails = 0

for coin in coins:
    if coin == 'H':
        heads += 1
    elif coin == 'T':
        tails += 1

flips_needed = min(heads, tails)
print(f"Минимальное количество монет, которые нужно перевернуть: {flips_needed}")
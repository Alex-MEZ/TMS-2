# Дан список целых чисел.
# Подсчитать сколько четных чисел в списке

arr = [i for i in range(1, 20)]
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(count)

print(arr)

h = float(input('Höjd? '))
i=0
while h > 0.01:
    h = h * 0.7
    i= i + 1
print(f'Den studsar {i} gånger')
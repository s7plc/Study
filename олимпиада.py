n = int(input('Enter cabins amount\n'))
x = int(input('Enter cabin number\n'))
y = (n - x) - x + 1
if n < x or x <= 0 or n <= 0:
    print('stupid combination')
elif y == 0:
    print("You reach your cabin")
elif y < 0:
    print(f"go backward {y * -1} cabins")
else:
    print(f'go forward {y} cabins')

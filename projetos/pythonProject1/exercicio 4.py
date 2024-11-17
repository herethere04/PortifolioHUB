print(f"{'Fahrenheit':^12} | {'Celsius':^12}")
print('-' * 27)

for f in range(45, 81):
    celsius = (5 * (f - 32)) / 9
    print(f"{f:^12.1f} | {celsius:^12.3f}")

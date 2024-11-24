def investment_value(P, r, n):
    V = P * (1 + r/n)**n
    return V

# Values of P, r, and n
P_values = list(range(1000, 11000, 1000))
r_values = [0.10 + i*0.01 for i in range(11)]
n_values = list(range(1, 11))

# Print header
print(f"{'P':<8} {'r':<8} {'n':<8} {'V':<10}")

# Print investment table
for P in P_values:
    for r in r_values:
        for n in n_values:
            V = investment_value(P, r, n)
            print(f"{P:<8} {r:<8.2f} {n:<8} {V:<10.2f}")
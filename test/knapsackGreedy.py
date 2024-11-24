

def functional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    remaining_capacity = capacity
    for weight, value in items:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += (value/weight)*remaining_capacity
            break
    return total_value


#list of item[weight, profit]
items = [(10, 60), (20, 100),(30, 120)]
knapsack_capacity = 50
max_value = functional_knapsack(items, knapsack_capacity)
print(max_value)

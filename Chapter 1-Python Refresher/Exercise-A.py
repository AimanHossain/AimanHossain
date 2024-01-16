# Outer loop for tables from 1 to 10
for i in range(1, 11):
    print(f"\nMultiplication table of : {i}")
    
    # Inner loop for multiples from 1 to 10
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

# Iterative Fibonacci with step counter
count = 0
n_terms = int(input("Enter Number of Terms: "))

if n_terms <= 0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n_terms):
        print(a)
        a, b = b, a + b
        count += 1  # Step count for each loop iteration

print(f"Steps required for iterative approach: {count}")

# Recursive Fibonacci with step counter
count = 0

def fibonacci_recursive(n):
    global count
    count += 1
    return n if n <= 1 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n_terms = int(input("\nEnter Number of Terms for recursive Fibonacci: "))

if n_terms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(n_terms):
        print(fibonacci_recursive(i))

print(f"Steps required for recursive approach: {count}")

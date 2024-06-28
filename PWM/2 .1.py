/*  main.py
 *  Создан: 27 мая 2024 г.
 *  Автор: Damir
*/
k_values = [i for i in range(10)]  # Example k values
m_values = [k**2 + 3*k + 5 for k in k_values]  # Example function: quadratic

# Step 2: Define the second-order polynomial equation
def polynomial(k, a, b, c):
    return a * k**2 + b * k + c

# Step 3: Implement a function to calculate the sum of squared residuals (SSR)
def sum_squared_residuals(a, b, c):
    return sum((polynomial(k, a, b, c) - m)**2 for k, m in zip(k_values, m_values))

# Step 4: Use a numerical method to find the coefficients that minimize the SSR
# For simplicity, we'll use a simple gradient descent approach
def gradient_descent(learning_rate, iterations):
    a, b, c = 0, 0, 0  # Initial guesses
    n = len(k_values)
    for _ in range(iterations):
        a -= learning_rate * (2/n) * sum((polynomial(k, a, b, c) - m) * k**2 for k, m in zip(k_values, m_values))
        b -= learning_rate * (2/n) * sum((polynomial(k, a, b, c) - m) * k for k, m in zip(k_values, m_values))
        c -= learning_rate * (2/n) * sum(polynomial(k, a, b, c) - m for k, m in zip(k_values, m_values))
    return a, b, c

# Find the coefficients that minimize the SSR
learning_rate = 0.0001
iterations = 10000
a, b, c = gradient_descent(learning_rate, iterations)

# Step 5: Use the polynomial equation to approximate m for any given k
k_test = 7
m_approx = polynomial(k_test, a, b, c)
print(f"The polynomial approximation of m at k = {k_test} is: {m_approx}")
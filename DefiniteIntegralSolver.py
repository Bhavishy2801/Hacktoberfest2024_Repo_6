def trapezoidal_rule(func, a, b, n):
    """
    Calculate the definite integral of func from a to b using the trapezoidal rule.

    Parameters:
    func : callable
        The function to integrate.
    a : float
        The lower limit of integration.
    b : float
        The upper limit of integration.
    n : int
        The number of subintervals.

    Returns:
    float
        The approximate value of the definite integral.
    """
    h = (b - a) / n  # Width of each subinterval
    integral = 0.5 * (func(a) + func(b))  # Initialize with the first and last terms

    # Sum the middle terms
    for i in range(1, n):
        integral += func(a + i * h)

    integral *= h  # Multiply by the width of the subintervals
    return integral

def definite_integral_solver():
    # Define the function to integrate
    def func(x):
        return eval(func_input)  # Evaluate the function input as a Python expression

    # Get user input for the function and limits
    global func_input
    func_input = input("Enter the function to integrate (in terms of x, e.g., x**2, sin(x), etc.): ")
    lower_limit = float(input("Enter the lower limit of integration: "))
    upper_limit = float(input("Enter the upper limit of integration: "))
    n = int(input("Enter the number of subintervals (e.g., 1000): "))

    # Calculate the definite integral
    integral_value = trapezoidal_rule(func, lower_limit, upper_limit, n)

    # Display the result
    print(f"\nThe approximate value of the definite integral of {func_input} from {lower_limit} to {upper_limit} is: {integral_value}")

# Run the solver
if __name__ == "__main__":
    definite_integral_solver()

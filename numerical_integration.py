import math

def numerical_integration(lower, upper, N):
    """
    Compute numerical integration of abs(sin(x)) between lower and upper
    using a simple rectangle method.
    """
    step = (upper - lower) / N
    area = 0.0
    for i in range(N):
        x = lower + i * step
        area += abs(math.sin(x)) * step
    return area

def main():
    # Example usage:
   

    lower = 0
    upper = 3.14159

    for N in [10, 100, 1000, 10_000, 100_000, 1_000_000]:
        result = numerical_integration(lower, upper, N)
        print(f"N={N} -> {result}")

if __name__ == "__main__":
    main()

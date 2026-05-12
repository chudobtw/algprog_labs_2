import math

def calculate_max_wire_length(w: int, heights: list[int]) -> float:
    n = len(heights)
    if n <= 1:
        return 0.0

    dp_1 = 0.0
    dp_h = 0.0

    for i in range(1, n):
        prev_h1 = 1
        prev_h2 = heights[i - 1]

        curr_h1 = 1
        curr_h2 = heights[i]

        dist_1_to_1 = math.sqrt(w**2 + (prev_h1 - curr_h1) ** 2)
        dist_h_to_1 = math.sqrt(w**2 + (prev_h2 - curr_h1) ** 2)

        new_dp_1 = max(dp_1 + dist_1_to_1, dp_h + dist_h_to_1)

        dist_1_to_h = math.sqrt(w**2 + (prev_h1 - curr_h2) ** 2)
        dist_h_to_h = math.sqrt(w**2 + (prev_h2 - curr_h2) ** 2)

        new_dp_h = max(dp_1 + dist_1_to_h, dp_h + dist_h_to_h)

        dp_1 = new_dp_1
        dp_h = new_dp_h

    # Повертаємо чисте значення, форматування до 2 знаків робить print або unittest
    return max(dp_1, dp_h)

def main():
    w = int(input("Введіть відстань між стовпами: "))
    heights_str = input("Введіть висоти стовпів через пробіл: ").split()
    heights = [int(h) for h in heights_str]

    ans = calculate_max_wire_length(w, heights)
    print(f"Максимальна довжина дроту: {ans:.2f}")

if __name__ == "__main__":
    main()
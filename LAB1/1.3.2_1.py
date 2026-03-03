def get_employees_input():
    employees = []
    print("Введіть дані працівників (Enter замість імені для зупинки)")
    
    while True:
        first_name = input("ІМ'Я: ")
        if first_name == '':
            break
        last_name = input("ПРІЗВИЩЕ: ")
        
        while True:
            try:
                rating = float(input("РЕЙТИНГ: "))
                break
            except ValueError:
                print("Будь ласка, введіть число") 
                
        employees.append({
            'first_name': first_name,
            'last_name': last_name,
            'rating': rating
        })
        print("---")
    return employees

def find_unsorted_part(employees):
    n = len(employees)
    if n <= 1: return (-1, -1)

    nums = [emp['rating'] for emp in employees]

    left = 0 
    while left < n - 1 and nums[left] <= nums[left + 1]:
        left += 1
    
    if left == n - 1: return (-1, -1)

    right = n - 1
    while right > 0 and nums[right] >= nums[right - 1]:
        right -= 1

    unsorted_slice = nums[left:right + 1]
    unsorted_min = min(unsorted_slice)
    unsorted_max = max(unsorted_slice)

    while left > 0 and nums[left - 1] > unsorted_min: left -= 1 
    while right < n - 1 and nums[right + 1] < unsorted_max: right += 1

    return (left, right)

def quick_sort_employees(arr):

    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]['rating']
    
    left = [x for x in arr if x['rating'] < pivot]
    middle = [x for x in arr if x['rating'] == pivot]
    right = [x for x in arr if x['rating'] > pivot]
    
    return quick_sort_employees(left) + middle + quick_sort_employees(right)

def print_table(employees):
    print("-" * 50)
    print(f"| {'NAME':<12} | {'SURNAME':<15} | {'RATING':<11} |")
    print("-" * 50)
    for emp in employees:
        print(f"| {emp['first_name']:<12} | {emp['last_name']:<15} | {emp['rating']:<11.1f} |")
    print("-" * 50)

def main():
    employees = get_employees_input()
    
    if not employees:
        print("Список порожній")
        return

    left, right = find_unsorted_part(employees)

    if left == -1 and right == -1:
        print("\nВЖЕ ВІДСОРТОВАНО!")
    else:
        print(f"\nЗнайдено невідсортовану частину: від індексу {left} до {right}.")
        print("Сортуваня...")
        
        part_to_sort = employees[left:right + 1]
        
        sorted_part = quick_sort_employees(part_to_sort)
        
        employees[left:right + 1] = sorted_part

    print("Фінальний результат:")
    print_table(employees)

if __name__ == '__main__':
    main()
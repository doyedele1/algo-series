from collections import deque

def parse_input(file_content):
    test_cases = []

    for line in file_content.strip().split('\n'):
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        test_cases.append((test_value, numbers))
    return test_cases

def can_perform_operations(numbers, test_value):
    count_of_operators_needed = len(numbers) - 1
    q = deque([(numbers[0], 0)])
    visited = set([(numbers[0], 0)])

    while q:
        result, index = q.popleft()

        if index == count_of_operators_needed:
            if result == test_value:
                return True
            # If result != test_value, we skip the rest of the loop and continue to the next iteration
            continue

        next_number_to_process = numbers[index + 1]
        new_states = [
            (result + next_number_to_process, index + 1),
            (result * next_number_to_process, index + 1),
            (int(f"{result}{next_number_to_process}"), index + 1)
        ]

        for state in new_states:
            if state not in visited:
                visited.add(state)
                q.append(state)
    
    return False

def is_valid_equation(test_value, numbers):
    return can_perform_operations(numbers, test_value)

def calculate_total_calibration_sum(test_cases):
    total = 0
    for test_value, numbers in test_cases:
        if is_valid_equation(test_value, numbers):
            total += test_value
    return total

def main():
    with open("input.txt", "r") as file:
        file_content = file.read()

    test_cases = parse_input(file_content)
    result = calculate_total_calibration_sum(test_cases)
    print(result)

if __name__ == "__main__":
    main()
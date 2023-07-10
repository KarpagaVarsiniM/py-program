numbers = input("Enter the list of numbers, separated by commas: ")
numbers = [int(num) for num in numbers.split(",")]

element = int(input("Enter the element to be found: "))

positive_indices = []
negative_indices = []

occurrence_count = numbers.count(element)

if occurrence_count > 0:
    for i in range(len(numbers)):
        if numbers[i] == element:
            positive_indices.append(i)
            negative_indices.append(i - len(numbers))
    
    print("Element", element, "occurs", occurrence_count, "times in the list.")
    print("Positive Index:", ", ".join(str(idx) for idx in positive_indices))
    print("Negative Index:", ", ".join(str(idx) for idx in negative_indices))
else:
    print("Element", element, "is not present in the list.")

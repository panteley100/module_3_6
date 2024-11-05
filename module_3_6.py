data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum (data):
    all_sum = 0
    all_length = 0
    result = all_sum + all_length

    if isinstance(data, (list, tuple, set)):
        for item in data:
            sum, length = calculate_structure_sum(item)
            all_sum += sum
            all_length += length
            #result += sum_
            #result += length_
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_key, length_key = calculate_structure_sum(key)
            sum_value, length_value = calculate_structure_sum(value)
            all_sum += sum_key + sum_value
            all_length += length_key + length_value
    elif isinstance(data, str):
        all_length += len(data)
    elif isinstance(data, int):
        all_sum += data

    return all_sum, all_length
result = calculate_structure_sum (data_structure)

print (sum(result))

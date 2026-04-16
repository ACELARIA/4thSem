def count_matching_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

strings_list = ['abbba', 'xybdmz', 'cvnhf', 'aba', '1221']
matching_strings_count = count_matching_strings(strings_list)
print("Number of matching strings:", matching_strings_count)  


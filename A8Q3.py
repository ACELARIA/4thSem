def decode_message(encoded):
    def helper(encoded, index, current_decoded, result):
        if index == len(encoded):
            result.append(current_decoded)
            return
        
        if index < len(encoded) and encoded[index] != '0':
            helper(encoded, index + 1, current_decoded + chr(int(encoded[index]) - 1 + ord('A')), result)
        
        if index + 1 < len(encoded) and encoded[index] != '0' and 10 <= int(encoded[index:index+2]) <= 26:
            helper(encoded, index + 2, current_decoded + chr(int(encoded[index:index+2]) - 1 + ord('A')), result)

    result = []
    
    helper(encoded, 0, "", result)
    
    return result

encoded_message = input("Enter the encoded message: ")

decoded_messages = decode_message(encoded_message)

if decoded_messages:
    print("Possible decoded messages:")
    for decoded in decoded_messages:
        print(decoded)
else:
    print("No valid decoded message found.")

def generate_c_array_declaration_with_initialization(m):
    array_declaration = f'signed char myArray[{m}] = {{'
    for i in range(m):
        if i in hash_array:
            array_declaration += str(hash_array.index(i))
        else:
            array_declaration += "-1"

        if i < m - 1:
            array_declaration += ', '

    array_declaration += '};'

    return array_declaration


unique_array = [0x50, 0x11, 0x92, 0xD3, 0x20, 0x61, 0xE2, 0xA3, 0x64, 0x25,
                0xA6, 0xE7, 0xA8, 0xE9, 0x6A, 0x2B, 0xEC, 0xAD, 0x2E, 0x47, 0x49, 0x3C, 0x7D]

hash_array = [i % 59 for i in unique_array]

m = 59  # 數組大小
declaration = generate_c_array_declaration_with_initialization(m)

# 打印生成的C代碼
print(declaration)

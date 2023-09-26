data = [(0x50, 0), (0x11, 1), (0x92, 2), (0xD3, 3), (0x20, 4), (0x61, 5), (0xE2, 6), (0xA3, 7), (0x64, 8), (0x25, 9), (0xA6, 10),
        (0xE7, 11), (0xA8, 12), (0xE9, 13), (0x6A, 14), (0x2B, 15), (0xEC, 16), (0xAD, 17), (0x2E, 18), (0x47, 19), (0x49, 20), (0x3C, 21), (0x7D, 22)]

# Generate C language switch code
c_code = "switch (value) {\n"

for case_value, return_value in data:
    c_code += f"    case 0x{case_value:02X}U:\n"
    c_code += f"        // Do something for case 0x{case_value:02X}\n"
    c_code += f"        return {return_value}U;\n"

c_code += "    default:\n"
c_code += "        // Default case\n"
# c_code += "        // Handle the default case here\n"
c_code += "        break;\n"
c_code += "}\n"

# Output generated C code
print(c_code)

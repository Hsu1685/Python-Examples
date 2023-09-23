def generate_c_array(m, n, ones_positions):
    # 打印 C 語言的數組聲明
    print(f'signed char arr[{m}][{n}] = {{')

    # 生成初始化的值
    for i in range(m):
        print('    {', end='')
        for j in range(n):
            if (i, j) in ones_positions:
                print(ones_positions.index((i, j)), end='')
            else:
                print("-1", end='')
            if j != n - 1:
                print(', ', end='')
        print('},')

    print('};')


# 自定義需要初始化為特殊值的位置
custom_ones_positions = [(1, 0), (2, 1), (3, 2), (4, 3),
                         (5, 4), (6, 5), (7, 6), (8, 6), (8, 7)]

# 調用函數生成 C 語言數組聲明和初始化代碼
generate_c_array(10, 9, custom_ones_positions)

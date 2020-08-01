def sum_command(command):
    data = command.split() # 文字列を分解
    command_args = data[1:]
    result = 0
    for num in command_args:
        result += int(num)
    response = '合計は「{}」です'.format(result)
    return response

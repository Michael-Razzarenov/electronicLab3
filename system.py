def to_decimal(number, base):
    # Проверяем, является ли число отрицательным
    negative = number[0] == '-'
    if negative:
        number = number[1:]

    decimal = 0
    # Словарь для преобразования букв в числовые значения
    hex_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    # Преобразуем каждую цифру числа в десятичную систему
    for digit in number:
        if '0' <= digit <= '9':
            value = int(digit)
        else:
            value = hex_dict[digit.upper()]
        decimal = decimal * base + value

    # Возвращаем отрицательное число, если оно было отрицательным
    return -decimal if negative else decimal


def from_decimal(number, base):
    # Обрабатываем случай, когда число равно нулю
    if number == 0:
        return '0'

    # Проверяем, является ли число отрицательным
    negative = number < 0
    if negative:
        number = -number

    digits = []
    # Словарь для преобразования числовых значений в буквы
    hex_chars = '0123456789ABCDEF'

    # Преобразуем число из десятичной системы в конечную систему счисления
    while number > 0:
        digits.append(hex_chars[number % base])
        number //= base

    # Добавляем знак минус, если число было отрицательным
    if negative:
        digits.append('-')

    # Разворачиваем список цифр и объединяем их в строку
    digits.reverse()
    result = ''.join(digits)
    return result


def to_direct(binary_str, bits):
    # Преобразуем отрицательное число в прямой код
    if binary_str[0] == '-':
        binary_str = binary_str[1:]
        # Дополняем до нужной размерности и обрезаем, если нужно
        binary_str = binary_str.zfill(bits)[-bits:]
        # Заменяем первый бит слева на знаковый бит (1)
        direct = '1' + binary_str[1:]
    else:
        # Дополняем до нужной размерности и обрезаем, если нужно
        binary_str = binary_str.zfill(bits)[-bits:]
        # Заменяем первый бит слева на знаковый бит (0)
        direct = '0' + binary_str[1:]

    return direct


def main():
    while True:
        try:
            # Ввод исходной и конечной систем счисления
            input_system = int(input('Введите исходную систему счисления (2-16): '))
            output_system = int(input('Введите конечную систему счисления (2-16): '))
            number = input('Введите исходное число: ')

            # Проверка корректности ввода систем счисления
            if input_system < 2 or input_system > 16 or output_system < 2 or output_system > 16:
                print('Нарушено заданное ограничение систем счисления')
                continue

            # Преобразование числа из исходной системы счисления в десятичную
            decimal = to_decimal(number, input_system)

            # Преобразование числа из десятичной системы счисления в целевую
            if output_system == 2:
                bits = 8  # Размерность
                binary = from_decimal(decimal, output_system)
                direct = to_direct(binary, bits)
                result = f'Прямой код: {direct}, Двоичное представление: {binary}'
            else:
                result = from_decimal(decimal, output_system)

            # Вывод результата
            print(f'Результат: {result}')

        except ValueError:
            print('Некорректный ввод')


if __name__ == "__main__":
    main()

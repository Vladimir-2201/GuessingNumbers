from random import randint

def is_valid(variant, end):
    return variant.isdigit() and 1 <= int(variant) <= end

def start_game():
    while True:
        end = input('Введите максимальное целое число для генерации (больше 0) ').strip()
        if end.isdigit() and int(end) >= 1:
            return randint(1, int(end)), 0, int(end)
        else:
            print('А может быть все-таки введем целое число больше 0?')

def restart(yes, no, ext = ''):
    while ext != yes and ext != no:  
        ext = input(f'Чтобу сыграть ещё раз введите "{yes}". Для завершения игры введите "{no}": ').strip()
    return ext == yes

print('Добро пожаловать в числовую угадайку')
num, total, end = start_game()
while True:
    input_num = input(f'Введите целое число от 1 до {end}: ').strip()
    total += 1
    if is_valid(input_num, end):
        input_num = int(input_num)
    else:
        print(f'А может быть все-таки введем целое число от 1 до {end}?')
        continue

    if input_num < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')       
    elif input_num > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print(f'Вы угадали с {total} попытки, поздравляем!')

        if restart("+", "-"):
            num, total, end = start_game()
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

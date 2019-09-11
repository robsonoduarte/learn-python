def get_text_day(day):
    days = {
        (1,7) : 'Weekend',
        tuple(range(2,7)): 'Week day'
    }
    chosen_day = (text for numbers, text in days.items() if day in numbers)
    return next(chosen_day, 'Invalid Day')


if __name__ == '__main__':
    for day in range(0,9):
        print(f'{day}: {get_text_day(day)}')


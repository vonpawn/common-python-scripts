import random


def seeded_random():
    # as random module is deterministic, setting a starting seed will allow for repeated runs with the same data
    random.seed(1234)
    a = random.randint(1,100)
    random.seed(1234)
    b = random.randint(1, 100)
    print(f'a == b: {a == b}')


def rand_int_between(start=0, end=100):
    return random.randint(start, end)


def rand_int_with_steps(start=0, end=100, step=5):
    return random.randrange(start, end, step)


def rand_float_between(start=0, end=100, precision=3):
    return round(random.uniform(start, end), precision)


def rand_choice(sequence):
    return random.choice(sequence)


def rand_choices():
    # useful for data generation with a module like faker when attempting to make a varied dataset
    user_data = {
        'title': 'Mr.',
        'fname': 'James',
        'mname': 'Earl',
        'lname': 'Jones'
    }
    templates = [
        '{fname} {lname}',
        '{fname} {mname[0]}. {lname}',  # include middle initial, real solution would need guarding for empty middle name
        '{title} {lname}',
        '{lname}, {fname[0]}.'
    ]

    chosen_templates = random.choices(population=templates, k=3)

    print(f'\nchosen name formats:')
    for i, temp in enumerate(chosen_templates):
        print(f'{i}: {temp.format(**user_data)}')


def rand_weighted_choices():
    # useful for data generation with a tool like faker when attempting to make a varied dataset
    # may want to use normal (or some other distrobution) if the desired data requires it
    # rough values taken from https://en.wikipedia.org/wiki/File:Personal_Household_Income_U.png
    household_income_ranges = [
        (0, 25000),
        (25001, 50000),
        (50001, 75000),
        (75001, 100000),
        (100001, 125000),  # note: wiki has unbound cap, for simplicity just keeping the bucket sizes the same
    ]
    household_income_weights = [
        0.25,
        0.23,
        0.18,
        0.11,
        0.17
    ]

    income_ranges = random.choices(household_income_ranges, household_income_weights, k=5)

    incomes = []
    for low, high in income_ranges:
        incomes.append(random.randint(low, high))

    print(f'\ngenerated incomes: \n{incomes}')


def roll_dice(dice: str):
    # ex. "3d6" will roll 3 6-sided dice and return the sum
    print(f'\nrolling {dice}')
    num_dice, num_sides = [int(s) for s in dice.split('d')]

    roll_sum = [random.randint(1, num_sides) for _ in range(num_dice)]
    print(roll_sum)


if __name__ == '__main__':
    rand_choices()
    rand_weighted_choices()

    roll_dice('6d6')
    roll_dice('1d20')

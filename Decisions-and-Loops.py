# This program requests a series of inputs from a user, like family member
# details and cover tier, and then work out their insurance premium.

# Named constants to represent important values in the program.
BASE_PRICE = 20
WEEKS = 52.143
MONTH = 4.345

# Assign initial values to variables.
keep_going = 'y'
second_adult = 1.95
zero_four = .50
five_nine = .60
ten_thirteen = .70
fourteen_seventeen = .80

# Initial calculation for different categories and tiers.
silver = 1.25 * BASE_PRICE
gold = 1.5 * BASE_PRICE

# Program heading
print('--------------------------------')
print('Welcome to Medicare Health Fund')
print('--------------------------------')
print('Let us get you a quote')
print('')

# Initialise while loop and prompt the user to input the number of adults and number of children.
while keep_going == 'y':
    number_of_adults = int(input('Enter the number of adults (1-2): '))
    number_of_children = int(input('Enter the number of children (0+): '))

# Declare more variables that will be used in computations.
    total_adult = 1
    child = 0
    child_premium_total = 0

# Initialise a for loop and prompt the user to input the age of each child.
    children_ages = []
    for kid in range(number_of_children):
        age = int(input(f'Enter the age of child {kid + 1}: '))
        children_ages.append(age)

# Prompt the user to input the desired premium.
    tier_cover = input('What tier of cover would you like? [B]asic/[S]ilver/[G]old: ')

# Decision structure: if-elif-else statement. Assign a final value to tier_cover.
    if tier_cover == 'b' or tier_cover == 'B':
        tier_cover = BASE_PRICE
    elif tier_cover == 's' or tier_cover == 'S':
        tier_cover = silver
    else:
        tier_cover = gold

# Beginning of premium calculation.
# Identifying the number of adults.
    while number_of_adults > 1 and total_adult < 2:
        total_adult = total_adult + 1

# Identifying the premium of each child including the total.
    for i in children_ages:
        if i < 5:
            child_premium_total = child_premium_total + zero_four * tier_cover
        elif i < 10:
            child_premium_total = child_premium_total + five_nine * tier_cover
        elif i < 14:
            child_premium_total = child_premium_total + ten_thirteen * tier_cover
        elif i < 18:
            child_premium_total = child_premium_total + fourteen_seventeen * tier_cover
        else:
            print('Age is out of range')

# Calculation of insurance premium.
    if number_of_children == 0:
        weekly_cover = (total_adult if total_adult < 2 else second_adult) * tier_cover
        monthly_cover = weekly_cover * MONTH
        annual_cover = weekly_cover * WEEKS
    else:
        weekly_cover = ((total_adult if total_adult < 2 else second_adult) * tier_cover) + child_premium_total
        monthly_cover = weekly_cover * MONTH
        annual_cover = weekly_cover * WEEKS

# Display insurance premium.
    print('')
    print('Thank you. Your premium is: ')
    print(f'$ {weekly_cover: .2f} per week, OR')
    print(f'$ {monthly_cover: .2f} per month, OR')
    print(f'$ {annual_cover: .2f} per annum')
    print('')

# Prompt the user if they need to generate another quote or exit the program.
    keep_going = input('Do you need another quote (y/n)? ')
    print('')

# End the program.
print('Have a great day.')

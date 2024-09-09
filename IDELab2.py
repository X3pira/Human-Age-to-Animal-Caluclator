# this is part 1 for the dog age
def calculate_dog_age(human_age):
    dog_age = human_age * 7
    return dog_age

def calculate_dog_age_in_years_months_days(human_age):
    dog_age = calculate_dog_age(human_age)
    years = int(dog_age)
    months = int((dog_age - years) * 12)
    days = 0  # No fractional days
    return years, months, days

# now onto part 2 for the cat age
def calculate_cat_age(human_age):
    cat_age = human_age / 9
    return cat_age

def calculate_cat_age_in_years_months_days(human_age):
    cat_age = calculate_cat_age(human_age)
    years = int(cat_age)
    months = int((cat_age - years) * 12)
    days = 0  # No fractional days
    return years, months, days

# part 3 for horse age
def calculate_horse_age(human_age):
    horse_age = 3 * (((human_age ** 2) - 47) / 7 + 12)
    return horse_age

def calculate_horse_age_in_years_months_days(human_age):
    horse_age = calculate_horse_age(human_age)
    years = int(horse_age)
    months = int((horse_age - years) * 12)
    days = int(((horse_age - years) * 12 - months) * 30)  # Convert months to days
    return years, months, days

# Main program
try:
    human_age = float(input("Enter your age: "))

    dog_age = calculate_dog_age_in_years_months_days(human_age)
    cat_age = calculate_cat_age_in_years_months_days(human_age)
    horse_age = calculate_horse_age_in_years_months_days(human_age)

    print(f'Your age in dog years is {dog_age[0]:.1f} years {dog_age[1]:.1f} months {dog_age[2]:.1f} days')
    print(f'Your age in cat years is {cat_age[0]:.1f} years {cat_age[1]:.1f} months {cat_age[2]:.1f} days')
    print(f'Your age in horse years is {horse_age[0]:.1f} years {horse_age[1]:.1f} months {horse_age[2]:.1f} days')

except ValueError:
    print("Invalid input. Please enter a valid age.")
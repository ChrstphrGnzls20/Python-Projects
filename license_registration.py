# a simple license plate registration with that obeys local guidelines
def peek_database():
    with open('sample_database.txt', 'r+') as database:
        print(database.read().split())

def insert_database(to_check):
    with open('sample_database.txt', 'r+') as database:
        content = database.read().split()
        if to_check in content:
            print('\nAlready registered!')
            return False
        else:
            database.write(' ' + to_check.rstrip())
            return True

def is_correct(to_validate):
    num = 0
    alpha = 0
    for x, letter in enumerate(to_validate):
        if letter.isalpha() and alpha <= 3:
            alpha += 1
        elif letter.isdigit() and num <= 3:
            num += 1
        elif letter == '-' and x == 3:  # if connector is not '-', or '-' is not in 4th index, it is not valid
            pass
        else:                           # if it is not a digit, letter, or '-', it is not valid
            return False
    return num == 3 and alpha == 3      # to be valid, it must have 3 digit and 3 letter connected with dash in middle

def validate(plate_to_reg):
    # if the plate is valid according to some guidelines
    if is_correct(plate_to_reg):
        # if the plate is not yet registered
        if insert_database(plate_to_reg):
            return True
    return None


if __name__ == '__main__':
    my_input = input('Enter plate to register: ').upper()
    # we check if the plate is valid and not yet registered
    if validate(my_input):
        print('Registered Successfully!')
    else:
        print("\nInvalid details.\n"
              "The plate must have:\n\t"
              "1. Unique sequence"
              "2. 3 numerical digits\n\t"
              "3. 3 alphabetical letters\n\t"
              "4. Does not contain any special character\n\t"
              "5. Supports 'xxx-xxx' format")
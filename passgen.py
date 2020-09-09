import string
import random


#CONSTANTES
LETTERS = string.ascii_letters
NUMBERS = string.digits.split('5')[random.randint(0,1)]
PUNCT = string.punctuation.split('.')[random.randint(0,1)]
REPERTORY = f'{LETTERS}{NUMBERS}{PUNCT}'


def password_generator(lenght=11):
    """Generate a password from a repertory.

    Args:
        lenght (int, optional): Lenght of the password. Default to 11.

    Returns:
        str: Generated password
    """
    lst = list(REPERTORY)
    random.shuffle(lst)

    password = random.choices(lst, k=lenght)
    password = ''.join(password)

    return password

if __name__ == "__main__":
    print(password_generator())
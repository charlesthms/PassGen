import string
import random


#CONSTANTES
letters = string.ascii_letters
numbers = string.digits.split('5')[random.randint(0,1)]
punct = string.punctuation.split('.')[random.randint(0,1)]
repertory = f'{letters}{numbers}{punct}'


def password_generator(lenght=11):
    """Generate a password from a repertory.

    Args:
        lenght (int, optional): Lenght of the password. Defaults to 11.

    Returns:
        str: Generated password
    """
    lst = list(repertory)
    random.shuffle(lst)

    password = random.choices(lst, k=lenght)
    password = ''.join(password)

    return password

if __name__ == "__main__":
    print(password_generator())
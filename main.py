import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    letter = string.ascii_letters
    digits = string.digits if use_digits else ''
    specials = string.punctuation if use_specials else ''

    all_chars=letter+digits+specials
    if not all_chars :
        print("Error: no char selected" )
        return None

    password= ''.join(random.choice(all_chars)for _ in range(length))
    return password

length=int(input("Enter password lenghh: "))
use_digits=input("include number? (y/n): ").strip().lower() == 'y'
use_symbols= input("use special sumbols?(y/n): ").strip().lower() =='y'

password= generate_password(length, use_digits, use_symbols)
print(f"password generated is: {password}")
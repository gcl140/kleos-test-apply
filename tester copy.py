# tester.py

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def check_email(email):
    try:
        validate_email(email)
        print(f"\n✅ '{email}' is a valid email address.\n")
    except ValidationError:
        print(f"\n❌ '{email}' is not a valid email address.\n")

if __name__ == "__main__":
    while True:
        email = input("Enter an email address to validate (or type 'exit' to quit): ").strip()
        if email.lower() == 'exit':
            print("Exiting email tester.")
            break
        check_email(email)

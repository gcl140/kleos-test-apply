# advanced_email_tester.py

from validate_email_address import validate_email

def check_email_advanced(email):
    is_valid = validate_email(email, verify=True)
    if is_valid:
        print(f"\n✅ '{email}' is valid and exists (SMTP verified).\n")
    else:
        print(f"\n❌ '{email}' is invalid or does not exist.\n")

if __name__ == "__main__":
    while True:
        email = input("Enter an email to verify (or 'exit' to quit): ").strip()
        if email.lower() == 'exit':
            print("Exiting advanced email tester.")
            break
        check_email_advanced(email)

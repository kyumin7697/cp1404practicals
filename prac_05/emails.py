"""""
Emails
Estimate: 30 minutes
Actual:
pseudocode:
define extract_name_from_email function
    get part before '@'
    split it by '.'
    join the parts with spaces
    convert to title case
    return name

define main function
    email_to_name = {}
    while True
        get user email
        if email == blank
            break
        call extract_name_from_email
        check user to confirm the name
        if confirmation not in ('', 'y')
            get correct name

        email_to_name[email] = name

    for email, name in the dictionary
        print "{name} ({email})"

end main function
"""

def main():
    while True:
        email = input("Email: ")
        if email == "":
            break

        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ('', 'y'):
            name = input("Name: ")

def extract_name_from_email(email):
    """Extracting names from emails"""
    parts = email.split('@')[0].split('.')
    name = ' '.join(parts).title()
    return name

main()

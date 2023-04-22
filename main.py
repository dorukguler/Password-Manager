from password_generator.generator import generate_password
def main():
    # Prompt the user for the desired password length
    length = int(input("Enter the desired password length (5-15 characters): "))
        

    # Prompt the user for the desired password complexity level
    complexity = int(input("Enter the desired password complexity level (1-3): "))


    # Prompt the user for the name or URL of the site or service
    site_name = input("Enter the name or URL of the site or service: ")

    # Prompt the user for their username or email
    username = input("Enter your username or email: ")

    # Generate the password
    password = generate_password(int(length), int(complexity))

    

    # Display the password to the user
    print(f"Your password for {site_name} ({username}) is: {password}")
    

    # Write the site name and password to a file
    with open('passwords.txt', 'a') as file:
        file.write(f"{site_name} ({username}): {password}\n")

    # Print a message to the terminal
    print("Your password has been saved to passwords.txt")

if __name__ == '__main__':
    main()

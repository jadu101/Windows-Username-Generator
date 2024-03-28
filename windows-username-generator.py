def generate_usernames(name):
    # Split the input name into first and last name
    parts = name.split()
    first_name = parts[0].lower()
    last_name = ''.join(parts[1:]).lower()

    # Generate username variations
    variations = [
        first_name,
        first_name + last_name,
        first_name + '.' + last_name,
        first_name[0] + '.' + last_name,
        first_name + '_' + last_name,
        first_name[0] + '_' + last_name,
        first_name[0] + last_name  # New variation style
    ]

    return variations

def main():
    # Display the logo
    print("""
    ██████╗ ██╗   ██╗███████╗███████╗ █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██████╔╝██║   ██║███████╗███████╗███████║   ██║   ██║   ██║██████╔╝
    ██╔═══╝ ██║   ██║╚════██║╚════██║██╔══██║   ██║   ██║   ██║██╔═══╝ 
    ██║     ╚██████╔╝███████║███████║██║  ██║   ██║   ╚██████╔╝██║     
    ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     
                                                                        
    """)

    # Display copyright and source information
    print("Copyright (c) jadu101")
    print("Source: jadu101.github.io\n")

    # Prompt for usernames until "run" is entered
    print("Username variations will be created following this pattern:")
    print("| Pattern                      | Example           |")
    print("|------------------------------|-------------------|")
    print("| first-name                   | robert            |")
    print("| first-namelast-name          | roberthilton      |")
    print("| first-name.last-name         | robert.hilton     |")
    print("| first-name-initial.last-name | r.hilton          |")
    print("| first-name_last-name         | robert_hilton     |")
    print("| first-name-initial_last-name | r_hilton          |")
    print("| first-letter-last-name       | rhilton           |")
    print()

    usernames = []

    # Prompt for usernames until "run" is entered
    while True:
        username = input("Enter a username (type 'run' to generate variations): ").strip()
        if username.lower() == 'run':
            break
        else:
            usernames.append(username)

    # Generate and print variations for each username
    all_variations = []
    for username in usernames:
        username_variations = generate_usernames(username)
        all_variations.extend(username_variations)

    # Print the full list of variations
    print("\nFull list of username variations:")
    for variation in all_variations:
        print(variation)

if __name__ == "__main__":
    main()

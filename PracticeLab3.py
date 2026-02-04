# Juan Hilbron 
# Maria Saavedra

################# Exercise 1 ####################

print("=== Secure Notes App ===")

choice = input("Choose add / view: ").strip().lower()

if choice == "add":
    note = input("Enter note: ").strip().lower()

    if note != "":
        encrypted = ""
        # In that line start the Encription and it will shift each character by +1 in ASCII
        for ch in note: 
            encrypted = encrypted + chr(ord(ch) + 1)

        file = open("secure_notes.txt", "a")
        file.write(encrypted + "\n") # Append encrypted note to the file
        file.close()

        print("Note saved securely. ")
    else:
        print("There is nothing in the note, so " \
        "there would be no changes in the document")

elif choice == "view":
    file = open("secure_notes.txt", "r")

    count = 0
    total_characters = 0
    for line in file: 
        decrypted = ""
        for ch in line.strip():
            # Reverse the encription made by shifting -1 inn ASCII
            decrypted = decrypted + chr(ord(ch) -1)

        print("- " + decrypted.title())
        count = count + 1
        total_characters += len(decrypted)

    file.close()
    print("Total notes: ", count)
    print("Total characters across all notes:", total_characters)


else: 
    print("Invalid option. ") 


################# Exercise 2 ####################

print("######### Secure Feedback App #########")
print("Welcome to the Secure Feedback App")

booleanito = True
while booleanito == True: 
    print("This is the menu \n" \
    "1. Add Feedback \n" \
    "2. View Feedback  \n" \
    "3. Analyze Feedback  \n" \
    "4. Search Feedback  \n" \
    "5. Exit ")
    menuChoice = int(input("Choose an option: ").strip())
    print("#########################")

    if menuChoice == 1:
        feedbackNote = input("Enter Feedback: ").strip().lower()
        if feedbackNote != "":
            encrypted = ""

            for ch in feedbackNote: 
                encrypted = encrypted + chr(ord(ch) + 1)

            file = open("feedback.txt", "a")
            file.write(encrypted + "\n") 
            file.close()

            print("Note saved securely. ")
            print("#########################")
        else:
            print("There is nothing in the note, so " \
            "there would be no changes in the document")
            print("#########################")

    elif menuChoice == 2:
        file = open("feedback.txt", "r")

        counts = 0
        for line in file: 
            decrypted = ""
            for ch in line.strip():
                decrypted = decrypted + chr(ord(ch) -1)

            print(f"Note {counts} " + decrypted.title())
            counts = counts + 1

        file.close()
        print("Total Feedbacks: ", counts)
        print("#########################")

    elif menuChoice ==3:
        file = open("feedback.txt", "r")
        total_entries = 0
        total_words = 0
        total_characters = 0
        for line in file:
            decrypted = ""
            for ch in line.strip():
                    decrypted = decrypted + chr(ord(ch) - 1)
            total_entries = total_entries + 1
            total_characters = total_characters + len(decrypted)
            total_words = total_words + len(decrypted.split())
        file.close()
        print("--- Feedback Analysis ---")
        print("Total entries:", total_entries)
        print("Total words:", total_words)
        print("Total characters:", total_characters)
        print("#########################")

    elif menuChoice == 4:

        keyword = input("Enter keyword to search: ").strip().lower()
        file = open("feedback.txt", "r")

        counts = 0
        matches_found = 0
        for line in file:
            decrypted = ""
            for ch in line.strip():
                decrypted = decrypted + chr(ord(ch) - 1)
            counts = counts + 1

            if keyword in decrypted.lower():
                matches_found = matches_found + 1
                print(f"Note {counts}: " + decrypted.title())

        file.close()

        if matches_found == 0:
            print("No matching feedback found.")
        else:
            print(f"Total matches found: {matches_found}")
        print("#########################")

    elif menuChoice == 5:
        print("Thank you for using the program")
        booleanito = False
    else:
        print("Your choice is wrong Try again")




################# Answer of the Questions ####################
# 1. Why is encryption applied before saving data?

# Encription is applied before saving data in order to protect
# privacy and security. If anyone gets to open the file, that 
# person won't be able to read the original message.

# 2. Why must decryption happen before searching?

# The data in the file is encripted so the serching will 
# compare the keyword with scrambled characters. Decription 
# must happen first in order to serch the original readable 
# text, in other case the matches will be never found.

# 3. What breaks if the shift value changes?

# If the value changes the decrypted text will be completely
# incorrect and unreadable. Encription and decription must 
# use the same shift value in order to recover correctly the 
# original message. 

# 4. Why is this encryption not suitable for real systems?

# the first reason is because this encription is too easy 
# to break bacause: 
# 1. It uses a fixed shift 
# 2. The pattern can be guessed quickly 
# 3. There is no randomness or advanced protection. 
# Real systems use strong algorithms, secret keys 
# and multiple layers of security. 


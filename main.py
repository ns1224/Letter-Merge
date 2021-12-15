PLACEHOLDER = "[name]"

# Gets names, creates stripped list
names = []
with open('names.txt', mode='r') as names_file:
    for name in names_file:
        names.append(name.strip('\n'))

# Gets file text
with open('note.txt', mode='r') as letter_file:
    lines = letter_file.read()
    for name in names:
        new_letter = lines.replace(PLACEHOLDER, name)
        with open(f"ReadyToSend/{name}-invitation.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
            





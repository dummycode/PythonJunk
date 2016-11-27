import pyperclip

print("Previous clipboard...\n\n" + pyperclip.paste() + "\n\n")
print("Enter what you want to copy: ", end='')

pyperclip.copy(input())

print("Done.")

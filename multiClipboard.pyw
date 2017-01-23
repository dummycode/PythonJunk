import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb')

args = sys.argv

# Save or delete
if (len(args) == 3):
    if (args[1].lower() == 'save'):
        mcbShelf[args[2]] = pyperclip.paste()
    elif (args[1] == 'delete' and args[2] in mcbShelf):
        del mcbShelf[args[2]]
elif (len(args) == 2):
    if (args[1].lower() == 'list'):
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif (args[1].lower() == 'delete'):
        os.remove('mcb.db')
    elif (args[1] in mcbShelf):
        pyperclip.copy(mcbShelf[args[1]])

mcbShelf.close()

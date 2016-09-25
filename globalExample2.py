def bacon():
    global eggs
    eggs = '42' #this is global

def spam():
    eggs = 'spam' # this is local

def ham():
    print(eggs) # this is globa
    
eggs = 'eggs'
bacon()
spam()
ham()
print(eggs)

def print_lol(a_lista):
    for cada_filme in a_lista:
        if isinstance(cada_filme, list) == True:
            print_lol(cada_filme)
        else:
            print(cada_filme)

def print_ja(b_lista):
	print(b_lista)
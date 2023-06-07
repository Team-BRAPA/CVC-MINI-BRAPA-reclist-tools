consonantuwu = ['b',  'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'rh', 'ch', 'dj', 'lh', 'ng', 'nh', 'rr', 'rw', 'sh']
vowels = ["an", "en", "in", "on", "un", "ax", "eh", "ae", "oh", "a", "e", "i", "o", "u"]
ignorelist = ['ch', 'dj', 'lh', 'ng', 'nh', 'rr', 'rw', 'sh', 'rh']
numlist = ['0','1','2','3','4','5','6','7','8','9', 'r']
ignore2 = ['c', 'd', 'l' ,'h', 'g', 'n', 'r', 's', 'j']
antes = ['c', 'd', 'l', 'n', 'r', 's']
depois = ['h', 'g', 'j']

consonants = [c for c in consonantuwu if c not in ignorelist]

reprules = {}

def verify(mystr):
    w = ''
    for i in range(len(mystr) - 1):
        if mystr[i] == mystr[i + 1] and mystr[i] not in numlist:
            print('Repeated char', mystr[i])
        else:
            w += mystr[i]
    w += mystr[-1]
    return w

for j in vowels:
    for i in consonantuwu:
        reprules[f' {i},'] = f' {i}-,'
        reprules[f'={i} '] = f'=-{i} '


with open("edit.txt", "r") as input_file:
    lines = input_file.readlines()

with open("modified.txt", "w") as output_file:
    for line in lines:
        for old_text, new_text in reprules.items():
            line = verify(line.replace(old_text, new_text))
        output_file.write(line)

print("Programa finalizado")
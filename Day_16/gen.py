import pdb

def num_gen():
    for i in range(5):
        yield i

gen = num_gen()

for i in gen:
    print(i)

options = 'red yellow blue white black green purple'.split()

def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'

print(list(create_select_options_gen()))


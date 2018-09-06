import pdb
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob blederbos',
        'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites',
        'bob belderbos', 'julian sequera', 'al pacino', 'brad pitt',
        'matt damon', 'brad pitt']

def get_name(names=NAMES):
    for name in names:
        yield name.split()

def gen_pairs(names=NAMES):
    for x in range(10):
        name1 = random.choice(NAMES).split()[0].title()
        name2 = random.choice(NAMES).split()[0].title()
        # name1 += name1.split()[0].upper()
        yield f"{name1} teams up with {name2}"

name_obj = get_name()
for name in name_obj:
    print("{} {}".format(name[0].title(), name[1].title()))

ran_nam = gen_pairs()
for name in ran_nam:
    print(name)

pdb.set_trace()

# if __name__ == "__main__":
#     names = get_name()
#     for x in range(len(NAMES)):
#         next(get_name)
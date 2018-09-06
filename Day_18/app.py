import pdb

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    t_list = []
    for name in names:
        name = name.title()
        if name not in t_list:
            t_list.append(name)
    return t_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names = [(name.split()[1] + " " + name.split()[0]) for name in names]
    names.sort(reverse=True)
    names = [(name.split()[1] + " " + name.split()[0]) for name in names]
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    t_list = [(name.split()[0]) for name in names]
    return min(t_list, key=len)

# print(dedup_and_title_case_names(NAMES))
# print("-" * 40)
print(shortest_first_name(NAMES))
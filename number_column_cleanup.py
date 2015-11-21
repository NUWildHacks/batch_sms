# number_column_cleanup.py

import re

def main():
    in_file = open('hackers_dirty.txt', 'rb')
    out = open('hackers.txt', 'w')
    numbers = []
    for line in in_file.readlines():
        if line.strip() != '':
            numbers.append(line)

    numbers = [re.sub("[^0-9]", "", i) for i in numbers]
    # not_numbers = [i for i in numbers if not (len(i) < 12 and len(i) > 9)]
    # numbers = [i for i in numbers if  (len(i) < 12 and len(i) > 9)]
    numbers = ["+1%s" % i for i in numbers if len(i) == 10]

    for n in numbers:
        out.write(n + '\n')

if __name__ == '__main__':
    main()

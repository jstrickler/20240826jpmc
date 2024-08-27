

def find_word(word, *files, **options):
    for file in files:
        with open(file) as file_in:
            for line in file_in:
                if word in line:
                    print(line, end="")


find_word("bird", "DATA/alice.txt", "DATA/parrot.txt", ignore_case=True)

def all_params(rp1, rp2, *args, rn1, rn2, **kwargs):
    pass


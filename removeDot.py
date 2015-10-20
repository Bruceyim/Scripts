import os

def parse(file):
    parseList = []
    with open(file, 'r') as f:
        for strline in f:
            if strline.startswith(">>> ") or strline.startswith("... "):
                strline = strline[4:]

            parseList.append(strline)
    return parseList


def main():
    dir = os.getcwd()
    for file in os.listdir(dir):
        if file.startswith('ch'):
            path = os.path.join(dir, file)
            parseList = parse(path)
            with open(file[-6:], 'w') as fout:
                for line in parseList:
                    fout.write(line)
    print('done')

if __name__ == '__main__':
    main()
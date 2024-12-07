def read_from_file(file):
    lines = []
    with open(file) as f:
        lines = f.readlines()
    return lines
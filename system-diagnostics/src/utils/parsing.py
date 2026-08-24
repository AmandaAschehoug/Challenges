def parse_line(line):
    return line.strip()


def parse_csv(lines):
    return [parse_line(line) for line in lines]

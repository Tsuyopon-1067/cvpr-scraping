import sys


def extract_from_file(input_file, target):
    input_lines = []
    result = []
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                input_lines.append(line)
    except IOError as e:
        print(f"Failed to read file. {e}")
        sys.exit(1)

    for line in input_lines:
        lower = line.lower()
        if target in lower:
            result.append(line)

    print(
        f"Found {len(result)}/{len(input_lines)} lines that contain '{target}'", file=sys.stderr)
    for line in result:
        print(line, end='')


def main():
    if len(sys.argv) < 3:
        print("usage: python extract.py <input file name> <search target>")
        sys.exit(1)

    input_filename = sys.argv[1]
    search_target = sys.argv[2]

    extract_from_file(input_filename, search_target)


if __name__ == "__main__":
    main()

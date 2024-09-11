import sys

head = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Monochrome Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 20px auto;
            padding: 0 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f8f8f8;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f5f5f5;
        }
    </style>
</head>
<body>
    <table>
        <thead>
            <tr>
                <th>Title</th>
            </tr>
        </thead>
           <tbody >
           """
tail = """</tbody >
    </table>
</body>
</html>
"""


def generate_html(list):
    res = head
    for v in list:
        splited = v.split(',')
        res += '<tr>\n'
        res += '<td>\n'
        res += f'<a href="{splited[1]}">{splited[0]}</a>'
        res += '</td>\n'
        res += '</tr>\n'
    res += tail
    return res


def generate_html_from_file(input_file):
    input_lines = []
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                input_lines.append(line)
    except IOError as e:
        print(f'Failed to read file. {e}')
        sys.exit(1)
    html = generate_html(input_lines)
    print(html)


def main():
    if len(sys.argv) < 2:
        print('usage: python html.py <input file name>')
        sys.exit(1)

    input_filename = sys.argv[1]
    generate_html_from_file(input_filename)


if __name__ == '__main__':
    main()

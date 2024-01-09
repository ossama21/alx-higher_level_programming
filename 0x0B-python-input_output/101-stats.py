#!/usr/bin/python3
"""
Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))


if __name__ == "__main__":
    import sys

    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    splitted_line = []
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(file_size, status_codes)
                count = 1
            else:
                count += 1

            splitted_line = line.split()

            try:
                file_size += int(splitted_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if splitted_line[-2] in status_codes:
                    status_codes[splitted_line[-2]] += 1
            except IndexError:
                pass

        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
        raise

    """['242.182.96.142', '-', '[2024-01-09', '17:33:51.002132]',
    '"GET', '/projects/260', 'HTTP/1.1"', '401', '58']"""

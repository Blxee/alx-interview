#!/usr/bin/python3
"""0. Log parsing"""
import re
import sys


if __name__ == "__main__":
    pattern = re.compile(
        r'.+ - \[.+\] "GET /projects/260 HTTP/1.1" (?P<code>.+) (?P<size>\d+)'
    )

    status_codes = {
        code: 0
        for code in (200, 301, 400, 401, 403, 404, 405, 500)
    }
    total_size = 0

    def show_info():
        """Prints information about logs every 10 lines"""
        print('File size:', total_size)
        for code in sorted(status_codes.keys()):
            n = status_codes[code]
            if n:
                print(f'{code}: {n}')

    try:
        i = 0
        for line in sys.stdin:
            match = re.match(pattern, line)
            if not match:
                continue
            i += 1
            code = int(match.group('code'))
            size = int(match.group('size'))
            if code in status_codes:
                status_codes[code] += 1
            total_size += size
            if i % 10 == 0:
                show_info()
    except Exception:
        pass
    finally:
        show_info()

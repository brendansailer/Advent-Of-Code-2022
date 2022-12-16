#!/usr/bin/env python3

import sys
import collections

# In hindsight, using something like os.path.abspath and os.path.join would have been better to manage the paths

def read_input():
    fs = collections.defaultdict(list)
    cwd = '/'

    for line in sys.stdin:
        values = line.strip().split()

        if values[0] == '$' and values[1] == 'cd':
            if values[2] == '..': # If we're going up a dir, chop off the last part of the path
                cwd = '/'.join(cwd.split('/')[:-1])
            else: # Otherwise add it on
                if values[2] == '/' and cwd == '/':
                    pass
                elif cwd == '/': # Don't double up slashes for the top-level
                    cwd += values[2]
                else:
                    cwd += '/' + values[2]
        elif values[0] == '$' and values[1] == 'ls':
            pass
        elif values[0] == 'dir':
            dir_name = values[1]
            fs[cwd].append(('D', dir_name, 0))
        else:
            size, filename = int(values[0]), values[1]
            fs[cwd].append(('F', filename, size))

    return fs

def count_filesystem_r(files, cwd, sizes):
    for ftype, fname, fsize in files[cwd]:
        if ftype == 'F':
            sizes[cwd] += fsize
        else:
            if cwd == '/':
                path = cwd + fname
            else:
                path = cwd + '/' + fname
            count_filesystem_r(files, path, sizes)
            sizes[cwd] += sizes[path]

    return sizes

def main():
    files = read_input()
    sizes = collections.defaultdict(int)
    count_filesystem_r(files, '/', sizes)
    print(f'Result: {sum([size for size in sizes.values() if size <= 100000])}')

if __name__ == '__main__':
    main()

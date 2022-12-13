#!/usr/bin/env python3

import sys
import collections

def read_input():
    fs = collections.defaultdict(list)
    cwd = '/'

    for line in sys.stdin:
        values = line.strip().split()

        if values[0] == '$' and values[1] == 'cd':
            if values[2] == '..': # If we're going up a dir, chop off the last part of the path
                cwd = '/'.join(cwd.split('/')[:-1])
            elif values[2] == '/' and cwd == '/': 
                pass
            else: # Otherwise add it on
                cwd += '/' + values[2]
        elif values[0] == '$' and values[1] == 'ls':
            pass
        elif values[0] == 'dir':
            dir_name = values[1]
            fs[cwd].append(('dir', dir_name, 0))
        else:
            size, filename = int(values[0]), values[1]
            fs[cwd].append(('file', filename, size))

    return fs

def calculate_size(files, cwd, result):
    print(cwd)
    total = 0
    for type, name, size in files[cwd]:
        #print(type, name, size)
        if type == 'file':
            total += size
        else:
            for entry in files[cwd]:
                size += calculate_size(files, '/' + entry[1], result)

    if total != 0:
        result.append(total)
    return total

def main():
    files = read_input()
    print(files)
    sizes = []
    calculate_size(files, '', sizes)
    print("Sizes: ", sizes)
    #print(f'Result: {sum([size for size in sizes if size <= 100000])}')

if __name__ == '__main__':
    main()

'''
$ cd /
$ ls
dir bfbjzfd
dir mbc
dir psqmv
dir qqpgw
59022 rrqzqwl.frp
dir sscj
dir vpfdwq
dir zzp
$ cd bfbjzfd
$ ls
125000 bmzjjgzc.dcr
dir brmgzjp
165351 hgm
dir rhrqttg
dir zfdc
$ cd brmgzjp
$ ls
298676 zzp.wrm
$ cd ..
$ cd rhrqttg
$ ls
dir hmz
dir hpcrbfq
$ cd hmz
$ ls
297949 lqcg
$ cd ..
'''
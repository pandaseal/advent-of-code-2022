from collections import defaultdict
from itertools import accumulate

# Comment: learned a lot by looking at others' solutions. Sometimes it do be like that.
def calc_directory_sizes():

    dirs = defaultdict(int)

    with open('input.txt') as f:
        for line in f:
            command = line.strip().split()

            match command:
                case '$', 'cd', '/':
                    path = ['/']
                case '$', 'cd', '..':
                    path.pop()
                case '$', 'cd', dir:
                    path.append(dir + '/')
                case '$', 'ls':
                    continue
                case 'dir', _:
                    continue
                case size, _:
                    # genious solution by https://github.com/viliampucik/adventofcode/blob/master/2022/07.py
                    for d in accumulate(path):
                        dirs[d] += int(size)

    return dirs

def main():
    dirs = calc_directory_sizes()

    # Find all of the directories with a total size of at most 100.000. 
    # What is the sum of the total sizes of those directories?
    print("Part 1:", sum(size for size in dirs.values() if size <= 100000))

    # Find the smallest directory that, if deleted, 
    # would free up enough space on the filesystem to run the update. 
    # What is the total size of that directory?
    free_space = 70000000 - dirs['/']
    needed_space = 30000000 - free_space
    print("Part 2:", min(size for size in dirs.values() if size >= needed_space))


if __name__ == "__main__":
    main()
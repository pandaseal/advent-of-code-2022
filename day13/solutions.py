import ast
from functools import cmp_to_key

def in_order(left, right) -> int:
    match left, right:
        # If both values are integers, 
        # ---
        # the lower integer should come first. 
        # If the left integer is lower than the right integer, 
        # the inputs are in the right order. 
        # If the left integer is higher than the right integer, 
        # the inputs are not in the right order. 
        # Otherwise, the inputs are the same integer; 
        # continue checking the next part of the input.
        case int(), int():
            if left < right:
                return 1
            elif left > right:
                return -1
            return 0
        # If both values are lists, 
        # ---
        # compare the first value of each list, 
        # then the second value, and so on. 
        # If the left list runs out of items first, 
        # the inputs are in the right order. 
        # If the right list runs out of items first, 
        # the inputs are not in the right order. 
        # If the lists are the same length 
        # and no comparison makes a decision about the order, 
        # continue checking the next part of the input.
        case list(), list():
            for result in map(in_order, left, right):
                if result:
                    return result
            return in_order(len(left), len(right))
        # If exactly one value is an integer, 
        # ---
        # convert the integer to a list 
        # which contains that integer as its only value, 
        # then retry the comparison. 
        case int(), list():
            return in_order([left], right)
        case list(), int():
            return in_order(left, [right])

def part1(filename="input.txt"):
    with open(filename) as f:
        pairs = [
            [ast.literal_eval(side) for side in pair.split("\n")] 
                 for pair in f.read().split("\n\n")
        ]
    pairs_in_order = []
    for i, pair in enumerate(pairs, 1):
        match in_order(pair[0], pair[1]):
            case 1 | 0:
                pairs_in_order.append(i)
    print("part 1:", sum(pairs_in_order))

def part2(filename="input.txt"):
    with open(filename) as f:
        packets = [ast.literal_eval(packet) for packet in f.read().split()]
    packets.extend([[[2]], [[6]]])

    packets = sorted(packets, key=cmp_to_key(in_order), reverse=True)

    idx1 = packets.index([[2]]) +1
    idx2 = packets.index([[6]]) +1
    decoder = idx1 * idx2
    print("part 2:", decoder)

if __name__ == "__main__":

    part1()
    part2()

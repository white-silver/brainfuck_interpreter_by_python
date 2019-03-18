import sys

# + : increment the memory's data
# - : decrement the memory's data
# [ : goto ']' if the memory is null(0)
# ] : goto '[' if the memory is not null
# . : output from the memory
# , : input to the memory
# > : increment memory position
# < : decrement memory position
mem_size = 30000
mem = [0 for i in range(mem_size)]
ptr = 0

if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    with open(path) as f:
        code = f.read()
    code_list = list(code)
    for i in range(code_list.count('\n')):
        code_list.remove('\n')

    head = 0 #reading program tape like a turing machine
    while head < len(code_list):
        if code_list[head] == '+':
            mem[ptr] += 1

        elif code_list[head] == '-':
            mem[ptr] -= 1

        elif code_list[head] == '[':
            #if pointer -> 0, break loop, jump to ]
            if mem[ptr] == 0:
                count = 1
                while count != 0:
                    head += 1
                    if head == len(code_list):
                        print("']' is missing")
                        sys.exit(1)
                    if code_list[head] == '[':
                        count += 1
                    elif code_list[head] == ']':
                        count -= 1
        elif code_list[head] == ']':
            #if pointer -x-> 0, jump to [
            if mem[ptr] != 0:
                count = 1
                while count != 0:
                    head -= 1
                    if head < 0:
                        print("'[' is missing")  
                    if code_list[head] == ']':
                        count += 1
                    elif code_list[head] == '[':
                        count -= 1
        elif code_list[head] == '.':
            #chr: char -> code point
            print(chr(mem[ptr]),end = "") #no line break
        elif code_list[head] == ',':
            #ord: code point -> char
            mem[ptr] = ord(sys.stdin.buffer.read(1))
        elif code_list[head] == '>':
            ptr += 1       
            if ptr > mem_size:
                print("overflow!")
                sys.exit(1)
        elif code_list[head] == "<":
            if ptr == 0:
                print("Can't decrement anymore")
            ptr -= 1

        head += 1    
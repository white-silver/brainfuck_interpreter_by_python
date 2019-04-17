import sys
import bf

if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    if len(args) <= 2:
        with open(path) as f:
            code = f.read()
        code_list = list(code) 
        bf.interpret(code)
    else:
        with open(path) as f:
            code = f.read()

        bf_der_path = args[2] #for brainfuck derivative codes
        with open(bf_der_path) as f:
            commands = f.readlines()
        commands = [i.strip('\n') for i in commands]
        commands_dict = bf.make_trans_dict(commands)

        op = ['>','<','+','-','.',',','[',']']
        for i in op:
            code = code.replace(commands_dict[i],i)
        bf.interpret(code)
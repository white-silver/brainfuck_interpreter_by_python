import sys
#+, オラ
#-, 無駄
#みたいな感じでコマンドが入ってくることを想定

def trans_to_bf(commands):
    commands_dict = {}
    for line in commands:
        item = line.split(':')
        #新コマンドをキーにしてもとのbrainfuck命令を呼び出す
        commands_dict[item[1]] = item[0]
    return commands_dict    

if __name__ == "__main__":
    args = sys.argv
    path = args[1]
    with open(path) as f:
        commands = f.readlines()
        commands = [i.strip('\n') for i in commands]
    commands_dict = trans_to_bf(commands)
    print(commands_dict)
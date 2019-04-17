# brainfuck_interpreter_by_python
## 使い方
```python3 bf_interpreter.py **.bf```  
とすると動きます。brainfuck derivativesを動かしたいときは、
```python3 bf_interpreter.py **.bf commands.txt```
のようにします。commands.txtはコマンドの対応表で、
```
>: Ook.Ook?                                                                                                  
<: Ook?OOK.
……
```
みたいなかたちで与えられることを想定しています。

## 中身
cormoran氏がC++で書いてたやつ（https://github.com/cormoran/BrainfuckInterpreter )をpython３で書き直したみたいな感じになってます。~~パクりました。~~  
いろいろなbrainfuck derivativesを動かせるようにしたりしました。

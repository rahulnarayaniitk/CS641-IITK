
from itertools import product
from pwn import *
from os import urandom
import pexpect
import random

#config
host = "172.27.26.188"
user = "students"
password = "cs641a"
team_name = 'INFINITY'
team_pass = 'godlike'


def enc(inp):
    out = ""
    for i in inp:
        out += chr(int(i, 16)+ord('f'))
    return out

# TO connect to the server and receive the required output for the inputs given


def conn_to_server():
    child = pexpect.spawn("ssh students@172.27.26.188")
    child.expect('password:')
    print('Entering Password')
    child.sendline("cs641a")
    print("Connected to sever")
    child.expect('Enter your group name')
    print('Entering Group Name')
    child.sendline("INFINITY")
    child.expect('Enter password')
    print('Entering team Password')
    child.sendline("godlike")
    child.expect('You have solved 5 levels so far.')
    print('Entering Level=5 to reach next level')
    child.sendline('5')

    child.expect('You are in a passage. There is very little light here.')
    child.sendline('go')
    child.expect('You bravely decide to go ahead. With slow and deliberate')
    child.sendline('wave')
    child.expect('Magically, your fall downwards is arrested! Almost in slow')
    child.sendline('dive')
    child.expect(
        'Diving under the water, you immediately notice mild yellowish')
    child.sendline('go')
    child.expect('You walk down the passage. After quite a long walk, the')
    child.sendline('read')
    child.expect('You come up to the closed door and look at the screen')
    # Sending Password to move to the main screen, where we can use input
    child.sendline('password')
    child.expect('Slowly, a new text starts appearing on the screen. It reads')
    child.sendline('c')
    # print("Password encrypted ", child.buffer)
    return child


def gen_inp():
    x = []
    for i in range(8):
        t = []
        for j in range(128):
            c = ['ff']*8
            c[i] = enc(hex(j)[2:].zfill(2))
            t.append(''.join(c))
        x.append(t)
    x = [' '.join(i) for i in x]
    x = '\n'.join(x)
    open('inputs.txt', 'w').write(x)


def get_cip(inp, child):
    child.expect('The text in the screen vanishes')
    child.sendline(inp)
    child.expect('Slowly, a new text starts appearing on the screen. It reads')
    child.sendline('c')
    my_string = child.buffer
    my_string = my_string.decode("utf-8")[:]
    text = my_string.split()
    if(len(text) > 1):
        return text[1]
    else:
        return "Blah"+inp  # Added Blah to find in the output.txt if any such value exists, this property is used later in easy_decrypt file


def get(child):
    a = (open('inputs.txt', 'r').read()+' ').split('\n')
    # Convert input into a list
    a = [i.split(' ') for i in a]
    # to remove last space in the last line
    a[7] = a[7][:-1]

    x = []
    for i in range(8):
        print(i)
        t = []
        for j in range(128):
            out = get_cip(a[i][j], child)
            t.append(out)
        x.append(t)
    x = [' '.join(i) for i in x]
    x = '\n'.join(x)
    open('outputs.txt', 'w').write(x)


if __name__ == '__main__':
    print("-"*50)
    print("Generating inputs....")
    gen_inp()
    print("Inputs Generated")
    print("-"*50)
    print("Connecting to server...")
    io = conn_to_server()
    print("-"*50)
    print("Using inputs.txt to generate the output.txt")
    get(io)
    print("Output.txt Generated")
    print("-"*50)
    print("Please proceed to run break_cipher.py")
    io.close()

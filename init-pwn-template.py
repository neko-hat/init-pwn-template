import sys

def main(file_name : str, target_name : str, libc : str):
    code = f"""
from pwn import *
import sys

def slog(k, v): return success(' : '.join([k, v]))
def clog(k, v): return log.critical(' : '.join([k, v]))

mode = 'debug'
if sys.argv[1] == "":
    mode = 'debug'
else:
    mode = sys.argv[1]
    
e = ELF('{target_name}')
#libc = ELF('{libc}')

if mode == 'debug':
    p = e.process()
    gdb.attach(p, gdbscript='''
''')
elif mode == "local":
    p = e.process()
else:
    p = remote('')

context.log_level = 'debug'

p.interactive()
"""
    with open(f"{file_name}", 'w') as f:
        f.write(code)

if __name__ == '__main__':
    option_handle_list = ['--o', '--binary', '--b', '--libc']
    options = {}
    
    if '--help' in sys.argv:
        print("usage : ./setup_ex_template --o <file name> --binary(--b) <target binary>  --libc <libc>")
        exit(0)

    for option_handle in option_handle_list:
        options[option_handle[2:]] = sys.argv[sys.argv.index(option_handle) + 1] if option_handle in sys.argv else None
    file_name = 'exploit.py'
    target_name = './example'
    libc = '/usr/lib/libc.so.6'
    
    if options['binary'] != None:
        target_name = options['binary']
    if options['b'] != None:
        target_name = options['b']
    if options['o'] != None:
        file_name = options['o']
    if options['libc'] != None:
        libc = options['libc']

    main(file_name, target_name, libc)


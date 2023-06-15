# init-pwn-template

## usage

```bash
./initpt --o <file name> --binary(--b) <target binary>  --libc <libc>
```
### setup
```bash
./setup.sh
```

## purpose
**`It automatically creates a troublesome exploit code structure every time`**

## Auto-generated code
```py
from pwn import *
import sys

def slog(k, v): return success(' : '.join([k, v]))
def clog(k, v): return log.critical(' : '.join([k, v]))

mode = 'debug'
if sys.argv[1] == "":
    mode = 'debug'
else:
    mode = sys.argv[1]
    
e = ELF('')
#libc = ELF('')

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
```

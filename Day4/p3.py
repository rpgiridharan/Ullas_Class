#Problem: Given IP address in binary as 32-bit number, convert to dotted-decimal notation
s = "1" * 32 # '111111111...111'
# O/P: '255.255.255.255'
# ipaddress : module

# s[0:8]
# s[8:16]
# s[16:24]
# s[24:32]

# [s[i:i+8] for i in range(0,32,8)]

# ['11111111', '11111111', '11111111', '11111111']
#
#[ int(s[i:i+8],2) for i in range(0,32,8)]
# [255, 255, 255, 255]
# [str(int(s[i:i+8],2)) for i in range(0,32,8)]
# ['255', '255', '255', '255']
# ".".join([str(int(s[i:i+8],2)) for i in range(0,32,8)])

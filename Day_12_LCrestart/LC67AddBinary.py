def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # abin = ''.join(format(ord(i), '08b') for i in a)
        # # treats each character as a character from ASCII and 
        # # converts it to an 8-bit binary string
        # bbin = ''.join((format(ord(i), '08b') for i in b)

        # sum = abin + bbin

        # return str(sum)

        x = int(a, 2)
        #converts BINARY string into int
        y = int(b, 2)
        sumxy = x + y
        sumxy = bin(sumxy)
        print(sumxy)
        #converts it back into binary, but adds a 0b at the beginning
        
        return sumxy[2:]

result = addBinary("11", "1")
print(result)

'''
TRACING :

x = int(a, 2)
int(value, base)
value - number or a string that can be converted into an integer number
base - number representing number format, default = 10

so I am converting "a" into decimal(considering it as binary as specified with the base 2)
next convert b into decimal

add those two

convert it back into binary. 
but, it will give the result as 0b10101.
So that is why we need to remove the first two indices and return only the numbers, 
and hence we are returning sumxy[2:]
'''

def addBinary2(a, b):
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
                if i >= 0:
                        carry = carry + int(a[i])
                        i = i - 1
                
                if j >= 0:
                        carry = carry + int(b[i])
                        j = j - 1
                
                s.append(str(carry % 2))
                carry = carry // 2

        return ''.join(reversed(s))

result2 = addBinary2("11", "1")
print(result2)

'''
TRACING :

a = '11'
b = '1'

s = []
i = len(a) - 1 -> len(a) = 2 
i = 2 - 1 -> 1
i = 1

j = len(b) - 1 -> len(b) = 1
j = 1 - 1 -> 0
j = 0

while i >= 0 or j >= 0 or carry:
        (or carry means, if carry = 0, then don't go inside loop )
        i = 1 -> true, goes inside

        if i >= 0:
                carry = carry + int(a[i])
                carry = 0 + int(a[1]) -> 0 + int('1')
                carry = 1
                i = i - 1 -> 1 - 1
                i = 0

        if j >= 0:
                carry = carry + int(b[j])
                carry = 1 + int(b[j]) -> 1 + int('1')
                carry = 2
                j = j - 1 -> 0 - 1
                j = -1
        
        s.append(str(carry % 2))
        s.append(str(2 % 2)) -> 0
        s.append(str(0))

        s = ['0']

        carry = carry // 2
        carry = 2 // 2 -> 1
        carry = 1

while i >= 0 or j >= 0 or carry:
        i = 0, j = -1, carry = 1

        if i >= 0:
                carry = carry + int(a[i]) -> carry + int(a[0])
                carry = 1 + int('1')
                carry = 2
                i = i - 1 -> 0 - 1
                i = -1
        
        if j >= 0:
                -> false, j = -1

        s.append(str(carry % 2))
        s.append(str(2 % 2))
        s.append(str(0))

        s = ['0', '0']

        carry = carry // 2
        carry = 2 // 2
        carry = 1

while i >= 0 or j >= 0 or carry:
        i = -1
        j = -1
        carry = 1 -> true

        i >= 0 
                -> false
        
        j >= 0 
                -> false

        s.append(str(carry % 2))
        s.append(str(1 % 2)) -> 1
        s.append(1)

        s = ['0', '0', '1']

        carry = carry // 2
        carry = 1 // 2
        carry = 0

while i >= 0 or j >= 0 or carry:
        i = -1
        j = -1
        carry = 0

        outside

return ''.join(reversed(s))

Result: '0' + '0' + '1' → '001'

reversed('001')
 
Output = 100






        

'''

                        
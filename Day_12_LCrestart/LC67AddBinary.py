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
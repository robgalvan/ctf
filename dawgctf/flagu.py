class EmptyStackError(Exception):
    def __init__(self):
        super().__init__("Stack is empty: cannot pop from an empty stack!")


class FullStackError(Exception):
    def __init__(self):
        super().__init__("Stack is full: cannot push to a full stack!")


# A simple stack in python with ints.
class Stack:
    def __init__(self, max_size=16):
        self.max_size = max_size
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True

    def is_full(self):
        if len(self.data) == self.max_size:
            return True

    def push(self, data):
        if not self.is_full():
            self.data.append(data)
            return data
        else:
            raise FullStackError()

    def pop(self):
        if not self.is_empty():
            output = self.data[len(self.data) - 1]
            del self.data[len(self.data) - 1]
            return output
        else:
            raise EmptyStackError()





def main():
    ba = {0,0,0,0,0,0,0,0}
    ca = {0,0,0,0,0,0,0,0}
    ma = {0,0,0,0,0,0,0,0}
    stack = Stack()
    stack.max_size = 512

    with open("flagulator", "rb") as binary_file:
        z = 0
        while True:
            z = z + 1
            d = binary_file.read(1)
            # print(d)
            # print("sizeof(stack): " + str(stack.)
            if d.hex() == "00":
                # print("00")
                break
            elif d.hex() == "10":
                e = binary_file.read(1).hex()
                # print("push: " + str(int("0x"+e, 16)))
                stack.push(int("0x" + e, 16))
            elif d.hex() == "11":
                # print("11")
                # print("discarded: " + binary_file.read(1))
                stack.pop()
            elif d.hex() == "04":
                # print("sub a: " + str(a) + " b: " + str(b) + " diff: " + str((a + b)%256))
                a = stack.pop()
                b = stack.pop()
                stack.push((a + b) % 256)
            elif d.hex() == "05":
                a = stack.pop()
                b = stack.pop()
                # print(a)
                # print(b)
                # print("sub a: " + str(a) + " b: " + str(b) + " diff: " + str((a - b + 256) %255))
                stack.push((a-b + 256) % 256)
            elif d.hex() == "06":
                # print("06")
                a = stack.pop()
                b = stack.pop()
                stack.push(a*b)
            elif d.hex() == "07":
                # print("xor a: " + str(a) + " b: " + str(b) + "xor: " + str(a^b))
                a = stack.pop()
                b = stack.pop()
                stack.push(a^b)
            elif d.hex() == "42":
                # print("42")
                g = stack.pop()
                print(chr(g))
if __name__ == "__main__":
    main()
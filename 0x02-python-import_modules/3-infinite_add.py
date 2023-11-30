#!/usr/bin/python3
if __name__ == "__main__":
    import sys
sum = 0
length = len(sys.argv)
for i in range(1, length):
    sum += int(sys.argv[i])
    print("{}".format(sum))

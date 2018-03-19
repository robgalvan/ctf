def solution(input_data):
    result=""
    for i in range(0,256):
        result+="NEXT KEY"
        for ch in input_data:
            result+= chr(ord(ch) ^ i)
    return result

def main():
    input_data = open('enc', 'r').read()
    result_data=''
    result_data=solution(input_data)
    out_file = open("solution.txt", 'w')
    out_file.write(result_data)
    out_file.close()

main()

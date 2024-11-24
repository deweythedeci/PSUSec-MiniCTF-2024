def check_flag(flag):
    if(len(flag) != 13):
        return False
    if(ord(flag[11]) + 12 * 3 - 4 != 95):
        return False
    if(ord(flag[0]) % 100 - 3 != -1):
        return False
    if(ord(flag[1]) >> 2 != 26):
        return False
    if(ord(flag[4]) + 27 != 150):
        return False
    if(ord(flag[12]) - 24 / 3 != 117):
        return False
    if(ord(flag[6]) ** 2 != 2601):
        return False
    if((ord(flag[7]) - 55 * 2) * -1 != 43):
        return False
    if(~ord(flag[3]) != -104):
        return False
    if(ord(flag[5]) + ord(flag[2]) != 133):
        return False
    if(ord(flag[8]) + ord(flag[9]) != 166):
        return False
    if(ord(flag[10]) + -1 * ord(flag[9]) != 64):
        return False
    if(ord(flag[8]) - ord(flag[10]) != -2):
        return False
    if(ord(flag[2]) != 0x61):
        return False
    return True

def main():
    flag = input("Enter the flag: ")

    if check_flag(flag):
        print("You got it!")
    else:
        print("That's not it.")

if __name__ == "__main__":
    main()
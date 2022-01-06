'''cross platform clear screen'''
import os

def main():
    if os.name == 'windows':
        os.system('cls')
    else:
        os.system('clear')
if __name__ == '__main__':
    main()

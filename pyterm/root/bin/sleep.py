'''waits for specifed amount of time in seconds'''
import time

def main():
    if len(argv) == 2:
        try:
            if argv[1] == '-0':
                raise ValueError
            time.sleep(float(argv[1]))
        except OverflowError:
            print(f'sleep: {argv[1]} is too large')
        except ValueError:
            print(f'sleep: {argv[1]} is not a  valid time')
    elif len(argv) > 2:
        print('too many arguments')
    else:
        print(f'sleep: no argument was provided')
if __name__ == '__main__':
    main()

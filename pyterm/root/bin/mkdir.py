'''makes a directory'''
import os


def main():
    if len(argv)<2:
        print('mkdir: missing operand')
        
    else:
        file = os.path.join(workingDir,argv[1])
        pathWhead = os.path.split(file)
        if os.path.exists(pathWhead[0]):
            if os.path.exists(file):
                print(f'mkdir: cannot create directory {pathWhead[1]} file exist')
            else:
                os.mkdir(file)
        else:
            print(f'mkdir: cannot create directory {pathWhead[1]} no such file or directory')
if __name__ == '__main__':
    main()

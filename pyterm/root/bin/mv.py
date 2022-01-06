'''cross platform move'''
import os
import shutil

def main():
    if len(argv) == 3:
        path1 = os.path.join(workingDir,argv[1])
        path2 = os.path.join(workingDir,argv[2])
        if os.path.exists(path1) and os.path.exists(path2):
            shutil.move(path1,path2)
        elif not(os.path.exists(path1)) and  not(os.path.exists(path2)):
            print(f'mv:paths {path1} and  {path2} do not exist')
        elif not os.path.exists(path1):
            print(f'mv:path {path1} does not exist')
        elif not os.path.exists(path2):
            print(f'mv:path {path2} does not exist')
    elif len(argv) <= 2:
        print('mv:mising arguments needs source and destination')
    else:
        print('mv:too many args')

if __name__ == '__main__':
    main()
    del main

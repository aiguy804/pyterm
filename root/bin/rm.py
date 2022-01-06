'''remove file'''
import os

def main():
    if len(argv)<2:
        print('no file spesified')
        
    else:
        fileName = os.path.join(workingDir,argv[1])
        if os.path.exists(fileName):
            if os.path.isfile(fileName):
                os.remove(fileName)
            else:
                os.rmdir(fileName)
        else:
            print("The file was not found or does not exist")
if __name__ == '__main__':
    main()

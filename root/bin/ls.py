"""lists directorys and files in the curent path"""
#simple ls
import os
import colorama

def main():
    colorama.init()
    for i in os.listdir(workingDir):
        iFull = os.path.join(workingDir,i)
        if os.path.isfile(iFull):
            if '.py' == i[-3:]:
                color = colorama.Fore.RED
            else:
                color = colorama.Fore.GREEN
        elif os.path.isdir(iFull):
            color = colorama.Fore.BLUE
        else:
            color = ''
        print(color + i + colorama.Style.RESET_ALL)
if __name__ == '__main__':
    main()

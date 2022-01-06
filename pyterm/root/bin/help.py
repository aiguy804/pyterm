'''shows all programs and gives there docs'''
import os
import runpy


def main():
    if len(argv) == 2:
        path = None
        if os.path.exists(os.path.join(workingDir,argv[1])):
            path = os.path.join(workingDir,argv[1])
        elif os.path.exists(os.path.join(PATH,argv[1] + '.py')):
            path = os.path.join(PATH,argv[1]+'.py')
        elif os.path.exists(os.path.join(PATH,argv[1])):
            path = os.path.join(PATH,argv[1])
        else:
            print(f'help:{argv[1]} command not found')
        
        if path != None:
            globa = {'argv':[argv[1]],'PATH':PATH,'workingDir':workingDir}
            doc = runpy.run_path(path,init_globals = globa,run_name = "__None__")['__doc__']
            if doc == None:
                print(f'help:there is no doucumentation for {argv[1]}')
            else:
                print(doc)
    elif len(argv) >= 3:
        print('help:too many arguments')
    else:
        programs = []
        for i in  os.listdir(PATH):
            programs.append(i[:-3])
        print('\n'.join(programs))
if __name__ == '__main__':
    main()

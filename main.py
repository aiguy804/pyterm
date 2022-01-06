import os
import runpy

print('no')
PATH = './root/bin'
workingDir = './root/home'
history = []


#runs a python file with provided arguments
def run(filePath, args=[]):
    "runs a python file with provided arguments"
    fileName = os.path.split(filePath)[1]
    globa = {'argv': [fileName] + args, 'PATH': PATH, 'workingDir': workingDir, 'history': history}
    runpy.run_path(filePath, init_globals=globa, run_name="__main__")


variables = {'~': './root/home','~~': './root'}
while True:
    workingDirOut = workingDir.replace('./root/home', '~').replace('./root','/root')
    comandWargs = input(f'pyterm@python:{workingDirOut}$')
    for i in variables.keys():
        comandWargs = comandWargs.replace(i, variables[i])
    comandWargs = comandWargs.split(' ')
    comand = comandWargs[0] 
    args = comandWargs[1:]
    history.append(comand)
    if comand == '':
        history = history[:-1]
        pass
    elif os.path.isfile(os.path.join(workingDir, comand)):
        run(os.path.join(workingDir, comand), args)
    elif os.path.isfile(os.path.join(PATH, comand + '.py')):
        run(os.path.join(PATH, comand + '.py'), args)
    elif os.path.isfile(os.path.join(PATH, comand)):
        run(os.path.join(PATH, comand), args)
    elif (os.path.isdir(os.path.join(workingDir, comand))
          or (os.path.normpath(comand) == os.path.normpath('./root'))):
        if os.path.normpath(comand) == os.path.normpath('./root'):
            print('bash: root: is a dir')
        else:
            print(f'bash: {comand}: is a dir')
    else:
        print(f'bash: {comand}: command not found')

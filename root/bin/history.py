'''shows history of commands'''

def main():
    history = []
    #yay! spaghetti code
    #can be optimized
    print('\n'.join(['  '+str(i+1)+'  '+history[i] for i in range(len(history))]))

if __name__ == '__main__':
    main()
    del main

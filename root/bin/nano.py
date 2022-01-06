'''text editor'''
import curses



def main():
    stdscr = curses.initscr()
    #stdscr.nodelay(True)
    curses.echo(False)
    stdscr.keypad(True)
    curses.curs_set(0)
    stdscr.clear()
    current = ''
    pointer = '|'
    pos = 0
    stdscr.addstr(pointer)
    while True:
      char = stdscr.getch()
      if char == 263: #backspace
        if (pos != 0):
          current = current[:pos-1] + current[pos:]
          pos -= 1
      elif char == 260:#left arrow key
        if (pos != 0):
          pos -= 1
      elif char == 261:#right arrow key
        pos += 1
      elif char == 259:#up arrow key
        pass
      elif char == 258:#down arrow key
        pass
      elif char == 27:#esc key
        
        #compleetly remove every var
        del char
        del pointer
        del current
        del stdscr
        del pos
        curses.endwin()
        break
      else:
        current = current[:pos] + chr(char) + current[pos:]
        pos += 1
      stdscr.clear()
      stdscr.addstr(current[:pos]+ pointer + current[pos:])
      stdscr.addstr(str(char)) #prints the char code, used for debug
if __name__ == '__main__':
    main()
    del main

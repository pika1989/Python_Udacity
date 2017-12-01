import time
import webbrowser


total_breaks = 3
break_count = 0
work_time = 2 * 60 * 60

print 'This program started on %s' % (time.ctime())
while (break_count < total_breaks):
    time.sleep(work_time)
    webbrowser.open('https://www.youtube.com/watch?v=djV11Xbc914')
    break_count = break_count + 1

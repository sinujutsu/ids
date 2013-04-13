#! /usr/bin/env python
# adapted code from http://stackoverflow.com/questions/6005082/python-2-6-problem-capturing-output-from-tcpdump-subprocess

import subprocess, time
# import fcntl, os

def tcpdump():

    # sudo tcpdump -i en0 -n -s 0 -w - | grep -a -o -E "Host\: .*|GET \/.*"
    cmd1 = ['sudo', 'tcpdump', '-v']
    cmd2 = ['grep', '-a', '-o', '-E', 'Host\: .*|GET \/.*']

    p1 = subprocess.Popen( cmd1 )
    # p1 = subprocess.check_output( cmd1 )
    # p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    # p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stdin=p1.stdout)

    # set stdout file descriptor to nonblocking
    # flags = \
    # fcntl.fcntl(p1.stdout.fileno(), fcntl.F_GETFL)
    # fcntl.fcntl(p1.stdout.fileno(), fcntl.F_SETFL, (flags | os.O_NDELAY | os.O_NONBLOCK))

    return p1



if __name__ == "__main__":
    dumpProcess = tcpdump()
    # time.sleep(10)
    print( dumpProcess.communicate()[1] )
    dumpProcess.terminate()
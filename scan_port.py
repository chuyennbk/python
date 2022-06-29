import optparse
import socket
from socket import *
from threading import *
def connScan(tgtHost, tgtPort):
    try:
        connSkt  =  socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        results  =  connSkt.recv(100)
        print ('[ + ]%d/tcp open'% tgtPort)
        print ('[ + ] '  +  str(results))
        connSkt.close()
    except:
        print ('[-]%d/tcp closed'% tgtPort)
def portScan(tgtHost, tgtPorts):
    print ('Here1')
    try:
        tgtIP  =  gethostbyname(tgtHost)
    except:
        print ("[-] Cannot resolve '%s': Unknown host" %tgtHost)
        return
    try:
        tgtName  =  gethostbyaddr(tgtIP)
        print ('\n[ + ] Scan Results for: '  +  tgtName[0])
    except:
        print ('\n[ + ] Scan Results for: '  +  tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print ('Scanning port '  +  tgtPort)
        connScan(tgtHost, int(tgtPort))
def portScanAll(tgtHost):
    print ('Here1')
    # try:
    #     tgtIP  =  gethostbyname(tgtHost)
    # except:
    #     print ("[-] Cannot resolve '%s': Unknown host" %tgtHost)
    #     return
    # try:
    #     print ('\n[ + ] Scan Results for: ', tgtIP)
    # except:
    #     print ('\n[ + ] Scan Results for: ',  tgtIP)
    setdefaulttimeout(1)
    for ip2 in range(1,255):
        for tgtPort in range(1,100):
            t  =  Thread(target = connScan, args = (tgtHost+str(ip2), int(tgtPort)))
            t.start()
        #print ('Scanning port ', tgtPort)
        #connScan(tgtHost, int(tgtPort))
def main():
    parser  =  optparse.OptionParser("usage%prog " + "-H <target host> -p <target port>")
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'string', help = 'specify target port[s] separated by comma')
    (options, args)  =  parser.parse_args()
    tgtHost  =  options.tgtHost
    tgtPorts  =  str(options.tgtPort).split(',')
    if (tgtHost  ==  None) | (tgtPorts[0]  ==  None):
        print ('[-] You must specify a target host and port[s].')
        exit(0)
    #portScan(tgtHost, tgtPorts)
    portScanAll(tgtHost)
if __name__  ==  '__main__':
  main()
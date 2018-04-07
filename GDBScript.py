#Author: SAMIR Radouane
#Date: 14/08/2016

import gdb
import os

class SAVANTGdbTools:
        """ This command is created to help me to show the path
            open by fopen function. It's get the address from the
            (info locals) path variable and call 'po address'
        """
        countfile = ''
        gdbfile = ''
        def __init__(self):
                #super (showPath, self).__init__(gdb.BP_BREAKPOINT,internal=True)
                #gdbfile = open("GDB.txt", "r")
                countfile = open("COUNTER.txt", "w")
                countfile.write("0")
                countfile.close()
                return

        def changeRegisters(self, event):

                print event.breakpoint.location
                #*********** Gathering and initializing **********#
                gdb.execute("set logging off")
                registers = gdb.execute("info reg", False, True)
                lines = registers.split('\n', 1)
                #*************************************************#

                print  "Crack Running ..."
                eax = lines[0] #Get eax line
                eax_checkAuth = eax[-3:] #Get the last number to test it out
                eax_license = eax[-1:]

                countfile = open('COUNTER.txt', 'r')
                counter = countfile.read()
                countfile.close()
                print "Counter Env: " + str(counter)

                if (eax_checkAuth == '-84'):
                        if (counter == '0'):
                                #gdb.execute("set $eax=10000")
                                print "-84 detected"
                                gdb.execute("set $eax=10000")
                                countfile = open("COUNTER.txt","w")
                                countfile.write('1')
                                countfile.close()
                        else:
                                print "Second -84 detected"
                                gdb.execute("set $eax=-4")
                                countfile = open("COUNTER.txt","w")
                                countfile.write('0')
                                countfile.close()

                '''if (eax_license == '0'):
                        print "zero detected"
                        gdb.execute("set $eax=0x1")
                '''
                #*****  Test mechanism to stop the script *****#
                ''' 
                    I create a file GDB.txt that will contain 0 or 1. 
                    This will allow to stop the script 
                '''
                gdbfile = open("GDB.txt","r")
                isStop = gdbfile.read()
                gdbfile.close()
                print "GDB env: " + isStop

                if (isStop[0] == '1'):
                        print ("continue ...") #.format(isStop))
                        gdb.execute("set pagination off")
                        gdb.execute("continue")
                if (isStop[0] == '0'):
                        print ("Stop script ...") #.format(isStop))
                        gdb.execute("set pagination on")
                        gdb.events.stop.disconnect(self.changeRegisters)
                #**********************************************#

        def printPaths(self, event):
                #show the path returned by info locals' path
                #frame = gdb.selected_frame()
                gdb.execute("set logging off")
                registers = gdb.execute("info reg", False, True)
                eax = registers.split('\n', 1)

                print "Registers list"
                print eax[:-3]
                gdb.execute("set logging on")
                #gdb.execute("set $eax=10000", False, False)
                #gdb.execute("finish", False, False)
                #gdb.execute("set $eax=1", False, False)
                #finish_cmd = gdb.execute("finish", False, True)
                #path = frame.read_var("path")
                #print "****** OUTPUTS ********"
                #print "Finish: " + str(finish_cmd)
                #print "Path var: " + str(path)
                #print "***********************"

                gdb.events.stop.disconnect(self.printPaths)

        def disconnect_function(self, function):
                gdb.events.stop.disconnect(function)

        def connect_function(self, function):
                gdb.events.stop.connect(function)

tools = SAVANTGdbTools()
gdb.events.stop.connect(tools.changeRegisters)

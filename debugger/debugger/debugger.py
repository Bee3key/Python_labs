__author__ = 'fkuts'

from ctypes import *
from debugg_define import *

#PROCESS_ALL_ACCESS = (0x000F0000L | 0x00100000L | 0xFFF)

kernel32 = windll.kernel32

class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        #creation_flags = CREATE_NEW_CONSOLE

        startUpInfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        startUpInfo.dwFlags = 0x1
        startUpInfo.wShowWindow = 0x0

        startUpInfo.cb = sizeof(startUpInfo)

        if kernel32.CreateProcessA(
            path_to_exe,
            None,
            None,
            None,
            None,
            creation_flags,
            None,
            None,
            byref(startUpInfo),
            byref(process_information)
        ):
            print "[*] We have successfully launched the process!"
            print "[*] PID: %d" %process_information.dwProcessId

            #Obtain a valid handle to the newly created process
            # and store it for future access

            self.h_process = self.open_process(process_information.dwProcessId)

        else:
            print "[*] Error: 0x%08x." %kernel32.GetLastError()

    def open_process(self, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS,False, pid)
        return h_process

    def attach(self, pid):
        self.h_process = self.open_process(pid)

        if kernel32.DebugActiveProcess(pid):
            print "[*] Debugger active"
            self.debugger_active = True
            self.pid = int (pid)
            #self.run()

        else:
            print "[*] Unable to attach to the process"

    def run(self):
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):

        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE

        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
            #raw_input("Press a key")
            #self.debugger_active = False
            kernel32.ContinueDebugEvent( debug_event.dwProcessId, debug_event.dwThreadId, continue_status )

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print "Finishing..."
            return True
        else:
            print "There was an error"
            print "[*] Error: 0x%08x." %kernel32.GetLastError()
            return False


    def open_thread(self, thread_id):
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, thread_id)
        if h_thread is not None:
            return h_thread
        else:
            print "[] Couldn't obtain valid tread handle"
            return False

    def enumerate_thread(self):
        print "[+] Ennumerate thread func starts here"
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)

        if snapshot is not None:
            print "[+] snapshot is not None"
            thread_entry.dwSize = sizeof(thread_entry)
            success = kernel32.Thread32First(snapshot, byref(thread_entry))
            print success

            while success:
                print thread_entry.th32OwnerProcessID
                print "Self pid: %d" % self.pid
                if thread_entry.th32OwnerProcessID == self.pid:
                    print thread_entry.th32ThreadID
                    thread_list.append(thread_entry.th32ThreadID)
                    success = kernel32.Thread32Next(snapshot, byref(thread_entry))
                    print success
            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            print "[-] snapshot is not not None"
            return False


    def get_thread_context(self,thread_id=None, h_thread=None):
        print "[+] get thread func starts here "

        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS

        if not h_thread:
            self.open_thread(thread_id)

        h_thread = self.open_thread(thread_id)
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            return False



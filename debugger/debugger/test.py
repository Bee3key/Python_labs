__author__ = 'Bee3Key'

import debugger

d = debugger.debugger()

pid = raw_input("Enter a pid: ")

d.attach(int(pid))

list_ = d.enumerate_thread()

for thread in list_:
    thread_context = d.get_thread_context(thread)
# Now let's output the contents of some of the registers
    print "[*] Dumping registers for thread ID: 0x%08x" % thread
    print "[**] EIP: 0x%08x" % thread_context.Eip
    print "[**] ESP: 0x%08x" % thread_context.Esp
    print "[**] EBP: 0x%08x" % thread_context.Ebp
    print "[**] EAX: 0x%08x" % thread_context.Eax
    print "[**] EBX: 0x%08x" % thread_context.Ebx
    print "[**] ECX: 0x%08x" % thread_context.Ecx
    print "[**] EDX: 0x%08x" % thread_context.Edx
    print "[*] END DUMP"

d.detach()


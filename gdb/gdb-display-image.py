import gdb
import ctypes
import Image

class Disp(gdb.Command):
  def __init__ (self):
    super (Disp, self).__init__("alpha",
                                 gdb.COMMAND_SUPPORT,
                                 gdb.COMPLETE_NONE, True)

  def invoke (self, arg, from_tty):
    args = arg.split(", ")
    byte = gdb.parse_and_eval(args[0])
    stride = int(gdb.parse_and_eval(args[1]))
    height = int(gdb.parse_and_eval(args[2]))

    pix_clr = (ctypes.c_ubyte*(stride * height))()

    print "start list"

    print "started copying"

    for i in xrange(0, stride * height):
      pix_clr[i] = byte[i]

    print "copying done."

    image = Image.fromstring("L", [stride, height], pix_clr)
    image.show()

Disp()

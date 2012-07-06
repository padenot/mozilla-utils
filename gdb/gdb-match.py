import gdb
import re

class Match(gdb.Command):
  '''Matches a regex against the stack trace of the threads'''
  def __init__ (self):
      super (Match, self).__init__ ("match",
                                                     gdb.COMMAND_SUPPORT,
                                                     gdb.COMPLETE_NONE, True)

  def invoke (self, arg, from_tty):
    thread = gdb.selected_thread()
    if thread == None:
      print 'No thread selected.'
      return

    for thread in gdb.inferiors():
      frame = gdb.newest_frame()
      while frame:
        # if that matches our regexp, select that.
        try:
          match = re.match(arg, frame.name(), flags=re.IGNORECASE)
        except Exception, e:
          print "Error: invalid regex: %s" % str(e)
          return

        if match:
          sal = frame.find_sal()
          print "Found: %s, thread %s, file %s:%s, in function %s" % (frame.name(), thread.num,sal.symtab.filename, sal.line, frame.function())
          frame.select()
          return

        frame = frame.older()
        if not frame:
          return

    thread.switch()

Match()

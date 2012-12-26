import sublime, sublime_plugin
import subprocess as sp
import os

class GnomeTerminalCommand(sublime_plugin.TextCommand):
    def run(self, edit,prog):
        '''prog is the full path to the program to be executed with sp.Popen() and the run_linux_program_sub script'''
        if self.view.file_name():
            #print self.view.file_name()
            cmd=['gnome-terminal','-x','/home/admalledd/bin/run_linux_program_sub']
            dir=os.path.realpath(os.path.split(self.view.file_name())[0])+'/'
            #print dir
            cmd.append(dir)
            cmd.append(prog)
            cmd.append(self.view.file_name())
            sublime.status_message('running pypy file')
            p = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE)
        

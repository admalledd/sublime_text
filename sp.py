import sublime, sublime_plugin
import subprocess as sp
import os,sys
import fs.osfs

class subprocessCommand(sublime_plugin.TextCommand):
    def run(self, edit, exe,args=None ,fname=None, curdir=None):
        if fname == None:
            fname = self.view.file_name()
        if curdir ==None:
            curdir = os.path.dirname(fname)

        #print exe,fname,args
        #print sublime.packages_path()

        cmd=['start',"cmd.exe",'/C',os.path.join(sublime.packages_path(),'User','sp.bat'),exe,fname]
        if args is not None:
            cmd.append(*args)
        print sp.list2cmdline(cmd)
        proc = sp.Popen(cmd,cwd=curdir,shell=True)
class subprocess_buildCommand(sublime_plugin.WindowCommand):

    def run(self, exe=None,args=None ,fname=None, curdir=None,clean_localdir=None):
        if fname == None:
            fname = self.view.file_name()
        if curdir ==None:
            curdir = os.path.dirname(fname)

        print exe,fname,curdir
        if clean_localdir:
            #clean the local directory that is in %APPDATA%, $HOME/.config/ ect... (leaving root dir)
            if sys.platform == 'win32':
                rmcmd=["start","cmd.exe",'/C',os.path.join(sublime.packages_path(),'User','sp.bat'),
                        'C:\\cygwin\\bin\\rm','-rf',  os.path.expandvars('$APPDATA/revabotica/')]
                proc = sp.Popen(rmcmd,shell=True)
                import time
                time.sleep(2.5)
        cmd=['start',"cmd.exe",'/C',os.path.join(sublime.packages_path(),'User','sp.bat'),exe,fname]
        if args is not None:
            cmd.append(*args)
        print sp.list2cmdline(cmd)
        proc = sp.Popen(cmd,cwd=curdir,shell=True)
import sublime, sublime_plugin
import subprocess as sp
import os,sys

class subprocessCommand(sublime_plugin.TextCommand):
    def run(self, edit, exe,args=None ,fname=None, curdir=None):
        if fname == None:
            fname = self.view.file_name()
        runner(exe,fname,curdir,args)

class subprocess_buildCommand(sublime_plugin.WindowCommand):
    def run(self, exe,args=None ,fname=None, curdir=None):
        if fname == None:
            fname = self.view.file_name()
        runner(exe,fname,curdir,args)

def runner(exe,fname,curdir,args,clean_localdir=None,dat=None):
    if curdir ==None:
        curdir = os.path.dirname(fname)

    if sys.platform == "win32":
        cmd = [
                'start',
                "cmd.exe",
                '/C',
                os.path.join(sublime.packages_path(),'User','sp.bat'),
                exe,
                fname
              ]

    elif sys.platform in ("linux2","linux" ):
        cmd = [
                'xfce4-terminal',
                '-x',
                os.path.join(sublime.packages_path(),'User','run_linux_program_sub'),
                curdir+"/",
                exe,
                fname
              ]

    if args is not None:
        cmd.append(*args)
    print(sys.platform)
    print(sp.list2cmdline(cmd))
    sublime.status_message('running subprocess')

    if sys.platform == "win32":
        proc = sp.Popen(cmd,cwd=curdir,shell=True)
    elif sys.platform in ("linux2","linux" ):
        proc = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE)
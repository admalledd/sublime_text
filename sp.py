import sublime, sublime_plugin
import subprocess as sp
import os,sys

class subprocessCommand(sublime_plugin.TextCommand):
    def run(self, edit, exe,exe_args=None,args=None ,fname=None, curdir=None):
        if fname == None:
            fname = self.view.file_name()
        runner(exe,fname,curdir,exe_args,args)

class subprocess_buildCommand(sublime_plugin.WindowCommand):
    def run(self, exe,exe_args=None,args=None ,fname=None, curdir=None):
        if fname == None:
            fname = self.view.file_name()
        runner(exe,fname,curdir,exe_args,args)

def runner(exe,fname,curdir,exe_args,args,clean_localdir=None,dat=None):
    if curdir ==None:
        curdir = os.path.dirname(fname)

    if sys.platform == "win32":
        if exe_args is not None:
            exe = exe + '" "'+'" "'.join(exe_args)


        subcmd = '""'+os.path.join(sublime.packages_path(),'User','sp.bat')+'" "'+\
                exe+'" "'+\
                fname+'""'
        cmd = [
                'start',
                '/D',
                '"'+ curdir+'"',
                "cmd.exe",
                '/C',
                subcmd
              ]

    elif sys.platform in ("linux2","linux" ):
        cmd = [
                'gnome-terminal',
                '-x',
                os.path.join(sublime.packages_path(),'User','run_linux_program_sub'),
                curdir+"/",
                exe
              ]
        if exe_args is not None:
            cmd.appen(*exe_args)
        cmd.append(fname)
        if args is not None:
            cmd.append(*args)

    print(sys.platform)
    print(cmd)
    print(" ".join(cmd))
    sublime.status_message('running subprocess')

    if sys.platform == "win32":
        os.system(" ".join(cmd))
        #proc = sp.Popen(cmd,cwd=curdir)
    elif sys.platform in ("linux2","linux" ):
        proc = sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE)

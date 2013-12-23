import sublime, sublime_plugin


class keymapperCommand(sublime_plugin.TextCommand,sublime_plugin.WindowCommand):
    """Key Mapper, sadly you still have to define all the keymaps in your
    .sublime-keymap just point them all here that you want to be able to map around.

    this subclasses both TextCommand and WindowCommand so that it can be used for anything!

    in your project file have a new index called "keymapper", inside define keys as you would
    in a .sublime-keymap. Note again that these keys that are available are only the ones 
    that you pointed to run keymapper in your master keymap file.

    samples:::

    ** added to Default ($OS).sublime-keymap
        { "keys": ["ctrl+alt+r"], "command": "keymapper","args":{"key":"ctrl+alt+r"}}

    ** added to $PROJECT.sublime-project
        "keymapper":[
        { "keys": ["ctrl+alt+r"], "command": "subprocess", "args": {"exe": "/home/admalledd/bin/pypy3"}},
    ]

    Note that the .sublime-project sample is using one of my other plugins (sp.py/subprocess),
    just because it is all I really use the keymapper for...
    """
    def run(self,*args,key=None):
        if ((not sublime.active_window().project_file_name()) or 
                'keymapper' not in sublime.active_window().project_data()):
            print("keymapper: no project file found! aborting!")
            return False

        self.proj_keys = sublime.active_window().project_data()['keymapper']

        for keymap in self.proj_keys:
            if key in keymap['keys']:
                print('keymapper: found keybinding!')
                #here is where more complicated logics would go if more crazy is wanted
                return sublime.active_window().active_view().run_command(
                    keymap['command'],keymap['args']
                    )
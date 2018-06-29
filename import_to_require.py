# Sublime Text 2/3 plugin
# Transform seletion containing JavaScript's ES6 syntax `import ... from ...` to `const ... = require(...)`.
# 
# @example
# import react from 'react';
# // => const react = require('react');
# 
# import { foo } from 'react';
# // => const { foo } = require('react');
#
# Install
# 1. save as import_to_require.php
# 2. Tools -> Developer -> new Plugin
# 3. Preferences -> Key Bindings, insert { "keys": ["super+e"], "command": "import_to_require"}
# 
# {@link https://www.sublimetext.com/docs/3/api_reference.html#sublime.Selection}
# {@link http://stackoverflow.com/questions/18606682/how-can-i-open-command-line-prompt-from-sublime-in-windows7}
# {@link https://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685}

# replace in sublime
# import\s+([\{\s\w\-\},]+)\s+from\s+([\'"])([^\'\"]+)[\'"]
# const \1 = require(\2\3\2)

import re
import sublime
import sublime_plugin

class Text():
  @staticmethod
  def all(view):
    return view.substr(sublime.Region(0, view.size()))

  @staticmethod
  def sel(view):
    text = []
    for region in view.sel():
      if region.empty():
        continue
      text.append(view.substr(region))
    return "".join(text)

  @staticmethod
  def get(view):
    text = Text.sel(view)
    return text
    # if len(text) > 0:
    #   return text
    # return Text.all(view)

class ToRequireCommand(sublime_plugin.TextCommand):
    @staticmethod
    def importToRequire(import_str):
        print("import_str: " + import_str)
        return re.sub(r'import\s+([\s\S]+)\s+from\s+([\'"])([^\'\"]+)[\'"]', r'const \1 = require(\2\3\2)', import_str)

    def run(self, edit):
        view = self.view
        selection = Text.get(self.view)

        for region in view.sel():
            if not region.empty():
                self.view.replace(edit, region, ToRequireCommand.importToRequire(view.substr(region)))

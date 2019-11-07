import sublime
import sublime_plugin
import re
from meow.emojis import EMOJIS

class MeowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # self.view.insert(edit, 0, "Hello, World!")
        file_contents = self.view.substr(sublime.Region(0, self.view.size()))
        region = sublime.Region(0, self.view.size())
        self.view.replace(edit, region, self.emojify(file_contents))

    def emojify(self, file_contents):
        return self.multiple_replace(EMOJIS, file_contents)

    def multiple_replace(self, adict, text):
        # Create a regular expression from all of the dictionary keys
        regex = re.compile("|".join(map(re.escape, adict.keys(  ))))

        # For each match, look up the corresponding value in the dictionary
        return regex.sub(lambda match: adict[match.group(0)], text)



class MeowCompletionsListener(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        source = EMOJIS.keys()
        completions = [[key + " " + EMOJIS[key] , EMOJIS[key]] for key in source if prefix in key]
        if not completions:
            return None
        return completions

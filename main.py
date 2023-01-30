#!/usr/bin/python3

import re
import os
import sys
import time

from googletrans import Translator

global_input = ""
global_output = ""
global_languages = ["zh-cn", "eo", "ar"]
global_lang_out = "de"
global_timeout = 2

global_translator = Translator()


def print_help():
    print("usage: {} [OPTIONS]".format(sys.argv[0]))
    print("required options:")
    print("--input     <file> : Input language file to translate")
    print("--output    <file> : Output language file")
    print("optional options:")
    print("--lang-list <list> : List of languages to use")
    print("                     Default: \"ar, la, ja, zh-cn, de\"")
    print("--lang-out  <lang> : Final output language")
    print("--timeout  <delay> : Seconds between translations")
    sys.exit(0)


def parse_arguments():
    global global_input, global_output, global_languages, global_lang_out, global_timeout

    entry_last = ""
    for i, entry in enumerate(sys.argv):
        if entry_last == "--input":
            global_input = entry
        if entry_last == "--output":
            global_output = entry.split(".")[0]
            global_output = global_output + ".json"
        if entry_last == "--lang-list":
            global_languages = []
            for lang in entry.split(" "):
                global_languages.append(lang)
        if entry_last == "--lang-out":
            global_lang_out = entry
        if entry_last == "--timeout":
            global_timeout = int(entry)
        entry_last = entry
    
    if global_input.replace(" ","") == "": print_help()
    if global_output.replace(" ","") == "": print_help()
    if global_lang_out.replace(" ","") == "": print_help()
    if not global_languages: print_help()
    
    if not os.path.exists(global_input):
        print("Input file {} does not exist!".format(global_input))
        sys.exit(0)


def do_translate(text: str, languages: list, target_language: str, timeout: int, translator_instance: Translator) -> str:
    while languages[len(languages) - 1] == target_language:
        languages.remove(target_language)
    languages.append(target_language)

    for lang in global_languages:
        text = translator_instance.translate(text, dest=lang).text
        time.sleep(timeout)
    return text


def repair_string(text: str) -> str:
    for i in range(1, 10):
        search = "[" + 'A' * i +  "]"
        text = text.replace(search, "\\n")
        search = "[" + 'B' * i +  "]"
        text = text.replace(search, "%s")
    text = text.replace(" .", ".")
    text = text.replace(" !", "!")
    text = text.replace(" ?", "?")
    text = text.replace(" ,", ",")
    text = text.replace(" :", ":")
    text = text.replace(" ;", ";")
    text = text.replace(" )", ")")
    text = text.replace("( ", "(")
    text = text.replace(" ]", "]")
    text = text.replace("[ ", "[")
    text = text.replace(" }", "}")
    text = text.replace("{ ", "{")
    text = text.replace(" \\n", "\\n")
    text = text.replace("\\n ", "\\n")
    text = text.lstrip(" ")
    text = re.sub("\s\s+", " ", text)
    return text




def main():
    global global_input, global_output, global_languages, global_lang_out, global_timeout, global_translator

    parse_arguments()

    with open(global_input, "r") as file_in:
        with open(global_output, "w") as file_out:

            for i, line in enumerate(file_in):
                if line.startswith("{"):
                    file_out.write("{\n")
                elif line.startswith("}"):
                    file_out.write("\"\": \"\"\n")
                    file_out.write("}")
                else:
                    in_split = line.split("\": \"")
                    key = in_split[0].replace("\"", "")
                    key = key.lstrip(" ")

                    value = in_split[1].replace("\"", "")
                    value = value.replace("\\n", " [AAAAA] ")
                    value = value.replace("%s", " [BBBBB] ")
                    value = value.replace("\n", "")
                    value = value.replace(",", "")

                    value_old = value

                    value = do_translate(value, global_languages, global_lang_out, global_timeout, global_translator)
                    value = repair_string(value)

                    print("[{}] old: {}".format(str(i).center(10), value_old))
                    print("[{}] new: {}".format(len(str(i).center(10)) * " ", value))

                    file_out.write("\"{}\": \"{}\",\n".format(key, value))


if __name__ == '__main__':
    main()
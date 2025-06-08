"""Colorize text.

Available text colors:
    black, red, green, yellow, blue, magenta, cyan, white,
    light_grey, dark_grey, light_red, light_green, light_yellow, light_blue,
    light_magenta, light_cyan.

Available text highlights:
    on_black, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white,
    on_light_grey, on_dark_grey, on_light_red, on_light_green, on_light_yellow,
    on_light_blue, on_light_magenta, on_light_cyan.

Available attributes:
    bold, dark, underline, blink, reverse, concealed.

Example:
    colored('Hello, World!', 'red', 'on_black', ['bold', 'blink'])
    colored('Hello, World!', 'green')
"""

import termcolor

color = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white",
         "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue",
         "light_magenta", "light_cyan"]

higglight = ["on_black", "on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan", "on_white",
             "on_light_grey", "on_dark_grey", "on_light_red", "on_light_green", "on_light_yellow", "on_light_blue", "on_light_magenta", "on_light_cyan"]

attribute = ["bold", "dark", "underline", "blink", "reverse", "concealed"]

for i in color:
    for j in attribute:
        print(termcolor.colored(f"Hello in {i} with {j}", i, "on_black", [j]))
    print()
    # for j in higglight:
    #     for k in attribute:
    #         print(termcolor.colored(f"Hello in {i} with {j} and {k}", i, j, [k]))
    #     print()
    # print()
# print(termcolor.colored("Hello in red", "red", "on_black", ["bold"]))
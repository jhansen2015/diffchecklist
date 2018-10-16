#!/usr/bin/env python3

import subprocess
import urwid
import sys

#
# ./checkboxes.py $(for ((i=0; i < 100; ++i)); do echo $i; done)
#
if len(sys.argv) < 2:
    exit(0)

choices = sys.argv[1:]

#body = [urwid.Text(title), urwid.Divider()]
body = []
lb = urwid.ListBox(urwid.SimpleFocusListWalker(body))

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def next_unactivated(_loop, lb):
    # Needed to update the widget states
    for x in range(lb.focus_position, len(lb.body)):
        if not lb.body[x].original_widget.state:
            # Update the focus position and redraw the screen
            lb.focus_position=x
            _loop.draw_screen()

            # Activate the selected unchecked item.
            _loop.process_input(["enter"])
            break

def menu(choices):
    i = 0
    # Determine width for padding
    width = len(str(len(choices)))
    for c in choices:
        i+=1
        num = f"{i:{width}d}"
        button = urwid.CheckBox(f"{num} {c}")
        #urwid.connect_signal(button, 'change', item_chosen, lb)
        urwid.connect_signal(button, 'postchange', item_postchange, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    lb.body = body
    return lb

#def item_chosen(button, new_state, lb):
#    old_state = button.state
#    if not new_state
#        return

def item_postchange(button, new_state, choice):
    if not button.state:
        return

    # Update the screen so the new state is shown.
    loop.draw_screen()

    # TODO: Run this in the background
    # https://docs.python.org/3.4/library/subprocess.html#subprocess.Popen
    subprocess.call(["kdiff3", "empty.txt", choice])
    loop.set_alarm_in(0, next_unactivated, lb)

def select_first(_loop, _ignored):
    _loop.process_input(["enter"])

menu(choices)
loop = urwid.MainLoop(
    lb,
    palette=[('reversed', 'standout', '')], 
    unhandled_input=show_or_exit
)
loop.set_alarm_in(0, next_unactivated, lb)
loop.run()


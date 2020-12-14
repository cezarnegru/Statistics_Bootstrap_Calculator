#!/usr/bin/env python3

import tkinter as tk
import bootstrap_window
import about_window
import help_window

global window_bg 
global button_bg
global button_fg 
global button_pady
global button_bd 
global button_font
global button_highlightbackground
global label_fg

window_bg = '#5882FA'
button_bg = '#000000'
button_fg = '#FFFF00'
button_pady = 6
button_bd = 3
button_font = 'bold'
button_highlightbackground = window_bg
label_fg = 'white'

def main():

    main_window = tk.Tk()
    main_window.title('Bootstrapping Calculator')
    main_window.geometry('310x210')
    main_window.resizable(width=False, height=False)
    main_window.configure(bg=window_bg)

    # SPACE LABEL
    label_space_main_window = tk.Label(main_window, text='\t'*5,bg=window_bg)
    label_space_main_window.grid(row=0,column=0,columnspan=3)
    # BOOTSTRAP BUTTON
    button_bootstrap = tk.Button(main_window, text='Bootstrap', fg=button_fg, bg=button_bg, font=button_font, pady=button_pady, bd=button_bd, highlightbackground=window_bg, command=bootstrap_window.main)
    button_bootstrap.grid(row=1,column=1)
    # HELP BUTTON
    button_help = tk.Button(main_window, text='Help', fg=button_fg, bg=button_bg, font=button_font, bd=button_bd, pady=button_pady, highlightbackground=window_bg, command=help_window.main)
    button_help.grid(row=2,column=1)
    # ABOUT BUTTON
    button_about = tk.Button(main_window, text='About', fg=button_fg, bg=button_bg, font=button_font, bd=button_bd, pady=button_pady, highlightbackground=window_bg, command=about_window.main)
    button_about.grid(row=3,column=1)
    # EXIT BUTTON
    button_exit = tk.Button(main_window, text='Exit', fg=button_fg, bg=button_bg, font=button_font, bd=button_bd, pady=button_pady, highlightbackground=window_bg, command=main_window.destroy)
    button_exit.grid(row=4,column=1)

    main_window.mainloop()

if __name__ == '__main__':
    main()



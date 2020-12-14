#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import main_window as m_w

global name_of_app
global version
global email
global license_type
global date_of_creation
global label_color
global label_padx

def main():
    name_of_app = 'Bootstrapping'
    version = '0.0.1'
    email = 'negru.cezar@gmail.com'
    license_type = 'GNU GPLv3'
    date_of_creation = '8 December 2020'
    label_color = '#2E2E2E' # black-ish (very dark grey)
    label_padx = 30

    about_window = tk.Tk()
    about_window.title('About')
    about_window.geometry('250x220')
    about_window.resizable(width=False, height=False)
    about_window.configure(bg=m_w.window_bg)

    # SPACE LABEL
    label_space_about_window = tk.Label(about_window, text='\t'*2, bg=m_w.window_bg)
    label_space_about_window.grid(row=0, column=0, columnspan=3)

    # NAME OF APP LABEL - PREFIX
    label_name_of_app = tk.Label(about_window, text='    Name: ', bg=m_w.window_bg, fg=m_w.label_fg)
    label_name_of_app.grid(row=1, column=1)

    # NAME OF APP LABEL
    label_name_of_app_1 = tk.Label(about_window, text=name_of_app, bg=m_w.window_bg, fg=label_color)
    label_name_of_app_1.grid(row=1, column=2)

    # VERSION LABEL - PREFIX
    label_version = tk.Label(about_window, text='Version:', bg=m_w.window_bg, fg=m_w.label_fg)
    label_version.grid(row=2, column=1)

    # VERSION LABEL
    label_version_1 = tk.Label(about_window, text=version, bg=m_w.window_bg, fg=label_color)
    label_version_1.grid(row=2, column=2)

    # EMAIL OF DEVELOPER - PREFIX
    label_email = tk.Label(about_window, text='    Email: ', bg=m_w.window_bg, fg=m_w.label_fg)
    label_email.grid(row=3, column=1)

    # EMAIL OF DEVELOPER
    label_email_1 = tk.Label(about_window, text=email, bg=m_w.window_bg, fg=label_color)
    label_email_1.grid(row=3, column=2)

    # LICENSE TYPE - PREFIX 
    label_license_type = tk.Label(about_window, text='  License: ', bg=m_w.window_bg, fg=m_w.label_fg)
    label_license_type.grid(row=4, column=1)

    # LICENSE TYPE
    label_email_1 = tk.Label(about_window, text=license_type, bg=m_w.window_bg, fg=label_color)
    label_email_1.grid(row=4, column=2)

    # CREATION DATE - PREFIX
    label_creation_date = tk.Label(about_window, text=' Created: ', bg=m_w.window_bg, fg=m_w.label_fg)
    label_creation_date.grid(row=5, column=1)

    # CREATION DATE
    label_creation_date_1 = tk.Label(about_window, text=date_of_creation, bg=m_w.window_bg, fg=label_color)
    label_creation_date_1.grid(row=5, column=2)

    # SPACE LABEL_1
    label_space_about_window_1 = tk.Label(about_window, text='\t'*2, bg=m_w.window_bg)
    label_space_about_window_1.grid(row=6, column=0, columnspan=3)

    # EXIT BUTTON
    button_exit_about_window = tk.Button(about_window, text='Exit', fg=m_w.button_fg, bg=m_w.button_bg, font=m_w.button_font, bd=m_w.button_bd, padx=label_padx , pady=m_w.button_pady, highlightbackground=m_w.window_bg, command=about_window.destroy)
    button_exit_about_window.grid(row=7, column=1, columnspan=2)

    about_window.mainloop()

if __name__=='__main__':
    main()

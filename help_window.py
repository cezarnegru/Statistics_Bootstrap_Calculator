#!/usr/bin/env python3

import tkinter as tk
import main_window as m_w

def main():
    help_window = tk.Tk()
    help_window.title('Help')
    help_window.geometry('550x410')
    help_window.configure(bg=m_w.window_bg)
    help_window.resizable(width=False, height=False)

    help_info = """
                                INFO
       This program is meant to be used for estimating the distribution of a statistic.
       At this stage, it is using only the 'Case resampling method'. Hopefully, 
       in the future, I'll be adding some other methods of Bootstrapping 
       like: Bayesian bootstrap, Smooth bootstrap, Parametric bootstrap, and others.
    """

    help_guide = """
                            GUIDE
    1. Add the path of the file in the 'Path (to file):' entry field.
    2. Select the spreadsheet containing the data to be calculate.
    3. Type the number/letter of the column containing the rows of data/scores 
        to be bootstrapped.
    4. Type the number of resamples.
        Do not separate with '.' or ','.     Example:       OK --> 3000
                                                            NOT OK --> 3.000 or 3,000 
    5. Click the 'Ok' button.
    """

    # SPACE LABEL
    label_space_help_window = tk.Label(help_window, text='\t'*2,bg=m_w.window_bg)
    label_space_help_window.grid(row=0, column=0, columnspan=3)
    # INFO LABEL
    label_info = tk.Label(help_window, text=help_info, bg=m_w.window_bg, justify='left')
    label_info.grid(row=1, column=2)
    # GUIDE LABEL
    label_guide = tk.Label(help_window, text=help_guide, bg=m_w.window_bg, justify='left')
    label_guide.grid(row=2, column=2)
    # EXIT BUTTON
    button_exit_help = tk.Button(help_window, text='Exit',fg=m_w.button_fg, bg=m_w.button_bg, font=m_w.button_font, bd=m_w.button_bd, pady=m_w.button_pady, padx=20, highlightbackground=m_w.window_bg, command=help_window.destroy)
    button_exit_help.grid(row=3, column=2)

    help_window.mainloop()

if __name__ == '__main__':
    main()
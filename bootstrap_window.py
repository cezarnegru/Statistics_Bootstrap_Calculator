#!/usr/bin/env python3

import tkinter as tk
import main_window as m_w
import results_window

global original_list

def main():
    
    bootstrap_window_tk = tk.Tk()
    bootstrap_window_tk.title('Bootstrap')
    bootstrap_window_tk.geometry('530x242')
    bootstrap_window_tk.resizable(width=False, height=False)
    bootstrap_window_tk.configure(bg=m_w.window_bg)
    entry_data_txt = 'entry_data.txt'
    
    def ok():
        default_entry_data_text = ['File path:','Spreadsheet:','Column:','Resamples:']
        data_entries = []

        f = open(entry_data_txt,'w')
        for default_label in default_entry_data_text:
            f.write(default_label+'\n')
        f.close()
        
        file_path_to_read = entry_file_path.get()
        spreadsheet = entry_spreadsheet.get()
        data_column = entry_column.get()
        number_of_resamples = entry_custom_resamples.get()
        data_entries = [file_path_to_read,spreadsheet,data_column,number_of_resamples]

        tmp_list = []
        f = open(entry_data_txt,'r')
        for line in f.readlines():
            tmp_list.append(line)
        f.close()

        for index in range(len(tmp_list)):
            tmp_list[index] = tmp_list[index].strip() 
            tmp_list[index] += data_entries[index]

        f = open(entry_data_txt,'w')
        for item in tmp_list:
            f.write(item+'\n')
        f.close()
        results_window.main()

    # SPACE LABEL
    label_space_bootstrap_window_tk = tk.Label(bootstrap_window_tk, text='\t'*2,bg=m_w.window_bg)
    label_space_bootstrap_window_tk.grid(row=0,column=0)
    # FILE PATH LABEL
    label_path = tk.Label(bootstrap_window_tk, text='Path (to file):', bg=m_w.window_bg, fg=m_w.label_fg, font=m_w.button_font)
    label_path.grid(row=1,column=0)
    # FILE PATH ENTRY
    entry_file_path = tk.Entry(bootstrap_window_tk, bg=m_w.button_bg, fg=m_w.button_fg, font=m_w.button_font, bd=m_w.button_bd, highlightbackground=m_w.button_highlightbackground)
    entry_file_path.grid(row=1,column=1)
    # SPREADSHEET LABE
    label_spreadsheet = tk.Label(bootstrap_window_tk, text='Spreadsheet:', bg=m_w.window_bg, fg=m_w.label_fg, font=m_w.button_font)
    label_spreadsheet.grid(row=2, column=0)
    # SPREADSHEET ENTRY
    entry_spreadsheet = tk.Entry(bootstrap_window_tk, bg=m_w.button_bg, fg=m_w.button_fg, font=m_w.button_font, bd=m_w.button_bd, highlightbackground=m_w.button_highlightbackground)
    entry_spreadsheet.grid(row=2, column=1)
    # COLUMN LABEL
    label_column = tk.Label(bootstrap_window_tk, text='Column:', bg=m_w.window_bg, fg=m_w.label_fg, font=m_w.button_font)
    label_column.grid(row=3, column=0)
    # COLUMN ENTRY
    entry_column = tk.Entry(bootstrap_window_tk, bg=m_w.button_bg, fg=m_w.button_fg, font=m_w.button_font, bd=m_w.button_bd, highlightbackground=m_w.button_highlightbackground)
    entry_column.grid(row=3, column=1)
    # NUMBER OF RESAMPLES LABEL
    label_num_of_resamples = tk.Label(bootstrap_window_tk, text='Number of Resamples:', bg=m_w.window_bg, fg=m_w.label_fg, font=m_w.button_font)
    label_num_of_resamples.grid(row=4,column=0)
    # CUSTOM RESAMPLES ENTRY
    entry_custom_resamples = tk.Entry(bootstrap_window_tk, bg=m_w.button_bg, fg=m_w.button_fg, font=m_w.button_font, bd=m_w.button_bd, highlightbackground=m_w.button_highlightbackground)
    entry_custom_resamples.grid(row=4,column=1)
    # MOST COMMON NUM. OF RESAMPLES EXAMPLE    
    most_common = tk.Label(bootstrap_window_tk, text='(most common: 5.000, 10.000, 15.000)', bg=m_w.window_bg, fg=m_w.label_fg, font=m_w.button_font)
    most_common.grid(row=5,column=1)
    # SPACE LABEL
    label_space_bootstrap_window_tk_3 = tk.Label(bootstrap_window_tk, text='\t'*2,bg=m_w.window_bg)
    label_space_bootstrap_window_tk_3.grid(row=6,column=0)
    # OK BUTTON
    button_ok = tk.Button(bootstrap_window_tk, text='OK',fg=m_w.button_fg, bg=m_w.button_bg, font=m_w.button_font, bd=m_w.button_bd, pady=m_w.button_pady, padx=15, highlightbackground=m_w.window_bg, command=ok)
    button_ok.grid(row=10,column=0,columnspan=2)
    # EXIT BUTTON
    button_exit = tk.Button(bootstrap_window_tk, text='Exit', fg=m_w.button_fg, bg=m_w.button_bg, font=m_w.button_font, bd=m_w.button_bd, pady=m_w.button_pady, highlightbackground=m_w.window_bg, command=bootstrap_window_tk.destroy)
    button_exit.grid(row=10,column=1)

    bootstrap_window_tk.mainloop()

if __name__ == '__main__':
    main()
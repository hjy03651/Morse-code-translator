# -*- coding: utf-8 -*-
# UTF-8 encoding when using Japanese

"""
Morse Code Translator (Ver 1.1.0)
Date: 2022-08-12
Creator: JaeyoungHan

Version History:
Ver 1.0.0 // 2022-08-09
"""

# Import modules ===================================================
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk as ttk
import pyperclip as clip


# Declare Necessary Dictionaries ===================================
morse_eng = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
             '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n',
             '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u',
             '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z'}
morse_eng_sym = {'.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                 '--...': '7', '---..': '8', '----.': '9', '-----': '0',
                 '.-.-.-': '.', '--..--': ',', '---...': ':', '-.-.-.': ';', '..--..': '?', '-.-.--': '!',
                 '.----.': "'", '.-..-.': '"', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
                 '.-.-.': '+', '-....-': '-', '-...-': '=', '..--.-': '_',
                 '.-...': '&', '.--.-.': '@', '...-..-': '$'}
morse_jpn = {'--.--': 'あ', '.-': 'い', '..-': 'う', '-.---': 'え', '.-...': 'お',
             '.-..': 'か', '-.-..': 'き', '...-': 'く', '-.--': 'け', '----': 'こ',
             '-.-.-': 'さ', '--.-.': 'し', '---.-': 'す', '.---.': 'せ', '---.': 'そ',
             '-.': 'た', '..-.': 'ち', '.--.': 'つ', '.-.--': 'て', '..-..': 'と',
             '.-.': 'な', '-.-.': 'に', '....': 'ぬ', '--.-': 'ね', '..--': 'の',
             '-...': 'は', '--..-': 'ひ', '--..': 'ふ', '.': 'へ', '-..': 'ほ',
             '-..-': 'ま', '..-.-': 'み', '-': 'む', '-...-': 'め', '-..-.': 'も',
             '.--': 'や', '-..--': 'ゆ', '--': 'よ',
             '...': 'ら', '--.': 'り', '-.--.': 'る', '---': 'れ', '.-.-': 'ろ',
             '-.-': 'わ', '.-..-': 'ゐ', '.--..': 'ゑ', '.---': 'を', '.-.-.': 'ん', '.--.-': 'ー'}
morse_jpn_sym = {'.----': '１', '..---': '２', '...--': '３', '....-': '４', '.....': '５', '-....': '６',
                 '--...': '７', '---..': '８', '----.': '９', '-----': '０',
                 '..': '゛', '..--.': '゜', '.-.-..': '。', '.-.-.-': '、',
                 '---...': '：', '-.-.-.': '；', '..--..': '？', '-.-.--': '！',
                 '.----.': "'", '.-..-.': '"', '-..-.': '・', '-.--.': '（', '-.--.-': '）',
                 '.-.-.': '＋', '-....-': '－', '-...-': '＝', '..--.-': '＿',
                 '.-...': '＆', '.--.-.': '＠', '...-..-': '＄'}  # em-size characters

reverse_morse_eng = {v: k for k, v in morse_eng.items()}
reverse_morse_jpn = {v: k for k, v in morse_jpn.items()}
reverse_morse_eng_sym = {v: k for k, v in morse_eng_sym.items()}
reverse_morse_jpn_sym = {v: k for k, v in morse_jpn_sym.items()}

kana_to_dakuten = {'か': 'が', 'き': 'ぎ', 'く': 'ぐ', 'け': 'げ', 'こ': 'ご',
                   'さ': 'ざ', 'し': 'じ', 'す': 'ず', 'せ': 'ぜ', 'そ': 'ぞ',
                   'た': 'だ', 'ち': 'ぢ', 'つ': 'づ', 'て': 'で', 'と': 'ど',
                   'は': 'ば', 'ひ': 'び', 'ふ': 'ぶ', 'へ': 'べ', 'ほ': 'ぼ'}
kana_to_handakuten = {'は': 'ぱ', 'ひ': 'ぴ', 'ふ': 'ぷ', 'へ': 'ぺ', 'ほ': 'ぽ'}

dakuten_to_kana = {v: k for k, v in kana_to_dakuten.items()}
handakuten_to_kana = {v: k for k, v in kana_to_handakuten.items()}

small_kana = {'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お', 'ヵ': 'か',
              'ヶ': 'け', 'っ': 'つ', 'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ', 'ゎ': 'わ'}


# Declare functions for program ====================================
def text_to_morse(text, select):
    """
    Convert text to morse code
    :param text: String to convert
    :param select: A parameter for language
    :return: Converted code
    """
    text = text.lower()
    output = ''
    if select == 'eng':
        for t in text:
            if t.isalpha():
                output += reverse_morse_eng[t] + ' '
            elif t.isspace():
                continue
            else:
                output += reverse_morse_eng_sym.get(t, '[?]') + ' '
        return output
    else:
        for t in text:
            if t.isalpha():
                output += reverse_morse_jpn[t] + ' '
            elif t.isspace():
                continue
            else:
                output += reverse_morse_jpn_sym.get(t, '[?]') + ' '
        return output


def morse_to_text(text, select):
    """
    Convert morse code to text
    :param text: String to convert
    :param select: A parameter for language
    :return: Converted text
    """
    output = ''
    if select == 'eng':
        for t in text:
            if t in morse_eng.keys():
                output += morse_eng[t]
            else:
                output += morse_eng_sym.get(t, '[?]')
        return output
    elif select == 'jpn':
        for t in text:
            if t in morse_jpn.keys():
                output += morse_jpn[t]
            else:
                output += morse_jpn_sym.get(t, '[?]')
        return output


def attach_ten(kana, ten):
    """
    Attach a detached point in Japanese conversion
    :param kana: Japanese character for convert
    :param ten: The type of dot to attach to the letter
    :return: Dotted character
    """
    if kana in kana_to_dakuten.keys():
        if ten == 'daku':
            return kana_to_dakuten[kana]
        elif ten == 'handaku':
            return kana_to_handakuten[kana]
    else:
        if ten == 'daku':
            return kana + '゛'
        elif ten == 'handaku':
            return kana + '゜'


def release_ten(kana, select):
    """
    Release the attached point in Japanese conversion
    :param kana: Japanese character for convert
    :param select: The type of dot to detach to the letter
    :return: Undotted character
    """
    if select == 'handaku':
        return handakuten_to_kana[kana] + '゜'
    elif select == 'daku':
        return dakuten_to_kana[kana] + '゛'


def occur_error():
    """
    Display a messagebox when an error occurs
    :return: Blank
    """
    msg.showwarning('Error', 'The input column is blank.')
    label_input['text'] = 'Input'
    label_output['text'] = 'Output'
    return ''


def exit_window(_=None):
    """
    Close the program
    :param _: Key binding (Ctrl + Q)
    :return: None
    """
    msg_quit = msg.askquestion('Quit', 'Really quit?')
    if msg_quit == 'yes':
        root.destroy()


# Declare functions for converting =================================
def change_english_to_morse(text):
    """
    Main function for convert English to morse code
    :param text: String for convert
    :return: converted code
    """
    text = text.lower()
    if not text:
        return occur_error()
    else:
        output = text_to_morse(text, 'eng')
        return output


def change_japanese_to_morse(text):
    """
    Main function for convert Japanese to morse code
    :param text: String for convert
    :return: converted code
    """
    output = ''
    if not text:
        return occur_error()
    else:
        for k in text:
            if k in dakuten_to_kana.keys():
                output += release_ten(k, 'daku')
            elif k in handakuten_to_kana.keys():
                output += release_ten(k, 'handaku')
            elif k in small_kana.keys():
                output += small_kana[k]
            else:
                output += k

        encoding = text_to_morse(output, 'jpn')
        return encoding


def change_morse_to_english(text):
    """
    Main function for convert morse code to English
    :param text: String for convert
    :return: converted text
    """
    text = text.lower().split()
    if not text:
        return occur_error()
    else:
        output = morse_to_text(text, 'eng')
        return output


def change_morse_to_japanese(text):
    """
    Main function for convert morse code to Japanese
    :param text: String for convert
    :return: converted text
    """
    text = text.lower().split()
    if not text:
        return occur_error()
    else:
        output = morse_to_text(text, 'jpn')
        for k in output:
            index = output.index(k)
            if k == '゛':
                output = output[:index - 1] + attach_ten(output[index - 1], 'daku') + output[index + 1:]
            elif k == '゜':
                output = output[:index - 1] + attach_ten(output[index - 1], 'handaku') + output[index + 1:]
        return output


# Declare functions for button event ===============================
def start_convert(_=None):
    """
    Start conversion
    :param _: Key binding (Return)
    :return: None
    """
    code = entry_input.get()
    entry_output.delete(0, tk.END)
    if menu_var.get() == 1:
        label_input['text'] = 'Input - English'
        label_output['text'] = 'Output - Morse code'
        output = change_english_to_morse(code)
    elif menu_var.get() == 2:
        label_input['text'] = 'Input - Morse code'
        label_output['text'] = 'Output - English'
        output = change_morse_to_english(code)
    elif menu_var.get() == 3:
        label_input['text'] = 'Input - Japanese'
        label_output['text'] = 'Output - Morse code'
        output = change_japanese_to_morse(code)
    else:
        label_input['text'] = 'Input - Morse code'
        label_output['text'] = 'Output - Japanese'
        output = change_morse_to_japanese(code)
    entry_output.insert(tk.END, output)


def clear_all(_=None):
    """
    Clear all entry
    :param _: Key binding (Escape)
    :return: None
    """
    entry_input.delete(0, tk.END)
    entry_output.delete(0, tk.END)
    label_input['text'] = 'Input'
    label_output['text'] = 'Output'


def view_code(_=None):
    """
    Show whole code
    :param _: Key binding (Ctrl + W)
    :return: None
    """
    # main window
    table = tk.Toplevel(root)
    table.title('Morse Code List')
    table.geometry('250x270+500+300')
    table.resizable(False, False)
    table['bg'] = color_bg1

    # listbox
    language_list = tk.Listbox(table, exportselection=False, selectmode='extended', width=0, height=0)
    language_list.insert(0, 'English')
    language_list.insert(1, 'Japanese')
    language_list.place(x=10, y=10)

    # label
    label_tip = tk.Label(table, text='[Ctrl + C] or Double click to copy the code',
                         font=(font, 9), fg=color_fg2, bg=color_bg1)
    label_tip.place(x=10, y=240)

    # button
    button_exit = tk.Button(table, text='exit', font=(font, 10), width=6,
                            command=lambda: table.destroy(), fg=color_fg1, bg=color_bg2)
    button_exit.place(x=10, y=200)

    # treeview
    column = ['alphabet', 'code']
    code_table = ttk.Treeview(table, columns=column, displaycolumns=column)
    code_table.place(x=75, y=10)
    code_table.column(column[0], width=80, anchor='center')
    code_table.heading(column[0], text='Language', anchor='center')
    code_table.column(column[1], width=80, anchor='center')
    code_table.heading(column[1], text='Morse', anchor='center')
    code_table['show'] = 'headings'

    # functions
    def select_language(_):
        """
        Show the selected language on the table
        :param _: Key binding (Select listbox)
        :return: None
        """
        # > initializing
        code_table.delete(*code_table.get_children())  # initialize the treeview
        code_table.yview_moveto(0)  # initialize the scrollbar

        # > show the table
        value = language_list.get(language_list.curselection())  # selected language
        if value == 'English':
            code_table.heading(column[0], text='English', anchor='center')
            tree_value = list(reverse_morse_eng.items()) + list(reverse_morse_eng_sym.items())
            for i in range(len(tree_value)):
                code_table.insert('', 'end', text='', values=tree_value[i], iid=i)
        else:
            code_table.heading(column[0], text='Japanese', anchor='center')
            tree_value = list(reverse_morse_jpn.items()) + list(reverse_morse_jpn_sym.items())
            for i in range(len(tree_value)):
                code_table.insert('', 'end', text='', values=tree_value[i], iid=i)

        # > set scrollbar
        scroll = ttk.Scrollbar(table, orient='vertical', command=code_table.yview)
        scroll.place(x=237, y=10, height=225)
        code_table.configure(yscrollcommand=scroll.set)

    def copy_in_clipboard(_):
        """
        Copy the code from the box
        :param _: Key binding (Double-click or Ctrl + C)
        :return: None
        """
        selections = code_table.selection()
        copy_word = code_table.item(selections, 'values')
        clip.copy(copy_word[1] + ' ')

    # binding
    language_list.bind('<<ListboxSelect>>', select_language)
    code_table.bind('<Double-Button-1>', copy_in_clipboard)
    code_table.bind('<Control-Key-c>', copy_in_clipboard)
    table.bind('<Escape>', lambda e: table.destroy())

    table.mainloop()


def copy_output():
    """
    Copy the text of the output column
    :return: None
    """
    output = entry_output.get()
    clip.copy(output)


# Font & Colors ====================================================
font = 'Yu Gothic UI'
color_bg1 = '#CCCCCC'
color_bg2 = '#666666'
color_fg1 = '#F3F3F3'
color_fg2 = '#222222'


# Main code ========================================================
# > main window
root = tk.Tk()
root.title('Morse Code Translator')
root.geometry('500x370+100+100')
root.resizable(False, False)
root['bg'] = color_bg1

# > version
label_version = tk.Label(root, text='Ver 1.1.0', font=(font, 10), fg='blue', bg=color_bg1)
label_version.place(x=440, y=344)

# > attention
attention_eng = '* Please select the menu and enter the text in the "input" column. *'
attention_jpn = '* メニューを選んで、「input」欄に入力してください。ひらがなのみお願いします。*'
label_attention_eng = tk.Label(root, text=attention_eng, font=(font, 11), fg='red', bg=color_bg1)
label_attention_jpn = tk.Label(root, text=attention_jpn, font=(font, 11), fg='red', bg=color_bg1)
label_attention_eng.place(x=25, y=7)
label_attention_jpn.place(x=20, y=27)

# > menu
label_menu = tk.Label(root, text='Menu', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_menu.place(x=10, y=70)

menu_var = tk.IntVar()
btn_eng_to_morse = tk.Radiobutton(root, text="Eng → Morse", value=1, variable=menu_var, bg=color_bg1)
btn_morse_to_eng = tk.Radiobutton(root, text="Morse → Eng", value=2, variable=menu_var, bg=color_bg1)
btn_jpn_to_morse = tk.Radiobutton(root, text="Jpn → Morse", value=3, variable=menu_var, bg=color_bg1)
btn_morse_to_jpn = tk.Radiobutton(root, text="Morse → Jpn", value=4, variable=menu_var, bg=color_bg1)
btn_eng_to_morse.select()

btn_eng_to_morse.place(x=10, y=100)
btn_morse_to_eng.place(x=150, y=100)
btn_jpn_to_morse.place(x=10, y=120)
btn_morse_to_jpn.place(x=150, y=120)

# > input entry
label_input = tk.Label(root, text='Input', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_input.place(x=10, y=155)
entry_input = tk.Entry(width=68)
entry_input.place(x=10, y=180, height=20)

# > buttons
button_convert = tk.Button(text='convert', font=(font, 10), command=start_convert, fg=color_fg1, bg=color_bg2)
button_clear = tk.Button(text='clear', font=(font, 10), command=clear_all, fg=color_fg1, bg=color_bg2)
button_code = tk.Button(text='code list', font=(font, 10), command=view_code, fg=color_fg1, bg=color_bg2)
button_copy = tk.Button(text='copy output', font=(font, 10), command=copy_output, fg=color_fg1, bg=color_bg2)
button_convert.place(x=35, y=230, width=100)
button_clear.place(x=145, y=230, width=100)
button_code.place(x=255, y=230, width=100)
button_copy.place(x=365, y=230, width=100)

# > output entry
label_output = tk.Label(root, text='Output', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_output.place(x=10, y=275)
entry_output = tk.Entry(width=68)
entry_output.place(x=10, y=300, height=20)

# > shortcuts
label_shortcut1 = tk.Label(root, text='[Ctrl + Q] to quit the program', font=(font, 9), fg=color_fg2, bg=color_bg1)
label_shortcut2 = tk.Label(root, text='[Ctrl + W] to view the codes', font=(font, 9), fg=color_fg2, bg=color_bg1)
label_shortcut1.place(x=10, y=325)
label_shortcut2.place(x=10, y=344)

# > key binding
root.bind('<Return>', start_convert)
root.bind('<Escape>', clear_all)
root.bind('<Control-q>', exit_window)
root.bind('<Control-w>', view_code)

# > quit program
root.protocol('WM_DELETE_WINDOW', exit_window)

root.mainloop()

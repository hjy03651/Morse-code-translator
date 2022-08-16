# -*- coding: utf-8 -*-
# UTF-8 encoding when using Japanese

"""
Morse Code Translator (Ver 1.2.0)
Date: 2022-08-16
Creator: JaeyoungHan

Version History:
Ver 1.0.0 // 2022-08-09
Ver 1.1.0 // 2022-08-12
Ver 1.1.1 // 2022-08-12
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
            if t in reverse_morse_eng:
                output += reverse_morse_eng[t] + ' '
            elif t.isspace():
                continue
            else:
                output += reverse_morse_eng_sym.get(t, '[?]') + ' '
        return output
    else:
        for t in text:
            if t in reverse_morse_jpn:
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
    msg.showwarning(titles[4], messages[0])
    label_input['text'] = 'Input'
    label_output['text'] = 'Output'
    return ''


def exit_window(_=None):
    """
    Close the program
    :param _: Key binding (Ctrl + Q)
    :return: None
    """
    msg_quit = msg.askquestion(titles[5], messages[1])
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
    table.title(titles[1])
    table.geometry('250x270+500+300')
    table.resizable(False, False)
    table['bg'] = color_bg1

    table.focus_set()

    # listbox
    language_list = tk.Listbox(table, exportselection=False, selectmode='extended', width=0, height=0)
    language_list.insert(0, 'English')
    language_list.insert(1, 'Japanese')
    language_list.place(x=10, y=10)

    # label
    label_tip = tk.Label(table, text=shortcuts[1],
                         font=(font, 9), fg=color_fg2, bg=color_bg1)
    label_tip.place(x=10, y=240)

    # button
    button_exit = tk.Button(table, text=buttons[3], font=(font, 10), width=6,
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
    table.bind('<Escape>', lambda _: table.destroy())

    table.mainloop()


def open_help(_=None):
    """
    Open menu 'Help'
    :param _: Key binding (F1)
    :return: None
    """
    # main window
    table = tk.Toplevel(root)
    table.title(titles[2])
    table.geometry('590x130+500+300')
    table.resizable(False, False)
    table['bg'] = color_bg1

    table.focus_set()
    table.grab_set()

    # label
    explain_frame = tk.Frame(table, height=120, width=580, relief='ridge', bd=2, bg=color_bg1, padx=2, pady=2)
    label_explain = tk.Label(table, text=explain, font=(font, 11), fg=color_fg2, bg=color_bg1, justify='left')
    explain_frame.place(x=5, y=5)
    label_explain.place(x=10, y=10)

    # button
    button_close = tk.Button(table, text=buttons[3], font=(font, 10), width=10,
                             command=lambda: table.destroy(), fg=color_fg1, bg=color_bg2)
    button_close.place(x=490, y=85)

    # key binding
    table.bind('<Escape>', lambda _: table.destroy())


def open_program_info(_=None):
    """
    Open menu 'program info'
    :param _: Key binding (F12)
    :return: None
    """
    # main window
    table = tk.Toplevel(root)
    table.title(titles[3])
    table.geometry('250x100+500+300')
    table.resizable(False, False)
    table['bg'] = color_bg1

    table.focus_set()
    table.grab_set()

    # label
    label_info = tk.Label(table, text=info, font=(font, 10), fg=color_fg2, bg=color_bg1, justify='left')
    label_info.place(x=10, y=10)

    # button
    button_close = tk.Button(table, text=buttons[3], font=(font, 10), width=7,
                             command=lambda: table.destroy(), fg=color_fg1, bg=color_bg2)
    button_close.place(x=180, y=60)

    # key binding
    table.bind('<Escape>', lambda _: table.destroy())


def change_language():
    """
    Change the language of the program.
    :return: None
    """
    global titles, messages, translate, buttons, shortcuts, explain, info, font
    if language.get() == 1:  # English
        titles = ['Morse Code Translator', 'Code List', 'Help', 'Info', 'Error', 'Quit']
        messages = ['The input column is blank.', 'Really quit?']
        translate = ['Eng → Morse', 'Morse → Eng', 'Jpn → Morse', 'Morse → Jpn']
        buttons = ['convert', 'clear', 'copy output', 'exit']
        shortcuts = ['[Ctrl + Q] to quit the program / [Ctrl + W] to view the codes',
                     '[Ctrl + C] or Double click to copy the code']
        explain = '1. From the menu, choose the language (or code) you wish to convert.\n' \
                  '2. Then enter it in the "Input" field.\n' \
                  '3. And click the "convert" button or hit Return to convert it into the "Output" column.\n' \
                  '4. To reset two columns, use the "clear" button.'
        info = '[Morse code translator]\n' \
               'Version: 1.2.0 (16-08-2022)\n' \
               'Creator: JaeyoungHan\n'

        font = 'Yu Gothic UI'

    elif language.get() == 2:  # Japanese
        titles = ['モールス信号翻訳機', 'コード一覧', 'ヘルプ', '情報', 'エラー', '終了']
        messages = ['Input欄が空白です。', '終了しますか？']
        translate = ['英語 → モールス', 'モールス → 英語', '日本語 → モールス', 'モールス → 日本語']
        buttons = ['変換', '初期化', 'コピー', '閉じる']
        shortcuts = ['［Ctrl + Q］でプログラムが終了 / ［Ctrl + W］でコード一覧',
                     '［Ctrl + C］やダブルクリックでコピー']
        explain = '1. メニューから変換するものを選んでください。\n' \
                  '2. 「Input」欄に入力してください。\n' \
                  '3. 「変換」ボタンやエンターキーで「Output」欄に変換結果が出ます。\n' \
                  '4. 「初期化」ボタンやEscキーで「Input」「Output」欄が空白になります。'
        info = '[Morse code translator]\n' \
               'バージョン: 1.2.0 (2022-08-16)\n' \
               '制作: JaeyoungHan\n'

        font = 'Helvetica'

    elif language.get() == 3:  # Korean
        titles = ['모스부호 번역기', '모스부호 표', '도움말', '정보', '오류', '종료']
        messages = ['입력이 공백입니다.', '종료하시겠습니까?']
        translate = ['영어 → 모스부호', '모스부호 → 영어', '일어 → 모스부호', '모스부호 → 일어']
        buttons = ['변환', '초기화', '복사', '닫기']
        shortcuts = ['[Ctrl + Q]로 종료 / [Ctrl + W]로 모스부호 표 일람',
                     '[Ctrl + C]나 더블클릭으로 복사']
        explain = '1. 메뉴에서 무엇을 변환할지 선택해주세요.\n' \
                  '2. Input란에 입력해주세요.\n' \
                  '3. "변환"버튼이나 엔터를 누르면 Output란에 변환되어 출력됩니다.\n' \
                  '4. "초기화"버튼이나 Esc를 누르면 Input과 Output이 초기화됩니다.'
        info = '[Morse code translator]\n' \
               '버전: 1.2.0 (2022-08-16)\n' \
               '제작: JaeyoungHan\n'

        font = 'Meiryo UI'

    # text and font
    btn_eng_to_morse['text'] = translate[0]
    btn_morse_to_eng['text'] = translate[1]
    btn_jpn_to_morse['text'] = translate[2]
    btn_morse_to_jpn['text'] = translate[3]

    btn_eng_to_morse['font'] = font, 9
    btn_morse_to_eng['font'] = font, 9
    btn_jpn_to_morse['font'] = font, 9
    btn_morse_to_jpn['font'] = font, 9

    button_convert['text'] = buttons[0]
    button_clear['text'] = buttons[1]
    button_copy['text'] = buttons[2]

    button_convert['font'] = font, 10
    button_clear['font'] = font, 10
    button_copy['font'] = font, 10

    label_shortcut['text'] = shortcuts[0]
    label_shortcut['font'] = font, 9


# Font & Colors ====================================================
font = 'Yu Gothic UI'
color_bg1 = '#CCCCCC'  # light gray
color_bg2 = '#666666'  # dark gray
color_fg1 = '#F3F3F3'  # white
color_fg2 = '#222222'  # black
color_blue = '#1e80c1'  # blue


# Texts ============================================================
titles = ['Morse Code Translator', 'Code List', 'Help', 'Info', 'Error', 'Quit']
messages = ['The input column is blank.', 'Really quit?']
translate = ['Eng → Morse', 'Morse → Eng', 'Jpn → Morse', 'Morse → Jpn']
buttons = ['convert', 'clear', 'copy output', 'exit']
shortcuts = ['[Ctrl + Q] to quit the program / [Ctrl + W] to view the codes',
             '[Ctrl + C] or Double click to copy the code']
explain = '1. From the menu, choose the language (or code) you wish to convert.\n' \
          '2. Then enter it in the "Input" field.\n'\
          '3. And click the "convert" button or hit Return to convert it into the "Output" column.\n'\
          '4. To reset two columns, use the "clear" button.'
info = '[Morse code translator]\n'\
       'Version: 1.2.0 (16-08-2022)\n'\
       'Creator: JaeyoungHan\n'


# Main code ========================================================
# > main window
root = tk.Tk()
root.title(titles[0])
root.geometry('500x315+100+100')
root.resizable(False, False)
root['bg'] = color_bg1

# > menu
menubar = tk.Menu(root)
menu_file = tk.Menu(menubar, tearoff=0)
menu_file.add_command(label='Code list', command=view_code, accelerator='Ctrl+W')
menu_file.add_separator()
menu_file.add_command(label='Help', command=open_help, accelerator='F1')
menu_file.add_command(label='About..', command=open_program_info, accelerator='F12')
menu_file.add_separator()
menu_file.add_command(label='Exit', command=exit_window, accelerator='Ctrl+Q')
menubar.add_cascade(label='Info', menu=menu_file)

language = tk.IntVar()
menu_config = tk.Menu(menubar, tearoff=0)
menu_config_lang = tk.Menu(menu_config, tearoff=0)
menu_config_lang.add_radiobutton(label='English', value=1, variable=language, command=change_language)
menu_config_lang.add_radiobutton(label='日本語', value=2, variable=language, command=change_language)
menu_config_lang.add_radiobutton(label='한국어', value=3, variable=language, command=change_language)
menu_config.add_cascade(label='Languages', menu=menu_config_lang)
menubar.add_cascade(label='Options', menu=menu_config)

root.config(menu=menubar)

# > frame
menu_frame = tk.Frame(root, height=85, width=300, relief='ridge', bd=2, bg=color_bg1, padx=2, pady=2)
menu_frame.place(x=5, y=5)
input_frame = tk.Frame(root, height=57, width=490, relief='ridge', bd=2, bg=color_bg1, padx=2, pady=2)
input_frame.place(x=5, y=95)
output_frame = tk.Frame(root, height=57, width=490, relief='ridge', bd=2, bg=color_bg1, padx=2, pady=2)
output_frame.place(x=5, y=215)

# > selection
label_menu = tk.Label(root, text='Menu', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_menu.place(x=10, y=10)

menu_var = tk.IntVar()
btn_eng_to_morse = tk.Radiobutton(root, text=translate[0], font=(font, 9), value=1, variable=menu_var, bg=color_bg1)
btn_morse_to_eng = tk.Radiobutton(root, text=translate[1], font=(font, 9), value=2, variable=menu_var, bg=color_bg1)
btn_jpn_to_morse = tk.Radiobutton(root, text=translate[2], font=(font, 9), value=3, variable=menu_var, bg=color_bg1)
btn_morse_to_jpn = tk.Radiobutton(root, text=translate[3], font=(font, 9), value=4, variable=menu_var, bg=color_bg1)
btn_eng_to_morse.select()

btn_eng_to_morse.place(x=10, y=40)
btn_morse_to_eng.place(x=150, y=40)
btn_jpn_to_morse.place(x=10, y=60)
btn_morse_to_jpn.place(x=150, y=60)

# > input entry
label_input = tk.Label(root, text='Input', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_input.place(x=10, y=100)
entry_input = tk.Entry(width=59, font=(font, 11))
entry_input.place(x=10, y=125, height=20)

# > output entry
label_output = tk.Label(root, text='Output', font=(font, 11), fg=color_fg1, bg=color_bg2)
label_output.place(x=10, y=220)
entry_output = tk.Entry(width=59, font=(font, 11), fg=color_blue)
entry_output.place(x=10, y=245, height=20)

# > buttons
button_convert = tk.Button(text=buttons[0], font=(font, 10), command=start_convert, fg=color_fg1, bg=color_bg2)
button_clear = tk.Button(text=buttons[1], font=(font, 10), command=clear_all, fg=color_fg1, bg=color_bg2)
button_copy = tk.Button(text=buttons[2], font=(font, 10),
                        command=lambda: clip.copy(entry_output.get()), fg=color_fg1, bg=color_bg2)
button_convert.place(x=80, y=168, width=100)
button_clear.place(x=200, y=168, width=100)
button_copy.place(x=320, y=168, width=100)

# > shortcuts
label_shortcut = tk.Label(root, text=shortcuts[0], font=(font, 9), fg=color_fg2, bg=color_bg1)
label_shortcut.place(x=10, y=289)

# > version
label_version = tk.Label(root, text='Ver 1.2.0', font=(font, 10), fg='blue', bg=color_bg1)
label_version.place(x=440, y=289)

# > key binding
root.bind('<Return>', start_convert)
root.bind('<Escape>', clear_all)
root.bind('<Control-q>', exit_window)
root.bind('<Control-w>', view_code)
root.bind('<F1>', open_help)
root.bind('<F12>', open_program_info)

# > quit program
root.protocol('WM_DELETE_WINDOW', exit_window)

root.mainloop()

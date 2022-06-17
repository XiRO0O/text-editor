import PySimpleGUI as sg

menu_layout = [
    ['File',['Open','Save','---','Exit']],
    ['Tools',['Word Count']],
    ['Add']
]

sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untilted', key = '-DOCNAME-')],
    [sg.Multiline(no_scrollbar = True, size = (40,30), key = '-TEXTBOX-')]
]

window = sg.Window('Text editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Word Count":
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n',' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'words: {word_count}\ncharacters: {char_count}')

window.close()
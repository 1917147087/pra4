hex_colours.py
code_to_color = {'AliceBlue': '	#f0f8ff', 'AntiqueWhite': '	#faebd7', 'beige': '	#f5f5dc', 'darkkhaki': '#bdb76b',
              'gainsboro': '#dcdcdc', 'CornflowerBlue': '	#6495ed', 'light': '#eedd82', 'HotPink4': '#8b3a62',
              'mintcream': '#f5fffa', 'LawnGreen': '#7cfc00'}
code = input('Enter color name: ').lower()
while code != '':
    if code in code_to_color:
        print(code_to_color[code])
    else:
        print('Invalid color name')
    code = input('Enter color name: ').lower()

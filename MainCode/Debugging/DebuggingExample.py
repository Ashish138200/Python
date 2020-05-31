# box print
def BoxPrint(symbol, width, height):
    #debugging
    if len(symbol) != 1:
        raise Exception('Symbol needs to be length of 1')
    if width< 2 or height<2:
        raise Exception('Height and width must be greater than 2') #generates traceback error msg
    # debugging
    print(symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width-2)) + symbol)
    print(symbol * width)
BoxPrint('#',15,5)
BoxPrint('##',15,5) #bug
BoxPrint('#',1,1) #bug



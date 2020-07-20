
# DFL 20 Jul 2020

# this program defines a function that translates its known symbols into the
# corresponding HTML codes. 


htmlcodes={ "'" : '&apos;', '£':'&pound;',  '& ':'&amp;',   '€': '&euro;',
            'ß': '&szlig;', 'ä': '&auml;',  'ö':'&ouml;',   'ü': '&uuml;',
            'Ä': '&Auml;',  'Ö': '&Oml;',   'Ü': 'Uuml;',   'µ': '&micro;',
            '-': '&#45;',   '/': '&#47;',   '’': '&apos;',  '!': '&#33;'
            '"': '&quot;',  '#': '&#35;',   '$'; '&#36;',   '%': '&#37;',
            '(': '&#40;',   ')': '&#41;' } 


# this function takes two parameters, the text to be converted and a dictionary
# holding a series of (symbol: html code) pairs, it will use mine dictionary as
# a default

def tr (txt,codes=htmlcodes):
    for sym in codes.keys():
        txt=txt.replace(sym,codes[sym])
    return txt


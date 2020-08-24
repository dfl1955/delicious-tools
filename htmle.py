
# DFL 20 Jul 2020

# this program defines a function that translates its known symbols into the
# corresponding HTML codes. 


htmlcodes={ "'" : '&apos;', '£':'&pound;',  '& ':'&amp; ',  '€': '&euro;',
            'ß': '&szlig;', 'ä': '&auml;',  'ö':'&ouml;',   'ü': '&uuml;',
            'Ä': '&Auml;',  'Ö': '&Oml;',   'Ü': 'Uuml;',   'µ': '&micro;',
            '-': '&#45;',   '/': '&#47;',   '’': '&apos;',  '!': '&#33;',
            '"': '&#34;',  '$': '&#36;',   '%': '&#37;',
            '(': '&#40;',   ')': '&#41;',   '*': '&#42;',   '+': '&#43;',
            ':': '&#58;',   '=': '&#61;',   '?': '&#63;',
            '@': '&#64;' }

# [ 	&#91; 	  	left square bracket
# \ 	&#92; 	  	backslash
# ] 	&#93; 	  	right square bracket
# ^ 	&#94; 	  	caret / circumflex
# _ 	&#95; 	  	underscore
# ` 	&#96; 	  	grave / accent

# I took ';': '&#59;', out as it was double printing 

#Are we going to do ' #': ' &#35;'? And what about <>?

# this function takes two parameters, the text to be converted and a dictionary
# holding a series of (symbol: html code) pairs, it will use my dictionary as
# a default

def tr (txt,codes=htmlcodes):
    for sym in codes.keys():
        txt=txt.replace(sym,codes[sym])
    return txt


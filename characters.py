''' module for transforming unicode characters to their respective entities '''
import os.path
import unicodedata as uni

chars = {'̊': '&#x030a;', 'ſ': '&#x017f;', 'ạ': '&#x1ea1;', 'ẹ': '&#x1eb9;', 'ụ': '&#x1ee5;', 'ị': '&#x1ecb;', 'æ': '&#x00e6;', 'ė': '&#x0117;', 'ą': '&#x0105;', 'ę': '&#x0119;', 'į': '&#012f;', 'ų': '&#x0173;', 'ū': '&#x016b;', 'š': '&#x0161;'}

escapes = {v: k for k, v in chars.items()} # falls man das ganze mal umdrehen möchte



def use_escapes(instring):
    outstring = ''
    used = []
    for char in instring:
        if uni.category(char) == 'Mn' or uni.category(char) == 'Ll':
            for tc in chars:
                if char == tc:
                    char = chars[char]
                    used.append(tc)
        outstring = outstring + char

    print(set(used))
    print(len(set(used)), len(chars))
    return outstring

def test_stuff():
    for char in chars.keys():
        print(char, uni.category(char))

def standalone():
    infile = os.path.normpath('bretke_geb-asarie.tei')
    outfile = os.path.normpath('bretke_chars_changed.tei')
    with open(infile, 'r') as infi:
        text = infi.read()
    text = use_escapes(text)
    with open (outfile, 'w') as oufi:
        oufi.write(text)


if __name__ == '__main__':
    standalone()

''' module for transforming unicode characters to their respective entities '''
import os.path
import unicodedata as uni

chars = {'̊': '&#x030a;', 'ſ': '&#x017f;', 'ạ': '&#x1ea1;', 'ẹ': '&#x1eb9;', 'ụ': '&#x1ee5;', 'ị': '&#x1ecb;', 'æ': '&#x00e6;', 'ė': '&#x0117;', 'ą': '&#x0105;', 'ę': '&#x0119;', 'į': '&#012f;', 'ų': '&#x0173;', 'ū': '&#x016b;', 'š': '&#x0161;'}

escapes = {v: k for k, v in chars.items()} # falls man das ganze mal umdrehen möchte

filename = os.path.normpath('edition_bretke_asarie.tei')

def use_escapes():
    with open(filename, 'r') as infile:
        text = infile.read()

    outstring = ''
    used = []
    for char in text:
        if uni.category(char) == 'Mn' or uni.category(char) == 'Ll':
            for tc in chars:
                if char == tc:
                    char = chars[char]
                    used.append(tc)
        outstring = outstring + char

    print(set(used))
    print(len(set(used)), len(chars))

    with open('test_chars.xml', 'w') as outfile:
        outfile.write(outstring)

def test_stuff():
    for char in chars.keys():
        print(char, uni.category(char))

if __name__ == '__main__':
    use_escapes()


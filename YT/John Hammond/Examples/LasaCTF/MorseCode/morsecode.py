morseAlphabet ={
    "A" : ".-",    "a": ".-",
    "B" : "-...",     "b": "-...",
    "C" : "-.-.",     "c": "-.-.",
    "D" : "-..",     "d": "-..",
    "E" : ".",     "e": ".",
    "F" : "..-.",     "f": "..-.",
    "G" : "--.",     "g": "--.",
    "H" : "....",     "h": "....",
    "I" : "..",     "i": "..",
    "J" : ".---",     "j": ".---",
    "K" : "-.-",     "k": "-.-",
    "L" : ".-..",     "l": ".-..",
    "M" : "--",     "m": "--",
    "N" : "-.",     "n": "-.",
    "O" : "---",     "o": "---",
    "P" : ".--.",     "p": ".--.",
    "Q" : "--.-",     "q": "--.-",
    "R" : ".-.",     "r": ".-.",
    "S" : "...",     "s": "...",
    "T" : "-",     "t": "-",
    "U" : "..-",     "u": "..-",
    "V" : "...-",     "v": "...-",
    "W" : ".--",     "w": ".--",
    "X" : "-..-",     "x": "-..-",
    "Y" : "-.--",     "y": "-.--",
    "Z" : "--..",     "z": "--..",
    " " : "/",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}

inverseMorseAlphabet=dict((v,k) for (k,v) in morseAlphabet.items())

testCode = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.-- "

# parse a morse code string positionInString is the starting point for decoding
def decodeMorse(code, positionInString = 0):
    if positionInString < len(code):
        morseLetter = ""
        for key,char in enumerate(code[positionInString:]):
            if char == " ":
                positionInString = key + positionInString + 1
                letter = inverseMorseAlphabet[morseLetter]
                return letter + decodeMorse(code, positionInString)
            else:
                morseLetter += char
    else:
        return ""
    return ""
    
#encode a message in morse code, spaces between words are represented by '/'
def encodeToMorse(message):
    encodedMessage = ""
    for char in message[:]:
        encodedMessage += morseAlphabet[char.upper()] + " "
    return encodedMessage
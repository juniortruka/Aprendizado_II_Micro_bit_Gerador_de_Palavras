# Gerador de palavras

def on_gesture_shake():
    basic.show_string("" + (adjectives[randint(0, 2)]))
    basic.pause(2000)
    basic.show_string("" + (nouns[randint(0, 2)]))
    basic.pause(2000)
    basic.show_string("" + (verbs[randint(0, 2)]))
    basic.pause(2000)
    basic.show_string("" + (adverbs[randint(0, 2)]))
    basic.pause(2000)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

adverbs: List[str] = []
verbs: List[str] = []
nouns: List[str] = []
adjectives: List[str] = []
# Mostrar adjetivos 
adjectives = ["FELIZ", "GRANDE", "CORAJOSO"]
# Mostrar substantivos
nouns = ["CACHORRO", "FAMILIA", "LAR"]
# Mostrar  verbos
verbs = ["AMAR", "VIVER", "ALEGRAR-SE"]
# Mostrar   adverbIos
adverbs = ["RAPIDAMENTE", "SILENCIOSAMENTE", "AMAVELMENTE"]

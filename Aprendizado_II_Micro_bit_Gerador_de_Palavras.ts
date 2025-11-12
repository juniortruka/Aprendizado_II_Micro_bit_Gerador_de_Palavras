// Gerador de palavras

input.onGesture(Gesture.Shake, function () {
    basic.showString("" + (adjectives[randint(0, 2)]))

    basic.pause(2000)

    basic.showString("" + (nouns[randint(0, 2)]))

    basic.pause(2000)
    basic.showString("" + (verbs[randint(0, 2)]))

    basic.pause(2000)

    basic.showString("" + (adverbs[randint(0, 2)]))

    basic.pause(2000)
})
let adverbs: string[] = []
let verbs: string[] = []
let nouns: string[] = []
let adjectives: string[] = []

// Mostrar adjetivos 
adjectives = ["FELIZ", "GRANDE", "CORAJOSO"]
//  Mostrar substantivos
nouns = ["CACHORRO", "FAMILIA", "LAR"]
//Mostrar  verbos
verbs = ["AMAR", "VIVER", "ALEGRAR-SE"]
// Mostrar   adverbIos
adverbs = ["RAPIDAMENTE", "SILENCIOSAMENTE", "AMAVELMENTE"]

from spellchecker import SpellChecker
from textblob import TextBlob
from symspellpy import SymSpell, Verbosity
import enchant


pyspell_checker = SpellChecker()

symspell = SymSpell(max_dictionary_edit_distance=2)
symspell.load_dictionary("improving-writing-assistance-at-jetbrains-ai\\data\\frequency_dictionary_symspell.txt", term_index=0, count_index=1)

enchant_checker = enchant.Dict("en_US")


def pyspellchecker_correct(sentence):
    corrected_words = [pyspell_checker.correction(word) or word for word in sentence.split()]
    return ' '.join(corrected_words)


def textblob_correct(sentence):
    return str(TextBlob(sentence).correct())


def symspell_correct(sentence):
    corrected_words = []
    for word in sentence.split():
        suggestions = symspell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            corrected_words.append(suggestions[0].term)
        else:
            corrected_words.append(word)
    return ' '.join(corrected_words)


def enchant_correct(sentence):
    corrected_words = [
        word if enchant_checker.check(word) else (enchant_checker.suggest(word)[0] if enchant_checker.suggest(word) else word)
        for word in sentence.split()
    ]
    return ' '.join(corrected_words)






# Test examples :: DELETE LATER

# incorrect_sentences = ["Ths is an exmple.", "He went to the stor.", "Somrbodz tat i used to knoe"]
# correct_sentences = ["This is an example.", "He went to the store.", "Somebody that I used to know"]

# for incorrect, correct in zip(incorrect_sentences, correct_sentences):
#     pyspell_result = pyspell_correct(incorrect)
#     textblob_result = textblob_correct(incorrect)
#     symspell_result = symspell_correct(incorrect)
#     enchant_result = enchant_correct(incorrect)

#     print(f"Original: {incorrect}")
#     print(f"Corrected (PySpellChecker): {pyspell_result}")
#     print(f"Corrected (TextBlob): {textblob_result}")
#     print(f"Corrected (SymSpell): {symspell_result}")
#     print(f"Corrected (Enchant): {enchant_result}")
#     print(f"Expected Correct: {correct}\n")
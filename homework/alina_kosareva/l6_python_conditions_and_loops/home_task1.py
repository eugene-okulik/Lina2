punctuation = ".,!?;:-"
text="Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
" Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
words = text.split()
new_text = []
for i in words:
    if i[-1] in punctuation:
        core = i[:-1]
        punct = i[-1]
    else:
        core = i
        punct = ""

    new_word = core + "ing" + punct
    new_text.append(new_word)

print(" ".join(new_text))

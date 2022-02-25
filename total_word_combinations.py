#pylint: disable = C0114
#pylint: disable = C0115
#pylint: disable = C0116

# calculate the total combinations of vowels and consonents based on word length
def calculate(wordLen, maxVowels):

    if wordLen > 0:

        vowel = ['a', 'e', 'i', 'o', 'u']
        consonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                     'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        count = 0
        word = []
        strin = consonent
        strin *= wordLen

        if maxVowels > 0:

            for __ in vowel:
                for ___ in consonent:
                    # strin = strin[:k] + vowel + strin[k+1:]

                    word.append(strin)
                    count += 1

    print(count)


calculate(int(input()), int(input()))

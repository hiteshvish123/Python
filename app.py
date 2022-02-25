def calculate(wordLen=int(input()), maxVowels=int(input())):

    if wordLen > 0:

        vowel = ['a', 'e', 'i', 'o', 'u']
        consonent = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
                     'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        count = 0
        word = []
        strin = ''

        if maxVowels > 0:

            for i in range(0, wordLen):
                strin *= wordLen
                for j in vowel:
                    for k in consonent:
                        #strin = strin[:k] + vowel + strin[k+1:]
                        word.append(strin)
                        count += 1

    print(count)


calculate()

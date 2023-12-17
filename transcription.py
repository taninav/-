import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

vowels = ["ы","у", "э", "о","а"]
spec = ["е","ё","ю","я", "и"]

vse = vowels + spec

vowels_upper = ["Ы","У", "Э", "О","А"]
special_vowels_upper = ["Е","Ё","Ю","Я", "И"]
specials = {"Я": "jА", "Ё": "jО","Е": "jЭ","Ю": "jУ", "И": "И"}
specials_after_cons = {"Я": "А", "Ё": "О","Е": "Э","Ю": "У", "И": "И"}

zvon_gluh = {"б": "п","в": "ф", "д": "т", "ж": "ш", "з": "с"}

specials_lower = {"я": "iа", "ё": "iа","е": "iи","ю": "iу", "и": "и"}
vowels_lower = {"и": "и", "э": "и", "а": "а", "о": "а", "ы": "ы","у": "у"}
specials_lower_after_cons = {"я": "а", "ё": "и","е": "и","ю": "у", "и": "и"}

vel_consonants = ["ш","ж","ц"]
palat_consonants = ["й","ч","щ"]
znaks = ["ъ", "ь"]
vtoraya_stepen_redukcii = {"и": "ь", "э": "ь", "а": "ъ", "о": "ъ", "ы": "ы","у": "у"}
vtor_spec = {"е": "iь", "ё": "iь", "я": "iь", "ю": "iу", "и":"ь"}
vtor_spec_af_cons = {"е": "ь", "ё": "ь", "я": "ь","ю": "у", "и": "ь"}
consonants = ["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ"]



def transcription(str):
    prephase = str
    prephase = prephase.replace("ьИ","ьjИ")
    prephase = prephase.replace("ьи","ьiи")
    prephase = prephase.replace('Ъ','')
    prephase = prephase.replace('ь',"'")

    slovo = list(prephase)
    p = [i for i in range(len(slovo)) if slovo[i].isupper()]
    if len(p) != 1:
       raise
    n = p[0]
    if slovo[n] in special_vowels_upper:
        if n == 0:
            slovo[0] = specials[slovo[0]]
        else:
            if slovo[n-1] in consonants:
                if slovo[n-1] in vel_consonants:
                    slovo[n] = specials_after_cons[slovo[n]]
                elif slovo[n-1] in palat_consonants:
                    slovo[n] = specials_after_cons[slovo[n]]
                else:
                    slovo[n] = "'" + specials_after_cons[slovo[n]]
            else:
                slovo[n] = specials[slovo[n]]
    elif slovo[n] in vowels_upper:
        pass
    else:
        raise 
        
    if n == len(slovo) - 1:
        zaud = []
    if n != len(slovo) - 1:
        zaud = slovo[n+1:]
        if zaud[0] in spec:
            zaud[0] = vtor_spec[zaud[0]]
        for j in range(1,len(zaud)):
            if zaud[j] in vowels:
                zaud[j] = vtoraya_stepen_redukcii[zaud[j]]
            elif zaud[j] in spec:
                if zaud[j-1] in consonants:
                    if zaud[j-1] in vel_consonants or zaud[j-1] in palat_consonants:
                        zaud[j] = vtor_spec_af_cons[zaud[j]]
                    else:
                        zaud[j] = "'" + vtor_spec_af_cons[zaud[j]]
                else:
                    zaud[j] = vtor_spec[zaud[j]]
    if n == 0:
        predud = []
    if n > 0:
        predud = slovo[:n]
        glasn_id = [k for k in range(len(predud)) if predud[k] in vse]
        if len(glasn_id) == 0:
            pass
        elif len(glasn_id) == 1:
            if glasn_id[0] == 0:
                if predud[0] in vowels:
                    predud[0] = vowels_lower[predud[0]]
                if predud[0] in spec:
                    predud[0] = specials_lower[predud[0]]
            else:
                if predud[glasn_id[0]] in vowels:
                    predud[glasn_id[0]] = vowels_lower[predud[glasn_id[0]]]
                if predud[glasn_id[0]] in spec:
                    if predud[glasn_id[0]-1] in consonants:
                        if predud[glasn_id[0]-1] in vel_consonants or predud[glasn_id[0]-1] in palat_consonants:
                            predud[glasn_id[0]] = specials_lower_after_cons[predud[glasn_id[0]]]
                        else:
                            predud[glasn_id[0]] = "'" + specials_lower_after_cons[predud[glasn_id[0]]]
        else: 
            glasn_id.reverse()

            if glasn_id[len(glasn_id)-1] == len(predud)-1:
                if predud[glasn_id[len(glasn_id)-1]] in vowels:
                    predud[glasn_id[len(glasn_id)-1]] = vowels_lower[predud[glasn_id[len(glasn_id)-1]]]
                if predud[glasn_id[len(glasn_id)-1]] in spec:
                    predud[glasn_id[len(glasn_id)-1]] = specials_lower[predud[glasn_id[len(glasn_id)-1]]]
                if predud[glasn_id[0]] in vowels:
                    predud[glasn_id[0]] = vowels_lower[predud[glasn_id[0]]]
                if predud[glasn_id[0]] in spec:
                    if predud[glasn_id[0]-1] in consonants:
                        if predud[glasn_id[0]-1] in vel_consonants or predud[glasn_id[0]-1] in palat_consonants:
                            predud[glasn_id[0]] = specials_lower_after_cons[predud[glasn_id[0]]]
                        else:
                            predud[glasn_id[0]] = "'" + specials_lower_after_cons[predud[glasn_id[0]]]
                for t in range(1, len(glasn_id)-1):
                    if predud[glasn_id[t]] in vowels:
                        predud[glasn_id[t]] = vtoraya_stepen_redukcii[predud[glasn_id[t]]]
                    elif predud[glasn_id[t]] in spec:
                        if predud[glasn_id[t]-1] in consonants:
                            if predud[glasn_id[t]-1] in vel_consonants or predud[glasn_id[t]-1] in palat_consonants:
                                predud[glasn_id[t]] = vtor_spec_af_cons[predud[glasn_id[t]]]
                            else:
                                predud[glasn_id[t]] = "'" + specials_after_cons[predud[glasn_id[t]]]
                        else:
                            predud[glasn_id[t]] = vtor_spec[predud[glasn_id[t]]]
            else:
                if predud[glasn_id[0]] in vowels:
                    predud[glasn_id[0]] = vowels_lower[predud[glasn_id[0]]]
                if predud[glasn_id[0]] in spec:
                    if predud[glasn_id[0]-1] in consonants:
                        if predud[glasn_id[0]-1] in vel_consonants or predud[glasn_id[0]-1] in palat_consonants:
                            predud[glasn_id[0]] = specials_lower_after_cons[predud[glasn_id[0]]]
                        else:
                            predud[glasn_id[0]] = "'" + specials_lower_after_cons[predud[glasn_id[0]]]
                for t in range(1, len(glasn_id)):
                    if predud[glasn_id[t]] in vowels:
                        predud[glasn_id[t]] = vtoraya_stepen_redukcii[predud[glasn_id[t]]]
                    elif predud[glasn_id[t]] in spec:
                        if predud[glasn_id[t]-1] in consonants:
                            if predud[glasn_id[t]-1] in vel_consonants or predud[glasn_id[t]-1] in palat_consonants:
                                predud[glasn_id[t]] = vtor_spec_af_cons[predud[glasn_id[t]]]
                            else:
                                predud[glasn_id[t]] = "'" + vtor_spec_af_cons[predud[glasn_id[t]]]
                        else:
                            predud[glasn_id[t]] = vtor_spec[predud[glasn_id[t]]]

    prelast = ''.join(predud + list(slovo[n]) + zaud)
    prelast = prelast.replace("''","'")

    prelast = prelast.replace("ч","ч'")
    prelast = prelast.replace('щ',"щ'") 

    for i in range(len(prelast)):
        if prelast[i] == 'й':
            if i+1 < len(prelast) and prelast[i+1].isupper():
                prelast = prelast[:i] + 'j' + prelast[i+1:]
            else:
                prelast = prelast[:i] + 'i' + prelast[i+1:]
    prelast = prelast.replace("''","'")
    last = list(prelast)
    if last[-1] == "'":
        last.pop()
        if last[-1] in zvon_gluh.keys():
            last[-1] = zvon_gluh[last[-1]]
        last.append("'")
    else:
        if last[-1] in zvon_gluh.keys():
            last[-1] = zvon_gluh[last[-1]]


    itog = '['+''.join(last)+']'



    return itog


        

    

    



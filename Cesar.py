alfabeto =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']



def cesar(string,c):
    result = ''
    #iterar sobre el string
    for n in string:
        #Si es mayuscula
        if n.isupper():
            n = n.lower()        
            i = 0 
            while i<27:
                if alfabeto[i] == n:
                    break
                i+=1

            #Si no está presente en el alfabeto
            if i == 27:
                result += n
            else:
                if i+c >= 27:
                    j = i+c - 26
                    result += alfabeto[j].upper()
                else: 
                    result += alfabeto[i+c].upper()

        else:
            i = 0 
            while i<27:
                if alfabeto[i] == n:
                    break
                i+=1

            #Si no está presente en el alfabeto
            if i == 27:
                result += n
            else:
                if i+c >= 27:
                    j = i+c - 26
                    result += alfabeto[j]
                else:
                    result += alfabeto[i+c]

    print(result)




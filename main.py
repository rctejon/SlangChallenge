
def calculateNGrams(text, n):
    """Calculete n-grams of given string

    Complexity
    ----------
    This algorithm have O(t) (linear) complexity where t is the length of "text"

    Parameters
    ----------
    text : str
        The text to calculate ngrams
    n : int
        length of the ngrams

    Returns
    -------
    list
        a list of strings that represent the ngrams
    """

    #Indexes where one ngram could start (this operation have O(t) complexity)
    indexes=range(len(text)-n+1)
    #map from the array of indexes where an ngram start to an array that with the ngrams starting by those indexes( This operation have O(t))
    return list(map(lambda x: text[x:x+n],indexes))

def mostFrecuentNGram(text, n):
    """Calculete the first most frecuent n-gram of given string

    Complexity
    ----------
    This algorithm have O(t) (linear) complexity in the average case and O(t^2) (quadratic) in the worst case
    where t is the length of "text", due to the properties of an Hash Table where the searching and insetion of elements 
    complexity have an average case of O(1) and worst case O(e) where e is the number of elements inserted in the table (Which in this case is t-n+1) 

    Parameters
    ----------
    text : str
        The text to calculate ngrams
    n : int
        length of the ngrams

    Returns
    -------
    str
        a string which is the most frecuent ngram
    """

    # Declaration of an empty python dictionary (Hash Table Data Structure) where will be storage the number of appearances of all the ngrams (This operation have a constant complexity)
    diccionario={}
    # Calculation of the text ngrams (This operation have linear complexity)
    ngrams = calculateNGrams(text,n)
    # Declaration of auxiliar variable that stores the actual Most Frecuent Ngram( This operation have a constant complexity)
    actualMostFrecuentNgram = ""
    # Declaration of auxiliar variable that stores the number of appearences of the actual Most Frecuent Ngram( This operation have a constant complexity)
    actualMax = 0
    # Iteration over the ngrans of the text (This operation have O(t) complexity in the average case and O(t^2) in the worst case)
    for ngram in ngrams:
        # if the ngram is already in the hash table
        if ngram in diccionario.keys():
            #Sum 1 to the value of the ngram in the hash table
            diccionario[ngram]+=1
        # if the ngram is not already in the hash table
        else:
            # insert the ngram to the hash table with value 1
            diccionario[ngram]=1
        # if the value of ngram is bigger than the actual must frecuent ngram make the change
        if actualMax < diccionario[ngram]:
            actualMostFrecuentNgram = ngram
            actualMax = diccionario[ngram]
    return actualMostFrecuentNgram

print(calculateNGrams("to be or not to be",2))
print(mostFrecuentNGram("to be or not to be",2))
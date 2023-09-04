import pandas as pd
import numpy as np

def chunk_sizer(serie):
    """
        This functions takes a Pandas Series and summarizes
        its status in terms of number of NA entries and valid number entries.
        
        serie is a pandas.series object    
    """
    
    
    chunk = [] # to be used to populate size of the continous NA or number chunks
    
    k = 0 # index to count valid elements
    n = 0 # index to count NA elements
    m = np.isnan(serie[0]) # Checks whether the first element (and chunk) of the series is NA or valid.
    
    """
    Following for snippet with k and n counters;
        -Checks the NAN or valid status of an element
        -Considers the previous element validity or NA status
        -Accordingly, extends the chunk or finish it and move on with another chunk
    """
    
    for i in range(len(serie)):
        if (np.isnan(serie[i]) == False) & (n == 0): # The element is valid and it precedes a valid chunk
            k = k + 1
            if i == len(serie)-1: # This is series end modification, to be able to count the last chunk
                chunk.append(k)
        elif (np.isnan(serie[i]) == True) & (k != 0): # The element is NaN and it precedes a valid chunk
            chunk.append(k)
            k = 0
            n = n + 1
        elif (np.isnan(serie[i]) == True) & (k == 0): # The element is NaN and it precedes a NaN chunk
            n = n + 1
            if i == len(serie)-1:
                chunk.append(n)
        elif (np.isnan(serie[i]) == False) & (n != 0): # The element is valid and it precedes a NaN chunk
            chunk.append(n)
            n = 0
            k = k + 1
    
    k = 0 # resetting the previous index and using it to sum valid and NA elements total number
    
    for i in range(0, len(chunk), 2): # jumps by 2 to only count NA or valid chunks accordingly
        """
        If m below is true, i.e. the first element of "serie" is NaN, k sums NA row number
        Otherwise, k sums valid row number.
        """
        k = k + chunk[i] 
    
    """
    Because of the structure of the algorithm, half or half + 1 number of chunks will always be valid
        and the remaining half will be NaN.
    We exploit this by knowing the first element's NaN or valid status, 
        and size of the series and chunk series.
    
    len(chunk) is how many chunks we have from "serie".
    len(serie) gives the total number of elements/rows.
    """
    if m == True:
        if len(chunk) % 2 != 0:
            print("Number of NA chunks are", (len(chunk) // 2)+1, " within ", len(chunk), " chunks.")
            print("Number of Valid chunks are", (len(chunk) // 2), " within ", len(chunk), " chunks.")
        else:
            print("Number of NA chunks are", (len(chunk) // 2), " within ", len(chunk), " chunks.")
            print("Number of Valid chunks are", (len(chunk) // 2), " within ", len(chunk), " chunks.")
        print("There are " + str(k) + " NA rows within " + str(len(serie)) + " total rows.")
        print("There are " + str(len(serie) - k) + " number rows within " + str(len(serie)) + " total rows.")
    elif m == False:
        if len(chunk) % 2 != 0:
            print("Number of NA chunks are", (len(chunk) // 2))
            print("Number of Valid chunks are", (len(chunk) // 2)+1)
        else:
            print("Number of NA chunks are", (len(chunk) // 2))
            print("Number of Valid chunks are", (len(chunk) // 2))
        print("There are " + str(len(serie) - k) + " NA rows within " + str(len(serie)) + " total rows.")
        print("There are " + str(k) + " number rows within " + str(len(serie)) + " total rows.")                    
    return chunk

def valid_chunk(serie):
    """
    This function gives direct summary information (max and histogram)
    on valid number chunks and total valid rows of a series.
    """
    
    
    chunk = []
    k = 0
    for i in range(len(serie)):
        if np.isnan(serie[i]) == False:
            k = k + 1
            if i == len(serie)-1:
                chunk.append(k)
        elif (np.isnan(serie[i]) == True) & (k != 0):
            chunk.append(k)
            k = 0
    max_chunk = (np.array(chunk)).max()
    print("Total number of valid number elements: ", (np.array(chunk)).sum())
    print("Maximum length of a continuous valid number series: ",  max_chunk)
    if max_chunk > 400:
        hist, bins = np.histogram(chunk, bins = range(0, max_chunk, (max_chunk//20)))
    else:
        hist, bins = np.histogram(chunk, bins = range(0, max_chunk+1))
    print("Histogram distribution of chunk sizes in the series: ",hist)
    print("Histogram bins: ", bins)
    return chunk
    
def nan_chunk(serie):

    """
    This function gives direct summary information (max and histogram)
    on NA chunks and total valid rows of a series.
    
    As can be seen, it is the mirror of valid_chunk function.
    """
    
    chunk = []
    k = 0
    for i in range(len(serie)):
        if np.isnan(serie[i]) == True:
            k = k + 1
            if i == len(serie)-1:
                chunk.append(k)
        elif (np.isnan(serie[i]) == False) & (k != 0):
            chunk.append(k)
            k = 0
    max_chunk = (np.array(chunk)).max()
    print("Total number of NA elements: ", (np.array(chunk)).sum())
    print("Maximum length of a continuous NA series: ",  max_chunk)
    if max_chunk > 400:
        hist, bins = np.histogram(chunk, bins = range(0, max_chunk, (max_chunk//20)))
    else:
        hist, bins = np.histogram(chunk, bins = range(0, max_chunk+1))
    print("Histogram distribution of chunk sizes in the series: ",hist)
    print("Histogram bins: ", bins)
    return chunk
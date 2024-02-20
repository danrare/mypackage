def top_n(items, n):
    """Returns the top items in an array in descending other

        Args:
            items (array): list of arrays or array-like objects
        n (int): number of items to return.
        Return :
            array: top n items in desc order

        Egs:
            >>> top_n([8, 3, 2, 7 ,5], 3)
            [8, 7 , 5] 
    """
    for i in range(n):
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    top_n = items[-n:]

    return top_n[::-1]
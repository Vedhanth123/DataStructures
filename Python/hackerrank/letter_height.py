"""When you select a contiguous block of text in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

PDF-highighting.png

In this challenge, you will be given a list of letter heights in the alphabet and a string. Using the letter heights given, determine the area of the rectangle highlight in  assuming all letters are  wide.

For example, the highlighted . Assume the heights of the letters are  and . The tallest letter is  high and there are  letters. The hightlighted area will be  so the answer is ."""

def designerPdfViewer(h,word):

    list_of_height_of_each_letter = []

    for x in range(len(word)):

        list_of_height_of_each_letter.append(h[ord(word[x])-97])

    higest_height_of_word = 0

    for x in list_of_height_of_each_letter:
        if(higest_height_of_word < x):
            higest_height_of_word = x

    return higest_height_of_word * 1 * len(word)
    
print(designerPdfViewer([1, 3, 1, 3, 1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5, 5 ,5 ,5 ,5 ,5 ,7],"zoba"))
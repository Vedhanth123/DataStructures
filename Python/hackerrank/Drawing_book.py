# A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page  is always on the right side:

# image

# When they flip page , they see pages  and . Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and a student wants to turn to page , what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .

# even case

""" NOTE: NEED TO SOLVE THIS """


# def PageCount(no_of_pages, p):
    
    # if(no_of_pages % 2 == 0):
            
    #     front_page = 1
    #     back_page = no_of_pages
    #     no_of_turns = 0

    #     while (True):

    #         # checking for the starting page
    #         if(front_page == p or back_page == p):
    #             return no_of_turns
            
    #         # checking for next page by turning them
    #         front_page += 1
    #         back_page -= 1
    #         no_of_turns += 1

    #         # checking for the page after turning
    #         if(front_page == p or back_page == p):
    #             return no_of_turns

    #         front_page += 1
    #         back_page -= 1
    #         # next pages will be checked in the next iteration

    # else:

    #     front_page = 1
    #     back_page = no_of_pages 

    #     no_of_turns = 0

    #     while(True):

    #         # checking at the starting page
    #         if(back_page == p or front_page == p):
    #             return no_of_turns
            
    #         # going to left page on the back side
    #         back_page -= 1

    #         # checking for left back page
    #         if(back_page == p):
    #             return no_of_turns

    #         # turning page
    #         no_of_turns += 1
    #         front_page += 1
    #         back_page -= 1

    #         if(front_page == p or back_page == p):
    #             return no_of_turns

    #         front_page += 1
    #         back_page -= 1

def PageCount(n, p):

    # algorithm
    # To return minimum no. of turns to reach page p

    # 1) traverse through the book
    # 1.0) divide the book into two types even type of book and odd type of book
    # 1.1) use a variable for turning the book
    # 1.2) use another variable for comparing the pages in each turn with the actual page

    # 2) check every time for the p after traversing through the book

    # 3) return the minimun no. of turns

    last_page = n
    no_of_turns = 0
    front_page = 1

    # if the no of pages are even
    if(n % 2 == 0):

        while(True):

            if(last_page == p or front_page == p):
                return no_of_turns

            # turning to next page
            no_of_turns += 1
            last_page -= 1
            front_page += 1

            if(last_page == p or front_page == p):
                return no_of_turns
            
            last_page -= 1
            front_page += 1
      

    else:
        
        while(True):

            if(last_page == p or front_page == p):
                return no_of_turns
            
            last_page -= 1

            if(last_page == p):
                return no_of_turns
            
            no_of_turns += 1
            last_page -= 1
            front_page += 1

            if(last_page == p or front_page == p):
                return no_of_turns

            front_page += 1
        

# for x in range(10):

print(PageCount(5809,2668))   # ques = 5809 ,p = 2668 , ans = 1334, my_ans = 1570
    
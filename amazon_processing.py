
from bs4 import BeautifulSoup
# give a filename to python


##NOTE) use this later: https://nbviewer.jupyter.org/github/walshbr/humanists-nlp-cookbook/blob/master/file_structure.ipynb



#open this file from this folder, read it with bite, save it in ready_to_process
filename_goes_here = 'curious-incident/ref=cm_cr_arp_d_paging_btm_2@ie=UTF8&reviewerType=all_reviews&pageNumber=1'
with open(filename_goes_here, 'rb') as file_input:
  ready_to_process = file_input.read()

# now ready_to_process has our html

# turn that html into soup
soup = BeautifulSoup(ready_to_process)
text = soup.text.replace("\n", "")



cleantext = BeautifulSoup(text, "lxml")
# print(cleantext)

# use the soup documentation to process it


# <div class="a-row review-data"><span data-hook="review-body" class="a-size-base review-text">1) Plot (4 stars) - A boy with Asperger's sets off to solve the murder of a neighbor's dog, only to uncover the secrets of his own life.  What was so brilliant about the plot was not the final reveal (which the reader can guess before the limited main character can), but the tension of imagining this special needs kid trying to navigate across London by himself.<br /><br />2) Characters (5 stars) - Christopher has Asperger's--he's hyper-analytical, obsessive, has no sense of other people's emotions, and the slightest disorder will send him into a fit.  Yet with all these difficulties he is still brave enough to push out of his comfort zone to solve his case.  It's hard enough to assert your independence in a world of people like you, but this book shows the coming of age struggle when you're surrounded by aliens.  Speaking of aliens (i.e., the "normal" people in this book) they were also done magnificently, representing the full gamut of responses people have when encountering someone like Christopher--from teasing, to sympathy, to the challenge of being his parent.<br /><br />3) Theme (4 stars) - What it's like to be a stranger in a strange land.  We've seen this explored from the standpoint of ethnic minorities, females, gays, immigrants, and here we get it from the view of a mental minority.  Like with the others, this book sheds light on how society isn't built for all its citizens.<br /><br />4) Voice (5 stars) - Incredible.  Haddon's prose makes you feel like you have autism / Asperger's, makes you see every bit of the world through Christopher's eyes, which is remarkable magic.<br /><br />5) Setting (3 stars) - Setting wasn't really the point, but London was described fine.<br /><br />6) Overall (4 stars) - Highly recommended.  This is an important work which gives insight into the next group of minorities that society can either shun or accommodate.</span></div>

results = soup.find_all('span', attrs={'class':'a-size-base review-text'})


# first_result = results[0]
# first_result.find("span data-hook="review-body" class="a-size-base review-text")

results = [result.text for result in results]
# print(results)



with open('curious-review/1.txt', 'w') as fout:
    fout.write(results[0])


# -----NOTE) try this later: looping & saving each text files
# with open('curious-review/test.txt', 'a') as fout:
#      for result in results:
#          fin.write(results)

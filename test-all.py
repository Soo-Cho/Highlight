# urls = 'curious-incident/ref=cm_cr_arp_d_paging_btm_2@ie=UTF8&reviewerType=all_reviews&pageNumber='
# for count in range(1, 385):
#     print(urls + str(count))


# #open this file from this folder, read it with bite, save it in ready_to_process
# filename = 'curious-incident/urls'
# with open(filename, 'rb') as file_input:
#   ready_to_process = file_input.read()


# import glob
#
# filenames = glob('curious-incident/ref=cm_cr_arp_d_paging_btm_2@ie=UTF8&reviewerType=all_reviews&pageNumber=*.*')
# for line in fileinput.input(filenames):
#     pass




#-------------------------------------------------------------
#open this file from this folder, read it with bite, save it in ready_to_process
filename_goes_here = 'curious-incident/ref=cm_cr_arp_d_paging_btm_2@ie=UTF8&reviewerType=all_reviews&pageNumber='
for count in range (1,10):
    filename_goes_here + str(count)


with open(filename_goes_here, 'rb') as file_input:
  ready_to_process = file_input.read()

# now ready_to_process has our html

# turn that html into soup
soup = BeautifulSoup(ready_to_process)
text = soup.text.replace("\n", "")

cleantext = BeautifulSoup(text, "lxml")

# give a filename to python

with open(filename_goes_here, 'r') as file_input:
  ready_to_process = file_input.read()

# now ready_to_process has our html

# turn that html into soup
soup = BeautifulSoup(ready_to_process)
soup.text

# use the soup documentation to process it

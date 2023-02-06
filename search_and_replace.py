'''This are usefull functions to interact with
text files.
The following functions can modify plain text files such as:
-.txt
-.qcr

there is no need to import any library, this functions use python3 or over
installed methods
'''
# creating a variable and storing the text
# that we want to search
def replace_text_on_file(file,replaced_text,replacement_text):
    search_text = replaced_text

    # creating a variable and storing the text
    # that we want to add
    replace_text = replacement_text

    # Opening our text file in read only
    # mode using the open() function
    with open(file, 'r') as file1:

    	# Reading the content of the file
    	# using the read() function and storing
    	# them in a new variable
    	data = file1.read()

    	# Searching and replacing the text
    	# using the replace() function
    	data = data.replace(search_text, replace_text)

    # Opening our text file in write only
    # mode to write the replaced content
    with open(file, 'w') as file1:

    	# Writing the replaced data in our
    	# text file
    	file1.write(data)

    # Printing Text replaced
    print("Text replaced")

#Test
#search_text = "replaced"
#replace_text = "-------------THIS IS A REPLACEMENT------------"
#replace_text_on_file('test.qcr',search_text,replace_text)

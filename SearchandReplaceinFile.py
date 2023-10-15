#search_text = "els_base"
#replace_text = "els_vip_spi"
#file_path = "/home/vkewlani-extcon/pytest/tb_top.sv"
def FSearchandReplaceinFile(file_path,search_text,replace_text,debug_path):
    #print("S&R_for_file: " + file_path)
    open(debug_path,"a").write("S&R_for_file: " + file_path + '\n')
    # Opening our text file in read only
    # mode using the open() function
    with open(file_path, 'r') as file:
        # Reading the content of the file
        # using the read() function and storing
        # them in a new variable
        data = file.read()
        if data.find(search_text) != -1:
            # Searching and replacing the text
            # using the replace() function
            data = data.replace(search_text, replace_text)
            #print(file_path + "---text_found")
            open(debug_path,"a").write(file_path + "---text_found" + '\n')
            # Opening our text file in write only
            # mode to write the replaced content
            with open(file_path, 'w') as file:
                # Writing the replaced data in our
            	# text file
            	file.write(data)
            #print(search_text+" replaced with "+replace_text+" in "+file_path)
            open(debug_path,"a").write(search_text+" replaced with "+replace_text+" in "+file_path + '\n')
            open(debug_path,"a").write("----------------------------------------------------------------\n")

#    # Opening our text file in write only
#    # mode to write the replaced content
#    with open(file_path, 'w') as file:
#        # Writing the replaced data in our
#    	# text file
#    	file.write(data)
#    print(search_text+" replaced with "+replace_text+" in "+file_path)

# Call the function as shown below
#search_text = "els_base"
#replace_text = "els_vip_spi"
#file_path = "/home/vkewlani-extcon/pytest/tb_top.sv"
#FSearchandReplaceinFile(file_path, search_text, replace_text)

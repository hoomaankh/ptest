name_of_file = "testme"
completeName = '/home/'+ name_of_file + ".txt"
toFile = "this is the first chance to work\nwith python\n"
file1 = open(completeName , "w")
file1.write(toFile)
file1.close()

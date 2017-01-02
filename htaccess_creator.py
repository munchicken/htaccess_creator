""" htaccess_creator by Sarah Pierce
    (c) 1/1/2017 GPL
    Creates ErrorDocument statements for use in an Apache htaccess file
	Just copy and paste into your config file for your website
	---
	Currently configured to create HTTP Status Cats ErrorDocuments
	(https://http.cat/)
	but this can be changed on line 16
	---
	Reads from "errors.txt" (file with one error code per line, see HTTP Status Cats sample in repo)
"""
	

try:
	error_list = open('errors.txt')
	for a_error in error_list:
		try:
			with open('error_doc_list.txt','a') as error_doc_list:
				try:
					print ('ErrorDocument '+a_error.rstrip('\n')+' \'<style> body{background-color: #000000} iframe{display: block; margin-left: auto; margin-right: auto; width:750px; height:600px; border:none} </style> <iframe src="https://http.cat/'+a_error.rstrip('\n')+'"></iframe>', file=error_doc_list)
				except ValueError:
					pass
		except IOError as err:
			print('File error:' + str(err))
	error_list.close()
except IOError:
	print('The file containing the error list is missing')
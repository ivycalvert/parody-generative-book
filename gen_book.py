#!/usr/bin/python3
import csv
import glob
import os
import shutil
import time
import codecs
import sys

#HERE ARE THE THREE THINGS YOU MIGHT WANT TO CHANGE

## 1) input file template
idml = 'template.idml'

## 2) fields where data can be found
csv_file = 'fields.tsv'

## 3) output name (the idml part will be added)
output_filename = 'final_book'

#Separator for fields in the CSV file (in case you want a 'tab', just change to '\t')
#change this
separator='\t'

fields_to_replace = []
single_record = {}
with codecs.open(csv_file, 'r', encoding='utf-8-sig') as csvfile:
    #construct our reader for the CSV file
    reader = csv.reader(csvfile, delimiter=separator)

    for row in reader:
        record = {
            'search': "###{}###".format(row[0]), 'replace_key':row[0]
        }
        single_record[row[0]] = row[1]
        fields_to_replace.append(record)


#Unzip the IDML file and save it locally

template = 'template/'
shutil.unpack_archive(idml,template, 'zip')

#print it out to the console
print("Saving: {}".format(output_filename))

#Make a copy of our template
try:
        shutil.copytree(template,'tmp/')
except FileExistsError:
                #'tmp/' may be leftover from a previous attempt, or your OS handles file deletion poorly
                if os.path.isdir('tmp')==True:
                        dlt = input("\ntmp/ directory exists\nYou may need to re-run the program \nRemove tmp/(y/n)?").lower()
                        if dlt != 'n':
                                shutil.rmtree('tmp/')
                        else:
                                print("\nPlease manually remove 'tmp/' and try again")
                                sys.exit(1)

stories = os.listdir(template+'Stories')
#for each file that we want to modify
for entry in stories:
    #open a new file that we will write to
    try:
        with codecs.open('tmp.tmp', "w", encoding='utf-8') as fout:
            #open the file that we want to read from
            with codecs.open(template+'Stories/'+entry, "r", encoding='utf-8') as fin:
                #on every line
                for line in fin:
                    line2 = line
                    #for every thing we want to search for

                    for rep in fields_to_replace:
                        #see if this line has anything to replace and replace it with data from our CSV file
                        line2 = line2.replace(rep['search'], single_record[rep['replace_key']])
                    #write this line
                    fout.write(line2)
    except PermissionError:
        print("Perms error")
        sys.exit(1)


    shutil.move('tmp.tmp', 'tmp/'+'Stories/'+entry)


#make a .zip of the folder
shutil.make_archive(output_filename, 'zip', 'tmp/')
#change the name to .idml
shutil.move(output_filename+'.zip', output_filename+'.idml')
#delete the folder we were working in
shutil.rmtree('tmp/')

#delete our unzipped IDML directory
shutil.rmtree(template)

print("Done")

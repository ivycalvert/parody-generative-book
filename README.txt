-------OVERALL CONCEPT-------
Books typically inspire thoughts of readability. Especially childrens books. Especially childrens tongue twister books. This book is a subversion of that expectation, with the added bonus of mashing together digital and physical reading culture by adding in the bonus difficulty of reading CAPTCHA images on a page. Included within, the book has elements of deciphering code and plain text alike. The concept in its roots begun as an attempt to make reading tongue twisters just as difficult as reading them quickly aloud. This allowed exploration into multiple methods of text manipulation. 

-------INTENDED BOOK BINDING-------
 - PERF BOUND
 - A5 SIZE (PORTRAIT)
 - COLOUR

-------STEPS TO GENERATE CONTENT-------

To ensure the required libraries are installed on the computer running the script (assuming it is connected through the x transfer setup, if it is not it will require more setup but this is not included) the first step to running these scripts is running the setup.sh script:

Copy the below text into the terminal window and run:

	$ bash setup.sh

While this script is running, also take this time to install the fonts in the "fonts" directory as these are required later for the InDesign file creation

Next, generate a title for the book by running the "title" script:

	$ python title.py

This will provide multiple variations for a potential title for the book that is going to be generated. If the title that automatically places inside the end InDesign file, simply go to the "title" directory where this script outputs images to and simply replace the image in the InDesign file (this can be done as part of the curation process which is mentioned later in the README)

//NOTE: before running any other scripts, the user can adjust the contents of the "film-scripts" directory which will adjust the inputs for the following scripts, impacting what outputs the project will produce. Any added files are required to be plain text files. Currently, this file has a selection of B-grade kids film scripts, however it is not limited to content of this theme, but rather this was the theme chosen for exploring within the initial scope of the project.

To generate the book content, a series of events need to be undertaken:
 - an input text needs to be selected
 - POS need to be extracted
 - words for alliteration need to be selected and saved
 - rhyming words need selecting and saving
 - grammars need to be run
 - selected grammars need to be send for the CAPTCHA generation
 - CAPTCHA images need to be generated
 - all gramars need to be saved to a tsv file for later use
 - multiple iterations of the CAPTCHA images need to be saved (to accommodate font inconsistencies)

Thankfully, you can do all this by running one script: the "genImage" script like this:

	$ python genImage.py

//NOTE: if you do not want to generate any CAPTCHA images, you can alternatively run the "genTwisters" script:
//
//	$ python genTwisters.py
//
//However, this requires more work later as adjustments have to be made to the final script for the automation process to work

Once the "genImage" script has finished running, all the content required for the automation process will be generated. Namely, the "fields.tsv" file and the iterations of the CAPTCHA images (found in the CAPTCHAs directory). 

Next step: run the "gen_book" script to generate the InDesign document from the generated data:

	$ python gen_book.py

Once this script has finished, a new file will be created in the directory. This file will be called "final_book.idml"

OPTIONAL CURATION STEPS: Technically, at this step you could call the generation process completed. However, the InDesign document may require some curation (this stage is optional as the overall concept of the book allows for some discrepencies in the visuals from the expected, however to get the fully intended output, it is suggested you continue through the next steps)

Once you open the InDesign document, scroll and inspect the elements on each page. Due to the large variance in potential grammars, some font sizes will need to be reduced to ensure no text is lost due to overflowing the text area/page bounds. 
CAPTCHA fonts occasionally cannot be turned into images, and will either depict a line or a series of squares. Within the CAPTCHAs directory, there will be iterations of the same tongue twister as a different CAPTCHA image. These are organised in the book by order (e.g. the third CAPTCHA image seen in the book will be the third CAPTCHA grammar created in the CAPTCHAs directory). For swapping this, it is important to understand the naming scheme for the CAPTCHAs directory: "out-[grammar version]-[iteration number of grammar version].png". An example series of matching CAPTCHAs are as follows: "out-0-0.png", "out-0-1.png", "out-0-2.png"...
//ALSO NOTE: due to very infrequent errors that may occur in the code, there is the chance a grammar will not be printed in the InDesign document. If this occurs, simply open the "fields.tsv" file and manually replace the ###[name]### text with a new (unused) grammar from the bottom of the list. This will need to be places both in the plain english text box area and the coded text box area (matching) on each page this error occurs. 

Once you have finished curating the InDesign document, export it out as a PDF file and you are ready to print your new book!

ALTERNATIVELY:

You could simply run the "runall" script:

	$ bash runall.sh

Which does all the above for you aside from the curation step. 
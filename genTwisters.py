from __future__ import unicode_literals
import tracery
from tracery.modifiers import base_english
import random
import json
import csv
import spacy
import os
import pronouncing
import re
import sys

nlp = spacy.load('en')

# selects a random script from those saved in the "film-scripts" directory
script = random.choice(os.listdir("film-scripts/"))
# DEBUG
# print(script)

# uses the randomly selected script from above and reads it, ready for use later on
txt = nlp(open("film-scripts/" + script + "").read())
# DEBUG
# print(txt)

# getting all the below types of words
verbs = []
verbs_past = []
nouns = []
pronouns = []
propernouns = []
adjectives = []
adverbs = []
people = []
prepositions = []
interjections = []
conjunctions = []

# pull the POS from the defined script
# make sure it doesn't include broken words
for item in txt:
        if item.pos_ == 'VERB':
            if item.text != "'s" and item.text != "'re" and item.text != "ca" and item.text != " " and item.text != "^" and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "'em":
                verbs.append(item.text.lower())
for item in txt:
    if item.tag_ == 'VBD':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "'em":
            verbs_past.append(item.text.lower())
for item in txt:
    if item.tag_ == 'NNS':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text != "'em":
            nouns.append(item.text.lower())
for item in txt:
    if item.pos_ == 'PRON':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text != "'em":
            pronouns.append(item.text.lower())
for item in txt:
    if item.tag_ == 'NNP':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text != "'em":
            propernouns.append(item.text.lower())
for item in txt:
    if item.pos_ == 'ADJ':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text != "'em":
            adjectives.append(item.text.lower())
for item in txt:
    if item.pos_ == 'ADV':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text !="'t" and item.text != "'em":
            adverbs.append(item.text.lower())   
for item in txt.ents:
    if item.label_ == 'PERSON':
        people.append(str(item))
for item in txt:
    if item.pos_ == 'ADP':
        if item.text != "'s" and item.text != "'re" and item.text != "^" and item.text != " " and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text !="'t" and item.text != "'em":
            prepositions.append(item.text.lower())  
for item in txt:
    if item.pos_ == 'INTJ':
        if item.text != "ac-" and item.text != "f" and item.text != "'s" and item.text != " " and item.text != "'re" and item.text != "^" and item.text != "^ " and item.text != " ^" and item.text != "'m" and item.text != "'d" and item.text != "'ll" and item.text != "'ve" and item.text != "•" and item.text !="'t" and item.text != "fo" and item.text != "Pp" and item.text != "M.ay" and item.text != "Ff" and item.text != "'em":
            interjections.append(item.text.lower()) 
for item in txt:
    if item.tag_ == 'CC':
        conjunctions.append(item.text.lower()) 

# convert the list of POS into a string 
j_verbs = ' '.join(map(str, verbs))
j_verbp = ' '.join(map(str, verbs_past))
j_nouns = ' '.join(map(str, nouns))
j_pron = ' '.join(map(str, pronouns))
j_propn = ' '.join(map(str, propernouns))
j_adj = ' '.join(map(str, adjectives))
j_adv = ' '.join(map(str, adverbs))
j_peep = ' '.join(map(str, people))
j_prep = ' '.join(map(str, prepositions))
j_inter = ' '.join(map(str, interjections))
j_conj = ' '.join(map(str, conjunctions))

# define for the alliteration words
v_alt = []
vp_alt = []
n_alt = []
pn_alt = []
ppn_alt = []
adj_alt = []
adv_alt = []
peep_alt = []
prep_alt = []
inter_alt = []
con_alt = []

selected_letters = ["S", "T", "P", "M", "N", "B", "C"]
all_grammars = {}

# select a random letter for the words to begin with (from this predefined list)
# letters that don't have words : v, w
# letter = random.choice(["sS", "tT", "pP", "mM", "nN", "bB", "cC"])

for chosen_letter in selected_letters:
    letter = "{}{}".format(chosen_letter.lower(), chosen_letter.upper())
    # DEBUG
    # print(letter)

    # saves all the words starting with the random letter selected from the 
    # 'letter' variable into a txt file named "words.txt" as a string
    v_alt = ((re.findall(r'\b[' + letter + ']\w+', j_verbs)))
    vp_alt = ((re.findall(r'\b[' + letter + ']\w+', j_verbp)))
    n_alt = ((re.findall(r'\b[' + letter + ']\w+', j_nouns)))
    pn_alt = ((re.findall(r'\b[' + letter + ']\w+', j_pron)))
    ppn_alt = ((re.findall(r'\b[' + letter + ']\w+', j_propn)))
    adj_alt = ((re.findall(r'\b[' + letter + ']\w+', j_adj)))
    adv_alt = ((re.findall(r'\b[' + letter + ']\w+', j_adv)))
    peep_alt = ((re.findall(r'\b[' + letter + ']\w+', j_peep)))
    prep_alt = ((re.findall(r'\b[' + letter + ']\w+', j_prep)))
    inter_alt = ((re.findall(r'\b[' + letter + ']\w+', j_inter)))
    con_alt = ((re.findall(r'\b[' + letter + ']\w+', j_conj)))

    # if the new list is empty, reassigns back to original list of POS so the grammar still works
    if len(v_alt) == 0:
        v_alt = verbs
    if len(vp_alt) == 0:
        vp_alt = verbs_past
    if len(n_alt) == 0:
        n_alt = nouns
    if len(pn_alt) == 0:
        pn_alt = pronouns
    if len(ppn_alt) == 0:
        ppn_alt = propernouns
    if len(adj_alt) == 0:
        adj_alt = adjectives
    if len(adv_alt) == 0:
        adv_alt = adverbs
    if len(peep_alt) == 0:
        peep_alt = people
    if len(prep_alt) == 0:
        prep_alt = prepositions
    if len(inter_alt) == 0:
        inter_alt = interjections
    if len(con_alt) == 0:
        con_alt = conjunctions
    # DEBUG
    # print(("Using {}").format(letter))
    # print(v_alt)
    # print(vp_alt)
    # print(n_alt)
    # print(pn_alt)
    # print(ppn_alt)
    # print(adj_alt)
    # print(adv_alt)
    # print(peep_alt)
    # print(prep_alt)
    # print(inter_alt)
    # print(con_alt)
    # sys.exit("DONE")

    # create the rhyme words ready for the grammars
    rhyme1 = random.choice(verbs)
    rhyme2 = pronouncing.rhymes(rhyme1)
    # ensure that the rhyming words are not the same 
    # also remove words that make nonsensical rhymes:
    if rhyme1 == "is":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "are":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "guess":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "have":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "know":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "go":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    if rhyme1 == "wait":
    	rhyme1 = pronouncing.rhymes(rhyme1)
    rhyme3 = pronouncing.rhymes("moon")
    rhyme4 = random.choice(adjectives)
    rhyme5 = pronouncing.rhymes(rhyme4)
    rhyme6 = random.choice(interjections)
    rhyme7 = pronouncing.rhymes(rhyme6)
    rhyme8 = random.choice(verbs)
    rhyme9 = pronouncing.rhymes(rhyme8)
    rhyme10 = random.choice(nouns)
    rhyme11 = pronouncing.rhymes(rhyme10)
    rhyme12 = random.choice(propernouns)
    rhyme13 = pronouncing.rhymes(rhyme10)
    rhyme14 = random.choice("little")
    rhyme15 = pronouncing.rhymes(rhyme14)
    rhyme16 = random.choice(adjectives)
    rhyme17 = pronouncing.rhymes(rhyme16)

    # define a set of grammars
    rules = {
        # Multiple possible sentences structures have been created:
        "repitition": ["#pron# #thing# #con# #thing.ed# the #thing.ed# #pron# #thing.ed# to #thing#, #con# #prep# #pron# the #thing.ed# the #peep# #thing.s# #prop# won't #thing# the #thing.ed# #pron# #thing.ed# to #thing#"],
        "repeat": ["#[thing:#verb#]test#"],

        "rhy1": rhyme1,
        "rhy2": rhyme2,
        "rhy3": rhyme3,
        "rhy4": rhyme4,
        "rhy5": rhyme5,
        "rhy6": rhyme6,
        "rhy7": rhyme7,
        "rhy8": rhyme8,
        "rhy9": rhyme9,
        "rhy10": rhyme10,
        "rhy11": rhyme11,
        "rhy12": rhyme12,
        "rhy13": rhyme13,
        "rhy14": rhyme14,
        "rhy15": rhyme15,
        "rhy16": rhyme16,
        "rhy17": rhyme17,
        "rhyme": [
        	"#pron.capitalize# #rhy1#, #pron.capitalize# #rhy2#, #pron.capitalize# #rhy2#",
        	"#peep.capitalize# #vpast# over the moon, maybe because #peep.capitalize# was #rhy3#",
        	"#inter.capitalize#! #rhy4.capitalize# creature was #rhy5#.",
        	"#rhy6.capitalize# #rhy7# #rhy7#!",
        	"If #peep.capitalize# is #rhy8#, and #peep.capitalize# is #rhy9#, then does that mean #peep.capitalize# is #rhy9#?",
        	"Little #rhy10# little #rhy11# little #rhy11# little #rhy11#.",
        	"#rhy12.capitalize# #peep.capitalize# is a #rhy13# #peep.capitalize#.",
        	"#adv.capitalize# #rhy14# #rhy15# #rhy15# #noun# was #rhy16# #rhy17# #rhy17#."
        	],
        "verb": verbs,
        "vpast": verbs_past,
        "noun": nouns,
        "pron": pronouns,
        "prop": propernouns,
        "adj": adjectives,
        "adv": adverbs,
        "peep": people,
        "prep": prepositions,
        "inter": interjections,
        "con": conjunctions,

        "allit": ["#adj2.capitalize# #noun2# #adv2# #vpast2#.",
            "#peep2.capitalize# #vpast2# #prop2# #noun2#.",
            "#peep2.capitalize# and #peep2.capitalize# #verb2# together.",
            "#peep2.capitalize# #peep2.capitalize# #vpast2# #adj2.a# #noun2#.",
            "#peep2.capitalize# #vpast2# #adj2# #noun2#.",
            "#adj2.capitalize# #noun2# #vpast2# #adv2# #inter2#!"],
        "verb2": v_alt,
        "vpast2": vp_alt,
        "noun2": n_alt,
        "pron2": pn_alt,
        "prop2": ppn_alt,
        "adj2": adj_alt,
        "adv2": adv_alt,
        "peep2": peep_alt,
        "prep2": prep_alt,
        "inter2": inter_alt,
        "con2": con_alt,
    }

    # print/save the grammars
    grammar = tracery.Grammar(rules) # create a grammar object from the rules
    grammar.add_modifiers(base_english) # add pre-programmed modifiers
    all_grammars[chosen_letter] = grammar
# DEBUG
# print(script)

# if calls this function from another script, this section runs:
def gimme_a_tongue_twister():
    chosen_letter = random.choice(selected_letters)
    grammar = all_grammars[chosen_letter]
    # DEBUG
    # # print("Running with letter {}".format(chosen_letter))
    # save multiple variations of the allit garmmar to an array ready for turnign into a CAPTCHA image
    text =[]
    with open("fields.tsv", "w") as f:
        for i in range(20):
            eachone = grammar.flatten("#allit#")
            text.append(eachone)
            print("image{}\t".format(i), eachone, file=f)
            chosen_letter = random.choice(selected_letters)
            grammar = all_grammars[chosen_letter]
            # DEBUG
            # print("Running with letter {}".format(chosen_letter))
            try:
                # print(grammar.flatten("#repeat#"))
                # print("--------------")
                print("rhy{}\t".format(i), grammar.flatten("#rhyme#"), file=f)
                # print("--------------")
                print("alit{}\t".format(i), grammar.flatten("#allit#"), file=f) # and flatten, starting with origin rule
                # print("--------------")
            except IndexError:
                print("Oops! Cannot choose from an empty sequence. Skipping...")
            except UnicodeDecodeError:
                print("Oops! Cannot choose from an empty sequence. Skipping...")
        print("Using scrip:{}".format(script))
        print("DONE")
        # print(text)
        return text
        
            
        # print only alliteration grammar CAPTCHA
        # answer = None
        # while answer is None:
        #     try:
        #         # print(grammar.flatten("#rhyme#"))
        #         # print("--------------")
        #         # print("----------")
        #         answer = grammar.flatten("#allit#")
        #     except IndexError:
        #         print("Oops! Cannot choose from an empty sequence. Skipping...")
        #         pass
        # return answer


# if run this script directly, this section runs:
if __name__ == "__main__":
    with open("fields.tsv", "w") as f:
        for i in range(20):
            chosen_letter = random.choice(selected_letters)
            grammar = all_grammars[chosen_letter]
            # DEBUG
            # print("Running with letter {}".format(chosen_letter))
            try:
                # print(grammar.flatten("#repeat#"))
                # print("--------------")
                print("rhy{}\t".format(i), grammar.flatten("#rhyme#"), file=f)
                # print("--------------")
                print("alit{}\t".format(i), grammar.flatten("#allit#"), file=f) # and flatten, starting with origin rule
                # print("--------------")
            except IndexError:
                print("Oops! Cannot choose from an empty sequence. Skipping...")
            except UnicodeDecodeError:
                print("Oops! Cannot choose from an empty sequence. Skipping...")
        print("Using scrip:{}".format(script))
        print("DONE")

    # print the script to ensure tracking of theme
    # print(script)

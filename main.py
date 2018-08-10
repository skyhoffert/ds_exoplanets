# Sky Hoffert, Gabby Boehmer
# main.py
# Processes exoplanet data

import matplotlib
import sys

db_path = 'data/kepler.csv'

def main():
    filein = open(db_path, 'r')
    
    # create an empty db
    db = []
    
    # parse input file
    for line in filein.readlines():
        finalword = ''
        sections = line.split('"')
        
        # parse by splitting " sections
        for i, sect in enumerate(sections):
            # if current section was in a "
            if i%2 == 1:
                newword = ''
                # change , to ;
                for i, c in enumerate(sect):
                    if sect[i] == ',':
                        newword += ';'
                    else:
                        newword += c
                finalword += newword
            else:
                finalword += sect
                
        # only add to db if the columns are correct
        noendline = finalword[:-1]
        tokens = noendline.split(',')
        if len(tokens) == 98:
            db.append(tokens)
            
    # DEBUG
    print(len(db))
    
    
if __name__ == '__main__':
    main()
    sys.exit()
    
    
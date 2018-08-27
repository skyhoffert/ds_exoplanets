# Sky Hoffert, Gabby Boehmer
# main.py
# Processes exoplanet data

import matplotlib
import sys
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



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
	
	
	
    new_db = np.array(db)
	
	# names of each variable (columns)
    row_r1 = new_db[0, :]
    col = row_r1.tolist()
    
	# delete first row in db (just contains the headers)
    newer_db=np.delete(new_db,0,0)

	# create a dataframe from the columns and data
    df = pd.DataFrame(data=newer_db, columns = col)
	
	# replacing empty spaces with 0's
    df["radius"]=df["radius"].replace({"": 0})
    df["semi_major_axis"]=df["semi_major_axis"].replace({"":0})
	
	# changing the type of data from str to num
    df["radius"] = pd.to_numeric(df["radius"])
    df["semi_major_axis"] = pd.to_numeric(df["semi_major_axis"])
	
    # scatter plot of two columns
    plt.scatter(df["radius"], df["semi_major_axis"])
    plt.show()
	
	
	
if __name__ == '__main__':
    main()
    sys.exit()
    
    
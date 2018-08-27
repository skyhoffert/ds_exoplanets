# Sky Hoffert, Gabby Boehmer
# main.py
# Processes exoplanet data

import matplotlib.pyplot as plt
import sys
import numpy as np

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
    
    # remove the heading line
    header = db[0]
    db = db[1:]
    
    # DEBUG
    db = db[:int(len(db)/1)]
    
    # DEBUG
    print(len(db))
    
    x_idx = 11
    y_idx = 2
    
    x_data = []
    y_data = []
    
    # only add entries without null values
    for i,row in enumerate(db):
        if row[x_idx] != '' and row[y_idx] != '':
            x_data.append(float(row[x_idx]))
            y_data.append(float(row[y_idx]))
            
    x_min = min(x_data)
    x_max = max(x_data)
    y_min = min(y_data)
    y_max = max(y_data)
    x_lim = (x_min*0.2, x_max*5)
    y_lim = (y_min*0.2, y_max*5)
    
    m_earth = 1.0/317.8
    m_earth_data = np.empty(len(x_data))
    m_earth_data.fill(m_earth)
    op_earth = 365
    op_earth_data = np.empty(len(y_data))
    op_earth_data.fill(op_earth)
    
    # plot with matplotlib
    plt.plot(x_data, y_data, 'bo', x_data, m_earth_data, 'r-', op_earth_data, y_data, 'g-')
    plt.xlabel(header[x_idx])
    plt.ylabel(header[y_idx])
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.xscale('log')
    plt.yscale('log')
    plt.text(5*10e+3, m_earth*1.1, 'mass of earth', rotation=0)
    plt.text(op_earth*1.1, 10e-4, 'orbital period of earth', rotation=-90)
    plt.show()
    
    
if __name__ == '__main__':
    main()
    sys.exit()
    
    
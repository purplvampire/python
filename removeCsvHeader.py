#! python3
# removeCsvHeader.py - Removes the header from all CSV files in 
# the current working directory.
import csv, os

os.makedirs('headerRemoved', exist_ok=True)
csvRows = [] 
# Loop through every file in the current working directory and printing.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    elif not csvFilename.startswith('NAICS'):
        continue
    print('Removing header from ' + csvFilename + '...')
    # Read the CSV file in (skipping first row).
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        # skip first row
        if readerObj.line_num == 1:
            continue               
        # Append to list
        csvRows.append(row)
# Create a file for write
csvFileObj = open(os.path.join('headerRemoved','merge.csv'), 'w', newline='')
# Create a Writable CSV Object
csvWriter = csv.writer(csvFileObj)
# Write out the CSV Object to file
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()

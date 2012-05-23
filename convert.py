import csv  
import simplejson as json # just to add a little formatting function
import sys

def createDict(filename):    
    # Open the CSV  and read it
    f = open( filename + '.csv', 'U' )   
    reader = csv.reader( f, delimiter= ',', quotechar='|' ) 
    
    # Parse the CSV and create a dict from it
    keys = []
    values = []
    for row in reader:
        keys.append(row[0])
        values.append(row[1])
    csv_dict = dict(zip(keys, values))
    return csv_dict

def open_original_csv(filename):  
    # Open the original CSV
    f = open( filename + '.csv', 'U' )   
    reader = csv.DictReader( f )
    original_csv = json.dumps( [row for row in reader] )
    return original_csv
#
# Take all previous lookups and write the new original_csv JSON 
#

def main_json(original_csv,subject,comp_domain,core_comp):
    # load up the json from original_csv and all other lookup tables
    original_csv = json.loads(original_csv)
    
    for row in original_csv:
        # grab all the id's from theoriginal_csv json (table)
        subject_id = row['subjArea1']
        compDomain_id = row['Comp01'][:1]#only need the first character
        coreComp_id = row['Comp01']
        course_id = row['CourseID']
        
        # create the competency domain key/value
        if compDomain_id in comp_domain:
            row['competency_domain'] = comp_domain[compDomain_id]
        
        # create the core competency key/value
        if coreComp_id in core_comp:
            row['Comp01'] = coreComp_id + ' ' + core_comp[coreComp_id]
        
        # test for blank subject id's and assign the subject names
        if subject_id in subject:    
            subject_name = subject[subject_id]
            row['subjArea1'] = subject_name
        
        # create the id and label for exhibit
        row['id'] = row['CourseID']
        row['label'] = row['CourseTitle']
        

    
    # Format and save the JSON 
    filename = 'converted'
    items = dict() # need to wrap original_csv in an "items" object to make exhibit happy
    items['items'] = original_csv
    j = json.dumps( items , sort_keys=True, indent= 2 * ' ' ) #make it look pretty
    f = open( filename + '.json', 'w')  
    f.write(j)  
    print "Converted JSON saved!"
    
def main():
    main_json(open_original_csv("csv/cep"),
              createDict("csv/cep-data_subject_areas"),
              createDict("csv/cep-data_compDomain"),
              createDict("csv/cep-data_core_competency")
              )

 
if __name__ == "__main__":
    sys.exit(main())
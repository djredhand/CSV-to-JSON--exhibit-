import sys
import json
import csv

def main():
    filename = 'converted.json' #import the json file
    data = json.load(open(filename, 'rU'))
    c = csv.writer(open('new_csv.csv', 'w+b') )
    c.writerow(['Comp01','Comp01Level','Comp02','Comp02Level','Comp03',
                'Comp03Level','Comp04','Comp04Level','Comp05','Comp05Level',
                'Comp06','Comp06Level','Cost','CourseID','CourseTitle','CourseURL',
                'DateEdited','Description','Duration','Format','SubjArea2','TRAINURL',
                'UserEdited','competency_domain', 'display','email','id','label','original',
                'subjArea1','subjArea3'])
    for i, items in enumerate(data['items']):
        c.writerow([data['items'][i]['Comp01'],
                    data['items'][i]['Comp01Level'],
                    data['items'][i]['Comp02'],
                    data['items'][i]['Comp02Level'],
                    data['items'][i]['Comp03'],
                    data['items'][i]['Comp03Level'],
                    data['items'][i]['Comp04'],
                    data['items'][i]['Comp04Level'],
                    data['items'][i]['Comp05'],
                    data['items'][i]['Comp05Level'],
                    data['items'][i]['Comp06'],
                    data['items'][i]['Comp06Level'],
                    data['items'][i]['Cost'],
                    data['items'][i]['CourseID'],
                    data['items'][i]['CourseTitle'],
                    data['items'][i]['CourseURL'],
                    data['items'][i]['DateEdited'],
                    data['items'][i]['Description'],
                    data['items'][i]['Duration'],
                    data['items'][i]['Format'],
                    data['items'][i]['SubjArea2'],
                    data['items'][i]['TRAINURL'],
                    data['items'][i]['UserEdited'],
                    data['items'][i]['competency_domain'],
                    data['items'][i]['display'],
                    data['items'][i]['email'],
                    data['items'][i]['id'],
                    data['items'][i]['label'],
                    data['items'][i]['original'],
                    data['items'][i]['subjArea1'],
                    data['items'][i]['subjArea3'],
                    
                    ])
    print "Conversion is complete!"
        
if __name__ == '__main__':
    sys.exit(main())
    
    

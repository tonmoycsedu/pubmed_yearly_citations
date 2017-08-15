
# coding: utf-8

# In[2]:

import urllib.request as urllib
import json
import datetime
import csv
import time
import xml.etree.ElementTree as ET

def request_until_succeed(url):
    req = urllib.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception as e:
            print(e)
            time.sleep(5)

            print("Error for URL %s: %s" % (url, datetime.datetime.now()))
            print("Retrying.")

    return response.read()


# In[3]:

def search_pubmed(year,Table,counter,diseases):
    # print(disease)
    base = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    #count = []
    for disease in diseases: 
        #print(year)
        
        fields = "/?db=pubmed&term="+disease+"+AND+"+str(year)+"[pdat]"
        url = base + fields 

        # retrieve data
        data = request_until_succeed(url)
        root = ET.fromstring(data)
        myTable[counter].append(root[0].text)
        #print(root[0].text)
        #count.append(int(root[0].text))

        #print(data)
    return counter


# In[4]:

diseases = ['Acute+Lymphoblastic+Leukemia','Cancer+of+the+bladder','Duodenal+cancer', 'Gastric+cancer', 'Hemangioblastoma','Hepatocellular+carcinoma','Hodgkin+disease','Melanoma','NSCLC','Pituitary+adenoma']


# In[5]:

def write_list_in_file(final, name):
    with open(name, "w", newline="",encoding="utf8") as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(final)


# In[6]:

myTable = []
myTable.append([])
myTable[0].append("Year")
for disease in diseases:       
    myTable[0].append(disease)
print(myTable)
    


# In[7]:

total_cite=[]
counter = 1
for year in range(1900,2018):
    print('processing '+str(year))
    myTable.append([])
    myTable[counter].append(str(year))
    cite_no = search_pubmed(year,myTable,counter,diseases)
    #total_cite.append(cite_no)
    #print(cite_no)
    counter += 1
print(total_cite)


# In[8]:

#print(myTable)


# In[9]:

write_list_in_file(myTable,'pubmed_data.csv')


# In[ ]:




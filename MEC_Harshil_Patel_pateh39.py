##Import the libraries needed
import requests
from bs4 import BeautifulSoup

#Get the URL to the information
URL = 'https://github.com/MEC-2020-Programming/virus-tracking-application-harshil/blob/main/testing.txt'

#Get all the text from the URL
data_page=requests.get(URL).text

#Use Beautiful Soap Library to format the page
format_page = BeautifulSoup(data_page)

#Find all elements in the table: class[...[
table_info = format_page.find("table",{"class":"highlight tab-size js-file-line-container"})

#Get all the tr data in the table
extract_table_info = table_info.find_all('tr')

#
for i in range(len(extract_table_info)):
    data = extract_table_info[i].find_all("td")[1].string
    country_list=data.split(',')

    remove_chars = country_list[0].replace('["','')    
    country_names = remove_chars.replace('"]','')
    
    for j in range(len(country_list)):
        number_format = country_list[j].replace('[','')
        case_info = number_format.replace(']','')
        if case_info == ' ':
            case_info = 'No Data Available'
        if j ==0:            
            print ('{:<15}'.format('Country Name'),'{:>1}'.format('-'),case_info,'\n')
        if j ==1:            
            print ('{:<15}'.format('Total Cases'),'{:>1}'.format('-'),case_info,'\n')
        if j ==2:            
            print ('{:<15}'.format('New Cases'),'{:>1}'.format('-'),case_info,'\n')
        if j ==3:            
            print ('{:<15}'.format('Total Deaths'),'{:>1}'.format('-'),case_info,'\n')
        if j ==4:            
            print ('{:<15}'.format('Total Recovered'),'{:>1}'.format('-'),case_info,'\n')
        if j ==5:            
            print ('{:<15}'.format(' Active Cases'),'{:>1}'.format('-'),case_info,'\n')
    








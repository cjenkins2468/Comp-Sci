import csv
import pandas as pd
dictionary = open('words2.txt') 
common_words = open('common_words.txt')




counts = dict()
for line in dictionary:
    line = line.upper()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1





# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

print(counts.items())
text = ""
for key,value in counts.items():
    replace = False
    if value > 50:
        print(key,value)
        for ele in key:
            if ele in punc:
                key = key.replace(ele, "")
        for ele in key:
            if ele in common_words:
                key = key.replace(ele, "")
        text += str(key)+(",")+str(value)+"\n"
counts_list = list(key)  






f =  open("words_output.csv", "w")   # open the file in the write mode

f.write(text)  # writer

f.close() # after writing closing file

# reading the csv file
cvsDataframe = pd.read_csv('words_output.csv')

# creating an output excel file
wordsExcelFile = pd.ExcelWriter('wordsExcelFile.xlsx')

# converting the csv file to an excel file
cvsDataframe.to_excel(wordsExcelFile, index=False)

# saving the excel file
wordsExcelFile.save()
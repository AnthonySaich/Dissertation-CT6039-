#list of libraries used 
import csv
import mailbox
import html2text
import re, string,unicodedata
import nltk
import contractions
import inflect
from nltk.stem import LancasterStemmer, WordNetLemmatizer
mboxfile = 'phishingemails.mbox'#name of the mbox file
writer =  csv.writer(open('CLeanedMbox.csv','w',encoding='utf-8')#makes a new file called CleanedMOX.box

#this function removes non-asici from the dataset
def remove_not_asici_words(text):
    print ("remove nona asici words")
    new_words = []
    for text in text:
        new_word = unicodedata.normalize('NFKD', text).encode("ascii", "ignore").decode('utf-8', 'ignore')
        new_words.append(new_words)
    return new_words


##gets the subject of the emails 
def showMbox(mboxfile):
    mbox = mailbox.mbox(mboxfile)
    for msg in mbox:
        print(msg['Subject'])#prints the subject line
        showmainbody(msg)
        print('**********************************')

#gets the body of the email   
def showmainbody(msg):
    payload = msg.get_payload()
    if msg.is_multipart():
        div = ''
        for subMsg in payload:
            print(div)
            showmainbody(subMsg)
            div = '------------------------------'
    else:
        
        print (msg.get_content_type())#this removes the html from the exmail
        body = html2text.html2text(payload)
        print(payload)#prints the email
        words = replace_contractions(body)#call function 
        body = re.sub(r'(\s)0x\w+', r'\1', body)
        words = nltk.word_tokenize(body)
        replace_number_with_words(text)
        #normalize
        words = normalised(text)
        print(words)
        writer.writerow([msg['From'], msg['Subject'],words])#writers email to csv file









#this funnction replayes the words from your to your are
def replace_contractions(body):
    return contractions.fix(body)
    print (body)
    


#THis tokenise the data,
def tokenise_process(text):
    print("This is process of spliting senctese into single items to be analysed")
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for text in text:
        lemma = lemmatizer.lemmatize(text, pos='v')
        lemmas.append(lemma)
    return lemmas





def normalised(text):
    words = remove_not_asici_words(text)
    words = tokenise_process(text)

    






showMbox(mboxfile)






    
    

        
    

    
    





if __name__ == '__main__':
    showMbox(’emails-phishing.mbox’)



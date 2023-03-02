from bs4 import BeautifulSoup
import requests
import csv
URL = "https://gaming.stackexchange.com/questions?tab=newest&page="
URLAfter = 'https://gaming.stackexchange.com/'

fullText = ''
profile = []
title=[]
idInner =[]
tagCat = []
title_str = ""
edited_list = []
isEdited = False
CATarr =[]
isClosed = []
answer_score = []
author_name = []
author_id = []
author_rep = []
number_of_comments = []
answer_accepted = []
edited = []
post_comments = []
question_score = []
titleSTR = []
link = []
mainArr = []


amountOfPages = 20
c = 0
for i in range(amountOfPages):        
#Creates string of Url with appended page number
    next_page = URL + str(i+1)       
#Get page with created url from stackoverflow
    page = requests.get(next_page)  
#converts request to html page
    soup = BeautifulSoup(page.content, "html.parser")
    #Locates title of question for each entry in page
    fullText = fullText +  str(soup.prettify())
    #2.1
    PostTitle = []
    TitleHTML = soup.find_all(class_="s-post-summary--content-title")
    
    print('page', i+1, ': loaded')

    for l in TitleHTML:

        title = l.find_all('a')
        link.append(title[0]["href"])
        PostTitle.append(title[0].text)
        if title[0].text[len(title[0].text)- 8:] == '[closed]':
            isClosed.append(True)
        else:
            isClosed.append(False)
    ids = []

    for tag in soup.find_all(class_="s-post-summary js-post-summary") :
        ids.append(tag["id"].split('-')[2])

    
    rep = soup.find_all(class_ = "todo-no-class-here")
    reputationProf = []
    for t in rep:
        reputationProf.append(t.text)
        

    
    #2.3
    time = []
    timeBlock = soup.find_all(class_ = "relativetime")
    for t in timeBlock:
        time.append(t.text)

    #2.4
    votes = []
    answers = []
    views = []
    acceptedFind = soup.find_all(class_="s-post-summary--stats js-post-summary-stats")


    
    acceptedList = []
    count1 = 0
    for l in acceptedFind:
        accepted = l.find(class_="s-post-summary--stats-item has-answers has-accepted-answer")
        if accepted != None:
            acceptedList.append(True)
        else:
            acceptedList.append(False)
        count1+=1
    fun = soup.find_all(class_="s-post-summary--stats-item-number")
    for i in range(0,len(fun),3):
        votes.append(fun[i].text)
        answers.append(fun[i+1].text)
        views.append(fun[i+2].text)

    #2.5
    tagCat = soup.find_all(class_="s-post-summary--meta")
    count = 0
    tagCatInner = []
    for tag in tagCat:
            CatText = tag.find('ul')
            lp = CatText.find_all('a')
            tagCatInner.append(lp)

    for a in tagCatInner:
        inner = []
        for p in a:
            inner.append(p.text)
        CATarr.append(inner)
        
        
    namePoster = []
    userid = []
    for l in range(50):

        fullUrl = URLAfter+ link[c]
        page = requests.get(fullUrl)
        soupPage = BeautifulSoup(page.content, "html.parser")
     
    
        profile_user= soupPage.find('span', class_='d-none', itemprop='name').text.strip()
        namePoster.append(profile_user)
        
        
        poster_id =  soupPage.find('div', class_= 'user-details', itemprop='author')
        poster_link = poster_id.find('a')
        if poster_link is not None:
            poster_user_id = poster_link['href'].split('/')[2]
        
        userid.append(poster_user_id)
    
    
        mainArr.append([PostTitle[l ],
        ids[l ],
        namePoster[l ],
        userid[l ],
        time[l ],votes[l ],views[l ],answers[l ],CATarr[l ],
        isClosed[l ],False])
        



        qScore= soupPage.find('div', class_='js-vote-count').text.strip()
                
                
        question_score.append(qScore)
                    

        try:
            name = soupPage.find('a', {'title' : 'show all edits to this post'})['href']
            isEdited = True
        

        except TypeError:
                isEdited = False
                pass


        edited.append(isEdited)
        
        #how many comments on the question
        
        try:
            question_comments = soupPage.find('span', class_='d-none', itemprop='commentCount').text
            if question_comments<'1':
                question_comments=0
            
        except IndexError:
            question_comments = 0
        
        post_comments.append(question_comments)
        
        try:
            comment_finder = soupPage.find_all('span', class_='d-none', itemprop='commentCount')
            if len(comment_finder) > 1:
                comment_count = comment_finder[1].text.strip()
                if comment_count <'1':
                    comment_count = 0
                
            else:
                comment_count = 0
                
        except IndexError:
            comment_count = 0
        
        
        number_of_comments.append(comment_count)
        
        
        try:
            
            find_score_list = soupPage.find_all('div', class_='js-vote-count')
            if len(find_score_list) > 1:
                find_score = find_score_list[1]
                answer_score_data = find_score['data-value']
            else:
                find_score = 'No answers'
                answer_score_data = 'No answers'
                
        except IndexError:
            find_score = 'No answers'
            answer_score_data = 'No answers'
        
        
        answer_score.append(answer_score_data)
        
        #user name of the question
        answer_user = soupPage.find('div', {'class': 'answer'})
        
        try:
            user_name = answer_user.find_all('span', class_='d-none', itemprop='name')[0].text.strip()
            if(user_name!=' '):
                user_name = answer_user.find_all('span', class_='d-none', itemprop='name')[0].text.strip()
            else:
                user_name = 'Anonymous'
        
        except AttributeError:
            user_name = 'No user name'
            pass
        
        except IndexError:
            user_name = 'community wiki'

        author_name.append(user_name)

        try:
            answer_id = soupPage.find('div', {'class': 'answer'}).find('div', class_= 'user-details', itemprop='author')
            user_id = answer_id.find('a')['href'].split('/')[-2]
            
           
                            
        except (AttributeError, TypeError):
            user_id = "None"
            pass
        
        except IndexError:
            user_name = 'community wiki'
            
        
            
        
        
        author_id.append(user_id)
        
        try:
            reputation = soupPage.find('div', {'class': 'answer'}).find('div', class_= 'user-details', itemprop='author')
            reputation_score = reputation.find('span', {'class':'reputation-score'}).text
            
                
        # catches a possible error if the user has no reputation score (NONE)   
        except (AttributeError, IndexError):
            reputation_score = 'No reputation score'
            pass
        

        
        author_rep.append(reputation_score)
        
        # is the answer accepted?
        
        
        try:
            answer = soupPage.find('div', class_='accepted-answer')    
            answer_accepted_boolean = answer is not None 
            
            
        except AttributeError:
            answer = soupPage.find('div', class_='s-accepted-answer-indicator flex--item fc-green-700 py6 mtn8 d-none')
            answer_accepted_boolean = "No data"
            pass
        
        answer_accepted.append(answer_accepted_boolean)
        
        
        c+=1
        
        print('Question', c, ': loaded')
        
rows = []
profileStr = []
timeAndINFO = ""
index3 =0

fields = ['Title','Post Id','Name of poster','Id of poster','Time','Question score','Question views','Question answers','Tags','Closed','Accepted answer']

# name of csv file 
filename = "ARQADE-questions.csv"
    
# writing to csv file
with open(filename, 'w', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(mainArr)


fields_2 = ['Question_ID', 'Answer_Score', 'Author_Name', 'Author_ID', 'Author_Rep', 'Number_Of_Comments', 'Answer_Accepted']


columns = []

for i in range(c):
    columns.append([mainArr[i][1], 
    answer_score[i],
     author_name[i],
     author_id[i],
     author_rep[i],
     number_of_comments[i], 
     answer_accepted[i]])

filename2 ="ARQADE-answers.csv"

with open(filename2, 'w', newline='') as answers_file:
    answers_writer = csv.writer(answers_file)
    answers_writer.writerow(fields_2)    
    answers_writer.writerows(columns)

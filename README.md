# Data-Science-Mining-Stack-Exchange

In this project, you we collected data from Arqade questions on StackExchange Q&A sites.

1. Downloaded 1,000 most recent (“newest”) questions.

2. For each question on each index page, we used BeautifulSoup to extract the
following:
  2.1 The title (str) and the ID (str) of the question.
  2.2 The name (str), the ID (str), and the reputation score (int) of the
      original poster.
  2.3 The time the question was posted (str).
  2.4 The question score (int), the number of views (int), the number of
      answers (int), and whether an answer was accepted (bool).
  2.5 The question tags (str). A question may have at most five tags.
  2.6 Whether the question is closed (bool).
  
3. For each question on its own page, we used BeautifulSoup to extract the
following:
  3.1 Whether the question has been edited since posting (bool).
  3.2 The number of comments (int).
  3.3 The score of the answer (int); the name (str), the ID (str), and the
      reputation score (int) of the poster; the number of comments (int) for
      each answer, and whether the answer was accepted (bool).
     
4. Using the standard CSV writer, saved the collected data as two CSV files
  4.1 The first file ARQADE-questions.csv contains the questions, one question
      per row. The column names are: Question_Title, Question_ID,
      Author_Name, Author_ID, Author_Rep, Question_Post_Time, Question_Score, Number_Of_Views, Number_Of_Answers,
      Number_Of_Comments, Edited, Answer_Accepted, Tag_1, Tag_2, …, Tag_5
      (use empty strings to represent non-specified tags), Question_Closed.
  4.2 The second file ARQADE-answers.csv contains the answers, one answer per
      row. The column names are: Question_ID, Answer_Score, Author_Name,
      Author_ID, Author_Rep, Number_Of_Comments, Answer_Accepted.

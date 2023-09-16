# Fake_News_Detection
Extracted features from given information and classify the labels (false, misleading, true, unproven) of given fake news dataset with Python.

## Project Type 1
All undergraduate (including post-bachelor’s), and MCS students should work on this project type.
In this project, students should form teams of 2-members per team and notify the TA of your group
members by email no later than October 11th. Students that do not email the TA with their group
will be randomly allocated to other groups.
To evaluate the performance of your team, we will conduct a competition on Kaggle. Please visit
this [Kaggle competition](https://www.kaggle.com/competitions/smm-fall22-project2-type1/overview) and follow the instructions: 
(1) Go to “Team” and change your team name with the number assigned to your team (e.g., Team name will be something like “Team-11”)
(2) Go to “Data” and download the datasets
(3) Train your model using “train.csv” and predict labels using “test.csv” file
(4) Submit the result to the leaderboard following the format of sample submission.csv
(5) You can submit at most 15 times per day to avoid any potential tricks (i.e., random guessing)

### Task: Fake News Detection
Due to the ease of spreading fake news online, large volumes of fake news or misinformation are
produced online for a variety of purposes such as financial and political gain. The extensive spread
of fake news and misinformation can have a serious negative impact on individuals and society: (i)
breaking the authenticity balance of the news ecosystem; (ii) intentionally persuading consumers to
accept biased or false beliefs; and (iii) changing the way people interpret and respond to real news
and information. Therefore, it is important to detect fake news and misinformation on social media.
The goal of this task is to classify the labels of given fake news dataset correctly with given metric
(Accuracy). Using this metric, you are expected to get as high score as possible to minimize the
error of classifier. We formally define the task as follows. Given a claim of misinformation related
to COVID-19, participants are asked to classify the claim into one of the four categories (number
indicates the label):
* FALSE(0): claim that is deceptive or untruthful.
* MISLEADING(1): claim that gives people an incorrect understanding of the situation.
* TRUE(2): claim that is verified to be correct.
* UNPROVEN(3): claim that is not able to be verified.

As the claim is typically short, you might think about extracting other features using information
given by the data. For example, you can use the url provided in the dataset which is used for factchecking
the claim. To do so, you might need to use other tools such as web scraping tools.

Some helpful resources

A tutorial on selenium, a web scrapping tool, can be accessed from this [link](https://towardsdatascience.com/web-scraping-using-selenium-python-8a60f4cf40ab).

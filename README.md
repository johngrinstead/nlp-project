# NLP Project



------------

<h3> <a name="top"></a> Hi there 👋,</h3>

Welcome to the README file for my NLP Githup Repo Project.

In here, you will find expanded information on this project including goals, how we will be working through the pipeline and a data dictionary to help offer more insight to the variables that are being used.

------------
## Image goes here 
​
***
[[Project Description](#project_description)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Statistical Analysis](#stats)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___
​
​

------
## <a name="project_description"></a>Project Description:


The goal of this project is to predict the primary programming language used in a github repository by analyzing the readme files of repos found on the open source Microsoft github page. I will attempt to do so by using NLP exploration and modeling. Ultimately I will use classification machine learning to hopefully make a model that is more accurate than the baseline prediction, which in this case will be the mode, or most occuring language.

<u>Data Source</u>

* The data can be scraped directly from Microsoft's open source github page
    * https://github.com/microsoft
    
* There is also step by step reference on how to acquire the data in the wrangle.ipynb file

* This repository also has a CSV of the data available as well


[[Back to top](#top)]
​

------------
## Goals
​
The goals of the project are to answer the questions and deliver the following:
​
- Use NLP methods to find common words and phrases in readme files that will indicate the language the repository uses
- Deliver a final notebook that shows the model used to predict langauge 

​
***
## <a name="planning"></a>Project Planning: 



A link to the Trello board below can be found at https://trello.com/b/ADSguVCB/nlp-project



[[Back to top](#top)]
​

----------
### Projet Outline:
- Acquisiton of data through scraping Microsoft's github
    - scrape data from github
    - arrange into a dataframe that can be analyzed and used for machine learning
- Prepare and clean data with python - Jupyter Labs Notebook
    - normalize data by makings content lowercase
    - replaceing accented characters and removing special characters
    - tokenizing and lemmatizing each individual word
    - removing all standard English stopwords
- Explore data
    - Check for reoccuring to exclusive trends among programming languages
    - Visualize distribution of phrases
    - Create word clouds to see prominance of words and phrases
- Model data 
    - Run classification models to predict features of data
    - Attempt to beat baseline prediction
- Test Data
    - Choose best model and evaluate its performance on unseen data
- Conclude results
 
----------- 


## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

---
|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
|  repo | object  | Name of the repo that can be found on Microsfot's github    |
| language    | object| Primary programming language used in the repository / Target variable|
| readme_contents  | object | Text content of the repository's readme file|
| is_TypeScript | bool | A boolean value indicating whether or not the value of language feature is 'TypeScript', which is the baseline as it is the most reoccuring value|


-------------------
  <h3><u>Hypothesis and Questions</u></h3>

- How many unique languages are there?

- What are the most common words among Typescript repos vs non Typescript repos

- Are there any words that uniquely identify Typescript vs non Typescript

- Proportion of Typescript vs other for the 20 most common words


<h5> The questions above will be answered using visualizations and tables.</h5>


-------------------
  <h3><u>Takeaways</u></h3>
 
- I was able to make a predictive model that could more accurately predict whether or not a repo's primary was TypeScript using it as a binary feature

- I was ultimately unable to make a model that could also predict language when it is used as a discreet feature with multiple values that perfroms better than baseline.

--------------------
 <h3><u>How To Recreate This Project</u></h3>
 
- Acquire
     - Scrape the data directly from Microsoft's githup page or you may use the microsoft_github.csv file in this repository
     
     - In the acquire.py file in this repository, run the acquire_microsoft function
         - This function is also outlined in the acquire.py file
         
         
- Prepare
    - Once you have your data frame apply the prepare_microsoft function from the prepare.py file onto the 'readme_contents' column to prepare the data for analysis and modeling
        - This function is also outlined in the prepare.py file
    
    
- Explore
    - Explore data as desired
    

- Model/Evaluation
    - is_TypeScript
        - using this feature as the target, run classification models using default parameters
            - Logistic Regression
            - Decision Tree
            - Random Forest
            - K Nearest Neighbors
            
    - Language
        - Using this feature as the target, run classification models using the default parameters
            - Logistic Regression
            - Decision Tree
            - Random Forest
            - K Nearest Neighbors
--------------------



# Know Your Rights (KYR) @ Workplace
Know your rights in the workplace; an app that provides resources and lets women and other gender minorities know their rights when dealing with gender wage gaps, harrassment, and other problems in the workplace.

## Inspiration
Current methods of filing a complaint for workplace issues are cumbersome in that they require navigating to and going through a long line of options that people have to choose from. Not just that, 
*it's also extremely difficult to get the reliable data from the legislation
*the legislative laws vary from province to province making it difficult to exactly pin point what the user needs
*some of the provincial websites crash when loaded thus making the data unreliable


## What it does

The application empowers employees who may have experienced some form of harassment or human rights violation in the workplace. The user fills out a form and summarizes their experience. The application then displays recommendations, the Canadian law being violated, next steps, and resources available. Additionally, the output  displays a similar past user experience and the resolution (if any) experienced along with a similarity score comparing the two experiences.

A link to our powerpoint presentation can be found [here](https://drive.google.com/file/d/1Iu_up2ZKvQwOBHXBqKmZgnvDeGxf2V8D/view?usp=sharing).

## How we built it

First, we scraped the web for relevant workplace discrimination in Canada, and used the results to build a (fictional) archive of past user experiences stored in a CSV file. We then distributed task: 
1. Build a .py script that implements `word2vec` and `cosine_similarity` to return the most similar past user experience given our CSV archive.
2. Utilize Flask,   REST API, and a Sheets API to link .py file to mobile app front-end
3. Build a user-friendly mobile app that inputs a workplace violation and user experience, and outputs result from the REST API using Ionic on React and is being hosted on a subdomain



## Challenges we ran into

* Scraping legal information from Canada government websites
* Setting up the JS environment
* Connecting Ionic on React to the REST Api using ajax calls and AXIOS
* Bypassing the CORS protocol for HTTP 





## Accomplishments that we're proud of
* Return most similar text utilizing Machine Learning Algorithms and Word Embeddings 
* Web scraping government Human Rights Commission webpage using `BeautifulSoup`
* Successfully linking .py file to 
* Finally setting up JS and a subdomain to host the site 



## What we learned
* How to implement ML algorithm `word2vec` to get word embeddings over multiple sentences
* Write production level python script callable REST API from JavaScript
* How to use Sheets API and Flask for the first time!
* How to use Ionic on React 
* How to host on a sub-domain
* How to use Axios API


## What's next for KYR
* Crowdsourcing an archive of discriminatory workplace behavior and actual outcomes 
* Expanding topics from workplace to include:
  * immigration experiences
  * interactions with the police 
  * parking violations

This platform creates a community for people who have been treated unjustly in the workplace, enabling them to access resources, reference specific legislation, and view similar cases and their outcomes to know what to expect.


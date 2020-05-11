# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Molly Rowland, mhrowlan@ucsd.edu
- Myra Haider, myhaider@ucsd.edu
- Enrique Sanchez, ens004@ucsd.edu
- Mariam Qader, maqader@ucsd.edu
- Alexandria Kim, aek005@ucsd.edu

## Abstract


For the project proposal, please write a short abstract addressing the questions below. You should replace the entire contents of this section with one to two paragraphs addressing the following:
For our project we are interested in analyzing Monet’s art. On the wiki art page, many of the different works are classified into different categories (ie. genres, styles, medai). We are interested to see if we can make a classifier to be able to group the different works together, such as by landscapes, flowers, and many more. For this specific classifier, we would like to be able to classify Monet’s paintings into four categories: landscape, cityscape, flower painting, people. We think by limiting the amount of categories we will be able to make a more accurate model based on the size of the training data. According to his biography1, Monet struggled with depression, poverty, and illness throughout his life. It would be interesting to see how these hardships may have affected his art and if this can be assessed analytically.
Our research question is: Can we make a classifier that can correctly identify Monet’s paintings into categories as defined on the wiki art website? We hypothesize that our classifier will have an accuracy score of roughly 60%.
We will be using a variety of different analyses. We plan to use date data, edge detection, face detection, and a variety of other types of analysis to best fit a classifier. Many of the techniques and libraries demonstrated in class will be used to extract these features. All the used libraries are listed in the technical notes section. Results will be in the form charts and images. Charts will be used to assess the quality/power of the classifier built. Images will be used to depict the art of Monet over time. We are going to utilize the various image techniques used in class to generate features for Monet’s artwork and train a model to classify those works of art into their respective category. A classifier for images was not covered in class so this extension should be interesting and a good learning experience. 

1: https://www.biography.com/artist/claude-monet


## Data

**Claude Monet Artworks Data Set**
Claude Monet Artworks Data Set
Source: https://www.wikiart.org/en/claude-monet/all-works
The data set we will be working with is a complete set of artworks created by the famous French painter, Claude Monet. These works are freely available on www.wikiart.org. The data set consists of 1,365 artworks that were created between the years of 1858 and 1926. Much information is available for each of the works including its title, date of creation, style, genre, and a series of tags related to it. Given that these works were painted and needed to become available in a digital format, photos of the works were taken. The resolution of the images varies across each work. The quality and accuracy of the works are maintained by editors.



## Code

(20 points)

We used a variety of different image analyzing techniques to build our classifier. 
In our repo we have a handful of different files. The first step in building our classifier was getting our image set. We scrapped 1365 Monet images from the Wiki art. Our web scraping function collected, the image path to download, the date, style, and genre. The date and style will be features in our classifier, while we will use genre as our target for classification. From the images themselves we collected image height, width, mean hue, mean saturation, mean value, mean energy, edge count, and whether or not a face was detected. 
In the web scraping notebook, we ran all of the functions as defined by the script files. The first step was actually web scraping the images and metadata from wiki art. Each iteration was appended to a list and at the end of the web scraping execution, was turned into a dataframe. Additional columns were added onto the dataframe after the feature extractions were run, resulting in a 1365 row dataframe with 11 columns. 

[Webscraping.ipynb](code/webscraping.ipynb): running web scraping and feature extracting codes
[Facial_rec.py](code/Facial_rec.py): code to determine if there is a face or not
[Features.py](code/features.py): extracts mean hue, mean saturation, mean value, height, width, and mean energy
[Infoscrape.py](code/infoscrape.py): all the code for web scraping that was run in the notebook
[Probablistic_hough_lines.py](code/probablistic_hough_lines.py): counts number of edges as defined by minLineLength =400 and maxLineGap=10

When building the model, we cleaned the dataframe to only include variables that we deemed meaningful and useful for our classification. Therefore, we omitted the name and category columns, as the goal of the classifier is to predict genre by image features. We also removed images from the dataset that didn’t fall into our main categories: landscape, cityscape, flower painting, or people. This left us with 1311 images for our classifier. Next, to clean our data, we grouped images into decades rather than individual years, and one hot encoded the data to make the data more usable for the classifier. We ordinally encoded the genre options as well. We created a logistic regressor, a K-nearest neighbors regressor, a SVM, a Naive Bayes classifier, and a random forest classifier. 

Model.ipynb: cleaning the dataset for model creation and testing


## Results

For our project we chose to analyze Monet’s work and create a genre classifier for his works. 
Our first notebook [Monet_Work_through_the_Decades.ipynb](notebooks/Monet_Work_through_the_Decades.ipynb), explores Monet’s paintings by time. 
Our next notebook explores the classifier side of our analysis.  [Claude_Monet_Genre_Classifier.ipynb](notebooks/Claude_Monet_Genre_Classifier.ipynb) explores a variety of different classifiers for our image set. 


This section will contain links to documentation of your results. This can include figures, sound files, videos, bitmaps, as appropriate to your domain of analysis. Each result should include a brief textual description, and all should be listed below: 

- image files (`.jpg`, `.png` or whatever else is appropriate)
- audio files (`.wav`, `.mp3`)
- written text as `.pdf`

## Discussion

(30 points, three to five paragraphs)

The first paragraph should be a short summary describing your results.

The subsequent paragraphs could address questions including:
- Why is this culturally relevant?
- How does your computational approach differ from the traditional art historical, musicological, manuel/subjective approach to analyzing your cultural subject? 
- How do you think the original artists/musicians would respond to this type of analysis? Would it change/inform their practice in some way?
- How do your results relate to broader social, cultural, economic political, etc., issues? 
- In what future directions could you expand this work?

## Team Roles

Myra: Wrote code to web scrape images.
Enrique: Wrote code to web scrape time, categories, genres, and image features. Created model. 
Molly: Wrote code to run facial and edge analysis. Created dataframe/csv from compiled web scraping code and image processing to be used in classifier. Updated Abstract and wrote code, and technical notes and dependencies sections.    
Mariam: Analyzing work through the decades.


## Technical Notes and Dependencies

For our project, we used libraries that have been previously included in this class. This includes: BeautifulSoup, os, request, pandas, multiple packages from skimage, numpy, scipy, matplotlib, PIL Image, and cv2. These packages allowed us to analyze our images to make our classifier. 


## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts

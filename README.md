# Project Title

DSC160 Data Science and the Arts - Midterm Project Repository - Spring 2020

Project Team Members: 
- Molly Rowland, mhrowlan@ucsd.edu
- Myra Haider, myhaider@ucsd.edu
- Enrique Sanchez, ens004@ucsd.edu
- Mariam Qader, maqader@ucsd.edu
- Alexandria Kim, aek005@ucsd.edu

## Abstract

(10 points) 

For our project we are interested in analyzing Monet’s art. On the wiki art page, many of the different works are classified into different categories (ie. genres, styles, medai). We are interested to see if we can make a classifier to be able to group the different works together, such as by impressionism, landscapes, flowers, and many more. For this specific classifier, we would like to be able to classify Monet’s paintings into three categories: Architecture/man-made structures, people, flowers/nature. We think by limiting the amount of categories we will be able to make a more accurate model based on the size of the training data. According to his biography1, Monet struggled with depression, poverty, and illness throughout his life. It would be interesting to see how these hardships may have affected his art and if this can be assessed analytically.

Our research question is: Can we make a classifier that can correctly identify Monet’s paintings into categories as defined on the wiki art website? We hypothesize that our classifier will have an accuracy score of roughly 60%.

We will be using a variety of different analyses. We plan to use date data, edge detection, face detection, and a variety of other types of analysis to best fit a classifier. Many of the techniques and libraries demonstrated in class will be used to extract these features. Libraries like skimage, scipy, and cv2 may be used – it all depends on the features we find to be important. Of course, other libraries like pandas and numpy. Results will be in the form charts and images. Charts will be used to assess the quality/power of the classifier built. Images will be used to depict the art of Monet over time. We are going to utilize the various image techniques used in class to generate features for Monet’s artwork and train a model to classify those works of art into their respective category. A classifier for images was not covered in class so this extension should be interesting and a good learning experience. 

 
1: https://www.biography.com/artist/claude-monet


## Data

(10 points) 

This section will describe your data and its origins. Each item should contain a name of the data source, a link to the source, and any necessary background information such as:
- What is your cultural data source? 
- When was it made? 
- Who created the works? 
- Is it digital native, or is it some kind of scan, recording, photo, etc., of an analog form? 

**Claude Monet Artworks Data Set**

Source: https://www.wikiart.org/en/claude-monet/all-works

The data set we will be working with is a complete set of artworks created by the famous French painter, Claude Monet. These works are freely available on www.wikiart.org. The data set consists of 1,369 artworks that were created between the years of 1858 and 1926. Much information is available for each of the works including its title, date of creation, style, genre, and a series of tags related to it. Given that these works were painted and needed to become available in a digital format, photos of the works were taken. The resolution of the images varies across each work. The quality and accuracy of the works are maintained by editors. 

## Code

(20 points)

This section will link to the various code for your project (stored within this repository). Your code should be executable on datahub, should we choose to replicate your result. This includes code for: 

- data acquisition/scraping
- cleaning
- analysis
- generating results. 

Link each of your notebooks or .py files within this section, and provide a brief explanation of what the code does. Reading this section we should have a sense of how to run your code.

## Results

(30 points) 

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

Provide an account of individual members and their efforts/contributions to the specific tasks you accomplished.

## Technical Notes and Dependencies

Any implementation details or notes we need to repeat your work. 
- Additional libraries you are using for this project
- Does this code require other pip packages, software, etc?
- Does this code need to run on some other (non-datahub) platform? (CoLab, etc.)

## Reference

References to any papers, techniques, repositories you used:
- Papers
- Repositories
- Blog posts

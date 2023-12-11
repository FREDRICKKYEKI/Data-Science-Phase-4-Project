# Data Science: Phase 4 Project

> **Note:** This project is part of the [Flatiron School](https://flatironschool.com/) Data Science Bootcamp curriculum (offered by [Moringa School](https://moringaschool.com/courses/data-science-course-part-time/?utm_source=google&utm_medium=cpc&utm_campaign=DSPT_2024&utm_id=Mar_18th_2024&https://moringaschool.com/courses/data-science-course-part-time/?utm_source=google&utm_medium=cpc&utm_campaign=DSPT_2024&utm_id=Mar_18th_2024&gclid=CjwKCAiAg9urBhB_EiwAgw88meuVKuCgN0GbBrUrQdZcJasaz7zb7v1ilwIp0KgQOxs2CKKduCxZNxoCQCoQAvD_BwE)).

<a href="https://movies-like-x.onrender.com/">View Demo</a>

# Movie Recommender System

![image](images/movie_poster.jpeg)

---

- **Group 17**
- Student names:
  - [Fredrick Kyeki](https://github.com/FREDRICKKYEKI)
  - [Stacy Kiriiri](https://github.com/kiriiri)
  - [Wilfred Kivinda](https://github.com/willieki)
- Student pace: **part time**
- Scheduled project review date/time: $1st - 10th December, 2023$
- Instructor name: **Stella Waithera**

---


## Table of Contents:

- [Overview](#overview)
- [Business and Data Understanding](#business-and-data-understanding)
- [Modelling](#modelling)
- [Conclusion and Recommendation](#conclusion-and-recommendations)
- [Authors](#authors-people_holding_hands)
- [Acknowledgements](#acknowledgements-link)
- [Technologies Used](#technologies-used-gear)
- [Folder Structure](#folder-structure-open_file_folder)
- [License](#license-page_with_curl)

## Overview

**Objective:**
The goal of this project is to design and implement a movie recommender system that provides personalized recommendations to users based on their preferences and viewing history. The system employs various collaborative and content-based filtering techniques to enhance the accuracy and relevance of movie suggestions.

**Key Components:**

1. **Data Collection:**

   - Utilized a movie dataset containing information about movies, genres, user ratings, and tags.
   - Explored and cleaned the dataset to prepare it for modeling.

2. **Exploratory Data Analysis (EDA):**

   - Analyzed the dataset to understand its structure, features, and distributions.
   - Visualized key patterns, such as user preferences and movie popularity, to gain insights.

3. **Content-Based Filtering:**

   - Implemented a content-based recommender system using movie genres.
   - Explored the use of TF-IDF vectors to represent movie content and calculate similarities.

4. **Neighborhood-Based Collaborative Filtering (KNN):**

   - Implemented a neighborhood-based collaborative filtering model using SciKit Learn's KNN.
   - Explored both user-based and item-based collaborative filtering approaches.
   - Evaluated the model's performance using metrics such as RMSE and MAE.

5. **Model-Based Collaborative Filtering (SVD):**

   - Implemented a model-based collaborative filtering approach using the Surprise library and Singular Value Decomposition (SVD).
   - Evaluated the model's performance and explored hyperparameter tuning.

6. **Hybrid Approach:**
   - Recommended a hybrid model that combines the strengths of content-based and collaborative filtering approaches.
   - Highlighted the potential benefits of leveraging both user-item interactions and content features.

## Business and Data Understanding:

### Objective:

The primary objective of the recommender system project is to enhance user satisfaction and engagement on the MovieLens platform by delivering personalized and relevant movie recommendations. The recommender system aims to provide users with tailored suggestions based on their historical movie ratings and tagging activities, ultimately improving their overall experience.

## Modelling:

For this project, we explored the following models:

1. Unpersonalized model
1. Content-based model
1. Collaborative filtering model
   1. Memory/Neighbourhood based (KNN)
   1. Model based (Matrix factorization)
      1. Singular Value Decomposition

For the final model, we used the Neighbourhood based model (KNN) as it had the lowest RMSE and MAE scores.
We also explored the use of a hybrid model that combines the strengths of content-based and collaborative filtering approaches.

> **Note:** The code for the models can be found in the [notebooks](notebooks) folder.

## Conclusion and Recommendations:

In developing a movie recommender system, we explored various approaches including content-based filtering, neighborhood-based collaborative filtering (KNN), and model-based collaborative filtering (SVD). Each approach had its strengths and limitations.

- **Content-Based Filtering:** Utilizing movie features such as genres, we built a content-based recommender. While it provided recommendations based on similarities in content, it might face challenges in capturing diverse user preferences.

- **Neighborhood-Based Collaborative Filtering (KNN):** The KNN model, implemented using SciKit Learn, proved effective in leveraging user-item interactions to make recommendations. The item-based variant, focusing on cosine similarity, demonstrated good performance in finding similar movies.

- **Model-Based Collaborative Filtering (SVD):** We explored the Surprise library to implement SVD, a matrix factorization technique. While SVD showed reasonable performance with an RMSE of 0.8925, its effectiveness could be influenced by hyperparameter tuning.

**Recommendation:**

- Considering the trade-offs between different approaches, we recommend a hybrid model that combines the strengths of content-based filtering and collaborative filtering. This hybrid approach can leverage the detailed user-item interactions captured by collaborative filtering while incorporating content features for a more personalized and diverse recommendation.

- Additionally, further hyperparameter tuning and model evaluation, especially with a larger dataset, could enhance the performance of collaborative filtering techniques. Regular updates to the recommendation engine based on user feedback and evolving content can also contribute to its effectiveness over time.

- In conclusion, the choice of a recommender system depends on the specific requirements, user preferences, and the nature of the dataset. A well-balanced hybrid model, continually refined and validated, holds the potential to offer robust and accurate movie recommendations.

## Authors :people_holding_hands:

- [Fredrick Kyeki](https://github.com/FREDRICKKYEKI)
- [Stacy Kiriiri](https://github.com/kiriiri)
- [Wilfred Kivinda](https://github.com/willieki)

## Acknowledgements :link:

I wish to acknowledge https://github.com/krishnaik06 for the guidance and support in this project.

## Technologies Used :gear:

- Python 3.8.5
- SciKit Learn
- Surprise
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Flask
- Pickle
- onrender.com (for deployment)
- Saturn Cloud

## Folder Structure :open_file_folder:

```
📦 this-repo
├─ 
├─ LICENSE
├─ Phase 4 Presentation.pdf
├─ README.md
├─ data
│  └─ ml-latest-small
│     ├─ README.txt
│     ├─ links.csv
│     ├─ movies.csv
│     ├─ ratings.csv
│     └─ tags.csv
├─ flask_api
│  ├─ __init__.py
│  ├─ __pycache__
│  ├─ app.
│  ├─ data
│  │  └─ ml-latest-small
│  │     ├─ README.txt
│  │     ├─ links.csv
│  │     ├─ movies.csv
│  │     ├─ ratings.csv
│  │     └─ tags.csv
│  ├─ functions
│  │  ├─ __init__.py
│  │  ├─ __pycache__
│  │  ├─ pickle
│  │  │  ├─ knn_pv
│  │  │  └─ recom_model
│  │  └─ recom_functions.py
│  ├─ requirements.txt
│  ├─ templates
│  │  └─ index.html
│  └─ wsgi.py
├─ images
│  └─ movie_poster.jpeg
├─ requirements.txt
└─ student.ipynb
```

©generated by [Project Tree Generator](https://woochanleee.github.io/project-tree-generator)

## License :page_with_curl:

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

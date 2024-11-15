# First Project - Data Analysis

This project is centered around exploratory data
analysis techniques and presentation of results to a client.

**Once you start working please follow the [workflow](workflow.md) to help you achieve the tasks successfully!**

# The data

- You will use the King County Housing Data: This dataset contains information about home sales in King County (USA).
- You will find the data in the eda schema of our database. You can access it via DBeaver. Please save the csv file in the data folder where it will not be uploaded to github.
- Please explore the dataset in DBeaver and come up with a Join for the 2 tables.
- The description of the column names can be found in the `column_names.md` file.
- The column names may NOT be clear at times:

  _In the real world we will run into similar challenges. We would then go ask our business clients for more information. In this case, let us assume our business client who would give us information, left the company. Meaning we would have to identify and look up what each column names might actually mean. (google is your friend ;) )_

# The Tasks

1. Create a new repo using this [template](hhttps://github.com/neuefische/ds-eda-project-template).

2. Through EDA/statistical analysis above please come up with **AT LEAST 3 insights** regarding the overall data. One should be geographical.

3. In addition also come up with **AT LEAST 3 recommendations** for your client.

_Note, you can take either the perspective of a buyer or a seller. Choose a client from the list at the end of this file._

# The Deliverables

0. **New repository** from [template](https://github.com/neuefische/ds-eda-project-template)
1. A **well documented Jupyter Notebook** (see [here](https://www.kaggle.com/ekami66/detailed-exploratory-data-analysis-with-python) for an example) containing the code you've written for this project and comments explaining it. This work will need to be pushed to your GitHub repository in order to submit your project. Do not push all the analysis... just the analysis that is relevant! You can start with the [starter notebook](EDA.ipynb).
2. An **updated and organized README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository.
3. A **short Keynote/PowerPoint/Google Slides/Jupyter slides presentation** giving a **high-level overview** of your methodology and recommendations for **non-technical clients**. The duration of the presentation should be **10 minutes**, then the discussion will continue for 5 minutes. Also put your slides (delivered as a PDF export) on Github to get a well-rounded project. **Do not present using your jupyter notebook!**
4. _Optional_ - A Python script for processing and cleaning your data, here feel free to write clean code, using functions and docstrings. Even more optional you can also do unit tests. If you do this part, you may also update your EDA notebook to make use of these functions. See (optional)[optional] folder for example.

# The clients

- Please chose a client.

_Note: As these clients are made up (any resemblance to present people is absolutely random), please make assumptions about answers they would give to your questions. (i.e. How do you define a rich neighborhood? take the zipcodes with most houses in upper 10% percentile..). Whatever assumptions you make, please write them explicitly in your presentation and notebook._

| Name                | client | Characteristics                                                                                                                                                                 |
| ------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Thomas Hansen       | Buyer       | 5 kids, no money, wants nice (social) neighborhood, Timing?, Location?                                                                                                          |
| Charles Christensen | Seller      | Invest with big returns, wondering about renovation?, which Neighborhood? Timing?                                                                                               |
| Bonnie Brown        | Seller      | Has house and wants to move soon (timing?), but wants high profit in middle class NH (neighborhood)                                                                             |
| Larry Sanders       | Buyer       | Waterfront , limited budget, nice & isolated but central neighborhood without kids (but got some of his own, just doesn't want his kids to play with other kids .. because of germs) |
| Nicole Johnson      | Buyer       | Lively, central neighborhood, middle price range, right timing (within a year)                                                                                                  |
| Jennifer Montgomery | Buyer       | High budget, wants to show off, timing within a month, waterfront, renovated, high grades, resell within 1 year                                                                                  |
| Bonnie Williams     | Seller      | Has several houses, some in bad neighborhoods, willing to evict people, timing?, big returns, open for renovations                                                              |
| William Rodriguez   | Buyer       | 2 people, country (best timing & non-renovated) & city house (fast & central location), wants two houses                                                                        |
| Erin Robinson       | Buyer       | Invest in poor neighborhood, buying & selling, costs back + little profit, socially responsible                                                                                 |
| Jacob Phillips      | Buyer       | Unlimited Budget, 4+ bathrooms or smaller house nearby, big lot (tennis court & pool), golf, historic, no waterfront                                                            |
| Zachary Brooks      | Seller      | Invests in historical houses, best neighborhoods, high profits, best timing within a year, should renovate?                                                                     |
| Timothy Stevens     | Seller      | Owns expensive houses in the center, needs to get rid, best timing within a year, open for renovation when profits rise                                                         |
| Amy Williams        | Seller      | Italian mafiosi, sells several central houses(top10%) over time, needs average outskirt houses over time to hide from the FBI                                                   |

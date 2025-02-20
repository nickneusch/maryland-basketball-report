# maryland-basketball-report

I developed an interactive dashboard to optimize sports card submissions to PSA by using analytics to assess grading potential and maximize value while minimizing costs. Analytics were focused on the "Gem Rate" (percentage of cards that graded as a "gem") because these are the most profitable cards.

Currently only configured for my friend, but may restructure for other users in the future.

<img src="https://github.com/user-attachments/assets/bae9965d-ddf1-421a-8230-8cf000d5bd24" alt="PSA Grading Analytics Dashboard" width="1000">

## Motivation

My friend, Taylor, owns a sports cards business. Within his business, he submits cards for grading to PSA (Professional Sports Authenticator). Each card is graded on a scale from 1-10, depending on the quality of four main categories: centering, corners, edges, and surface condition. A higher numerical grade indicates a more prestine card. Thus, cards that receive higher grades are worth exponentially more than their raw (ungraded) value, however, cards that receive a low grade can decrease the value of the card. Additionally, there is a ~$20 fee to grade each card. Therefore, it is important to be selective when deciding which cards to submit. I created this dashboard to help Taylor use analytics to help guide his decision-making.

## Workflow
1. Download the data for each submission from PSA. A submission is a group of cards submitted in the same order.
2. Clean the data with a python script. Taylor allows other people to submit their cards in his orders. Therefore, the data was only used from his cards.
3. Process the data with a python script. The data downloaded from PSA lists the card description, but does not distinguish its qualities seperately (ex. 2020 PANINI SELECT 61 JUSTIN JEFFERSON DIE-CUT PURPLE PRIZM). The description was parsed to extract the year, brand, card number, variation/parallel, and player name.
4. Import the data into Tableau to create an interactive dashboard. Analytics were focused on the "gem rate" (percentage of cards that graded as a "gem") because these are the most profitable cards. Data was analyzed by gem rate vs. order number, brands, parallels, sports, and players. Filters were added to introduce new perspectives of the data. Filters include order number, brand, year, parallel, and player name.

##

### View Report

View the full PDF attached here:
[Data Analysis Report on Maryland Basketball.pdf](https://github.com/user-attachments/files/18887262/Data.Analysis.Report.on.Maryland.Basketball.pdf)


##

Created in October 2024


-------

Date: September 2024

Description: This report is looking for trends in Head Coach Willard’s teams that have had success, in addition to, correlation between shooting splits/shares and making the sweet sixteen over the past 4 seasons. Data cleaning and transformation were done in Excel, while exploratory data analysis and correlation assessments were executed using Python. Distribution analysis, hypothesis testing, regression modeling, and data visualization were performed in Tableau to effectively present the findings. Graph annotations were added in Adobe Photoshop.

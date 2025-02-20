# maryland-basketball-report

I developed a written report to analyzing the University of Maryland Basketball Team under the direction of head coach Kevin Willard. The purpose of the report was to seek trends in Willard's successful teams, as well as, find correlation between shooting splits/shares and reaching the Sweet 16 of the NCAA Tournament.

<img src="https://github.com/user-attachments/assets/bae9965d-ddf1-421a-8230-8cf000d5bd24" alt="PSA Grading Analytics Dashboard" width="1000">

<img width="713" alt="Screenshot 2025-02-20 at 2 48 58 PM" src="https://github.com/user-attachments/assets/1927df23-9051-4b2c-b713-ef066f02f34f" />


## Motivation

I have always loved College Basketball since I was a little kid growing up. This seemed like the perfect opportunity to improve my skills of exploratory data analysis and technical writing with something that I am very interested in. I really wanted to work with the University of Maryland basketball team, so I created this project trying to get my foot in the door after getting in contact with one of the assistant coaches. He had told me to create a project seeing "what Willard's teams has had success with in the past" and "what can help get us back to the Sweet 16". This was the result.

The report is looking for trends in head coach Willard’s teams that have had success, in addition to, correlation between shooting splits/shares and making the Sweet 16 over the past 4 seasons.

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

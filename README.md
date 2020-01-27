# DataProcessFormatAssignment
JSON data processing and formatting assignment


## Problem

The example JSON data below shows iPhone models and their details.  Write a program to process and format this data using a data structure with properties: "name", "color", "price", "storage", "rating", and "url".  Once you’ve processed the data sort it based on the “price" property in ascending order and return the final output. For sorting the raw data, please implement your own sorting code and do not use something “out of the box”.

Example Input JSON Data:


[
[“iPhone X”, “White”, “$799”, “256GB”, “3.5 stars”, “https://www.amazon.com/iPhone_X_White”],
[“iPhone 11”, “Rose Gold”, “$1099”, “256GB”, “4 stars”, “https://www.amazon.com/iPhone_11_Rose_Gold”],
[“iPhone 11”, “Black”, “$1099”, “256GB”, “4 stars”, “https://www.amazon.com/iPhone_X_Black”],
[“iPhone 11”, “White”, “$999”, “128GB”, “3.75 stars”, “https://www.amazon.com/iPhone_X_White”],
[“iPhone 11”, “Black”, “$999”, “128GB”, “3.75 stars”, “https://www.amazon.com/iPhone_X_Black”],
[“iPhone X”, “Black”, “$799”, “256GB”, “3.5 stars”, “https://www.amazon.com/iPhone_X_Black”]
]

Output JSON Data: Output should include the new data structure and be sorted in ascending order of price.


## Solution

My python environment: Anaconda Python 3.
Download the repo, in the terminal, change directory into this folder. The sample input and output is already in the folder.

### How to run

python3 instawork_p1.py

### Output

Name: iPhone X, Color: Black, Price: $799, Storage: 256GB, Rating: 3.5 stars, Url: https://www.amazon.com/iPhone_X_Blac

Name: iPhone X, Color: White, Price: $799, Storage: 256GB, Rating: 3.5 stars, Url: https://www.amazon.com/iPhone_X_White

Name: iPhone 11, Color: Black, Price: $999, Storage: 128GB, Rating: 3.75 stars, Url: https://www.amazon.com/iPhone_X_Black

Name: iPhone 11, Color: White, Price: $999, Storage: 128GB, Rating: 3.75 stars, Url: https://www.amazon.com/iPhone_X_White

Name: iPhone 11, Color: Black, Price: $1099, Storage: 256GB, Rating: 4 stars, Url: https://www.amazon.com/iPhone_X_Black

Name: iPhone 11, Color: Rose Gold, Price: $1099, Storage: 256GB, Rating: 4 stars, Url: https://www.amazon.com/iPhone_11_Rose_Gold

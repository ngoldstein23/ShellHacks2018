# GreenGrocer - Shell Hacks 2018

## We are on a mission to remove emissions

### Tech stack: Python, Azure, REST

### What it does
GreenGrocer helps users reduce their negative environmental impacts by analyzing their receipts and making them aware of the ecological impact of their groceries.

### How we built it
The GreenGrocer tool is accessible using REST endpoints. The URL containing the image of a receipt can be sent via POST request. After, GreenGrocer utilizes Azure's Computer Vision service to perform image to text analysis of receipts. This text is then matched to a database to look for high impact keywords. A dictionary of these high impact items is returned. 


### To run the code

```bash
FLASK_APP=flask_app.py flask run
```
Next, send a POST request containing the url of the receipt image to <url>/recieve_receipt to initiate the analysis of the receipt. 


### What's next for GreenGrocer
* Expand database of suggestions and facts to include more products
* Integrate location services to find best produce based on area
* Create rewards system to support eco friendly purchases


#### Contributers:
* Natalie Goldstein
* Anthony Brugal
* Jake Mellinger 

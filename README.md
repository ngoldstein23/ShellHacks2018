# Shell Hacks 2018

## We are on a mission to remove emissions

### Tech stack: Python, Azure, REST

### What it does
GreenGrocer helps users reduce their negative environmental impacts by analyzing their receipts and making them aware of the ecological impact of their groceries.

### How we built it
The GreenGrocer tool is accessible using REST endpoints. The URL containing the image of a receipt can be sent via POST request. After, GreenGrocer utilizes Azure's Computer Vision service to perform image to text analysis of receipts. This text is then matched to a database to look for high impact keywords. A dictionary of these high impact items is returned. 


### What's next for GreenGrocer
* Expand database of suggestions and facts to include more products
* Integrate location services to find best produce based on area
* Create rewards system to support eco friendly purchases


#### Contributers:
* Natalie Goldstein
* Anthony Brugal
* Jake Mellinger 

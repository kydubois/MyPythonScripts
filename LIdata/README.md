geoLIloader.py and geoLIdumper.py

These programs are used to geocode latitude and longitudes to a list of zip codes or addresses.  It created a SQL database of JSON data from the Goolge Geocoding API using DB Browser for SQLite.  

First open the geoLIloader.py and update the API_KEY to your specific Google Geocoding API.  Also, update the your file name in 'fh = open()' to the correct file of addresses or zip codes that you wish to geocode.
Finally, update the name of your SQL database to your desired title. 

Now, your geoLIloader.py which should iterate the the API 500 requests at a time.  After the 500 requests you may have to restart the program depending on the size of your geocoding list.

Once geoLIloader.py is complete a new SQLite database will be write.  Run geoLIdumper.py to write the JSON data into a CSV file.  Make you edit the SQLite address to your specific database to make sure you are accessing the correct databse.

You now have a CSV file which should contain three columns.  The formatted address, latitude, and Longitude.  




vetsearch.py

This program is used to lookup Veterinary Hospitals by zip code.  

Before you run this program make sure to update the api_key to your Google Places Web Services API.

Simple run the program and enter in the zip code of the area you would like to find the Veterinary Hospitals.  The program will return a list of those hospitals and their addresses along with a total count that were located.

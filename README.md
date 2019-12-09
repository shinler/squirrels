# Squirrel Sightings Web App

This file is written to describe the tools and features of this web application.

## Features
This Django-based web app keeps track of all recorded sightings found in Central Park in 2018. All data was retrieved from the [2018 US Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw). This dataset contains 3023 squirrel sightings, of which 3018 are unique. Users of the app can add, edit or delete a squirrel sighting. Additionally, general statistics of the sightings, and a map that visualizes the geographical locations of the sightings can be found. 

## Installation
Clone this repository into your project with the following:
```bash
git@github.com:shinler/squirrels.git
```
## Management Commands
These commands allow you to import and export the dataset: 

> **Import**: Import the data from the 2018 census file in CSV format. The file path should be specified at the command line after the name of the management command.

```bash
$ python manage.py import_squirrel_data /path/to/file.csv
```

> **Export**: Export the data in CSV format. The file path should be specified at the command line after the name of the management command. 

```bash
$ python manage.py export_squirrel_data /path/to/file.csv
```

## API
Different views location leads you to different APIs 

> **Sightings**:
* **Function**: Sightings lists all squirrel sightings with links to edit and update a particular sighting
* **Location**: /sightings

> **Add**:
* **Function**: Add a new sighting to the database. Required fields include: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent and Runs From.
* **Location**: /sightings/add
 
> **Update**: 
* **Function**: Update a sighting by adding the unique squirrel ID after sightings/
* **Location**: /sightings/<unique-squirrel-id>
 
> **Delete**: 
* **Function**: Delete a sighting by adding unique squirrel ID after sightings/
* **Location**: /sightings/<unique-squirrel-id>
 
> **Stats**:
* **Function**: Some Statistics on sightings  
* **Located at**: /sightings/stats
>
> **Map**:
* **Function**: Map displays the locations of squirrel sightings
* **Location**: /map
 
## Dependencies
- Django   (2.2.7)
- pytz     (2019.3)
- sqlparse (0.3.0)

## Additional Notes
* Plotting more than 100 at once may cause the map to freeze

## App Server link
```bash
https://handy-muse-255501.appspot.com/sightings
```
## Team Members
<li> Douglas Chan & Shin Ler Low
<li>UNIs: [sc4619, sl4619]
<li>Team 49 Section 2

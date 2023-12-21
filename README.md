# MediaTracker

Media Tracker is a simple application built with Pyhton and Flask that allows the user to keep track of the movies they have watched. Users can add movies or TV shows, with details including title, release year, genre, language, and rating.

## Table of Contents
- [Motivation](#motivation)
- [Features](#features)
- [Technologies](#technologies)
- [Database Design](#database-design)

## Motivation
There are many applications available to track movies and TV shows, yet not many provide an interconnection between mainstream American TV shows or movies and foreign works like Chinese wuxia dramas or Japanese Anime. The purpose of Media Tracker is to combine every work, foreign and domestic into one spot.

## Features
- Add movies with details such as title, release year, genre, language, and rating.
- View list of added movies
- Simple user interface for minimal navigation

## Technologies
- **Backend:** Python, Flask, SQL
- **Frontend:** Quarto, HTML, CSS, JavaScript

## Database Design

* media
    * id (PRIMARY KEY: max 4 digits)
    * title (String: max 256 characters)
    * releaseYear (int: only 4 digits)
    * languageID (int: max 2 digits)
    * genreID (int: max 2 digits)
    * rating (double: between 0 and 10)
    * episodes (int: max 5 digits)
    * completedEps (int: max 5 digits, less than episodes)

* genre
    * id (PRIMARY KEY: max 2 digits)
    * name (String: max 32 characters)

* language
    * id (PRIMARY KEY: max 2 digits)
    * name (String: max 32 characters)
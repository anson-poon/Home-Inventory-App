# Microservice for Random Card Generator

OSU Software Engineering I

This project is a microservice for a random card generator, it handles requests from a client program via a text file pipeline, then responds by randomly picking a card from a database and storing the results into two separate files, namely a result.txt file and a inventory.csv file. This lets the client program to access and display the generated card through these files. 

This README provides an overview of the technologies used, the procedure to how the client program can request and receive data from the microservice, and a UML sequence diagram to outline this process.

## Table of contents
* [Technologies](#technologies)
* [Requesting Data](#requesting-data)
* [Receiving Data](#receiving-data)
* [UML Sequence Diagram](#uml-sequence-diagram)
	
## Technologies
Project is created with:
* Python
* Pandas library

## Requesting data
1. The client program send a request to the microservice by send the keyword "run" to pipeline.txt
2. pipeline.txt forward this request to the microservice
3. The microservice read and pick a random card from database.csv
4. The microservice write the card in result.txt
5. The microservice append the card to inventory.csv
6. The microservice empty pipeline.txt for the next request

## Receiving data
1. The client program read result.txt to receive the single generated card
2. The client program read inventory.csv to receive an inventory of generated cards

## UML Sequence Diagram
![UML Sequence Diagram](/../main/documentation/Partner%20Program%20UML%20Sequence%20Diagram.png?raw=true)

# FarewellSI126
Automated bot for sending celebration letters to SI126 friends

## Congrats!

To celebrate my GSX-TU75 classmates (and my friends) at Siriraj Hospital (SI) -- more than a half of the class still study at the same faculty LoL, actually, in the parallel world, I would be graduated at SI -- who will become doctors to serve this country, I decided to code the automated script to congratulate them in the lonely holidays in Thailand. Thanks to the SI students union website that allow anyone to write their remembrances anonymously, based on Google Form service, it's possible to code this easy script to write for a lot amount of text with almost error-free to all of my friends.

(Updated 2021-04-17) My bot also works for my MDCU71 friends.

## What do I do in this project - in a nutshell and in a human language

I must find the URL - something that really long and unique on your address bar in Google Chrome - for each classmate in the students union website then find the Google Docs URL behind his/her URL for each student to fill in my letter. This code is very simple just choosing only my classmates, writing a template letter, submitting the button! That's it!

## Technical Details
### Site
[This site](https://sites.google.com/view/seniorfarewell2021/mirror) is a collection site of each SI student. In each page, there are 2 Google Docs embedded objects (Text Form and File Uploading System form). Using the inspection tools in your browser, it's possible to find a Google Docs links to fill in my letter. In this project, I use only the text form object for this automation.

### Code
This script was written in `Python 3.8.8` with some important libraries : `Beautifulsoup` for finding element in HTML code, `Selenium` for doing automated stuffs in a browser with `Chromedriver`, `urllib` for dealing with network stuffs, `pandas` for dealing with some data in python.

## Licence
Copyright (C) 2021, Sikkawit Amornnorachai Licensed under the MIT Licence (See the `License` file)

## Nice to know
This script is written with 5 hours of coding, debugging and learning from Youtube and stackoverflow and 1+ hours to write this Markdown file, 1 jar of orange juice, 1 bottle of water, and 1 pack of potato chip.

Thanks @pudit for improving codes

Made on a mac and VS Code.

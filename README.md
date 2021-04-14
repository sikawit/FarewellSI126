# FarewellSI126
Automated bot for sending celebration cards to SI126 friends

## Congrats Bros!

To celebrate my GSX-TU75 classmates at Siriraj Hospital (SI) -- more than a half of the class still study at the same faculty LoL, actually, in the parallel world, I would be graduated at SI -- who will become doctors to serve this country, I decided to code the automated script to congratulate them in the lonely holidays in Thailand. Thanks to the SI students union website that allow anyone to write their rememberances anonymously, based on Google Form service, it's possible to code this easy script to write for a lot amount of text with almost error-free to all of my classmates.

## Technical Details
### Site
[This site](https://sites.google.com/view/seniorfarewell2021/home) is a collection site of each SI student. In each page, there are 2 Google Docs embedded objects (Text Form and File Uploading System form). Using the inspection tools in your browser, it's possible to find a Google Docs links to fill in my letter. In this project, I use only the text form object for this automation.

The url was designated for each student with this pattern `main URL / folder / studentID`. My main job is to find the pattern for the `folder` name, which is the group of each 50 members in the site to find the site for each `studentID` site. Moreover, the ID in the site is not in consecutive order, I must check that each ID number has a site in the main site of not. Then,

### Code
This script was written in `Python 3.8.5` with some importance libraries : `Beautifulsoup` for finding element in HTML code, `Selenium` for doing automated stuffs in a browser, `urllib` for dealing with network requests, `pandas` for dealing with some data in python.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licence
Copyright (C) 2021, Sikkawit Amornnorachai Licensed under the MIT Licence (See the `Licence` file)

### Nice to know
This script was written with 5 hours of coding, debugging and learning from Youtube and stackoverflow. 1 jar of orange juice, 1 bottle of water, 1 pack of potato chip

Made on a mac and VS Code.

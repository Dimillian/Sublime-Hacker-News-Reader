#Sublime Hacker News Reader

##What ?? 

Because an image is better than any text, here it is: 

![image](https://raw.github.com/Dimillian/Sublime-Hacker-News-Reader/master/screen.png)

This is my first public Python project, well this is my first Python project ever, I'm open to any constructive criticism. I think the code is currently bad, but I've mad it for myself first, and its works, so I'm fine. 
I'll make it better with more features. Maybe soon, maybe later.

This plugin is not in Package Control yet, I'll submit it soon, this version or a later one.

##Features
* Clean and fast
* Load the Hacker News Front Page in a Sublime Text menu
* Select and item to read comments or the article
* Quick view on the user profile


##Coming soon
* Login
* Post comments
* more...

Submit any features request or bugs as issues, I'll be more than happy to work on them. 
This repo is also open to Pull Requests. 

##Install
**From here**: Download and copy this folder to your packages directory

**Package Control**: Coming soon, I'll submit this package soon to Package Control so you'll be able to install it right within Sublime Text 2

##Using
Open the Command Palette and search for 'Hacker News Feed', you can also access this command from the tool menu in the first section. 
Feel free to bind it to any shortcut. 

##What's new

###V1.5 (3/26/2013)

* ==Merge from Thibaultchat ==
* Error message if your internet connection is down
* Keymap to CMD+OPTIONS+N for OSX, keymap for linux and Windows too
* Internal refactor

###V1.4 (2/2/2013)

* You can get more info on the submiter

###V1.3 (2/2/2013)

* Display vote and comments count.
* Correctly close menu and do no action when esc key is pressed.

###V1.2 (2/2/2013)

* Rewrite using hn python API

###V1.1 (2/2/2013)

* On item selection allow to open the article or the Hacker News comments

###V1.0 (2/2/2013)

* First public version, this basic version only load and display the front page feed. Select ant item to open the link. 

##Libs

This plugin use and include [hnapi](https://github.com/scottjacksonx/hn-api)

##Licensing

Copyright (C) 2012 by Thomas Ricouard.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
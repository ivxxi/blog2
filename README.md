# Blog
A web application that allow users to read blogs and for writers to post, edit and delete blogs:

## By crystal alice

## Description
Blog is a web application that users can view other blog posts, comment on the blogs and sign in as writers. Writers are able to post new blog post, edit existing posts, delete posts and comments. Random quote is also displayed on every blog

## Specifications
* Users can view most recent blog posts
* Users can comment on blog posts
* Users can register and login to become writers
* Writers can create new blog posts
* Writers can update and delete blog posts
* Writers can delete comments

## Prerequisites
* Python 3.6 required

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `pip3 install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
## Live Link`

https://ivxxi-blog.herokuapp.com/

### Behaviour Driven Development
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Index Page loads as default | Home link | Loads the home page. |
| View Blogs| Click on view blogs | All posts are displayed starting with the most recent|
| Read Blog | Click on Read More| All the details of that specific blog is displayed|
| Delete Blog | Click on Delete | Post is deleted|
| Write Blogs| Click on Write Blogs| A form for a new blog is displayed|
| Add Comment| Full Blog Page| A comment form is displayed and older comments from other users|
| Update Blog | Click on Update | Form with the inital blog post that allows writer to edit|




## Known Bugs
None known at the moment.

## Technologies Used
* Python
* HTML
* BOOTSTRAP
* Flask

## Support and contact details
In case of clarification email me at crystalalice21@gmail.com

### License
MIT License
* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)

Copyright (c) 2020 crystal alice

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.


# Sole Mates

Sole Mates is an e-commerce website that sells shoes. It also contains a blog section where visitors can view various blog articles and comment on them should they so wish.

## Overview of features:

* A large catalogue of shoes, categorised by gender and shoe style.
* The ability to add shoes to a cart, update the cart, and checkout.
* A blog section where users can read articles about shoes and leave comments.
* The ability to create an account(sign-up) and to login/logout of profile.
* Information area for delivery and returns and contact information.
* This website was built in Python3 using the Django framework.
* A live version is hosted [here](https://katiemodonnell88-closet-k.herokuapp.com/).

# UX

The aim of this site, aside from selling shoes, is to provide the user with a variety of attractive images of shoes for sale; interesting blog content and pleasing blog images so that the user has a satisfying browsing session.

* The user immediately sees an impactful video on the homepage with an overlay of text when they arrive on the home page. The idea of this feature is to make the website stand out and be memorable to the user.

* There is a simple layout throughout the site with a grey and white colour scheme, keeping the website clean, modern and minimalist in design. The use of attractive imagery throughout the site improves the user experience and makes their time spent on the site enjoyable. The layout of the site enables the user to navigate throughout the site easily and with minimum confusion which also makes their experience more enjoyable and memorable.

* Users who are on the site to browse or purchase shoes can do so from either selecting men or women on the navigation bar or by scrolling down the home page to where all existing shoe categories are listed and linked to their respective pages. It is very easy for users to find the category of shoes that they are looking for which in turn makes a satisfied user.

* Users who are on the site to view the blog, can also find a link to the blog on the navigation bar or on the home page where they can choose from a variety of articles which again, makes it very easy for them to get to where they want to get to without being overloaded with information that they are not interested in.

* Users need to be logged in to purchase products and the user login functionality is easy to see on the navigation bar. If a user tries to purchase a product without being logged in, they will be immediately directed to the login screen, making the whole process very simple.  In addition, users need to be logged in to post comments on a blog - if they try to comment while not logged in, they will be directed to the login page.

# Wireframing

Wireframes were drawn manually and can be found in the wireframes folder.

# Features

(In addition to those features mentioned at the beginning of this document):

* Sign-up and login capability 
* logout capability
* linkable sections on the site from the navigation bar
* linkable sections on the home page to other parts of the site
* keyframe bouncing arrows on the home page

## Cart App - used for adding products to a cart session and updating the cart.

* Users can add items to a cart.
* Users can view the cart and see images of the items in the cart as well as other information such as the product price, size, quantity, description, and cart total.
* Users can remove items from a cart.
* The image for the cart in the navbar will display the amount of items currently in the cart.

## Checkout App - used for making purchases with stripe.

* Users can enter address and card information for making purchases.
* While making a payment, the order details are also available on the screen with a remove button so that users can see their cart and remove items if they want to before making payment.
* A confirmation message will display to the users once they have placed an order.
* Payment is processed using Stripe.

## Blog App 

* Users can read blog articles related to shoes and comment on the articles if they like.

## Product app

* Users can search for products using the search bar.
* Users can navigate through the products by selecting the category they are looking for.
* Shoes are presented in a simple layout, initially displaying a simple image, title, cost and option to “shop now”. Once clicked into, further information such as a description and options to choose a size, quantity and add to cart are presented.

## Features left to implement

* Add more images of the product to the product detail page so that the user can see the product from various angles.
* Option to delete and edit blog comments.
* Option to like blog articles.
* Display the number of views on a blog article. 
* Send users email confirmation after they have placed an order.
* Information area for “premier delivery”, and “student discount” that will be linked from the existing footer titles.

# Technologies Used

* HTML
* CSS
* Bootstrap - front-end framework used due to its user experience focus and ease of use (https://getbootstrap.com/).
* Bootswatch
* Font Awesome used to displays the arrows on the home page (https://fontawesome.com/).
* JQuery -  used to simplify DOM manipulation.
* JavaScript used to allow dynamic content to get executed in the site, for example the dropdowns in the navigation bar  (https://www.javascript.com/).
* javascript:history.go(-1) – used (on product_detail page) to enable user to “go back to previous page” rather than having to use their browsers back button.
* HttpResponseRedirect is used so that when a user adds an item to the cart, they remain on the same page once the item has been added.
* Python3 – the programming language used (https://www.python.org/).
* Popper.js - a JavaScript library for enabling dropdown.
* Google Fonts for downloading different font styles (https://fonts.google.com/).
* Django2 Framework
* SQLite Database
* Amazon Web Services (AWS) used to store images for live site.
* Hover.css - library for creating effects on hovering over an image.
* Stripe - used for processing payments.

# Testing

![Build Status](https://travis-ci.org/katiemodonnell/closet_k.svg?branch=master)

Automated testing was done using Travis - CI. 25 tests were written with an overall coverage score of 83%.


To run the tests when you have the project running locally, complete the following two steps:

1. Comment out these two lines in the .bashrc and then close the terminal and open a new one: 
“export DATABASE_URL="postgres://metcomqxuspdof:1fb871563687d7491bb8dda397cf54f1cceb1f5302b6c537002048cac42b4bfb@ec2-54-75-231-156.eu-west-1.compute.amazonaws.com:5432/dd8o67sl1uufu7" 

2. next enter the following in the terminal:
* “sudo pip3 install coverage”
* "coverage run --source=products,accounts,blog,checkout,cart manage.py test"
* "coverage report"

3.	Once this is done, don’t forget to un-comment out those two lines again in the .bashrc and again close the terminal and open a new one.

## Manual testing was also done:

The site was tested on 21" monitors, 15" and 13" laptop screens and on the following phone screens: iPhone 6/7/8; Galaxy S5, Pixel 2; Pixel 2XL; iPhone 5/SE; and iPhone x. It was also tested on iPad and iPad Pro screen sizes. The site is responsive and working on all screen sizes. Media queries, CSS and bootstrap grids were used to enable responsiveness across devices.
Manual tests were also done to ensure links; form submissions; model relationships; and purchases all worked correctly and that the site was defensively designed.

The site was also tested using Internet Explorer, Firefox and Chrome. 

User testing was done to ensure:

* New users can sign up.
* Users can login and logout.
* User is redirected to the correct pages after forms are posted.
* All links work correctly.
* The navbar links link to the correct section of the site.
* User generated content (blog comments) displayed correctly.
* Defensive design.
* Users can only enter comments on blog articles when logged in.
* Users must be logged in to make a purchase

## Issues

When viewing the site on Internet Explorer, I noticed that the product detail page, although working, the content is aligned slightly further to the left than it should be. In addition, the cart for mobile view only on the navigation bar is showing on desktop view in internet explorer. This does not happen on Mozilla or Chrome.

# Deployment

The site is hosted on heroku.(https://katiemodonnell88-closet-k.herokuapp.com/). 
Static assets are hosted on Amazon S3.

The credit card number to be used to make purchases is "4242424242424242".

The only differences between the production and development sites are that the category id numbers are different. In development, the links to the categories direct to the wrong category page becuase of these differences in id's. The links in the live site (prodution) all link to the correct pages though.

# Credits

## Content

* Converse blog came from: https://www.royalfashionist.com/ways-wear-converse-sneakers/
* Shoe wisdom blog - http://thedailyshoe-official.com/news-articles/shoe-wisdom/
* Tips to make your shoes last longer blog - https://www.cosmopolitan.com/uk/fashion/style/how-to/a40487/how-to-make-your-shoes-last-longer/
* Christian Louboutin blog - http://shoerazzi.com/christian-louboutin-fall-2016-collection/
* Gianvito blog - http://shoerazzi.com/gianvito-rossi-fall-winter-2016-collection/ 

## Media

The imagery used in this site were obtained from:

* https://unsplash.com/ 
* https://pixabay.com/en/. 
* https://www.office.co.uk/view/product/office_catalog/2,37/3489140736 
* https://www.zalando.ie/shoes/?wmc=SEM353_NB_GO._2650121041_1509525565_57563469029.&opc=2211&gclid=CjwKCAiA4OvhBRAjEiwAU2FoJSEpievdL3GwUhDmNavCNqzqWj5iBMG6a6p4WIyrUp9G5nijkHCNmxoC0ckQAvD_BwE
* https://purpletag.ie/
* https://www.schuh.ie/?gclid=CjwKCAiA4OvhBRAjEiwAU2FoJVkUAArOYOguE_qg0IuR05X3E7p9QvuB_aNsN1beZRZNUczZcFJL-RoC0d4QAvD_BwE


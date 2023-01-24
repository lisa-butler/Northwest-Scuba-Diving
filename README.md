Font used for main site header: Acme
json formatter.org
https://dashboard.stripe.com/test/logs?method%5B0%5D=post&method%5B1%5D=delete&direction%5B0%5D=self&direction%5B1%5D=connect_in&success=true&showIP=false

# Northwest Scuba Diving
## Portfolio Project 5 - Ecommerce
### This ecommerce site was built for Portfolio Project Five of the Code Institutes Diploma in Software Development.
### This ecommerce site was built to be a dive schools platform for allowing customers to get in contact to organsise dives and to purchase their diving experiences. The target customer base is people who are interested in learnig to dive and those who are already divers and want to dive in a different location.

------------------------------------------------------------------
### Lisa Butler
------------------------------------------------------------------
![Am I Responsive Testing](documentation/screenshots/amiresponsive.png)
------------------------------------------------------------------

## View the live site here
**[Live Site](https://northwest-scubadiving.herokuapp.com/)**

## View the Repository here
**[Repository](https://github.com/lisa-butler/Northwest-Scuba-Diving)**

------------------------------------------------------------------
## Contents

 1. [User Experience](#ux)
 2. [Application Features](#features)
 3. [Technology Used](#tech)
 4. [Testing](#testing)
 5. [Bugs](#bugs)
 6. [Deployment](#deploy)
 7. [Credits](#credits)
 8. [Content](#content)


------------------------------------------------------------------
## User Experience

<a name="ux"></a>
### **Pre project planning**

I decided to create a dive school page to sell a service rather than goods as my ecommerce project as this is a domain that i know quite well. Knowing the domain means i knew what functionality the customer and admin would want avalible. There is no dive school in my area, though i have heard that there used to be one, so it was interesting to think of what could be offered if a dive school was to set up in the region.
Pre project planning involved developing user stories, wireframe mock ups, logic flow diagrams and researching some basic styling ideas.
I also researched the software stack to use for this specific project. As it is Django based i was tied to using Django and Python, however, I looked into using React and various alternatives for Bootstrap. I ultimately ended up usiing Bootstrap and Djangos built in functionality. Styling relied heavily on inline Bootstrap styles, which was very effective.

**Strategy:**

Determining what to include in this ecommerce site involved some research. I looked at several dive school sites both in ireland and abroad to get an idea of what functionality these sites often had. From this i was able to develop user stories for both the customer and the admin of the site.

**User stories:**
### New Site Users

- As a new site user, I would like to register for an account, so that I can save my details to make checkout smoother.
- As a new site user, I would like to register for an account, so that I can login and view my orders.
- As a new site user, I would like to be able to see reviews, so that I can decide if i want to dive with this dive school.
- As a new site user, I would like to be able to contact the dive school, so that I can have my questions answered.

### Returning Site Users

- As a returning site user, I would like to be able to sign in, so that I can view my previous orders.
- As a returning site user, I would like to be able to sign up for a newsletter, so that I can be kept updated about upcoming courses and dive trips.
- As a returning site user, I would like to unsubscribe from a newsletter, so that I can no longer recieve them.
- As a returning site user, I would like to be able to submit  review, so that I can review my experience at the dive school.
- As a returning site user, I would like to be able to contact the dive school, so that I can organise my dives/courses.

### Site Admin

- As a site administrator, I should be able to view customers orders, so that I can take note of numbers signed up for courses/dives.
- As a site administrator, I should be able to add, remove and edit products, so that I can keep the avalible courses up to date and add things as they come up.

These were added into the Issues section on Github for effective project planning and moved on the projects board as i progressed through them.

 ![Issues](log/static/images/issues.jpg)

GitHub **[Issue Tracker](https://github.com/lisa-butler/My-Dive-Log/issues?q=is%3Aissue+is%3Aclosed)**

![Projects](log/static/images/projects.jpg)

GitHub **[Projects Board](https://github.com/users/lisa-butler/projects/3)**


### **Style**

Background: After some experimentation with backgrounds and overlays, it was concluded that a plain white background provided the most visually appealling and accessible style. These benefits for accessibility would enable the older population to have a better chance of navigating the application. A basic icon that was used on an earlier application was selected as this had a nice color pallet and fitted the theme in a visually pleasing way. A small banner of photographs was used to add some life to the home page, as was done in previous projects. At this stage i am aware thaat styling is not my strong suit so have elected to keep things simple and effiecient for this project and leave styling to the pros in the future.

### Colour Scheme
After some experimentation, a white background was chosen as it enabled the content to be very legible and to stand out for the user, making the site more navigatable for those with visual imparements etc.

- `Dark Grey` used for primary text as it is high contrast against the white background so is easy to read.
- `Teal` used for main logo text and some highlights as it is a water themed color.
- `Black` used for text as it stands out.
- `Red and Blue` used for edit and delete functionality for admin.

I used CSS Bootstrap convienience classes to apply to all Toasts.
![Convenience Classes](documentation/screenshots/convenience_classes.png)


### Typography

Google Fonts and Font Awesome were used to select fonts and icons for this ecommerce site.

- [Acme](https://fonts.google.com/specimen/Acme?query=acme) was used throughout the site as it was clear and legible while also having a water themed style.

- [Font Awesome](https://fontawesome.com/icons) icons were used throughout the site, such as the social media icons in the footer and for the account and shopping bag tabs.

**Scope:**

* The ecommerce site should have a clear and consistent layout including navigation and login, logout functionality.
* The ecommerce site should be responsive so that it can be used on all devices as a vast majority of online ecommerce is done on mobile devices in the modern world.
* The ecommerce site should have a navigation bar that is self explanitory and easy for users to navigate.
* Products should be split into intuitive categories and product details should be consise and informative.
* Adding, removing and modifying the number of items in the shopping bag should be straightforward and simple.
* Logging in and out and creating a user profile should be very simple.
* For the Admin, adding new products, editing current products and removing others should be straightforward.
* Newsletter registration should be easy to access and encoraging for users.
* Getting in contact should be easy to do and the form should have as few fields as possible to encourage users to utilise it.
* Reiews should be legible on all screen sizes and allow the user the opportunity to submit a review of their own.


## Wireframes

### Structural Planning

There were limited ways to achieve the above goals as one ecommerce site is much like the next. Three categories for products were used, alongside a home page for the users to get some info about the dive school etc, a contact page for the user to reach out and a reviews page for the user to read previous users testimonials. The site would also have shopping bag and account selectors, differentiated from the main nav bar and denoted with icons. The account option would activate a drop down menu, options in this menu would differ depending on the users login and admin status.

In preperation for these features, wireframes were created using [Balsamic Wireframes](https://balsamiq.com/wireframes).

### **Home**

This wireframe shows the positioning of the navigation bar, its elements and the proposed positioning of the account and shopping bag icons on the right side of the screen. It also shows a suggestion of where the quik links to encourage divers to progress further into the site will be positioned. Both for learn to dive and book a dive and for get in contact and signup for our newsletter.

![Homepage Wireframe](documentation/wireframes/home.png)

### **Products**

This layout will be the same across the three products pages, with the only difference being the products themselves. An idea of the approximate layout of product cards was estimated on this page. As well as this it was decided to have some text outlining the puropse of each category to aid navigation and product selection.

![Products page Wireframe](documentation/wireframes/products.png)

### **Contact**

A simple form was decided on for the contact page. This was to enable a user to quickly send off a message to the site owners with a question etc.

![Contact page Wireframe](documentation/wireframes/contact.png)

### **Shopping Bag**

After some research it was concluded to have a shoopping bag layout very similar to most ecommerce sites. The product image alongside its name would be displayed with the option to remove the item or increase or decrease the quantity.

![Shopping Bag Wireframe](documentation/wireframes/bag.png)

### **Checkout**

Checkout would include a simple checkout form for the users billing details that were required by Stripe to process the payment. There would also be an order summary beside this form for the user to review their order for a final time.

![Checkout Wireframe](documentation/wireframes/checkout.png)

### **Profile**

The profile page would be for all users to review their orders and update their personal details to make checkout smoother.

![Profile page Wireframe](documentation/wireframes/profile.png)

### **Reviews**

Reviews was something that many dive companies had so it was concluded that this would be something useful tto add to the site. I elected to have reviews as testimonals regarding the diving experience with the school rather than on each product. The reviews site will have a simple list of user reviews with their username and the date printed below. A user must be logged in to leave a review.

![Reviews Wireframe](documentation/wireframes/reviews.png)

### **Write a Review**

Write a review was designed very similarly to the contact form except that it will have the condition that the user must be logged in to view it. It is a basic form for the user to fill out regarding their diving experience.

![Write a Review Wireframe](documentation/wireframes/write_a_review.png)

### **Customer Orders**

This will be for the admin only and will be a method in which to review customers orders so that the site admin can keep track of diving numbers for specific course etc and have customers emails so that they can get in contact with them re their dives.

![Customer Orders Wireframe](documentation/wireframes/orders.png)

### **Product Management**

Product management is a tool for the admin to add products into the database. This will enable the simple addition of a product alongside its image so that the admin can keep the products avalible up to date.

![Product Management Wireframe](documentation/wireframes/product_management.png)


## Application Features

<a name="ux"></a>

### **Index.html**

![index.html](documentation/screenshots/index-html.png)

**Title:**

The title of the application "NorthWest Scuba Diving" is a link to return the user to the home page of the application, allowing for easier navigation, this persists across all of the pages. It is the largest text on screen and populates from templates/base.html. The color Teal was selected to give the page an ocean colored theme. This text is also the largest text throughout.

![Header and Logo](documentation/screenshots/icon-header.png)

**Icon:**

The dive mask icon was used throughout the application to provide a visual continuation throughout the pages. This is a simple and aesthetically pleasing symbol that reiterates the theme of the application. Its color pallet works very well with the other colors used in the application.

**The navigation bar:**

This is a simple banner containing the six pages, three of which are product categories. Due to utilising a base main nav for this application, it was difficult to have the active page show so this was left out for now. The text is black on white so it is easy to read and stands out against the background.

![Navigation Bar](documentation/screenshots/nav-bar.png)

**Account and Shopping cart:**

These icons sit above the navigation bar to the right hand side. They are black in color to stand out against the white background and the shopping bag goes teal on mouseover. The text below the shopping bag indicates the total cost of items in the bag and updates as items are added.

When the user is not logged in the options on display are;
- Login
- Register

When the user is logged in the options change to;
- My Profile
- Newsletter
- Logout

And when the user is an admin they have additional options of;
- Customers Orders
- Product Management

![Account and shopping cart](documentation/screenshots/account-dropdown.png)

**Cards:**

The cards containing the prompts to view the avalible courses or book into a dive are there to provide another way to navigate into these main areas of the application with ease. By placing these functions side by side in cards that hoover out from the page, the aesthetic of the page is improved and the options are highlighted for the user.

![Cards](documentation/screenshots/quick-link.png)

**Banner images:**

This trio of images was chosen to form the banner instead of using a single image as they worked well together and provided an appealing insight into the application theme. The images were all taken by the creator of this application so no permissions were required to be granted. The color tone of the images worked well with the general color theme that was selected for this application. A short piece of text about the dive school was also included on the page to introduce customers to what they could expect.

![Banner Images](documentation/screenshots/banner-images.png)

**Contact card:**

A get in contact card was also used below the banner images to prompt the customer who was new to the site to reach out. There is also a suggestion that the user might like to sign up for the newsletter in this card.

![Contact card](documentation/screenshots/get-in-contact.png)

**Footer:**

The footer contains links to various social media; Facebook, Twitter, YouTube and Instagram.
These links are created using Font Awesome icons. The links do not currently go to specific areas within these social medias. If this app was to be put to real use these platforms would be very beneficial for marketing strategies.

![Footer](documentation/screenshots/footer.png)

### **courses.html/qualified.html/gear.html**

As all three products pages are identical except for the products they house, they will all be discussed here.

![Products pages](documentation/screenshots/products-page.png)

**Product Cards:**

The products are displayed on product cards. Similarly to the cards used on the home page, the products cards are designed to sit out from the page and pop on mouseover, making where the mouse is more obvious to the user.

![Products pages](documentation/screenshots/product-cards.png)

These cards are two to a row on large and medium screens and one to a row on small screens to optimise viewing for the customer

![Products on Apple Ipad Air simulation](documentation/screenshots/products-responsive.png)


### **product_detail.html**

When a user clicks on a product in any of the three products pages, the detail view of the product opens.
This page involves the same image of the product as displayed on the products page with a detailed description of the product.

![Product details](documentation/screenshots/product-details.png)

**Product Info:**

The product info is displyed in dark text against a white background for easy viewing. The price of the course is also clearly displayed. The user can increase the quantity of the item before putting it into their basket.

**Admin Functionality:**

This page also hosts admin functionality only visable to the admin. This is the edit and delete buttons. They are strategically colored in red and blue to help indicate their use. The buttons can be used to edit details about a product or to delete a product.

![Products pages](documentation/screenshots/edit-delete.png)

### **contact.html**

The contact page included a very straight forward form for the user to fill in to reach out to the dive center with a simple button to send the form. The user fills in details such as name and email before reaching out to the club by clicking Send Message.

![Contact Form](documentation/screenshots/contact-page.png)

**Message sent:**

After clicking send the user is redirected to the message sent page. This informs the user that their message has been sent successfully.

![Message sent](documentation/screenshots/contact-sent.png)


### **reviews.html**

The reviews page consists of simple cards with the users review text on them. There are two cards per row on large and medium sized screens and one on smaller screens, allowing for ease of reading. The text is dark on a white background. For the logged in user, there is a button indicating that they can write a review at the bottom of the page.

![Reviews Page](documentation/screenshots/reviews-page.png)

**Review Card:**

The review cards pop on mouseover, similar to the other cards on the page. They contain a simple heading, review content and the users username and date of review.

![Review](documentation/screenshots/review-card.png)

**Write a review:**

The page for submitting a review contains a simple card with a form on it. This form asks for a title for the review and review content to be input. The username and date are stored automatically when the user hits the submit button.

![Write a review](documentation/screenshots/my-review-page.png)


### **newsletter.html**

The newsletter page is very straightforward. It checks if the user is logged in and if not it suggests that the user login or register to sign up for the newsletter.

![Newsletter Loggedout](documentation/screenshots/newsletter-loggedout.png)

If the user is logged in and hasnt registered before, it presents the user with an option to register for the newsletter.

![Newsletter subscibe](documentation/screenshots/newsletter-subscribe.png)

If the user is logged in and has already registered for the newsletter, it gives the user the opportunity to unsubscribe.

![Newsletter unsubscribe](documentation/screenshots/newsletter-unsubscribe.png)

**Subscribed:**

Clicking subscribe will take the user to the subscription sucessful page. This is a simple card with text indicating that the user has sucessfully subscribed to the newsletter.

![Newsletter subscribbed](documentation/screenshots/newsletter-subscribed.png)

**Unubscribed:**

Clicking subscribe will take the user to the unsubscribing sucessful page. This is a simple card with text indicating that the user has sucessfully unsubscribed from the newsletter.

![Newsletter unsubscribbed](documentation/screenshots/newsletter-unsubscribed.png)


### **bag.html**

The shopping bag page suck with the same clean objects on a white background theme as the previous pages. Items are visted with their price and the total cost at the bottom of the page alongside a checkout button.

![Shopping bag](documentation/screenshots/bag-page.png)

**Empty Bag:**

Initially the bag checks if the user had anything in their shopping bag. If not, it displays that there is nothing in the bag and to continue looking.

![Bag empty](documentation/screenshots/empty-bag.png)

**Items in Bag:**

If there are items to be displayed in the bag it shows the items images with their price and quantity listed. The user has the opportunity to increase or decrese the quantity or remove the item from the bag at this point. The subtotal is displayed alongside the product and the grand total is at the bottom. There is also a checkout option avalible.

![Bag items](documentation/screenshots/bag-quantity.png)

### **checkout.html**

This is the page that the user lands on after clicking checkout in the shopping bag page.

![Checkout page](documentation/screenshots/checkout-page.png)

**Checkout Form:**
The checkout page contains a form for the users billing details. These are required for stripe to process the payment and are pre populated for a logged in user who has saved their details on their profile. The form consists of seven text fields for the user to type in their address, email, phone number etc and one drop down for selcting country.
There is a box the user can tick to save this information to their profile.
There is a card details field below this that the user must fill their card details into to checkout. The checkout button at the bottom of the screen has a line of text below it to remind the user that they will be billed this amount.

![Checkout form](documentation/screenshots/checkout-form.png)

**Order Summary:**
The order summary is to the right of the checkout page and displays the items in the users basket alongside their quantity, the subtotals for each and the grandtotal. A small image of the item is displayed.

![Checkout page](documentation/screenshots/checkout-summary.png)

**Thank You Page:**
On hitting submit order the user is redirected to the thank you page. This page displays an order summary complete with their order number and order date alongside their basic details.

![Checkout page](documentation/screenshots/order-recieved.png)


### **profile.html**

This is the my profile page that is avalible to all users. It includes an order history and a form they can fill in to update their default details. This is intended to make checkout a smoother proceedure.

![Profile page](documentation/screenshots/profile-page.png)

**Default information:**
The default information form gives users the opportunity to update their address and phone number to save them from adding in these details in the checkout form everytime. It is a useful tool for returning users and reduces the mouse clicks involved in going from checkout to proceed with payment.

![Default information](documentation/screenshots/user-info-card.png)

**Order History:**
The order history is displayed next to this. It is a simple scrollable card with the users previous orders listed on it. There is a brief order summary and a grand total as well as the date the order was placed for each order. By clicking on the order number the user can expand the order confirmation box and view their previous order in detail.

![Order history](documentation/screenshots/order-history-card.png)

### **product_management.html**

Product management is a page that can only be accessed by the admin. This page consists of a form for the admin to fill out to add a new product.
The admin can select an image file for the product and once added, the new product will be populated in whatever category the admin selected from the dropdown.

![Product management](documentation/screenshots/product-manage-page.png)


### **orders.html**

Customer orders is another admin only page. This page is a list of all customer orders so that the admin can keep track of divers that have registered for each dive, course etc.

![Customers orders page](documentation/screenshots/cust-order-page.png)

 It consists of simple card boxes with the customers basic information, their order info and a total.

![Customer order card](documentation/screenshots/cust-order-card.png)

### **sign in/ sign out/ register**

Sign In, Sign Out and Register, as well as password recovery etc are all sourced form Allauth templates and as such look very similar throughout. I did not make massive styling changes to these templates but rather did some minor changes to the frequently utilised ones, such as sign in, sign out and register.

![Register](documentation/screenshots/signup.png)

These are simple forms for the user to fill in. They have form controls on them to ensure that the email is indeed an email, the password is not too simple and the username or email doesnt already exist in our database.

![Form validation](documentation/screenshots/register-validation.png)

When the user submits this form they are taken to a page that tells them they have been registered and to confirm their email address.


### **Confirmation Emails**

On registration an email is sent to the email address the user registered with. This can be seen below on a temporary email generator [Temp Mail](https://temp-mail.org/en/).

![Email confirmation](documentation/screenshots/confirm-mail.png)

The email that is sent can be seen below with a link for the user to click to verify this email address.

![Email Confirmation](documentation/screenshots/reg-email.png)

When the user makes a purchase they also recieve an email, this email confirms that the users order has been recieved and informs them that they will recieve further information regarding their diving experience etc in the coming days.

![Order Confirmation Email](documentation/screenshots/order-conf-email.png)

### **Toasts**
These are used extensively throughout the application. The code for toasts was taken from Bootstrap Toasts and modified for usage. These pop up when a customer registers, signs in, signs out, adds an item to their bag, removes an item from their bag etc. They are useful for showing the customer that their action has been recieved.

The toast below shows an item has been added to the bag

![Item added toast](documentation/screenshots/toast1.png)

The toast below shows the user has been signed out sucessfully.

![Logged out toast](documentation/screenshots/toast2.png)

**Further features I would implement:**

If I was to build this application again with the intentions of it being a live application, there are several additional features i would implement;

* A stock control counter to limit the number of a specific product avaliable. For example on one of the courses, limit the places in the course to a set number and once that many people have registered for the course, remove it from the products view.
* A more extensive customers orders page for the admin. This would display the products and the total number of customers who have registered for it.
* A gallery tab where users could share their photos with a comment about their dive.

------------------------------------------------------------------

## Technologies Used

<a name="tech"></a>

### **Languages**

The languages used in this project were;

- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.


### **Frameworks/Libraries/programs:**

- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) and/or [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Markdown Builder by Tim Nelson](https://traveltimn.github.io/readme-builder) used to help generate the Markdown files.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [AWS S3](https://aws.amazon.com/s3) used for online static file storage.

### **Other Requirements:**

The full list of requirements can be seen in requirements.txt

asgiref==3.5.2
boto3==1.26.36
botocore==1.29.36
dj-database-url==0.5.0
Django==3.2
django-allauth==0.51.0
django-countries==7.2.1
django-crispy-forms==1.14.0
django-storages==1.13.2
django-truncate==0.1
gunicorn==20.1.0
jmespath==1.0.1
oauthlib==3.2.2
Pillow==9.3.0
psycopg2==2.9.5
PyJWT==2.6.0
python-dotenv==0.21.0
python3-openid==3.2.0
pytz==2022.6
requests-oauthlib==1.3.1
s3transfer==0.6.0
sqlparse==0.4.3
stripe==5.0.0


### **Agile Development Process:**

* GitHub Issue Tracker **[Issues](https://github.com/lisa-butler/Northwest-Scuba-Diving/issues)**

* GitHub Projects Board **[Projects Board](https://github.com/users/lisa-butler/projects/5)**

------------------------------------------------------------------
### MoSCoW Prioritization

I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab by deciding where they fell in the below categories.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

## Ecommerce Business Model

This site sells services to individual customers, and therefore follows a `Business to Customer` model.
It is of the simplest **B2C** forms, as it focuses on individual transactions, and doesn't need anything
such as monthly/annual subscriptions, however, this is something i would consider looking into in the future.

It is still in its early development stages, although it already has a newsletter, and links for social media marketing.

Social media can potentially build a community of users around the business, and boost site visitor numbers,
especially when using larger platforms such a Facebook.

A newsletter list can be used by the business to send a regular update to customer regarding courses, new dives etc that are now on offer.
As well as updates to business hours, notifications of events, recuritment etc!

## Search Engine Optimization (SEO) & Social Media Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users
when searching online to find my page easily from a search engine.
This included a series of the following keyword types

- Short-tail (head terms) keywords
- Long-tail keywords

I also played around with [Word Tracker](https://www.wordtracker.com) a bit
to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://northwest-scubadiving.herokuapp.com

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://northwest-scubadiving.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the
[Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip)
provided by Code Institute.

![Balsamic facebook mockup](documentation/wireframes/fabebook-page-mockup.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in recieving newsletters.
I currently do not have functionality in place to send the user newsletters, however, this is something i would add in the future.
------------------------------------------------------------------
## Troubleshooting and testing

<a name="test"></a>

### **Troubleshooting:**

Troubleshooting was quite varied on this project as it involved quite a wide range of different technologies.
The biggest issue i ran into was getting the webhook handlers and Stripe to work effectively.
Stripe is now working well and recieveing orders correctly, after much ordeal.

![Stripe](documentation/screenshots/stripe.png)

There were some database related issues which were solved by googling how to clear databases etc.
There were countless other small errors solved throughout the development of this application.
Troubleshooting was managed using dev tools, printing to terminal and utilising a lot of googling.

**Error Handling and input control:**

Input control was something i spent some time thinking about as there were many forms in this application.
Forms like the signup form, require the correct parameters in their fields in order to accept the form. There must be an @ in the email field and the passwords must match and not be too similar to the username.
There was also some checking the db for if the email and user already existed. This is done when a user tries to register. I also have a check in to make sure that the user doesnt create duplicate orders.
When registering for the newsletter, there is a check to ensure the user is signed in, then to check if they are already subscribed.

### **Testing:**

**Code Validation:**

HTML:
Validated using **[W3C HTML Validator](https://validator.w3.org/)**

CSS:
Validated using Jigsaw via **[W3C](https://jigsaw.w3.org/css-validator/#validate_by_input)**

![CSS validation](log/static/images/W3CCSS.jpg)

Python:
Validated using **[ExtendsClass Python tester](https://extendsclass.com/python-tester.html)**

![Python validation](log/static/images/extendsclasspython.jpg)

**Browser Compatibility:**

Browser compatability was checked using both my own device (an Acer Aspire A514-52) which is running Google Chrome and with **[BrowserStack](https://www.browserstack.com/)**.

Compatability was confirmed on the following;

Google Chrome (tested on my own device) &#9745;

![Chrome testing](documentation/testing/chrome-testing.png)

Firefox (tested on my own device) &#9745;

![Firefox testing](documentation/testing/firefox-testing.png)

Microsoft Edge (tested on my own device) &#9745;

![Microsoft edge testing](documentation/testing/ms-edge-testing.png)

Opera (tested on BrowserStack) &#9745;

Safari (tested on BrowserStack) &#9745;

Compatabilty with both Android and IOS devices was checked as well.


**Accessibility Testing:**

Accessibility testing was done through Google LightHouse. The result was 97%. The only issue noted being the light grey used for the login/logout text. I chose to leave this as i liked the asthetic and felt it was not significant enough to cause issues.

![Accessibility test](documentation/testing/accessibility-testing.png)

**Performance Testing:**

Performace testing was checked using Google Lighthouse also with a very good result.

![Performance testing](documentation/testing/performance-testing.png)

**Responsivness:**

Responsivness was also checked using **[BrowserStack](https://www.browserstack.com/)**. This showed the application to work on all screen sizes.

### Testing reponsivness on an Ipad Pro
Viewport: 1024x1366 Screen size: 12.9" Monitor size: 15.4"

![Responsivness test on an Ipad Pro](documentation/testing/responsive-ipadpro.png)

### Testing reponsivness on a Samsung Galaxy Note 10
Viewport: 412x869 Screen size: 5.94" Monitor size: 15.4"

![Responsivness test on a Samsung Galaxy Note 10](documentation/testing/responsive-galaxynote10.png)

### Testing reponsivness on a Iphone X
Viewport: 375x812 Screen size: 5.8" Monitor size: 15.4"

![Responsivness test on a Iphone X](documentation/testing/responsive-iphonex.png)


The application was also responsive on larger and smaller screens and worked on different devices and browsers.

































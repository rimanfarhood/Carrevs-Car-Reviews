# CARREVS

CARREVS - Car Review site, a place for car enthusiasts to read and share their car reviews with each other.

![Responsive Mockup]()

Live Version can be accessed here: [CARREVS](https://carrevs-b0c8f9ee1e33.herokuapp.com/)

## Table of Contents

- [CARREVS](#carrevs)
  - [Table of Contents](#table-of-contents)
    - [Table of Contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
    - [Site-Goals](#site-goals)
    - [Agile Planning](#agile-planning)
      - [Epics](#epics)
      - [User Stories](#user-stories)
  - [The-Scope-Plane](#the-scope-plane)
  - [The-Structure-Plane](#the-structure-plane)
    - [Features](#features)
    - [Features Left To Implement](#features-left-to-implement)
  - [The-Skeleton-Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database-Design](#database-design)
    - [Security](#security)
  - [The-Surface-Plane](#the-surface-plane)
    - [Design](#design)
    - [Colour-Scheme](#colour-scheme)
    - [Typography](#typography)
  - [Technologies](#technologies)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Version Control](#version-control)
    - [Heroku Deployment](#heroku-deployment)
    - [Run Locally](#run-locally)
    - [Fork Project](#fork-project)
  - [Note](#note)
  - [Credits](#credits)


# User-Experience Design

### Site Goals

 The goal is to provide a place where car enthusiasts can share their opinions and experience about cars with each other. And for car buyers to read other peoples reviews about a car they might want purchase.

### Agile Methodology

The project was developed using a agile methodology, delivering a few small features in sprints. In total there were 3 sprints spaced out over 3 weeks.

The features were assigned to Milestones (epics), in total 6. Prioritized by labels 'Must have', 'Should have, 'Could have'. To ensure all core requirements were completed first.

Kanban board created using GitHub Projects, can be viewed here - [Project-board](https://github.com/users/rimanfarhood/projects/11)
All stories, with the exception of documentation tasks, have a complete set of acceptance criteria that defines the functionality that signifies completion.

#### Epics 


**Milestone 1 - Base Setup**

The base setup epic consists of all stories essential for the application's base setup
The app wouldn't work without setting up the base first, There for essential to do first.

**Milestone 2 - Authentication**

The authentication procedure involves signing up, logging in, and controlling who receives access.

**Milestone 3 - Reviews**

The reviews epic is for all stories that relate to the creating, deleting, editing and viewing of reviews. This allows for users to sign up and add their own reviews with a simple UI interface.

**Milestone 4 - Additional Pages**

The additional pages epic is for small pages that did not have enough user stories to justify their own full epics, instead of creating multiple epics for tiny features.

**Milestone 5 - Deployment**

This epic is for all stories related to deploying the app to heroku, so that the site is live for users.

**Milestone 6 - Documentation**

Epic for documentation related stories and tasks that are needed to document of the application. Aiming to explaining the development stages and necessary information on running, deploying and using the application.


#### User Stories


**Milestone 1 - Base Setup**

-As a developer I need to set up the project so that so it's ready to implement features.

-As a developer I need to create a base.html page and structure so that it can be reused for other pages.

-As a developer, i need to create static resources so that CSS, Javscript, icons, and images works on the website.

-As a developer I can create a navbar menu so that users easily can navigate the site on all devices.

-As a user I can find a footer with social media links so that i can visit the sites social media accounts.


**Milestone 2 - Authentication**

-As a developer i need to implement Allauth so that users can sign up and create their car reviews.

-As a website owner I want to have the Allauth pages customized so that the style matches the rest of the site. 

**Milestone 3 - Reviews**

-As a user i can add a car review so that i can share it for other users to read.

-As a user I can view all users reviews so that I can read them. 

-As a user I can view a specific review so that I can read it.

-As a user I can edit and update my own reviews, so I Can update the review if i want.

-As a user I can delete my review, if I don't want it 

-As a user i would like to receive feedback when add, edit or delete a review as well as sign up/in/out.

**Milestone 4 - Additional Pages**

-As a site owner I want home page so that users can read about the website.

-As a developer I need to implement a 404 error page to notify users the page they requested could not be found.

-As a developer I need create a 403 error page to redirect unauthorized users preventing them from accessing a resource or perform an action without the permissions.

-As a developer I need to create a 500 error page so that users is notified when an internal server error has occurred.
 

**Milestone 5 - Deployment**

-As a developer I need to deploy the final project to Heroku so that users can visit the live site.


**Milestone 6 - Documentation**

-Create a readme and write documentation.
-Write testing documentation.

- Tasks -Complete readme documentation
- Complete testing documentation


## The Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality
* Restricted role based features

## The Structure-Plane

### Features

#### Site Wide

**Navigation Bar menu**

USER STORY - As a developer I can create a navbar menu so that users can easily navigate the site on all devices.

  * Full responsive navigation menu displayed on all pages including links to Home, reviews, adding review, sign up/in/out pages.
  * Makes the navigation between the pages easier for the user.

![Nav Bar](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/navdt.png)


**Footer**

USER STORY - As a user I can find a footer with social media links so that I can visit the site's social media accounts.

   * Responsive footer with social media icons links, displayed on all pages.

![Footer](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/footer.png)


**Toast**

USER STORY - As a user i would like to receive feedback when add, edit or delete a review as well as sign up/in/out

   * Toast is displayed when user perform any of these actions: 
      - Sign up
      - Log in
      - Log out
      - Create a review
      - Edit a review
      - Delete a review

![Toast](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/toast.png)    

**Home Page**

USER STORY - As a site owner I want a home page so that users can read about the website.

  * Home page with some information about the site

![Home Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/homepg.png)


**Reviews Page**

USER STORY - As a user I can view all users' reviews so that I can read them.

   * A page with the all the reviews displayed
   * A search bar is included for users to be able to search for specific reviews

![Reviews Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/reviews.png)


**Add Review Page**

     USER STORY - As a user I can add a car review so that I can share it for other users to read.

   * The Add Review page includes a review form
   * If the user is not logged in they wont be able to access this page instead they will be asked to sign up or in.

![Add Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/addrv1.png)
![Add Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/addrv2.png)
![Add Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/addrv3.png)
![Add Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/addrv4.png)
![Add Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/addrv5.png)


**Review Detail page**

     USER STORY - As a user I can view a specific review so that I can read it.

  * Includes the full review with all the details.
  
![Review Detail](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/detail.png)

**Edit Review Page**

     USER STORY - As a user I can edit and update my own reviews, so I can update the review if I want.

   * If the viewer on the detail page is the logged in review owner they will have a edit button displayed.

![Edit Review](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/edit.png)
![Edit Button](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/editbtn.png)


**Delete Review page**

     USER STORY - As a user I can delete my review if I don't want it.

   * To get to the delete page, the review owner has to be logged in and view their review there will be a delete button displayed.
   * If the user want to delete the review they will be have to confirm the deletion before.

![Delete page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/confirmdeletion.png)
![Delete Button](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/edit.png)


**Error Pages**

**404 error page**

     USER STORY - As a developer I need to implement a 404 error page to notify users the page they requested could not be found.

 - A 404 error page is displayed when the users request could not be found. 
 - An explanation of the error is provided and a link to the home page. 



**403 error page**

     USER STORY - As a developer I need create a 403 error page to redirect unauthorized users preventing them from accessing a resource or perform an action without the permissions

 - A 403 error page is displayed when a unauthorized users is trying to perform an action without the necessary permissions. 
 - An explanation of the error is provided and a link to the home page. 



**500 error page**

     USER STORY - As a developer I need to create a 500 error page so that users are notified when an internal server error has occurred.

  - A 500 error page is displayed in case of an internal server error occurs.
  - An explanation of the error is provided and a link to the home page.




**Favicon**

    * Site wide favicon included on all pages was added.
    * The image icon on the tab makes it easier for the user to find the site when having multiple tabs open at the same time. 




### Features left to implement

If I had more time and or knowledge i would implement these features:

   - Add pagination to the reviews page if the reviews were to many. 
   - If I had more time I would do change the home page design, with sign up section there. 
   - The review detail page's layout is not completely done either, I would make it more symmetrical and design the layout more detailed, with sections and more.
   - I would implement a functionality for users to communicate with each other and like and dislike views.
   - I would like to implement an about us page with a contact us section. 
   - Implement a search filter in the reviews page.

I would there is a whole lot more features i would like to implement but this is a few of them. 


## The-Skeleton-Plane

### Wireframes

**Home page**

- Home page


![Home Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_wireframes/home.png)

- Reviews Page

![Reviews Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_wireframes/reviews.png)
![Reviews Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_wireframes/reviews-md.png)

- Review detail Page

![Review Detail Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_wireframes/carinfo.png)

- Add Review Page

![Add Review Page](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_wireframes/form.png)


### Database Design

- Database designed structure allow CRUD functionality to be available to users with an account registered. The model is the main key to the application, it's connected to the whole site, the home page, the reviews page, the creating and managing reviews.

**Entity Relationship Diagram**

-created using [Dbeaver](https://dbeaver.io/)

![Entity Relationship Diagram](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/readme_images/databasedesign.png)

### Security

The views are secured by using django auth mixins,LoginRequiredMixin, UserPassesTestMixin. A test function was created to use the mixin and checks were ran to ensure that the user who is trying to access the page is authorized. Any user restricted functionality listed in the features was secured using this method.

Environment variables stored in an env.py for local development. For security purposes to ensure no sensitive information was added the the repository. In production, the variables was added in heroku config vars within the project.


## The-Surface-Plane
### Design

### Color Schemes

Main color schemes used for the project is blue
   - Navy (#071330) background, 
   - White (#fff) font color in the body.
   - Mustard yellow (#D99326) to add a bit of colored details, used in navbar to underline the active page, hover text in home page.
   - Light blue (#99aec2) used in navbar and button hover.
   - Darker navy (#020a1b) used mainly navbar background color.
   - The darkest navy shade i used (#000511) for borders and box shadows mostly.


### Typography

For the navbar and headings the Playfair Display font was used and for the body Merriweather font was used, both imported from Google Fonts.


## Technologies 

**Technologies Used**

  * HTML, the main language used for the structure.
  * CSS, to add the style.
  * Python, the main programming language used for the application using the Django Framework.
  * JavaScript, to add timeout functionality to toasts.
  * [JSHint](https://jshint.com/), validating js code.
  * [Gitpod](https://www.gitpod.io/), Developed using Gitpod Ide coding, editing and preview.
  * [Github](https://github.com), source code hosted on Github.
  * [Python Linter CI](https://pep8ci.herokuapp.com/), to validation python code.
  * [Heroku](https://www.heroku.com/), used to deploy the application live.
  * [Uxwing](https://uxwing.com/), used for home icon and social media icons.
  * [Reverso](https://www.reverso.net/spell-checker/english-spelling-grammar/), to check spelling and grammar. 
  * [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/open/), Measuring for responsiveness.
  * [W3C HTML Validator](https://validator.w3.org/#validate_by_input), HTML validation.
  * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), CSS validation.
  * [Wave](https://wave.webaim.org/), accessibility evaluation tool.
  * [Am I responsive](https://ui.dev/amiresponsive), mockup image.
  * [Google Fonts](https://fonts.google.com/), fonts.
  * [Font Awesome](https://fontawesome.com/), icons.
  * [Favicon](https://favicon.io/), favicon in tab.


**Python Modules**
 
 - Django Class based views ListView, UpdateView, DeleteView, CreateView - Used to create classes to create, read, update and delete.

 - Mixins LoginRequiredMixin, UserPassesTestMixin - Used to enforce login required on views and test user is authorized to perform actions.

 - messages - Used to create messages to the toasts to display feedback to the user upon actions.


**External Python Modules**

- asgiref==3.7.2 - Installed as dependency with another package.

- black==23.12.1 - For PEP8 complaint.

- click==8.1.7 - Installed as dependency with another package.

- cloudinary==1.37.0 - Cloundinary set up for image hosting.

- crispy-bootstrap5==2023.10 - to allow bootstrap5 use with crispy forms.

- dj-database-url==2.1.0 = To parse database url for production environment.

- Django==4.2.9 - Framework used to build the application.

- django-allauth==0.53.0 - Used for the authentication system, user accounts sign /in/up/out.

- django-cloudinary-storage==0.3.0 - Storage system to work with cloudinary.

- django-crispy-forms==2.1 - Used to style the forms when rendering.

- django-resized==1.0.2 - Used tp automatically resize images when uploading.

- django-richtextfield==1.6.1 - To create custom charfields and widgets.

- gunicorn==21.2.0 - Server.

- oauthlib==3.2.2 - Installed as dependency with another package.

- pathspec==0.12.1 - Installed as dependency with another package.

- pillow==10.2.0 - Imaging library.

- psycopg2==2.9.9 - Database adapter.

- PyJWT==2.8.0 - Installed as dependency with another package.

- python3-openid==3.2.0 - Installed as dependency with another package.

- requests-oauthlib==1.3.1 - Installed as dependency with another package.

- sqlparse==0.4.4 - Installed as dependency with another package.

- whitenoise==6.6.0 - Used to serve static files directly without use of static resource provider like cloundinary. 


## Testing 

Testing file can be viewed here - [Testing](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/TESTING.md)

## Deployment

Project deployed to Heroku

- Steps
Before deploying to Heroku

   - Freeze requirements and push to GitHub

In Heroku

   - Navigate to Heroku's website and create an account or log in
   - Click on the 'new' button in the dashboard
   - Select Create New App
   - Name app and choose region 
   - Click Create app 
   - Go to app settings 
   - Click Reveal Config Vars
     Add these config vars: 
      - SECRET_KEY = (your secret key)
      - DATABASE_URL = (your database url)
      - CLOUDINARY_URL = (your cloudinary url)
   - Then navigate to the deploy tab
   - Select connect to GitHub
        - Search for your repository
        - Click connect
   - Then scroll down to deploy manual and select main branch
   - Click deploy

Usually takes a minute or two before the app is deployed, when it is done click on View.


## Fork

1. Navigate to the repository you want to fork
    
2. On the top right of the page under the header, click the fork button.

3. Now that will create a duplicate of the full project in your GitHub Repository.

## Creating a Local Clone

1. Navigate to the GitHub repository
2. Click on the "Code" drop-down button.
3. Choose local and HTTPS you will have a link copy that URL
4. If wanted, change the current working directory in GitPod to the location desired.
5. Type "git clone" and paste the URL from GitHub.
6. Press "Enter" and the local clone will be create.


## Credits

- Django recipe tutorial how to build a crud app with django on youtube by [Dee mc - click to view](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)

- How to create a subclass model [Click here to view](https://plainenglish.io/blog creating-reusable-models-with-django-and-mixins-2126c5f11eac#show-me-some-code) 

- Followed these recommendations [CI](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit#heading=h.5s9novsydyp1) 

media
- Here I found the main color #071330 used in the website - [Canva color pallettes](https://www.canva.com/colors/color-palettes/mountain-haze/)

[def]: https://carrevs-b0c8f9ee1e33.herokuapp.com/
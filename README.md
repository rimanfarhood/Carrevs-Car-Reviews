# CARREVS

CARREVS - Car Review site, a place for car enthusiasts to read and share their car reviews with each other.

![Responsive Mockup] ()

Live Version can be accessed here: [CARREVS](https://carrevs-b0c8f9ee1e33.herokuapp.com/)

## Table of Contents

- [CARREVS] (#carrevs)
  - [Table of Contents] (#table-of-contents)
  - [Target Audience] (#target-audience)
- [User-Experience Design] (#)


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

**Milestone 4 - Additional Pages**

-As a site owner I want home page so that users can read about the website.

-As a developer I need to implement a 404 error page to notify users the page they requested could not be found.

-As a developer I need create a 403 error page to redirect unauthorized users to prevent them from accessing.

-As a developer I need to create a 500 error page so that users is notified when an internal server error has occurred.
 

**Milestone 5 - Deployment**

-As a developer I need to deploy the final project to Heroku so that users can visit the live site.


**Milestone 6 - Documentation**

-Create a readme and write documentation.
-Write testing documentation.

- Tasks -Complete readme documentation
- Complete testing documentation


## The-Scope-Plane

* Responsive Design - Site should be fully functional on all devices from 320px up
* Hamburger menu for mobile devices
* Ability to perform CRUD functionality
* Restricted role based features

## The-Structure-Plane


### Features

**Site Wide**

* Navigation Bar

  * Full responisve navigation bar including links to Home, reviews, adding review, sign up/in/out.
  * Makes the navigation between the pages easier for the user.

![Nav Bar]()

![Nav Bar responsive]()

![Dropdown]()

* Footer

   * Responisve footer soical media icons with links.

![Footer]()

![Responsive Footer]()

* Favicon

    * Site wide favicon included on all pages.
    * The image icon on the tab makes it easier for the user to find the site when having multiple tabs open at the same time. 

![Favicon]()

* 404 Page

   * A costum made 404 page will be displayed when a broken link is used to navigate.
   * It will allow the user to comfortably be redirected to the main website. 

![404 Page]()



### Features left to implement

- 
- 
- 


## Wireframes

**Landing page**

**Reviews page**

**Review detail page**

**Add review page**

**Edit review page**

**Sign up page**

**Log in page**

**Log out page**


### Database Design

- 

### Design Color Schemes

- 

## Technologies 

**Technologies Used**

  - 
  - 
  - 
  - 
  - 
  - 
  - 

**Python Modules**



**External Python Modules**


## Testing 

Test file

## Deployment

- Steps
Before deploying to Heroku

1. Add list of dependencies to the requirements.txt file
   - To create list use this command in terminal: 'pip3 > freeze requirements.txt' and the list will be added.
   - Commit and push

In Heroku

- In dashboard Click 'Create new app'
- Name app and choose region, click create
- Go to settings then to config vars
   
   
- Go to deploy and select github and confirm
- search for repository
- click on connect
- select a deployment method
- deploy!

## Credits

- 
- 
- 

[def]: https://carrevs-b0c8f9ee1e33.herokuapp.com/
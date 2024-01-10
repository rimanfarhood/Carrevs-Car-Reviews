# Testings

## Manual Testing

Test Description:

**Ensure a user can sign up to the website**

**Steps:**


1. Navigate to carrevs and click Sign up in the navbar menu

2. Enter email, username and password, you’ll have to confirm password again

3. Click Sign up


**Expected:**

-The user’s account is created and the user is logged in,  toast displaying a success message. 

**Result:**

-The user's account is created and the user is logged in,  toast displaying a success message.


---

Test Description:

**Ensure a user can log in**

**Steps:**

1. Navigate to Carrevs and click on the login in the navbar menu

2. enter email or username and password

3. Click login


**Expected:**

-User is successfully logged in and redirected to the home page,  toast displaying a success message.

**Result:**:

-User is successfully logged in and redirected to the home page,  toast displaying a success message. 

---

Test Description:

**Ensure a user can sign out**

**Steps:**

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page
**Expected:**

-User is logged out, toast displaying a success message 

**Result:**:

-User is logged out,  toast displaying a success message 

---

Test Description:

**Ensure a user can’t add a review if not logged in to the website**

**Steps:**

1. Navigate to carrevs and click Add Review in the navbar menu

**Expected:**

-The user is asked to sign in or create an account.

**Result:**:

-The user is asked to sign in or create an account.

---

Test Description:

**Ensure a user can add a review once logged in to the website**

**Steps:**

1. Log in if not logged in already or create account
2. Navigate to carrevs and click Add Review in the navbar menu
3. Fill in all the required fields in form
4. Click Add Review

**Expected:**

-The user's review is submitted successfully and the user is redirected to the home page where their review is displayed,  toast displaying success 
message.

**Result:**:

-The user's review is submitted successfully and the user is redirected to the home page where their review is displayed,  toast displaying success message.

---

Test Description:

**Ensure only logged in review owners can access editing their review.**

**Steps:**

1. Navigate to the reviews, select a review you have not created

**Expected:**

-Edit button is not being displayed.

**Result:**:

-Edit button is not being displayed.

---

Test Description:

**Ensure the logged in review owner can edit their review.**

**Steps:**

1. Log in or sign up.
2. Navigate to the reviews, select a review you have created or add review
3. Click on edit button
4. Change Car Make
5. Click on the Edit Review button

**Expected:**

-Review is successfully updated and toast is displaying a success message .

**Result:**

-Review is successfully updated and toast is displaying a success message.

---

Test Description:

**Ensure only the logged in review owner can delete their review.**

**Steps:**

1. If logged in, log out.
2. Navigate to the reviews, select a review you have created

**Expected:**

-Delete button is not being displayed.

**Result:**

-Delete button is not being displayed.

---

Test Description:

**Ensure the logged in review owner can delete their review.**

**Steps:**

1. Login or create an account
2. Navigate to your review in reviews or create one and view it.
3. Click the delete button
4. Click the confirm button on the delete page

**Expected:**

-Review successfully deleted and toast message displaying success.

**Result:**

-Review successfully deleted and toast message displaying success.

---


### Testing links

**Navbar menu Links**

Test Description:

**To ensure that all navigation links on respective pages navigate to the correct page as designed.**

**Steps**

**-By clicking on the navigation links on each page:**

 * Home --> index.html

 * Reviews --> reviews.html

 * Add Review (logged in user) --> add_review.html

 * Add Review (not logged in) --> allauth singup.html page

 * Sign Up --> allauth signup.html page

 * Log Out --> allauth logout.html page

 * Log In --> allauth login.html page

**Expected:**

-All navigation links directs to the correct pages.

**Result**

-All navigation links directed to the correct pages.


**Footer**

Test Description:

**Ensuring footer social media icon links works properly** 

**Steps** 

**-By clicking on each icon link:**

 * Youtube --> opens up youtube in new tab

 * Instagram  --> opens up Instagram in new tab

 * Twitter/X --> opens up Twitter/X in new tab

 * Facebook --> opens up Facebook in new tab

**Expected:**

-Links opens up in new tab directs to correct social media site

**Results**

-Links opens up in new tab directed to correct social media site

--- 

#### Negative Testing

Tests performed on Add Review ensures:

- That the form cannot be submitted when a required field is left blank.

- The value in the horsepower can not be submitted when too low or high and the user is informed if it is too low or high.

- No more than 15 characters in the Retail Price field, the reason for it being a charfield and not an integerfield is so that the user can specify the currency.


## Validators

**HTML W3C**

All pages were ran through the W3C HTML Validator. There were no errors on any page but there was a info messages on 
 about a trailing slash, it was some of the django elements I couldn't access in my files but it was just infos not errors.

![W3C-html](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/htmlw3c.png)



**CSS W3C**

CSS were ran through W3C CSS Validator without any remarks.

![W3C-css](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/cssw2c.png)

**JsHint**

JavaScript file was ran through the jshint, no error.

![jshint](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/jshint.png)


**PEP8**

All pages were ran through the Code Institutes Python linter to ensure all code was pep8 compliant, no errors was detected on any file. with the exception of the settings.py file.

Django's auto generated code for AUTH_PASSWORD_VALIDATORS were showing up as lines too long. I could not find a way to split the lines. Hopefully this is acceptable since they were auto generated and not my own custom code.

![pep8](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/pep8.png)

![pep8](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/pep8set.png)


**Wave**

Wave Accessibility testing were run on all pages with no warnings, just an alert that the home icon and the logo links go to the same URL.

![Wave](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/wave.png)


**Lighthouse**

Lighthouse testing was ran on all pages, I improved SEO by adding a meta description and keywords. I could use  'eliminate render-blocking resources' for better performance but I do not know how if there were more time i would try and fix it but it was not crucial and there were no time left.

![lighthouse](https://github.com/rimanfarhood/Carrevs-Car-Reviews/blob/main/docs/test/lighthouse.png)


## Bugs

There has been some issues with cloudinary images not loading, not sure how to fix it but it suggest it is a cloudinary cache issues that appears from time to time. There were some issues when deploying in the begging with the css not displaying and reading the static files, o whitenoise was installed to for the app to read files from the static folders.
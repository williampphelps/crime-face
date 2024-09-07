# Software Requirements Specification for CrimeFace

Version 1.0 approved

Prepared by Nathan S, William P, and Rylynn P
03/01/2024

## Revision History

- All Authors, 03/05/2024, Finalize Requirements Document, 1.0

# 1. Introduction

## 1.1 Purpose
This document specifies the software requirements for a criminal networking application named "CrimeFace". This document covers the initial release (v1.0) of the application.

## 1.2 Document Conventions

Requirements are denoted by "REQ-" followed by a unique identifier.\
Priorities are indicated in brackets following the requirement identifier (e.g., REQ-1 [High]).

## 1.3 Intended Audience and Reading Suggestions
This document is intended for developers, testers, and product managers involved in the development and testing of CrimeFace.

**Developers**: Use this document to understand the functionalities and technical requirements of CrimeFace.\
**Testers**: Use this document to design test cases that cover the specified requirements.\
**Product Managers**: Use this document to ensure the application aligns with product vision and user needs.\


It is recommended to read this document sequentially, starting with the introduction and proceeding through the detailed sections.

## 1.4 Product Scope
CrimeFace is a web application that enables users to send and receive encrypted text messages with self-destruct timers. Users can create individual or group chats, and messages disappear after a set time determined by the sender. The application prioritizes user privacy and security by employing Emoji encryption and not storing any user data or message content on its servers.

## 1.5 References
No References at this point

# 2. Overall Description

## 2.1 Product Perspective
CrimeFace is a new, self-contained web application. It does not integrate with any existing systems and functions independently.

## 2.2 Product Functions
 - Secure User Registration and Login (REQ-1 [High])
 - Secure Messaging (REQ-2 [High])
 - Individual and Group Chats (REQ-2.1 [High])
 - Emoji Encryption (REQ-2.2 [High])
 - Self-Destructing Messages (REQ-2.3 [Medium])
 - Disliked Post Leaderboard (REQ-3 [High])
 - Like/Dislike Buttons on Post (REQ-3.1 [Medium])
 - Contact Management (REQ-4 [Medium])
 - Add/Remove Contacts (REQ-4.1 [Medium])
 - Search Contacts (REQ-4.2 [Low])
 - User Settings (REQ-5 [Medium])
 - Manage Profile Information (REQ-5.1 [Medium])
 - Set Default Message Timer (REQ-5.2 [Low])
## 2.3 User Classes and Characteristics

**Primary Users**: Individuals seeking a secure platform for private communication.\
**Secondary Users**: Organizations or groups requiring temporary and confidential communication channels.

Both user classes are assumed to be comfortable with using web applications and possess basic technical literacy.

## 2.4 Operating Environment

**Web Browser**: Google Chrome, Safari, Microsoft Edge, and Firefox\
**Internet Connection**: Required for initial user registration and message delivery.\

## 2.5 Design and Implementation Constraints
Secure development practices to prevent vulnerabilities and data breaches.\
Third-party libraries for encryption functionalities should be open-source and well-maintained.

## 2.6 User Documentation
**User Guide**: Provides comprehensive instructions on using all application features.\
**FAQs**: Addresses common user questions and troubleshooting steps.\

Both documents will be available online.

## 2.7 Assumptions and Dependencies
Users have a basic understanding of secure communication practices.\
A reliable internet connection is available during initial registration and message sending/receiving.\
Third-party libraries used for encryption functions maintain their security and functionality throughout the application lifecycle.\

## 3. External Interface Requirements

### 3.1 User Interfaces
Each web page will be designed to try and make it easy for the user to navigate the site whether it's logging in or 
Sending another user a message we'll try and make it very easy on the users eyes. 
We'll also make sure to have logs of lot's of things to make trouble shooting a bit easier.

### 3.2 Hardware Interfaces
Devices that users will use will be phones as well as a desktop within a web browser for both.

### 3.3 Software Interfaces
Use easy db for the database for storing things like users, posts, and direct messages. Using Flask and html for the frontend and python for the backend. 

### 3.4 Communications Interfaces
Just connection to the flask server is needed. If it is hosted we'd use stuff like HTTP to add security.

## 4. System Features

This template illustrates organizing the functional requirements for the
product by system features, the major services provided by the product. You may
prefer to organize this section by use case, mode of operation, user class,
object class, functional hierarchy, or combinations of these, whatever makes the
most logical sense for your product.

You may modify the structure of this secture according to the software process
you are using for this project. For example, if you are using agile (or some of
its derivations) and you need to format the features in terms of user stories,
you may replace the format below with your own adaptation for each user story.

### 4.1 Have messages be deleted 24 hours after being viewed.


### 4.1.1 Description and Priority
This is a pretty high priority as it is one of the key functions of the app. After a user views an image it will date a time when the message was sent 
Whenever the message is loaded again it will check if it has been a day since and if it has delete it from the db.

### 4.1.2 Stimulus/Response Sequences
The user has to login, then add a user as a friend mutually, then after that send a message.

### 4.1.3 Functional Requirements
* User should be able to search for other users by their usernames (REQ-4.1.1).
* As they user types it should update with a list of users based off of the string within the text box(REQ-4.1.2).
* Have an email based two factor authentication for users logging in. 
* Force password complexity requirements .
* Securely store user passwords using a hashing algorithm.
* Be able to create an account with a email, username, and password. 
* User should be able to send messages securely to other users they're friends with.
* Users should be able to see message delievered status.
* Users should be able to block other users. 
* system will encrypt message content before transmission.
### 4.2 Have a leaderboard for top posts

### 4.2.1 Description and Priority 
On the main page have a leaderboard for users posts from highest to lowest within a week or day time span that the user can toggle between.

### 4.2.2 Stimulus/Response Sequences 
The user has to login, and then just view them on the main homepage.

### 4.2.3 Functional Requirements 
1. Implement the layout of the page.
2. Figure out how to tally the highest likes within a week timespan
3. Figure out how to do it for daily
4. Add a toggle for the uses to switch between the two``

## 5. Other Nonfunctional Requirements

### 5.1 Security Requirements

<p> Security is the foremost objective application as that is what is meant
to drive users to the application. This means that it needs to be extremely
secure and allow users to be protected.</p>

#### 5.1.1 User Encryption

1. Encrypt all passwords and usernames/email addresses in the database.
2. Encrypt all user information accept to those authorized to view said information.

#### 5.1.2 Post Encryption

1. Create a system for encrypting certain words into emojis.
2. Create a system to encrypt all other words in the post.
3. Lock post images behind encrypted links.

### 5.2 Performance Requirements

<p>User information will of course be accessed from a database. This means that algorithms are needed
to ensure the fluid access of said database. Since the main function of this application is security,
it is not necessary to make the application very quick. It simply needs to be quick enough to not cause
frustration when using the application. To achieve this it is imperative to:</p>

#### 5.2.1 Access of the Database

1. Create a database that is ordered in some manner so that it can be searched through quickly.
2. Load content in chunks so that a full screen of content can be loaded in 10 seconds or less.
3. Add users to the website in 25 seconds or less
4. Send messages and requests from one user to another in 15 seconds or less.

#### 5.2.2 Interaction with the website

<p>As is stated in the introduction to this section, it is not imperative to have a quick 
application. It just needs to be quick enough in order to avoid major frustrations. Posts 
should be easy to quickly create. This means that it should be intuitive to create a post 
and it should also take about 15 seconds at most for the user's post to be encrypted and 
posted.</p>

### 5.3 Safety Requirements

<p>When the word came down for this project, many of us were shocked. Top brass
said that collateral damage didn't matter as long as enough criminals were caught
by the software. This means that the safety requirements for our project are bit
different.<p>

#### 5.3.1 Data Collection

1. Avoid using any sort of automated data collection.
2. Create convincing accounts and gain trust of users.
3. Use these accounts to collect posts to tie users to crimes.

#### 5.3.2 Collateral Acceptance

1. Catch at least 5 leaders of criminal organizations.
2. Catch at least 200 criminals.

<p>Top brass said that as long as these requirements are met, any collateral or
negative public opinion will be overlooked when it comes time for promotions.</p>

### 5.4 Software Quality Attributes

<p>This software should look modern and like it was created by a competent team,
not Jack from Nation Ranch. Yes, he got our department great insurance rates, but
he can't design a website; the website we filled out our forms on looked as if it
was from the 90s. That's why we have to do better!</p>

#### 5.4.1 Appearance

1. Colorscheme should include no more than 5 colors.
2. Fonts should be sans-serif or other easy-to-read fonts.
3. Similar colors should be used between sections to bleed sections together.

#### 5.4.2 Portability

1. The application should be available on mobile devices
2. The application should fit entirely on the screen of a mobile device
3. This means the UI may need to be slightly different for mobile

### 5.5 Business Rules

<p>This operation may be running outside the rules, but it still has rules.</p>

#### 5.1.1 Security Clearance

1. Only the three assigned individuals can work on the project.
2. Only one other person can overview the project.
3. The members of the project cannot discuss the project until the completion of the operation.

#### 5.1.2 Roles for accessing the database.

1. Certain agents will be given CrimeFace accounts
2. The developers' accounts will be for updates on CrimeFace only

## 6. Other Requirements

<p>So far, a few things need to be considered with this project. The developers of the
project cannot, under any circumstances, involve themselves in the crimes within. The
agents tasked with creating undercover accounts can only do so if their cover is certain
to be blown by a lack of criminal particpation. All agents have signed waivers agreeing
that they will be 'charged' with crimes and shown in the news until this operation is over,
after which they will be released.</p>
<p>Jeffery found out about the project and said he will blow the whistle if we don't give
him a box of doughnuts every day. Therefore, we must have the intern buy a box every single
day. If Jeffery threatens to blow the whistle on this thing, give him whatever he wants
in order to prevent him doing so.</p>
<p>Our lawyers keep saying this is, "Unconstitutional", "A breach of the fourth amendment",
"Wrong on every level", and "Likely not legal under any circumstances." Don't listen to them
and just keep working until the project is finished.</p>

### FOURTH WALL BREAK

<p>Okay, so it should be said that we should take care not to make any posts for this project
go too far. It is important that if we allow people to create posts on our platform during testing,
we should remove any posts that go too far such as: insinuating that real life individuals are
comitting crime as even if its a joke it could lead to bad consequences, advocating for individuals
to commit crime, or discussing absolutely heinous crimes. We can decide these things on a
case-by-case basis.</p>

## Appendix A: Glossary
Tiny DB: Simple database model library used in python that uses json to store data.

## Appendix B: Analysis Models

<Optionally, include any pertinent analysis models, such as data flow diagrams,
class diagrams, state-transition diagrams, or entity-relationship diagrams.>

## Appendix C: To Be Determined List

So far none as of right now

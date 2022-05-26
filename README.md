# **NOTE**

### This project is unfortunately being submitted in an unfinished state and I wish to apologise for such.

#### The following README will reflect the unfinished nature of the project and will also discuss its envisaged features.

<hr>
<hr>


# blogsocial

Blogsocial is a reddit style social media/ news application where users can find a communities of like-minded people, create posts, interact with other users posts, discuss topics and explore other communities.

The main goal of blogsocial is to create an open discussion environment that encourages community engagement.

## Currently implimented features
<hr>

### Account registrtion, authorisation and login/logout

- In order to interect with and create posts, each user must be registered and authenticated. Users can easily create an account using the "Register" link in the nav bar. This will take the user to an account registration page. Each user must have a unique username (which is automatically checked and will inform the user if their chosen usernme is unavailable), and the email field is optional to afford users extra anonymity if they desire. The form has 2 password fields to perform a parity check and will inform the user if the 2 fields do not match. Once the account has been registered, the user is redirected to the homepage with confirmation that they have been successfully logged in as the appropiate user.

- If a user has already registered, they can login using the "Login" link in the nav bar. This will only show if the user is not currently logged in. Clicking the link will take the user to a seperate login page where they can enter their username and associated password to log in. Upon successful login, the user will be redirected to the homepage with a success messsage being displayed.

- If the user is logged in, they can logout by using the "logout" link in the nav bar. This will only be visible if the user is currently logged in. Clicking the link will direct the user to a confirmation page where they must confirm they wish to logout. If the user confirms the logout, they will be redirected to the homepage, but they will no longer be logged in. A successful logout message will appear and the links in the nav bar will revert to "register" and "login"

<hr>

### Home Page

- The current home page shows a list of all posts on the site, regardless of community. Posts are presented in a grid based view, soted by most recently created. Sorting by most recently created encourages users to interact with current events. This particular ordering also lends itself to creating a "news feed" where users can see the current discussion points in a community.

- Each post is contained in a card and displays the community the post was published in, the title of the post, the body content of the post along with an optionl image. Each card is then punctuated with the authors username, the date and time the post was created on, and a live counter for number of likes the post has.

- The feed of posts is paginated to allow for a digestable amount (12) of posts to be viewd on each page. Each row of "post cards" holds 3 posts and will create a new row for each multiple of 3 reached.

<hr>

### Post Detail view, commenting and liking

- Each post can be expanded into a full page detailed view. This view will also allow logged in users to like and comment on a post.

- If the user is logged in and viewing a post in the detailed view, they will be presented with a form below the post content where they can write and post a comment. The only field required here is the "body" content of the comment. The thumbs up button will also become interactive in this view if the user is logged in. They can click on the icon and it will update the liked status and like counter. The user can also unlike a post they have previously liked by simply hitting the same thumbs up icon.

- Eaach comment is posted with the comment body, the author of the comment and the time to comment was made. This will allow users to easily identify individuals in a conversation and confirm a timeline of the discussion.

- A list of comments will be displayed under the post, sorted by oldest comment first. This allows the user to read throught the comments as if it were a chronological conversation.

- A user who is not logged in will not be able to interact with or comment on a post.

<hr>

### Features left to Implement

    - User created posts.
    - Community pages.
    - Community following/ unfollowing.
    - Deleting/ editing comments.
    - View list of followed groups.
    - User profiles with list of posts and comments created by the user.
    - Custom homepage showing posts from only communities followed by the user.
    - Allow multiple media types in posts
    - Visual Overhaul


### Technology Used 

    - Source control: Github
    - Project management: Github issues, milestomes and projects
    - Languages used: HTML, CSS, Javascript, Python
    - Frameworks: Django, Bootstrap
    - Media host/ CDN: Cloudinary
    - Libraries:
        -django_allauth: For user registration and authorisation handling
        -crispy_forms: For formatted form rendering
        -django_summerote: For post editing in /admin/

        -Full list of dependencies can be found in the requirements.txt file
    - Deployment: Heroku
    - IDE: Gitpod (using CI Gitpod template)


## Known Bugs

- Due to an undiagnosed URL conflict, there is no current interactable link to a posts detailed view. This can be overridden by typing the posts slug onto the end of the 'home' url. Each posts slug is the title of the post with any spaces being replaced with '-'. For example, to visit the detail view of the Image Test post you would simply add "/image-test/" to the end of "https://blogsocial-ci-portfolio-4.herokuapp.com/". 

<hr>


## Testing

<hr>

- No tests were performed with the built in django test suite.

<hr>

## Deployment

<hr>

- The site was deployed using Heroku following the CI django deployment instructions.
- This project has been deployed with DEBUG = False.

- Steps I took to deploy this project on heroku.
  - To keep secret keys and API urls safe, all sensitive information is stored in an env.py file that ws added to the .gitignore file.
  - In heroku I added the heroku postgres resourse, this is the production server.
  - I added the contents of env.py into Herokus config vars as the environment varibles are kept secret from the deployed commit.
  - I used the Heroku CLI to create a remote git repository that automatically builds the site when the repo is pushed to the remote branch.

The live link can be found here: 

"https://blogsocial-ci-portfolio-4.herokuapp.com/"


## Credits 

<hr>

- Code Institute for the gitpod template
- Code Institute "I think therefore I blog" for the majority of the django specific code.
- Relevant Django documentation for bug fixes and futher information.
- Bootstrap documentation.

# CBUS 2018


## A cool new app for finding events you want to go to and posting events that others want to come to.

---

I remember my mom talking about how she started a community-based non-profit organization 
and the lengths she had to go to in building a network to support its programming and outreach. It seemed that 
finding people with similar interests to come to her events was much easier said than done.
Simply putting up a listing on the internet or sending a facebook blast would
not reach people in a timely manner. Her experience is echoed by other community based
 not for profits and neighborhood organizations in the Columbus area that do not have enough funding to support a marketing campaign for their programs and outreach. This was the inspiration behind our app.

Our app is a message board where aybody can post an event listing, and anybody can attend a posted event.
The app will then notice, **without ever storing anything on our servers**, what types of events you seem to enjoy, and show you more of those. We also go one step further by adding
more features that enhance the user's ability to remember events and communicate 
with event coordinators and fellow attendees as well as rate the credibility of another user. All communication will be secured so that a user's critical information is permanently
known to them only.

---

## Architecture:

### The Client, the app, the frontend

#### Establishing the User's preferences

Events presented to the user will have a simple "Like" and "Dislike" button, Reddit-style.
Liking an event gives +1 to every associated tag, disliking an event gives -1 to every associated tag.

On first run, the user will be presented with some sample tags, and asked to rank them.
These first rankings are used to quickstart the user's preference selection, without having to wait for the user to like/dislike certain events.

Tag rankings can be changed manually by the user at any time.

#### Fetching appropriate content:

Stores user preferences exclusively locally, never sent to our servers.
On refresh, queries the central server for a list of event listings matching the user's preferred tags.
Events are then ranked to the user based on how many tags they and the preference selection have in common as well as how many other people have listed themself as interested.

Example user preference sheet:

Topic | User-rating
--- | ---
Socialist Meet-and-Greets | +256
Bicycle Riding | +147
Cold-War Reenactments | +34
Nazi Party Rallies | -42
Competitive Pickle-eating | -74

This particular user would get recommended a lot of Socialist events, but would receive relatively few pickle-eating-related events.

#### Ranking the received events

The app would then query the server for a list of Socialist events, a list of bike events, and a list of Cold War events.
It would first try to find the intersection of all three categories, a socialist bike race based around the Cold War, and then rank other received events according to how much the user likes associated tags and how many liked tags they have.

The aforementioned socialist Cold War bike race would have a score of 437.
A Cold War themed bicycle shop would have a score of 181.
A Socialist pickle-eating competition would have score of 182. 

#### But wait! there's more!

Hitting a like button for a particular event doesn't just update your user preferences, 
the app will also store that event on its calendar locally on your device. When you start 
the app up, you will see a calendar with all your liked events displayed. If you're 
having second thoughts about going to a socialist pickle-eating competition, you can simply 
remove that event from your calendar. When an event you liked/saved is coming up in a few
days, the app will send you push notifications to your mobile device so you won't forget
to go to your favorite events. 

#### Now you take charge

##### The karma score

There is no dirth of trolls in our world and our app's rating system helps deal with these
hapless souls. Say you showed up to your socialist pickle-eating competition, only to find
your time wasted because it was fake. You can simply go back into the calendar, pull up
your already-happened events and report it for being a nonexistant event. The idiot user who
created this fake event will have this factored into their karma score - so that in the
future, this user's events will be ranked towards the bottom of the content anybody sees. 

##### The group chat

Say you're at an event and you have no idea what is going on. The app also will have a 
group chat function so that you can chat with other users who also are attendees. Say you 
are really lost - well you can also send a message to the user who posted this event 
listing. All messages will be screened for profanity to ensure approriate content is being
sent. 

##### You can also post your own event

Simply navigate to the "create an event" page and fill out information regarding to what
your event is about, a date and time, your contact information and some relevant tags.
Our app will check to make sure that there is no profanity in your listing, and then send
your listing to our server. **That is the beauty of our platform, users who have 
preferences towards the tags you specify in your event listing will find your event at 
the top of your feed. It is the ultimate win-win!**


### The Server, the backend

#### Stored data

Our server will contain a database with all the posted event listings from our users. 
As said before, the app will send the server the user's preferences and in return will get
back a queried list of relevant events. This opens up a window for targeted advertising, in this case we would query a separate list of ads based on their similarity to the given 
user's tag preference. **However, we will not keep a copy of the user's preferences/tag data on our servers. **Any information sent to us will be kept temporarily to query results - but as soon as the server has sent out the approriate data back to the user, that user's
preferences will be destroyed.

#### Secure communication

We understand that people's user preferences should be private to them, thus we will take 
all steps to ensure that data is sent securely. **All connection between the app and our AWS 
server will be SSL encrypted. The group chat function will also be encyrpted using an 
implementation of Signal, an Open Whisper Systems product.**

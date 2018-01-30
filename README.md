# cbus-2018


## A community message board except it also has a calendar and doesn't spy on you.

---

Ever wanted a publicly-accessible community message board?
Sure you do!
That's what this is, a message board where aybody can post an event listing, and anybody can attend a posted event.
The app will then notice, **without ever sending anything to our servers**, what types of events you seem to enjoy, and show you more of those.

Because that's what differentiates us from Facebook, **we don't track you**.
Seriously, you can take a look at the code if you want.

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
Competitive Baby-eating | -74

This particular user would get recommended a lot of Socialist events, but would receive relatively few baby-eating-related events.

#### Ranking the received events

The app would then query the server for a list of Socialist events, a list of bike events, and a list of Cold War events.
It would first try to find the intersection of all three categories, a socialist bike race based around the Cold War, and then rank other received events according to how much the user likes associated tags and how many liked tags they have.

The aforementioned socialist Cold War bike race would have a score of 437.
A Cold War themed bicycle shop would have a score of 181.
A Socialist baby-eating competition would have score of 182.

### The Server, the backend

#### Stored data

The events database, and the tag database.

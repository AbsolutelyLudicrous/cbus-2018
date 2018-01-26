# cbus-2018

## ~~Flaming GitHub Vibrators for Dogs!~~

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

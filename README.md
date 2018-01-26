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

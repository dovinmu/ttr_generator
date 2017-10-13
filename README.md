# Make your own Ticket To Ride game (and automate the boring parts)
[Ticket to Ride](https://www.daysofwonder.com/tickettoride/en/usa) is a game where you build train routes between points. It's a perennial favorite of mine, but sadly there are only so many different maps to play on. So I decided to make my own map of Seattle. If you want to do what I did, you'll still need to hand-draw the board, that's not automated (yet), and decide on the placement of markers. Below is what I did to make the first prototype.

## For the board:
First, I hand-drew vector graphics over a map of Seattle in Inkscape, adding in destinations, train boxes, and score track.

To make painting in the lines easier, I covered a flat piece of wood with painter's tape and laser-etched the design into it. Then I peeled out the painter's tape just for the shapes I want to color and filled them in with paint. This part takes a while. Eventually ended up with most of the board filled with paint.

## For the ticket cards:
I used Stamen Design's [watercolor maps](http://maps.stamen.com/#watercolor/) to render a map of Seattle to be more pleasing to the eye. The file TTR_cards_all_locations.svg contains a marker for every possible destination, with its name marked in the title. The file is also sectioned out with comments for splitting it up conveniently.

You can change the design in the master .svg and then run the script to generate, render, and lay out the cards into 8.5 x 11 printable pdfs:

    bash make_cards.sh

Here's an image of a prototype of the card (there's still a bit of polishing left to do on the edges):

![Ballard-Georgetown](Ballard-Georgetown.png)

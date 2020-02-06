# swaytools
Collection of simple tools for sway (and i3)

## Available tools

*swayinfo*: Tool similar to xprop that lets you click on a window, and prints info on that window (retrieved from sway's tree).

*winfocus*: Program that uses dmenu/bemenu or similar to let you select a window from a menu and focuses that window.

## Dependencies

Required:

  * python
  * sway (or i3, though that isn't tested)

Optional:
  * slurp: for selecting the window with swayinfo
  * bemenu, dmenu or other dmenu compatible program: needed for winfocus


## Environment Variables

*DMENU_CMD*: A dmenu compatible command to use for menu selection. Used by `winfocus`

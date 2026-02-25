## Change It

> 📹 **Watch:** Keeping the Player on Screen
> *Record in Screencastify — show wrapping vs. stopping vs. bouncing approaches*
> *Objective: I can write boundary logic so my sprite doesn't disappear off the edge.*
> **[ADD VIDEO URL WHEN RECORDED]**

---

Don't worry — you can't break anything permanently! Experiment freely.

## 1: Complete the Missing Directions

Find the two `# TODO` lines in `move.py`. Add movement for the other arrow keys. Run the game and test each direction.

## 2: Change the Speed

Find the number `4` in each movement line. Try changing it to `2`, `8`, or `12`. How does it feel at each speed?

## 3: Add a Boundary

Right now the player can walk off the screen. Add code after the movement block to keep the player on screen. Try one of these approaches:

- **Stop at the edge:** `if player.x < 0: player.x = 0`
- **Wrap around:** `if player.x < 0: player.x = WIDTH`

What's the difference between stopping and wrapping? Which feels better for your game?

## 4: Add a Second Actor

Try adding an alien that starts at position `(100, 100)`. Don't forget to draw it in `draw()`!

---

> *[TODO: insert free-text-auto assessment — "What did you change in move.py? Describe one thing you tried and what happened."]*

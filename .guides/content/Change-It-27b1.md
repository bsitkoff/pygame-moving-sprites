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

Find the number `5` in each movement line. Try changing it to `2`, `8`, or `12`. How does it feel at each speed?

## 3: Complete the Boundary Logic

`move.py` already wraps the player left and right. Look at that code — then add the same wrapping for up and down. The `# TODO` comment shows you where.

- If `player.y` goes below `0`, wrap to `HEIGHT`
- If `player.y` goes above `HEIGHT`, wrap to `0`

You could also try **stopping** instead of wrapping: `if player.y < 0: player.y = 0`. What's the difference? Which feels better for your game?

## 4: Experiment in tryit.py

Open `tryit.py` — that's your blank canvas. Try a different boundary style than the one in `move.py`. Can you make your player stop at the edges instead of wrapping, or bounce?

---

> *[TODO: insert free-text-auto assessment — "What did you change in move.py? Describe one thing you tried and what happened."]*

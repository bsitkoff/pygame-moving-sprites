## Change It

<iframe width="720" height="600"
  src="https://app.screencastify.com/watch/slxa5wJvH51XrZQeYxra/embed"
  title="Handling Player Movement at Screen Edges in Games"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
  referrerpolicy="strict-origin-when-cross-origin"
  allowfullscreen
></iframe>
  
---

## 1: Finish the movement code

Find the `# TODO` line in `move.py` that says `add keyboard.left, keyboard.up, keyboard.down`. Add those three movement lines. Run the game and test each direction.

## 2: Change the Speed

Find the number `5` in each movement line. Try changing it to `2`, `8`, or `12`. How does it feel at each speed?

## 3: Complete the Boundary Logic

`move.py` already wraps the player left and right. Look at that code — then add the same wrapping for up and down. The `# TODO` comment shows you where.

- If `player.y` goes below `0`, wrap to `HEIGHT`
- If `player.y` goes above `HEIGHT`, wrap to `0`

You should also try **stopping** instead of wrapping: `if player.y < 0: player.y = 0`. 

{Check It!|assessment}(free-text-auto-1268512576)





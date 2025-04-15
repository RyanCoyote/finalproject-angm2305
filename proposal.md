# Title
Bullet Heaven
## Repository
<Link to your project's public GitHub respository>
https://github.com/RyanCoyote/finalproject-angm2305.git

## Description
This will be a simple 'bullet hell' style game in which you control a simple sphere hitbox via mouse and/or keyboard and attempt to dodge a variety of shapes moving down the screen.

## Features
- Player Control
	- A sphere will be assigned for a player hitbox and constantly be moved to the player's mouse.
- Moving Projectiles & Patterns
	- Moving squares will move down the screen in a geometric pattern, in various forms and ways depending on the attack being sent toward the player.
- Hit Registration & HP
	- If any projectile shapes overlap the player, they will lose a health point and hitstun will occur.

## Challenges
- How to register when one drawn shape overlaps another drawn shape for the purposes of registering the player being hit.
- Ensuring clean control of the player character via mouse tracking.
- HP Point tracking system
- Different ways to systematically move patterns of shapes in both a downward and diagonal fashion down the screen (similar but more complex than the digital rain program)

## Outcomes
Ideal Outcome:
- An ideal outcome would be for this program to have sprites for a player character, an enemy character, and at least 3 different attack patterns for the player to dodge.
- The player character could be controlled by following the player's mouse OR using arrow keys, with a button enabling/disabling slow player movement.
- If there is time after the bullet hell system is coded, a simple attacking system can be added for the player to shoot projectiles at a static enemy sprite.

Minimal Viable Outcome:
- The minimum outcome would be for squares to be moving down the screen in a set pattern constantly.
- The player character circle follows the player's mouse on the screen.
- When the player circle overlaps a projectile square, the circle will flash for a second to register that it has been hit.

## Milestones

- Week 1
  1. Create program that has a player character circle follow the mouse's movement during the program runtime.
  2. Begin coding program that allows creation of moving projectile patterns down the screen.

- Week 2
  1. Finish moving projectile program and add different projectile patterns to the program.
  2. Add hit registration and HP system for whenever player character overlaps projectiles.

- Week N (Final)
  1. Ensure player character has hitstun effects.
  2. If time allows, add sprites for player characters, projectiles, background, and enemy character.
  3. If time allows, add system for player to spawn projectiles that move forward toward the enemy, and decrease its HP on contact before disappearing.

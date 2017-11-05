# Turtle

Ever wondered who the fastest turtle is?  Well, wonder no more...

## How the game works out the winner

A turtle has 100 points of energy.

A turtle with a speed of 10 covers 1 metre / minute.

A turtle with a speed of 1 covers 10cm / minute.

A turtle with a stamina of 10 loses 10 energy points / metre.

A turtle with a stamina of 1 loses 19 energy points / metre (10 + (10 - 1)).

For each loss of 20 energy points, the turtle's speed decreases by 1 until speed is 0.1m.

If a turtle reaches 0 energy, it does not finish.

### Worked example 1: Turtle has speed of 4 and stamina of 5 and runs a race of 6 metres

After 1 metre:
    * Speed is 0.1 * 4 = 0.4m/minute
    * Covered in (1m / 0.4m) * 60s = 150s
    * Total time = 150s
    * Has 100 - 15 (=10+10-5) = 85 energy points left
    * Speed remains at 4

After 2 metres:
    * Speed is 0.1 * 4 = 0.4m/minute
    * Covered in (1m / 0.4m) * 60s = 150s
    * Total time = 300s
    * Has 85 - 15 = 70 energy points left
    * Speed drops to 3

After 3 metres:
    * Speed is 0.1 * 3 = 0.3m/minute
    * Covered in (1m / 0.3m) * 60s = 200s
    * Total time = 500s
    * Has 70 - 15 = 55 energy points left
    * Speed drops to 2

After 4 metres:
    * Speed is 0.1 * 2 = 0.2m/minute
    * Covered in (1m / 0.2m) * 60s = 300s
    * Total time = 800s
    * Has 55 - 15 = 40 energy points left
    * Speed remains at 2

After 5 metres:
    * Speed is 0.1 * 2 = 0.2m/minute
    * Covered in (1m / 0.2m) * 60s = 300s
    * Total time = 1100s
    * Has 40 - 15 = 25 energy points left
    * Speed drops to 1

After 6 metres:
    * Speed is 0.1 * 1 = 0.1/minute
    * Covered in (1m / 0.1) * 60s = 600s
    * Total time = 1700s
    * Has 25 - 15 = 10 energy points left

### Worked example 2: Turtle has speed of 7 and stamina of 8 and runs a race of 6 metres

After 1 metre:
    * Speed is 0.1 * 7 = 0.7m/minute
    * Covered in (1m / 0.7m) * 60s = 86s
    * Total time = 86s
    * Has 100 - (10 + 10 - 8) = 88 energy points left
    * Speed remains at 7

After 2 metres:
    * Speed is 0.1 * 7 = 0.7m/minute
    * Covered in (1m / 0.7m) * 60s = 86s
    * Total time = 172s
    * Has 88 - 12 = 76 energy points left
    * Speed drops to 6

After 3 metres:
    * Speed is 0.1 * 6 = 0.6m/minute
    * Covered in (1m / 0.6m) * 60s = 100s
    * Total time = 272s
    * Has 76 - 12 = 64 energy points left
    * Speed remains at 6

After 4 metres:
    * Speed is 0.1 * 6 = 0.6m/minute
    * Covered in (1m / 0.6m) * 60s = 100s
    * Total time = 372s
    * Has 64 - 12 = 52 energy points left
    * Speed drops to 5

After 5 metres:
    * Speed is 0.1 * 5 = 0.5m/minute
    * Covered in (1m / 0.5m) * 60s = 120s
    * Total time = 492s
    * Has 52 - 12 = 42 energy points left
    * Speed remains at 5

After 6 metres:
    * Speed is 0.1 * 5 = 0.5m/minute
    * Covered in (1m / 0.5m) * 60s = 120s
    * Total time = 612s
    * Has 42 - 12 = 30 energy points left

### Worked example 2: Turtle has speed of 1 and stamina of 1 and runs a race of 6 metres

After 1 metre:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 600s
    * Has 100 - (10 + 10 - 1) = 81 energy points left
    * Speed remains at 1

After 2 metres:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 1200s
    * Has 81 - 19 = 62 energy points left
    * Speed remains at 1 (should drop, but can't possibly go slower)

After 3 metres:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 1800s
    * Has 62 - 19 = 43 energy points left
    * Speed remains at 1

After 4 metres:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 2400s
    * Has 43 - 19 = 24 energy points left
    * Speed remains at 1

After 5 metres:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 3000s
    * Has 24 - 19 = 5 energy points left
    * Speed remains at 1

After 5 metres:
    * Speed is 0.1 * 1 = 0.1m/minute
    * Covered in (1m / 0.1m) * 60s = 600s
    * Total time = 3600s
    * Has 5 - 19 = -14 energy points left
    * Knackered...
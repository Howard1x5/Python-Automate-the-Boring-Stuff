import zombiedice
import random

class RandomDecisionZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            if random.choice([True, False]):  # Randomly decide to roll or stop
                diceRollResults = zombiedice.roll()
            else:
                break

class StopAtTwoBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class StopAtTwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class VariableRollsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        rolls = random.randint(1, 4)  # Decide to roll 1 to 4 times
        shotguns = 0
        for _ in range(rolls):
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                break
            shotguns += diceRollResults['shotgun']
            if shotguns >= 2:
                break  # Stop early if 2 shotguns are rolled

class MoreShotgunsThanBrainsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns > brains:
                break  # Stop if more shotguns than brains
            diceRollResults = zombiedice.roll()

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    RandomDecisionZombie(name='Random Decision'),
    StopAtTwoBrainsZombie(name='Stop at 2 Brains'),
    StopAtTwoShotgunsZombie(name='Stop at 2 Shotguns'),
    VariableRollsZombie(name='Variable Rolls'),
    MoreShotgunsThanBrainsZombie(name='More Shotguns than Brains'),
)

# Uncomment one of these lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

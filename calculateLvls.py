# TODO: LETS GO! IT WORKS! BOOYA!
def calculateLvls(self):
    # Get current level, XP, TP, and Hero Points
    cur_lvl = self.lvlSPN.value()
    xp_value = self.xpSPN.value()
    tp_value = self.tpSPN.value()
    hero_points = self.heroPtsSPN.value()

    if xp_value == None:
        xp_value = 0

    # Keep track of levels gained during this calculation
    initial_level = cur_lvl

    # Calculate the XP needed to reach the next level
    xp_needed = (cur_lvl + 1) * 100

    # Calculate how many levels can be gained from the current XP
    levels_gained = xp_value // xp_needed

    # Increment the level one at a time based on the levels gained
    for _ in range(levels_gained):
        # Award 2 TP for each level gained
        tp_value += 2

        # Award 1 Hero Point for every 3 levels
        if (cur_lvl + 1) % 3 == 0:
            hero_points += 1

        # Increment the level and reset XP
        cur_lvl += 1
        xp_value -= xp_needed

        # Calculate XP needed for the next level
        xp_needed = (cur_lvl + 1) * 100

        # If XP reaches or exceeds 100, reset to 0 and increment the level
        if xp_value >= xp_needed:
            cur_lvl += 1
            xp_value = 0

    # Update values in the respective boxes
    self.lvlSPN.setValue(cur_lvl)
    self.xpSPN.setValue(xp_value)
    self.tpSPN.setValue(tp_value)
    self.heroPtsSPN.setValue(hero_points)


def calculateBasedEvents(self, newlvl):
    cur_lvl = self.lvlSPN.value()

    heropts = 0

    # Get the initial level before changes
    initial_level = self.lvlSPN.value()

    # Update training points (2 for each level gained)
    new_tp_value = self.tpSPN.value() + 2

    # Update hero points (1 every third level)
    if cur_lvl % 3 == 0:
        heropts += 1
        new_hero_points = self.heroPtsSPN.value() + heropts
    else:
        new_hero_points = self.heroPtsSPN.value()

    # Set the new values
    self.tpSPN.setValue(new_tp_value)
    self.heroPtsSPN.setValue(new_hero_points)
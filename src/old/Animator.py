#TODO Actually fix this class
class Animator(object):


    def __init__(self):
        pass
        # self.setupSprites()
        # self.checkAnim(object)

    #Create sprites from class
    # def setupSprites(self):
    #     self.sprites = Sprite().build_spriteset()

    #
    # #Check which anim to play
    # def checkAnim(self, object):
    #     if object == 'left':
    #         positionX = self.walkLeft()
    #         return positionX
    #     elif object == 'right':
    #         positionX = self.walkRight()
    #         return positionX
    #     elif object == 'idle':
    #         positionX = self.idle()
    #         return positionX
    #     elif object == 'kick':
    #         positionX = self.selfKick()
    #         return positionX

    #
    # # Performs kick animation
    # # Returns our kickmove, which is currently just zero
    # def selfKick(self):
    #     self.sprite = itertools.cycle(self.sprites['kick'])
    #     return constants.KICKMOVE
    #
    # # Performs walk left animation
    # # Returns negated MSPEED, which is a positive 9
    # # This was the initial movement value, now contained in a variable
    # def walkLeft(self):
    #     self.sprite = itertools.cycle(self.sprites['walking'])
    #     return -Config.MSPEED
    #
    # # Performs walk left animation
    # # Returns MSPEED, which is a positive 9
    # # This was the initial movement value, now contained in a variable
    # def walkRight(self):
    #     self.sprite = itertools.cycle(self.sprites['walking'])
    #     return Config.MSPEED
    #
    # # Performs idle animation
    # # Returns IDLEMOVE, which is zero
    # # Unless you can magically move while being idle
    # def idle(self):
    #     self.sprite = itertools.cycle(self.sprites['idle'])
    #     return self.sprite
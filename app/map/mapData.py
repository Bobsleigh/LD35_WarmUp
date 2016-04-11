import pyscroll
import pytmx
import re

from app.enemy.enemyFactory import EnemyFactory
from app.powerup.powerUpFactory import PowerUpFactory
from app.sound.soundPlayerController import *
from app.player import *

class MapData:
    def __init__(self, mapName="Map_01", screenSize=(SCREEN_WIDTH, SCREEN_HEIGHT)):

        self.nameMap = mapName

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.mapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.mapData, screenSize, clamp_camera=True)
        self.soundController = soundPlayerController()

        self.allSprites = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.powerUpGroup = pygame.sprite.Group()
        self.friendlyBullet = pygame.sprite.Group()
        self.enemyBullet = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()

        eFactory = EnemyFactory()
        pUpFactory = PowerUpFactory()

        for object in self.tmxData.objects:
            if object.type == "enemy":
                enemy = eFactory.create(object, self)
                self.allSprites.add(enemy)
                self.enemyGroup.add(enemy)

            if object.type == "powerUp":
                powerUp = pUpFactory.create(object)
                self.allSprites.add(powerUp)
                self.powerUpGroup.add(powerUp)

        # TODO: Put camera in mapData
        self.camera = pyscroll.PyscrollGroup(map_layer=self.cameraPlayer, default_layer=SPRITE_LAYER)
        self.camera.add(self.allSprites)

    # Map names are "Map_XX" where XX is the number 01 to 99
    # Tiled names are "theme_vX.tmx" where X is the number 1 to 99
    def reqImageName(self, nameMap):

        numberOfTheMap = int((re.findall("\d+", nameMap))[0])
        return os.path.join('tiles', "theme_v" + str(numberOfTheMap) + ".tmx")

    def reqNameAndPositionNewMap(self, out_zone, player):

        if self.nameMap == "Map_01":
            if out_zone == 'out_zone_1':
                return "Map_02", 70, player.rect.y
            if out_zone == 'out_zone_2':
                return "Map_05", player.rect.x + 32*26, 454
            if out_zone == 'out_zone_3':
                return "Map_03", 600, 450

        if self.nameMap == "Map_02":
            if out_zone == 'out_zone_1':
                return "Map_01", 900, player.rect.y
            if out_zone == 'out_zone_2':
                return "Map_07", 65, player.rect.y + 6*32
            if out_zone == 'out_zone_3':
                return "Map_04", player.rect.x - 416, 70
            if out_zone == 'out_zone_4':
                return "Map_06", 600, 450

        if self.nameMap == "Map_03":
            if out_zone == 'out_zone_1':
                return "Map_01", 600, 70

        if self.nameMap == "Map_04":
            if out_zone == 'out_zone_1':
                return "Map_02", player.rect.x + 416, 474

        if self.nameMap == "Map_05":
            if out_zone == 'out_zone_1':
                return "Map_01", player.rect.x - 32*26, 65

        if self.nameMap == "Map_06":
            if out_zone == 'out_zone_1':
                return "Map_02", 600, 70

        if self.nameMap == "Map_07":
            if out_zone == 'out_zone_1':
                return "Map_02", 900, player.rect.y - 6*32
            if out_zone == 'out_zone_2':
                return "Map_08", 70, player.rect.y - 18*32

        if self.nameMap == "Map_08":
            if out_zone == 'out_zone_1':
                return "Map_07", 900, player.rect.y + 18*32
            if out_zone == 'out_zone_2':
                return "Map_09", 70, player.rect.y - 30*32

        if self.nameMap == "Map_09":
            if out_zone == 'out_zone_1':
                return "Map_08", 17*32-6, player.rect.y + 30*32
            if out_zone == 'out_zone_2':
                return "Map_10", 70, player.rect.y + 5*32

        if self.nameMap == "Map_10":
            if out_zone == 'out_zone_1':
                return "Map_09", 29*32-6, player.rect.y - 5*32
            if out_zone == 'out_zone_2':
                return "Map_11", 70, player.rect.y

        if self.nameMap == "Map_11":
            if out_zone == 'out_zone_1':
                return "Map_10", 29*32-6, player.rect.y
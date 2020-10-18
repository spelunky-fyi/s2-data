from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import IntFlag, IntEnum
import typing

class Type(ABC):
    @property
    @abstractmethod
    def size(self):
        raise NotImplementedError()

    @abstractmethod
    def from_binary(self, binary):
        raise NotImplementedError()

    @abstractmethod
    def to_binary(self, binary):
        raise NotImplementedError()

class BoolType(Type):
    @property
    def size(self):
        return 1

    def from_binary(self, binary):
        return binary[0] != 0

    def to_binary(self, value):
        return bytes([1 if value != 0 else 0])

class Int32Type(Type):
    @property
    def size(self):
        return 4

    def from_binary(self, binary):
        return int.from_bytes(binary, byteorder='little', signed=True)

    def to_binary(self, value):
        return value.to_bytes(lenth=self.size, byteorder='little', signed=True)

class Int64Type(Type):
    @property
    def size(self):
        return 8

    def from_binary(self, binary):
        return int.from_bytes(binary, byteorder='little', signed=True)

    def to_binary(self, value):
        return value.to_bytes(lenth=self.size, byteorder='little', signed=True)

class ByteType(Type):
    @property
    def size(self):
        return 1

    def from_binary(self, binary):
        return binary[0]

    def to_binary(self, value):
        return bytes([value])

class FlagType(Type):
    _size = None
    flag_definition = None

    def __init__(self, size, flag_definition):
        self._size = size
        self.flag_definition = flag_definition

    @property
    def size(self):
        return self._size

    def from_binary(self, binary):
        return self.flag_definition(int.from_bytes(binary, byteorder='little'))

    def to_binary(self, value):
        return value.to_bytes(length=self.size, byteorder='little')

class EnumType(Type):
    _size = None
    enum_definition = None

    def __init__(self, size, enum_definition):
        self._size = size
        self.enum_definition = enum_definition

    @property
    def size(self):
        return self._size

    def from_binary(self, binary):
        return self.enum_definition(int.from_bytes(binary, byteorder = 'little'))

    def to_binary(self, value):
        return value.to_bytes(lenth = self.size, byteorder = 'little')

class CharacterUnlockFlags(IntFlag):
    Ana        = 0x1
    Margaret   = 0x2
    Colin      = 0x4
    Roffy      = 0x8
    Alto       = 0x10
    Liz        = 0x20
    Nekka      = 0x40
    LISE       = 0x80
    Coco       = 0x100
    Manfred    = 0x200
    Jay        = 0x400
    Tina       = 0x800
    Valerie    = 0x1000
    Au         = 0x2000
    Demi       = 0x4000
    Pilot      = 0x8000
    Airyn      = 0x10000
    Dirk       = 0x20000
    Guy        = 0x40000
    ClassicGuy = 0x80000

class ShortcutProgressEnum(IntEnum):
    NotMet = 0x0
    Met = 0x1
    S1d4Gave2000 = 0x2
    S1d4GaveBomb = 0x3
    S1d4Gave10000 = 0x4
    S3d1GaveRope = 0x5
    S3d1GaveWeapon = 0x6
    S3d1GaveMount = 0x7
    S5d1Gave50000 = 0x8
    S5d1GaveHiredHand = 0x9
    S5d1GaveGoldenKey = 0xa

@dataclass(frozen = True)
class FieldDescriptor:
    offset: int
    name: str
    type: Type

@dataclass(frozen = True)
class Category:
    name: str
    fields: typing.Mapping[str, FieldDescriptor]

# The dictionary keys are meant to stay consistent so that programs that use
# those keys don't break. The names in the descriptors/category can change.

field_descriptors = {
    'magic_numbers': Category('Magic Numbers', {
        'magic_num1': FieldDescriptor(0x0, 'Magic number 1', ByteType()),
        'magic_num2': FieldDescriptor(0x1, 'Magic number 2', ByteType()),
    }),
    'places_discovered': Category('Journal: Places Discovered', {
        'dwelling':         FieldDescriptor(0x02, "Dwelling",          BoolType()),
        'jungle':           FieldDescriptor(0x03, "Jungle",            BoolType()),
        'volcana':          FieldDescriptor(0x04, "Volcana",           BoolType()),
        'olmec_lair':       FieldDescriptor(0x05, "Olmec's Lair",      BoolType()),
        'tide_pool':        FieldDescriptor(0x06, "Tide Pool",         BoolType()),
        'abzu':             FieldDescriptor(0x07, "Abzu",              BoolType()),
        'temple_of_anubis': FieldDescriptor(0x08, "Temple of Anubis",  BoolType()),
        'the_city_of_gold': FieldDescriptor(0x09, "The City of Gold",  BoolType()),
        'duat':             FieldDescriptor(0x0a, "Duat",              BoolType()),
        'ice_caves':        FieldDescriptor(0x0b, "Ice Caves",         BoolType()),
        'neo_babylon':      FieldDescriptor(0x0c, "Neo Babylon",       BoolType()),
        'tiamat_throne':    FieldDescriptor(0x0d, "Tiamat's Throne",   BoolType()),
        'sunken_city':      FieldDescriptor(0x0e, "Sunken City",       BoolType()),
        'eggplant_world':   FieldDescriptor(0x0f, "Eggplant World",    BoolType()),
        'hundun_hideaway':  FieldDescriptor(0x10, "Hundun's Hideaway", BoolType()),
        'cosmic_ocean':     FieldDescriptor(0x11, "Cosmic Ocean",      BoolType()),
    }),
    'bestiary_discovered': Category('Journal: Bestiary Discovered', {
        'snake':             FieldDescriptor(0x12, "Snake",             BoolType()),
        'spider':            FieldDescriptor(0x13, "Spider",            BoolType()),
        'bat':               FieldDescriptor(0x14, "Bat",               BoolType()),
        'caveman':           FieldDescriptor(0x15, "Caveman",           BoolType()),
        'skeleton':          FieldDescriptor(0x16, "Skeleton",          BoolType()),
        'horned_lizard':     FieldDescriptor(0x17, "Horned Lizard",     BoolType()),
        'moles':             FieldDescriptor(0x18, "Moles",             BoolType()),
        'quillback':         FieldDescriptor(0x19, "Quillback",         BoolType()),
        'mantrap':           FieldDescriptor(0x1a, "Mantrap",           BoolType()),
        'tiki_man':          FieldDescriptor(0x1b, "Tiki Man",          BoolType()),
        'witch_doctor':      FieldDescriptor(0x1c, "Witch Doctor",      BoolType()),
        'mosquito':          FieldDescriptor(0x1d, "Mosquito",          BoolType()),
        'monkey':            FieldDescriptor(0x1e, "Monkey",            BoolType()),
        'hang_spider':       FieldDescriptor(0x1f, "Hang Spider",       BoolType()),
        'giant_spider':      FieldDescriptor(0x20, "Giant Spider",      BoolType()),
        'magmar':            FieldDescriptor(0x21, "Magmar",            BoolType()),
        'robot':             FieldDescriptor(0x22, "Robot",             BoolType()),
        'fire_bug':          FieldDescriptor(0x23, "Fire Bug",          BoolType()),
        'imp':               FieldDescriptor(0x24, "Imp",               BoolType()),
        'lavamander':        FieldDescriptor(0x25, "Lavamander",        BoolType()),
        'vampire':           FieldDescriptor(0x26, "Vampire",           BoolType()),
        'vlad':              FieldDescriptor(0x27, "Vlad",              BoolType()),
        'olmec':             FieldDescriptor(0x28, "Olmec",             BoolType()),
        'jiangshi':          FieldDescriptor(0x29, "Jiangshi",          BoolType()),
        'jiangshi_assassin': FieldDescriptor(0x2a, "Jiangshi Assassin", BoolType()),
        'flying_fish':       FieldDescriptor(0x2b, "Flying Fish",       BoolType()),
        'octopy':            FieldDescriptor(0x2c, "Octopy",            BoolType()),
        'hermit_crab':       FieldDescriptor(0x2d, "Hermit Crab",       BoolType()),
        'pangxie':           FieldDescriptor(0x2e, "Pangxie",           BoolType()),
        'great_humphead':    FieldDescriptor(0x2f, "Great Humphead",    BoolType()),
        'kingu':             FieldDescriptor(0x30, "Kingu",             BoolType()),
        'crocman':           FieldDescriptor(0x31, "Crocman",           BoolType()),
        'cobra':             FieldDescriptor(0x32, "Cobra",             BoolType()),
        'mummy':             FieldDescriptor(0x33, "Mummy",             BoolType()),
        'sorceress':         FieldDescriptor(0x34, "Sorceress",         BoolType()),
        'cat_mummy':         FieldDescriptor(0x35, "Cat Mummy",         BoolType()),
        'necromancer':       FieldDescriptor(0x36, "Necromancer",       BoolType()),
        'anubis':            FieldDescriptor(0x37, "Anubis",            BoolType()),
        'ammit':             FieldDescriptor(0x38, "Ammit",             BoolType()),
        'apep':              FieldDescriptor(0x39, "Apep",              BoolType()),
        'anubis_ii':         FieldDescriptor(0x3a, "Anubis II",         BoolType()),
        'osiris':            FieldDescriptor(0x3b, "Osiris",            BoolType()),
        'ufo':               FieldDescriptor(0x3c, "Ufo",               BoolType()),
        'alien':             FieldDescriptor(0x3d, "Alien",             BoolType()),
        'yeti':              FieldDescriptor(0x3e, "Yeti",              BoolType()),
        'yeti_king':         FieldDescriptor(0x3f, "Yeti King",         BoolType()),
        'yeti_queen':        FieldDescriptor(0x40, "Yeti Queen",        BoolType()),
        'lahamu':            FieldDescriptor(0x41, "Lahamu",            BoolType()),
        'proto_shopkeeper':  FieldDescriptor(0x42, "Proto Shopkeeper",  BoolType()),
        'olmite':            FieldDescriptor(0x43, "Olmite",            BoolType()),
        'lamassu':           FieldDescriptor(0x44, "Lamassu",           BoolType()),
        'tiamat':            FieldDescriptor(0x45, "Tiamat",            BoolType()),
        'tadpole':           FieldDescriptor(0x46, "Tadpole",           BoolType()),
        'frog':              FieldDescriptor(0x47, "Frog",              BoolType()),
        'fire_frog':         FieldDescriptor(0x48, "Fire Frog",         BoolType()),
        'goliath_frog':      FieldDescriptor(0x49, "Goliath Frog",      BoolType()),
        'grub':              FieldDescriptor(0x4a, "Grub",              BoolType()),
        'giant_fly':         FieldDescriptor(0x4b, "Giant Fly",         BoolType()),
        'hundun':            FieldDescriptor(0x4c, "Hundun",            BoolType()),
        'eggplant_minister': FieldDescriptor(0x4d, "Eggplant Minister", BoolType()),
        'eggplup':           FieldDescriptor(0x4e, "Eggplup",           BoolType()),
        'celestial_jelly':   FieldDescriptor(0x4f, "Celestial Jelly",   BoolType()),
        'scorpion':          FieldDescriptor(0x50, "Scorpion",          BoolType()),
        'bee':               FieldDescriptor(0x51, "Bee",               BoolType()),
        'queen_bee':         FieldDescriptor(0x52, "Queen Bee",         BoolType()),
        'scarab':            FieldDescriptor(0x53, "Scarab",            BoolType()),
        'golden_monkey':     FieldDescriptor(0x54, "Golden Monkey",     BoolType()),
        'leprechaun':        FieldDescriptor(0x55, "Leprechaun",        BoolType()),
        'monty':             FieldDescriptor(0x56, "Monty",             BoolType()),
        'percy':             FieldDescriptor(0x57, "Percy",             BoolType()),
        'poochi':            FieldDescriptor(0x58, "Poochi",            BoolType()),
        'ghist':             FieldDescriptor(0x59, "Ghist",             BoolType()),
        'ghost':             FieldDescriptor(0x5a, "Ghost",             BoolType()),
        'cave_turkey':       FieldDescriptor(0x5b, "Cave Turkey",       BoolType()),
        'rock_dog':          FieldDescriptor(0x5c, "Rock Dog",          BoolType()),
        'axolotl':           FieldDescriptor(0x5d, "Axolotl",           BoolType()),
        'qilin':             FieldDescriptor(0x5e, "Qilin",             BoolType()),
        'mech_rider':        FieldDescriptor(0x5f, "Mech Rider",        BoolType()),
    }),
    'people_discovered': Category('Journal: People Discovered', {
        'ana_spelunky':       FieldDescriptor(0x60, "Ana Spelunky",       BoolType()),
        'margaret_tunnel':    FieldDescriptor(0x61, "Margaret Tunnel",    BoolType()),
        'colin_northward':    FieldDescriptor(0x62, "Colin Northward",    BoolType()),
        'roffy_sloth':        FieldDescriptor(0x63, "Roffy D. Sloth",     BoolType()),
        'alto_singh':         FieldDescriptor(0x64, "Alto Singh",         BoolType()),
        'liz_mutton':         FieldDescriptor(0x65, "Liz Mutton",         BoolType()),
        'nekka_the_eagle':    FieldDescriptor(0x66, "Nekka the Eagle",    BoolType()),
        'lise_project':       FieldDescriptor(0x67, "Lise Project",       BoolType()),
        'coco_von_diamonds':  FieldDescriptor(0x68, "Coco von Diamonds",  BoolType()),
        'manfred_tunnel':     FieldDescriptor(0x69, "Manfred Tunnel",     BoolType()),
        'little_jay':         FieldDescriptor(0x6a, "Little Jay",         BoolType()),
        'tina_flan':          FieldDescriptor(0x6b, "Tina Flan",          BoolType()),
        'valerie_crump':      FieldDescriptor(0x6c, "Valerie Crump",      BoolType()),
        'au':                 FieldDescriptor(0x6d, "Au",                 BoolType()),
        'demi_von_diamonds':  FieldDescriptor(0x6e, "Demi von Diamonds",  BoolType()),
        'pilot':              FieldDescriptor(0x6f, "Pilot",              BoolType()),
        'princess_airyn':     FieldDescriptor(0x70, "Princess Airyn",     BoolType()),
        'dirk_yamaoka':       FieldDescriptor(0x71, "Dirk Yamaoka",       BoolType()),
        'guy_spelunky':       FieldDescriptor(0x72, "Guy Spelunky",       BoolType()),
        'classic_spelunky':   FieldDescriptor(0x73, "Classic Spelunky",   BoolType()),
        'terra_tunnel':       FieldDescriptor(0x74, "Terra Tunnel",       BoolType()),
        'hired_hand':         FieldDescriptor(0x75, "Hired Hand",         BoolType()),
        'eggplant_child':     FieldDescriptor(0x76, "Eggplant Child",     BoolType()),
        'shopkeeper':         FieldDescriptor(0x77, "Shopkeeper",         BoolType()),
        'tun':                FieldDescriptor(0x78, "Tun",                BoolType()),
        'yang':               FieldDescriptor(0x79, "Yang",               BoolType()),
        'madame_tusk':        FieldDescriptor(0x7a, "Madame Tusk",        BoolType()),
        'tusk_bodyguard':     FieldDescriptor(0x7b, "Tusk's Bodyguard",   BoolType()),
        'waddler':            FieldDescriptor(0x7c, "Waddler",            BoolType()),
        'caveman_shopkeeper': FieldDescriptor(0x7d, "Caveman Shopkeeper", BoolType()),
        'ghist_shopkeeper':   FieldDescriptor(0x7e, "Ghist Shopkeeper",   BoolType()),
        'van_horsing':        FieldDescriptor(0x7f, "Van Horsing",        BoolType()),
        'parsley':            FieldDescriptor(0x80, "Parsley",            BoolType()),
        'parsnip':            FieldDescriptor(0x81, "Parsnip",            BoolType()),
        'parmesan':           FieldDescriptor(0x82, "Parmesan",           BoolType()),
        'sparrow':            FieldDescriptor(0x83, "Sparrow",            BoolType()),
        'beg':                FieldDescriptor(0x84, "Beg",                BoolType()),
        'eggplant_king':      FieldDescriptor(0x85, "Eggplant King",      BoolType()),
    }),
    'items_discovered': Category('Journal: Items Discovered', {
        'rope_pile':         FieldDescriptor(0x86, "Rope Pile",         BoolType()),
        'bomb_bag':          FieldDescriptor(0x87, "Bomb Bag",          BoolType()),
        'bomb_box':          FieldDescriptor(0x88, "Bomb Box",          BoolType()),
        'paste':             FieldDescriptor(0x89, "Paste",             BoolType()),
        'spectacles':        FieldDescriptor(0x8a, "Spectacles",        BoolType()),
        'climbing_gloves':   FieldDescriptor(0x8b, "Climbing Gloves",   BoolType()),
        'pitcher_mitt':      FieldDescriptor(0x8c, "Pitcher's Mitt",    BoolType()),
        'spring_shoes':      FieldDescriptor(0x8d, "Spring Shoes",      BoolType()),
        'spike_shoes':       FieldDescriptor(0x8e, "Spike Shoes",       BoolType()),
        'compass':           FieldDescriptor(0x8f, "Compass",           BoolType()),
        'alien_compass':     FieldDescriptor(0x90, "Alien Compass",     BoolType()),
        'parachute':         FieldDescriptor(0x91, "Parachute",         BoolType()),
        'udjat_eye':         FieldDescriptor(0x92, "Udjat Eye",         BoolType()),
        'kapala':            FieldDescriptor(0x93, "Kapala",            BoolType()),
        'hedjet':            FieldDescriptor(0x94, "Hedjet",            BoolType()),
        'crown':             FieldDescriptor(0x95, "Crown",             BoolType()),
        'eggplant_crown':    FieldDescriptor(0x96, "Eggplant Crown",    BoolType()),
        'the_true_crown':    FieldDescriptor(0x97, "The True Crown",    BoolType()),
        'ankh':              FieldDescriptor(0x98, "Ankh",              BoolType()),
        'tablet_of_destiny': FieldDescriptor(0x99, "Tablet of Destiny", BoolType()),
        'skeleton_key':      FieldDescriptor(0x9a, "Skeleton Key",      BoolType()),
        'royal_jelly':       FieldDescriptor(0x9b, "Royal Jelly",       BoolType()),
        'cape':              FieldDescriptor(0x9c, "Cape",              BoolType()),
        'vlad_cape':         FieldDescriptor(0x9d, "Vlad's Cape",       BoolType()),
        'jetpack':           FieldDescriptor(0x9e, "Jetpack",           BoolType()),
        'telepack':          FieldDescriptor(0x9f, "Telepack",          BoolType()),
        'hoverpack':         FieldDescriptor(0xa0, "Hoverpack",         BoolType()),
        'powerpack':         FieldDescriptor(0xa1, "Powerpack",         BoolType()),
        'webgun':            FieldDescriptor(0xa2, "Webgun",            BoolType()),
        'shotgun':           FieldDescriptor(0xa3, "Shotgun",           BoolType()),
        'freeze_ray':        FieldDescriptor(0xa4, "Freeze Ray",        BoolType()),
        'clone_gun':         FieldDescriptor(0xa5, "Clone Gun",         BoolType()),
        'crossbow':          FieldDescriptor(0xa6, "Crossbow",          BoolType()),
        'camera':            FieldDescriptor(0xa7, "Camera",            BoolType()),
        'teleporter':        FieldDescriptor(0xa8, "Teleporter",        BoolType()),
        'mattock':           FieldDescriptor(0xa9, "Mattock",           BoolType()),
        'boomerang':         FieldDescriptor(0xaa, "Boomerang",         BoolType()),
        'machete':           FieldDescriptor(0xab, "Machete",           BoolType()),
        'excalibure':        FieldDescriptor(0xac, "Excalibure",        BoolType()),
        'broken_sword':      FieldDescriptor(0xad, "Broken Sword",      BoolType()),
        'plasma_cannon':     FieldDescriptor(0xae, "Plasma Cannon",     BoolType()),
        'scepter':           FieldDescriptor(0xaf, "Scepter",           BoolType()),
        'hou_yi_bow':        FieldDescriptor(0xb0, "Hou Yi's Bow",      BoolType()),
        'arrow_of_light':    FieldDescriptor(0xb1, "Arrow of Light",    BoolType()),
        'wooden_shield':     FieldDescriptor(0xb2, "Wooden Shield",     BoolType()),
        'metal_shield':      FieldDescriptor(0xb3, "Metal Shield",      BoolType()),
        'idol':              FieldDescriptor(0xb4, "Idol",              BoolType()),
        'the_tusk_idol':     FieldDescriptor(0xb5, "The Tusk Idol",     BoolType()),
        'curse_pot':         FieldDescriptor(0xb6, "Curse Pot",         BoolType()),
        'ushabti':           FieldDescriptor(0xb7, "Ushabti",           BoolType()),
        'eggplant':          FieldDescriptor(0xb8, "Eggplant",          BoolType()),
        'cooked_turkey':     FieldDescriptor(0xb9, "Cooked Turkey",     BoolType()),
        'elixir':            FieldDescriptor(0xba, "Elixir",            BoolType()),
        'four-leaf_clover':  FieldDescriptor(0xbb, "Four-Leaf Clover",  BoolType()),
    }),
    'traps_discovered': Category('Journal: Traps Discovered', {
        'spikes':           FieldDescriptor(0xbc, "Spikes",           BoolType()),
        'arrow_trap':       FieldDescriptor(0xbd, "Arrow Trap",       BoolType()),
        'bear_trap':        FieldDescriptor(0xbe, "Bear Trap",        BoolType()),
        'log_trap':         FieldDescriptor(0xbf, "Log Trap",         BoolType()),
        'spear_trap':       FieldDescriptor(0xc0, "Spear Trap",       BoolType()),
        'thorny_vine':      FieldDescriptor(0xc1, "Thorny Vine",      BoolType()),
        'snap_trap':        FieldDescriptor(0xc2, "Snap Trap",        BoolType()),
        'powder_box':       FieldDescriptor(0xc3, "Powder Box",       BoolType()),
        'falling_platform': FieldDescriptor(0xc4, "Falling Platform", BoolType()),
        'spikeball':        FieldDescriptor(0xc5, "Spikeball",        BoolType()),
        'lion_trap':        FieldDescriptor(0xc6, "Lion Trap",        BoolType()),
        'giant_clam':       FieldDescriptor(0xc7, "Giant Clam",       BoolType()),
        'sliding_wall':     FieldDescriptor(0xc8, "Sliding Wall",     BoolType()),
        'crush_trap':       FieldDescriptor(0xc9, "Crush Trap",       BoolType()),
        'giant_crush_trap': FieldDescriptor(0xca, "Giant Crush Trap", BoolType()),
        'boulder':          FieldDescriptor(0xcb, "Boulder",          BoolType()),
        'spring_trap':      FieldDescriptor(0xcc, "Spring Trap",      BoolType()),
        'landmine':         FieldDescriptor(0xcd, "Landmine",         BoolType()),
        'laser_trap':       FieldDescriptor(0xce, "Laser Trap",       BoolType()),
        'spark_trap':       FieldDescriptor(0xcf, "Spark Trap",       BoolType()),
        'frog_trap':        FieldDescriptor(0xd0, "Frog Trap",        BoolType()),
        'sticky_trap':      FieldDescriptor(0xd1, "Sticky Trap",      BoolType()),
        'bone_drop':        FieldDescriptor(0xd2, "Bone Drop",        BoolType()),
        'egg_sac':          FieldDescriptor(0xd3, "Egg Sac",          BoolType()),
    }),
    'character_unlocks': Category('Character Unlocks', {
        'unlock_field': FieldDescriptor(0xe6, "Unlock field", FlagType(4, CharacterUnlockFlags)),
    }),
    'shortcut_unlocks': Category('Shortcut Unlocks', {
        'shortcut_progress': FieldDescriptor(0xeb, "Shortcut Progress", EnumType(1, ShortcutProgressEnum)),
    }),
    'bestiary_defeated': Category('Bestiary Defeated Counts', {
        'snake':             FieldDescriptor(0x0ee, "Snake",             Int32Type()),
        'spider':            FieldDescriptor(0x0f2, "Spider",            Int32Type()),
        'bat':               FieldDescriptor(0x0f6, "Bat",               Int32Type()),
        'caveman':           FieldDescriptor(0x0fa, "Caveman",           Int32Type()),
        'skeleton':          FieldDescriptor(0x0fe, "Skeleton",          Int32Type()),
        'horned_lizard':     FieldDescriptor(0x102, "Horned Lizard",     Int32Type()),
        'moles':             FieldDescriptor(0x106, "Moles",             Int32Type()),
        'quillback':         FieldDescriptor(0x10a, "Quillback",         Int32Type()),
        'mantrap':           FieldDescriptor(0x10e, "Mantrap",           Int32Type()),
        'tiki_man':          FieldDescriptor(0x112, "Tiki Man",          Int32Type()),
        'witch_doctor':      FieldDescriptor(0x116, "Witch Doctor",      Int32Type()),
        'mosquito':          FieldDescriptor(0x11a, "Mosquito",          Int32Type()),
        'monkey':            FieldDescriptor(0x11e, "Monkey",            Int32Type()),
        'hang_spider':       FieldDescriptor(0x122, "Hang Spider",       Int32Type()),
        'giant_spider':      FieldDescriptor(0x126, "Giant Spider",      Int32Type()),
        'magmar':            FieldDescriptor(0x12a, "Magmar",            Int32Type()),
        'robot':             FieldDescriptor(0x12e, "Robot",             Int32Type()),
        'fire_bug':          FieldDescriptor(0x132, "Fire Bug",          Int32Type()),
        'imp':               FieldDescriptor(0x136, "Imp",               Int32Type()),
        'lavamander':        FieldDescriptor(0x13a, "Lavamander",        Int32Type()),
        'vampire':           FieldDescriptor(0x13e, "Vampire",           Int32Type()),
        'vlad':              FieldDescriptor(0x142, "Vlad",              Int32Type()),
        'olmec':             FieldDescriptor(0x146, "Olmec",             Int32Type()),
        'jiangshi':          FieldDescriptor(0x14a, "Jiangshi",          Int32Type()),
        'jiangshi_assassin': FieldDescriptor(0x14e, "Jiangshi Assassin", Int32Type()),
        'flying_fish':       FieldDescriptor(0x152, "Flying Fish",       Int32Type()),
        'octopy':            FieldDescriptor(0x156, "Octopy",            Int32Type()),
        'hermit_crab':       FieldDescriptor(0x15a, "Hermit Crab",       Int32Type()),
        'pangxie':           FieldDescriptor(0x15e, "Pangxie",           Int32Type()),
        'great_humphead':    FieldDescriptor(0x162, "Great Humphead",    Int32Type()),
        'kingu':             FieldDescriptor(0x166, "Kingu",             Int32Type()),
        'crocman':           FieldDescriptor(0x16a, "Crocman",           Int32Type()),
        'cobra':             FieldDescriptor(0x16e, "Cobra",             Int32Type()),
        'mummy':             FieldDescriptor(0x172, "Mummy",             Int32Type()),
        'sorceress':         FieldDescriptor(0x176, "Sorceress",         Int32Type()),
        'cat_mummy':         FieldDescriptor(0x17a, "Cat Mummy",         Int32Type()),
        'necromancer':       FieldDescriptor(0x17e, "Necromancer",       Int32Type()),
        'anubis':            FieldDescriptor(0x182, "Anubis",            Int32Type()),
        'ammit':             FieldDescriptor(0x186, "Ammit",             Int32Type()),
        'apep':              FieldDescriptor(0x18a, "Apep",              Int32Type()),
        'anubis_ii':         FieldDescriptor(0x18e, "Anubis II",         Int32Type()),
        'osiris':            FieldDescriptor(0x192, "Osiris",            Int32Type()),
        'ufo':               FieldDescriptor(0x196, "Ufo",               Int32Type()),
        'alien':             FieldDescriptor(0x19a, "Alien",             Int32Type()),
        'yeti':              FieldDescriptor(0x19e, "Yeti",              Int32Type()),
        'yeti_king':         FieldDescriptor(0x1a2, "Yeti King",         Int32Type()),
        'yeti_queen':        FieldDescriptor(0x1a6, "Yeti Queen",        Int32Type()),
        'lahamu':            FieldDescriptor(0x1aa, "Lahamu",            Int32Type()),
        'proto_shopkeeper':  FieldDescriptor(0x1ae, "Proto Shopkeeper",  Int32Type()),
        'olmite':            FieldDescriptor(0x1b2, "Olmite",            Int32Type()),
        'lamassu':           FieldDescriptor(0x1b6, "Lamassu",           Int32Type()),
        'tiamat':            FieldDescriptor(0x1ba, "Tiamat",            Int32Type()),
        'tadpole':           FieldDescriptor(0x1be, "Tadpole",           Int32Type()),
        'frog':              FieldDescriptor(0x1c2, "Frog",              Int32Type()),
        'fire_frog':         FieldDescriptor(0x1c6, "Fire Frog",         Int32Type()),
        'goliath_frog':      FieldDescriptor(0x1ca, "Goliath Frog",      Int32Type()),
        'grub':              FieldDescriptor(0x1ce, "Grub",              Int32Type()),
        'giant_fly':         FieldDescriptor(0x1d2, "Giant Fly",         Int32Type()),
        'hundun':            FieldDescriptor(0x1d6, "Hundun",            Int32Type()),
        'eggplant_minister': FieldDescriptor(0x1da, "Eggplant Minister", Int32Type()),
        'eggplup':           FieldDescriptor(0x1de, "Eggplup",           Int32Type()),
        'celestial_jelly':   FieldDescriptor(0x1e2, "Celestial Jelly",   Int32Type()),
        'scorpion':          FieldDescriptor(0x1e6, "Scorpion",          Int32Type()),
        'bee':               FieldDescriptor(0x1ea, "Bee",               Int32Type()),
        'queen_bee':         FieldDescriptor(0x1ee, "Queen Bee",         Int32Type()),
        'scarab':            FieldDescriptor(0x1f2, "Scarab",            Int32Type()),
        'golden_monkey':     FieldDescriptor(0x1f6, "Golden Monkey",     Int32Type()),
        'leprechaun':        FieldDescriptor(0x1fa, "Leprechaun",        Int32Type()),
        'monty':             FieldDescriptor(0x1fe, "Monty",             Int32Type()),
        'percy':             FieldDescriptor(0x202, "Percy",             Int32Type()),
        'poochi':            FieldDescriptor(0x206, "Poochi",            Int32Type()),
        'ghist':             FieldDescriptor(0x20a, "Ghist",             Int32Type()),
        'ghost':             FieldDescriptor(0x20e, "Ghost",             Int32Type()),
        'cave_turkey':       FieldDescriptor(0x212, "Cave Turkey",       Int32Type()),
        'rock_dog':          FieldDescriptor(0x216, "Rock Dog",          Int32Type()),
        'axolotl':           FieldDescriptor(0x21a, "Axolotl",           Int32Type()),
        'qilin':             FieldDescriptor(0x21e, "Qilin",             Int32Type()),
        'mech_rider':        FieldDescriptor(0x222, "Mech Rider",        Int32Type()),
    }),
    'bestiary_killed_by': Category('Bestiary Killed by Counts', {
        'snake':             FieldDescriptor(0x226, "Snake",             Int32Type()),
        'spider':            FieldDescriptor(0x22a, "Spider",            Int32Type()),
        'bat':               FieldDescriptor(0x22e, "Bat",               Int32Type()),
        'caveman':           FieldDescriptor(0x232, "Caveman",           Int32Type()),
        'skeleton':          FieldDescriptor(0x236, "Skeleton",          Int32Type()),
        'horned_lizard':     FieldDescriptor(0x23a, "Horned Lizard",     Int32Type()),
        'moles':             FieldDescriptor(0x23e, "Moles",             Int32Type()),
        'quillback':         FieldDescriptor(0x242, "Quillback",         Int32Type()),
        'mantrap':           FieldDescriptor(0x246, "Mantrap",           Int32Type()),
        'tiki_man':          FieldDescriptor(0x24a, "Tiki Man",          Int32Type()),
        'witch_doctor':      FieldDescriptor(0x24e, "Witch Doctor",      Int32Type()),
        'mosquito':          FieldDescriptor(0x252, "Mosquito",          Int32Type()),
        'monkey':            FieldDescriptor(0x256, "Monkey",            Int32Type()),
        'hang_spider':       FieldDescriptor(0x25a, "Hang Spider",       Int32Type()),
        'giant_spider':      FieldDescriptor(0x25e, "Giant Spider",      Int32Type()),
        'magmar':            FieldDescriptor(0x262, "Magmar",            Int32Type()),
        'robot':             FieldDescriptor(0x266, "Robot",             Int32Type()),
        'fire_bug':          FieldDescriptor(0x26a, "Fire Bug",          Int32Type()),
        'imp':               FieldDescriptor(0x26e, "Imp",               Int32Type()),
        'lavamander':        FieldDescriptor(0x272, "Lavamander",        Int32Type()),
        'vampire':           FieldDescriptor(0x276, "Vampire",           Int32Type()),
        'vlad':              FieldDescriptor(0x27a, "Vlad",              Int32Type()),
        'olmec':             FieldDescriptor(0x27e, "Olmec",             Int32Type()),
        'jiangshi':          FieldDescriptor(0x282, "Jiangshi",          Int32Type()),
        'jiangshi_assassin': FieldDescriptor(0x286, "Jiangshi Assassin", Int32Type()),
        'flying_fish':       FieldDescriptor(0x28a, "Flying Fish",       Int32Type()),
        'octopy':            FieldDescriptor(0x28e, "Octopy",            Int32Type()),
        'hermit_crab':       FieldDescriptor(0x292, "Hermit Crab",       Int32Type()),
        'pangxie':           FieldDescriptor(0x296, "Pangxie",           Int32Type()),
        'great_humphead':    FieldDescriptor(0x29a, "Great Humphead",    Int32Type()),
        'kingu':             FieldDescriptor(0x29e, "Kingu",             Int32Type()),
        'crocman':           FieldDescriptor(0x2a2, "Crocman",           Int32Type()),
        'cobra':             FieldDescriptor(0x2a6, "Cobra",             Int32Type()),
        'mummy':             FieldDescriptor(0x2aa, "Mummy",             Int32Type()),
        'sorceress':         FieldDescriptor(0x2ae, "Sorceress",         Int32Type()),
        'cat_mummy':         FieldDescriptor(0x2b2, "Cat Mummy",         Int32Type()),
        'necromancer':       FieldDescriptor(0x2b6, "Necromancer",       Int32Type()),
        'anubis':            FieldDescriptor(0x2ba, "Anubis",            Int32Type()),
        'ammit':             FieldDescriptor(0x2be, "Ammit",             Int32Type()),
        'apep':              FieldDescriptor(0x2c2, "Apep",              Int32Type()),
        'anubis_ii':         FieldDescriptor(0x2c6, "Anubis II",         Int32Type()),
        'osiris':            FieldDescriptor(0x2ca, "Osiris",            Int32Type()),
        'ufo':               FieldDescriptor(0x2ce, "Ufo",               Int32Type()),
        'alien':             FieldDescriptor(0x2d2, "Alien",             Int32Type()),
        'yeti':              FieldDescriptor(0x2d6, "Yeti",              Int32Type()),
        'yeti_king':         FieldDescriptor(0x2da, "Yeti King",         Int32Type()),
        'yeti_queen':        FieldDescriptor(0x2de, "Yeti Queen",        Int32Type()),
        'lahamu':            FieldDescriptor(0x2e2, "Lahamu",            Int32Type()),
        'proto_shopkeeper':  FieldDescriptor(0x2e6, "Proto Shopkeeper",  Int32Type()),
        'olmite':            FieldDescriptor(0x2ea, "Olmite",            Int32Type()),
        'lamassu':           FieldDescriptor(0x2ee, "Lamassu",           Int32Type()),
        'tiamat':            FieldDescriptor(0x2f2, "Tiamat",            Int32Type()),
        'tadpole':           FieldDescriptor(0x2f6, "Tadpole",           Int32Type()),
        'frog':              FieldDescriptor(0x2fa, "Frog",              Int32Type()),
        'fire_frog':         FieldDescriptor(0x2fe, "Fire Frog",         Int32Type()),
        'goliath_frog':      FieldDescriptor(0x302, "Goliath Frog",      Int32Type()),
        'grub':              FieldDescriptor(0x306, "Grub",              Int32Type()),
        'giant_fly':         FieldDescriptor(0x30a, "Giant Fly",         Int32Type()),
        'hundun':            FieldDescriptor(0x30e, "Hundun",            Int32Type()),
        'eggplant_minister': FieldDescriptor(0x312, "Eggplant Minister", Int32Type()),
        'eggplup':           FieldDescriptor(0x316, "Eggplup",           Int32Type()),
        'celestial_jelly':   FieldDescriptor(0x31a, "Celestial Jelly",   Int32Type()),
        'scorpion':          FieldDescriptor(0x31e, "Scorpion",          Int32Type()),
        'bee':               FieldDescriptor(0x322, "Bee",               Int32Type()),
        'queen_bee':         FieldDescriptor(0x326, "Queen Bee",         Int32Type()),
        'scarab':            FieldDescriptor(0x32a, "Scarab",            Int32Type()),
        'golden_monkey':     FieldDescriptor(0x32e, "Golden Monkey",     Int32Type()),
        'leprechaun':        FieldDescriptor(0x332, "Leprechaun",        Int32Type()),
        'monty':             FieldDescriptor(0x336, "Monty",             Int32Type()),
        'percy':             FieldDescriptor(0x33a, "Percy",             Int32Type()),
        'poochi':            FieldDescriptor(0x33e, "Poochi",            Int32Type()),
        'ghist':             FieldDescriptor(0x342, "Ghist",             Int32Type()),
        'ghost':             FieldDescriptor(0x346, "Ghost",             Int32Type()),
        'cave_turkey':       FieldDescriptor(0x34a, "Cave Turkey",       Int32Type()),
        'rock_dog':          FieldDescriptor(0x34e, "Rock Dog",          Int32Type()),
        'axolotl':           FieldDescriptor(0x352, "Axolotl",           Int32Type()),
        'qilin':             FieldDescriptor(0x356, "Qilin",             Int32Type()),
        'mech_rider':        FieldDescriptor(0x35a, "Mech Rider",        Int32Type()),
    }),
    'people_defeated': Category('People Defeated Counts', {
        'hired_hand':         FieldDescriptor(0x3b2, "Hired Hand",         Int32Type()),
        'eggplant_child':     FieldDescriptor(0x3b6, "Eggplant Child",     Int32Type()),
        'shopkeeper':         FieldDescriptor(0x3ba, "Shopkeeper",         Int32Type()),
        'tun':                FieldDescriptor(0x3be, "Tun",                Int32Type()),
        'yang':               FieldDescriptor(0x3c2, "Yang",               Int32Type()),
        'madame_tusk':        FieldDescriptor(0x3c6, "Madame Tusk",        Int32Type()),
        'tusk_bodyguard':     FieldDescriptor(0x3ca, "Tusk's Bodyguard",   Int32Type()),
        'waddler':            FieldDescriptor(0x3ce, "Waddler",            Int32Type()),
        'caveman_shopkeeper': FieldDescriptor(0x3d2, "Caveman Shopkeeper", Int32Type()),
        'ghist_shopkeeper':   FieldDescriptor(0x3d6, "Ghist Shopkeeper",   Int32Type()),
        'van_horsing':        FieldDescriptor(0x3da, "Van Horsing",        Int32Type()),
        'parsley':            FieldDescriptor(0x3de, "Parsley",            Int32Type()),
        'parsnip':            FieldDescriptor(0x3e2, "Parsnip",            Int32Type()),
        'parmesan':           FieldDescriptor(0x3e6, "Parmesan",           Int32Type()),
        'sparrow':            FieldDescriptor(0x3ea, "Sparrow",            Int32Type()),
        'beg':                FieldDescriptor(0x3ee, "Beg",                Int32Type()),
        'eggplant_king':      FieldDescriptor(0x3f2, "Eggplant King",      Int32Type()),
    }),
    'people_killed_by': Category('People Killed by Counts', {
        'hired_hand':         FieldDescriptor(0x44a, "Hired Hand",         Int32Type()),
        'eggplant_child':     FieldDescriptor(0x44e, "Eggplant Child",     Int32Type()),
        'shopkeeper':         FieldDescriptor(0x452, "Shopkeeper",         Int32Type()),
        'tun':                FieldDescriptor(0x456, "Tun",                Int32Type()),
        'yang':               FieldDescriptor(0x45a, "Yang",               Int32Type()),
        'madame_tusk':        FieldDescriptor(0x45e, "Madame Tusk",        Int32Type()),
        'tusk_bodyguard':     FieldDescriptor(0x462, "Tusk's Bodyguard",   Int32Type()),
        'waddler':            FieldDescriptor(0x466, "Waddler",            Int32Type()),
        'caveman_shopkeeper': FieldDescriptor(0x46a, "Caveman Shopkeeper", Int32Type()),
        'ghist_shopkeeper':   FieldDescriptor(0x46e, "Ghist Shopkeeper",   Int32Type()),
        'van_horsing':        FieldDescriptor(0x472, "Van Horsing",        Int32Type()),
        'parsley':            FieldDescriptor(0x476, "Parsley",            Int32Type()),
        'parsnip':            FieldDescriptor(0x47a, "Parsnip",            Int32Type()),
        'parmesan':           FieldDescriptor(0x47e, "Parmesan",           Int32Type()),
        'sparrow':            FieldDescriptor(0x482, "Sparrow",            Int32Type()),
        'beg':                FieldDescriptor(0x486, "Beg",                Int32Type()),
        'eggplant_king':      FieldDescriptor(0x48a, "Eggplant King",      Int32Type()),
    }),
    'player_profile': Category('Player Profile', {
        'plays':         FieldDescriptor(0x048e, "Plays",         Int32Type()),
        'deaths':        FieldDescriptor(0x0492, "Deaths",        Int32Type()),
        'normal_wins':   FieldDescriptor(0x0496, "Normal Wins",   Int32Type()),
        'hard_wins':     FieldDescriptor(0x049a, "Hard Wins",     Int32Type()),
        'special_wins':  FieldDescriptor(0x049e, "Special Wins",  Int32Type()),
        'sum_of_score':  FieldDescriptor(0x04a2, "Sum of Score",  Int64Type()),
        'top_score':     FieldDescriptor(0x04aa, "Top Score",     Int32Type()),
        'deepest_area':  FieldDescriptor(0x04ae, "Deepest Area",  ByteType()),
        'deepest_level': FieldDescriptor(0x04af, "Deepest Level", ByteType()),
        'sum_of_time':   FieldDescriptor(0x288e, "Sum of Time",   Int64Type()),
        'best_time':     FieldDescriptor(0x2896, "Best Time",     Int32Type()),
    }),
}

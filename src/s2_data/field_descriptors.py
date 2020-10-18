from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import IntFlag, IntEnum, auto

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
    Ana = auto()
    Margaret = auto()
    Colin = auto()
    Roffy = auto()
    Alto = auto()
    Liz = auto()
    Nekka = auto()
    LISE = auto()
    Coco = auto()
    Manfred = auto()
    Jay = auto()
    Tina = auto()
    Valerie = auto()
    Au = auto()
    Demi = auto()
    Pilot = auto()
    Airyn = auto()
    Dirk = auto()
    Guy = auto()
    ClassicGuy = auto()

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
    description: str
    type: Type

field_descriptors = {
    'Magic Number': (
        FieldDescriptor(0x0, 'Magic number 1', 'First magic number byte',  ByteType()),
        FieldDescriptor(0x1, 'Magic number 2', 'Second magic number byte', ByteType()),
    ),
    'Journal Places': (
        FieldDescriptor(0x02, "Discovered Dwelling",          "", BoolType()),
        FieldDescriptor(0x03, "Discovered Jungle",            "", BoolType()),
        FieldDescriptor(0x04, "Discovered Volcana",           "", BoolType()),
        FieldDescriptor(0x05, "Discovered Olmec's Lair",      "", BoolType()),
        FieldDescriptor(0x06, "Discovered Tide Pool",         "", BoolType()),
        FieldDescriptor(0x07, "Discovered Abzu",              "", BoolType()),
        FieldDescriptor(0x08, "Discovered Temple of Anubis",  "", BoolType()),
        FieldDescriptor(0x09, "Discovered The City of Gold",  "", BoolType()),
        FieldDescriptor(0x0a, "Discovered Duat",              "", BoolType()),
        FieldDescriptor(0x0b, "Discovered Ice Caves",         "", BoolType()),
        FieldDescriptor(0x0c, "Discovered Neo Babylon",       "", BoolType()),
        FieldDescriptor(0x0d, "Discovered Tiamat's Throne",   "", BoolType()),
        FieldDescriptor(0x0e, "Discovered Sunken City",       "", BoolType()),
        FieldDescriptor(0x0f, "Discovered Eggplant World",    "", BoolType()),
        FieldDescriptor(0x10, "Discovered Hundun's Hideaway", "", BoolType()),
        FieldDescriptor(0x11, "Discovered Cosmic Ocean",      "", BoolType()),
    ),
    'Journal Bestiary': (
        FieldDescriptor(0x12, "Discovered Snake",             "", BoolType()),
        FieldDescriptor(0x13, "Discovered Spider",            "", BoolType()),
        FieldDescriptor(0x14, "Discovered Bat",               "", BoolType()),
        FieldDescriptor(0x15, "Discovered Caveman",           "", BoolType()),
        FieldDescriptor(0x16, "Discovered Skeleton",          "", BoolType()),
        FieldDescriptor(0x17, "Discovered Horned Lizard",     "", BoolType()),
        FieldDescriptor(0x18, "Discovered Moles",             "", BoolType()),
        FieldDescriptor(0x19, "Discovered Quillback",         "", BoolType()),
        FieldDescriptor(0x1a, "Discovered Mantrap",           "", BoolType()),
        FieldDescriptor(0x1b, "Discovered Tiki Man",          "", BoolType()),
        FieldDescriptor(0x1c, "Discovered Witch Doctor",      "", BoolType()),
        FieldDescriptor(0x1d, "Discovered Mosquito",          "", BoolType()),
        FieldDescriptor(0x1e, "Discovered Monkey",            "", BoolType()),
        FieldDescriptor(0x1f, "Discovered Hang Spider",       "", BoolType()),
        FieldDescriptor(0x20, "Discovered Giant Spider",      "", BoolType()),
        FieldDescriptor(0x21, "Discovered Magmar",            "", BoolType()),
        FieldDescriptor(0x22, "Discovered Robot",             "", BoolType()),
        FieldDescriptor(0x23, "Discovered Fire Bug",          "", BoolType()),
        FieldDescriptor(0x24, "Discovered Imp",               "", BoolType()),
        FieldDescriptor(0x25, "Discovered Lavamander",        "", BoolType()),
        FieldDescriptor(0x26, "Discovered Vampire",           "", BoolType()),
        FieldDescriptor(0x27, "Discovered Vlad",              "", BoolType()),
        FieldDescriptor(0x28, "Discovered Olmec",             "", BoolType()),
        FieldDescriptor(0x29, "Discovered Jiangshi",          "", BoolType()),
        FieldDescriptor(0x2a, "Discovered Jiangshi Assassin", "", BoolType()),
        FieldDescriptor(0x2b, "Discovered Flying Fish",       "", BoolType()),
        FieldDescriptor(0x2c, "Discovered Octopy",            "", BoolType()),
        FieldDescriptor(0x2d, "Discovered Hermit Crab",       "", BoolType()),
        FieldDescriptor(0x2e, "Discovered Pangxie",           "", BoolType()),
        FieldDescriptor(0x2f, "Discovered Great Humphead",    "", BoolType()),
        FieldDescriptor(0x30, "Discovered Kingu",             "", BoolType()),
        FieldDescriptor(0x31, "Discovered Crocman",           "", BoolType()),
        FieldDescriptor(0x32, "Discovered Cobra",             "", BoolType()),
        FieldDescriptor(0x33, "Discovered Mummy",             "", BoolType()),
        FieldDescriptor(0x34, "Discovered Sorceress",         "", BoolType()),
        FieldDescriptor(0x35, "Discovered Cat Mummy",         "", BoolType()),
        FieldDescriptor(0x36, "Discovered Necromancer",       "", BoolType()),
        FieldDescriptor(0x37, "Discovered Anubis",            "", BoolType()),
        FieldDescriptor(0x38, "Discovered Ammit",             "", BoolType()),
        FieldDescriptor(0x39, "Discovered Apep",              "", BoolType()),
        FieldDescriptor(0x3a, "Discovered Anubis II",         "", BoolType()),
        FieldDescriptor(0x3b, "Discovered Osiris",            "", BoolType()),
        FieldDescriptor(0x3c, "Discovered Ufo",               "", BoolType()),
        FieldDescriptor(0x3d, "Discovered Alien",             "", BoolType()),
        FieldDescriptor(0x3e, "Discovered Yeti",              "", BoolType()),
        FieldDescriptor(0x3f, "Discovered Yeti King",         "", BoolType()),
        FieldDescriptor(0x40, "Discovered Yeti Queen",        "", BoolType()),
        FieldDescriptor(0x41, "Discovered Lahamu",            "", BoolType()),
        FieldDescriptor(0x42, "Discovered Proto Shopkeeper",  "", BoolType()),
        FieldDescriptor(0x43, "Discovered Olmite",            "", BoolType()),
        FieldDescriptor(0x44, "Discovered Lamassu",           "", BoolType()),
        FieldDescriptor(0x45, "Discovered Tiamat",            "", BoolType()),
        FieldDescriptor(0x46, "Discovered Tadpole",           "", BoolType()),
        FieldDescriptor(0x47, "Discovered Frog",              "", BoolType()),
        FieldDescriptor(0x48, "Discovered Fire Frog",         "", BoolType()),
        FieldDescriptor(0x49, "Discovered Goliath Frog",      "", BoolType()),
        FieldDescriptor(0x4a, "Discovered Grub",              "", BoolType()),
        FieldDescriptor(0x4b, "Discovered Giant Fly",         "", BoolType()),
        FieldDescriptor(0x4c, "Discovered Hundun",            "", BoolType()),
        FieldDescriptor(0x4d, "Discovered Eggplant Minister", "", BoolType()),
        FieldDescriptor(0x4e, "Discovered Eggplup",           "", BoolType()),
        FieldDescriptor(0x4f, "Discovered Celestial Jelly",   "", BoolType()),
        FieldDescriptor(0x50, "Discovered Scorpion",          "", BoolType()),
        FieldDescriptor(0x51, "Discovered Bee",               "", BoolType()),
        FieldDescriptor(0x52, "Discovered Queen Bee",         "", BoolType()),
        FieldDescriptor(0x53, "Discovered Scarab",            "", BoolType()),
        FieldDescriptor(0x54, "Discovered Golden Monkey",     "", BoolType()),
        FieldDescriptor(0x55, "Discovered Leprechaun",        "", BoolType()),
        FieldDescriptor(0x56, "Discovered Monty",             "", BoolType()),
        FieldDescriptor(0x57, "Discovered Percy",             "", BoolType()),
        FieldDescriptor(0x58, "Discovered Poochi",            "", BoolType()),
        FieldDescriptor(0x59, "Discovered Ghist",             "", BoolType()),
        FieldDescriptor(0x5a, "Discovered Ghost",             "", BoolType()),
        FieldDescriptor(0x5b, "Discovered Cave Turkey",       "", BoolType()),
        FieldDescriptor(0x5c, "Discovered Rock Dog",          "", BoolType()),
        FieldDescriptor(0x5d, "Discovered Axolotl",           "", BoolType()),
        FieldDescriptor(0x5e, "Discovered Qilin",             "", BoolType()),
        FieldDescriptor(0x5f, "Discovered Mech Rider",        "", BoolType()),
    ),
    'Journal People': (
        FieldDescriptor(0x60, "Discovered Ana Spelunky",       '', BoolType()),
        FieldDescriptor(0x61, "Discovered Margaret Tunnel",    '', BoolType()),
        FieldDescriptor(0x62, "Discovered Colin Northward",    '', BoolType()),
        FieldDescriptor(0x63, "Discovered Roffy D. Sloth",     '', BoolType()),
        FieldDescriptor(0x64, "Discovered Alto Singh",         '', BoolType()),
        FieldDescriptor(0x65, "Discovered Liz Mutton",         '', BoolType()),
        FieldDescriptor(0x66, "Discovered Nekka the Eagle",    '', BoolType()),
        FieldDescriptor(0x67, "Discovered Lise Project",       '', BoolType()),
        FieldDescriptor(0x68, "Discovered Coco von Diamonds",  '', BoolType()),
        FieldDescriptor(0x69, "Discovered Manfred Tunnel",     '', BoolType()),
        FieldDescriptor(0x6a, "Discovered Little Jay",         '', BoolType()),
        FieldDescriptor(0x6b, "Discovered Tina Flan",          '', BoolType()),
        FieldDescriptor(0x6c, "Discovered Valerie Crump",      '', BoolType()),
        FieldDescriptor(0x6d, "Discovered Au",                 '', BoolType()),
        FieldDescriptor(0x6e, "Discovered Demi von Diamonds",  '', BoolType()),
        FieldDescriptor(0x6f, "Discovered Pilot",              '', BoolType()),
        FieldDescriptor(0x70, "Discovered Princess Airyn",     '', BoolType()),
        FieldDescriptor(0x71, "Discovered Dirk Yamaoka",       '', BoolType()),
        FieldDescriptor(0x72, "Discovered Guy Spelunky",       '', BoolType()),
        FieldDescriptor(0x73, "Discovered Classic Spelunky",   '', BoolType()),
        FieldDescriptor(0x74, "Discovered Terra Tunnel",       '', BoolType()),
        FieldDescriptor(0x75, "Discovered Hired Hand",         '', BoolType()),
        FieldDescriptor(0x76, "Discovered Eggplant Child",     '', BoolType()),
        FieldDescriptor(0x77, "Discovered Shopkeeper",         '', BoolType()),
        FieldDescriptor(0x78, "Discovered Tun",                '', BoolType()),
        FieldDescriptor(0x79, "Discovered Yang",               '', BoolType()),
        FieldDescriptor(0x7a, "Discovered Madame Tusk",        '', BoolType()),
        FieldDescriptor(0x7b, "Discovered Tusk's Bodyguard",   '', BoolType()),
        FieldDescriptor(0x7c, "Discovered Waddler",            '', BoolType()),
        FieldDescriptor(0x7d, "Discovered Caveman Shopkeeper", '', BoolType()),
        FieldDescriptor(0x7e, "Discovered Ghist Shopkeeper",   '', BoolType()),
        FieldDescriptor(0x7f, "Discovered Van Horsing",        '', BoolType()),
        FieldDescriptor(0x80, "Discovered Parsley",            '', BoolType()),
        FieldDescriptor(0x81, "Discovered Parsnip",            '', BoolType()),
        FieldDescriptor(0x82, "Discovered Parmesan",           '', BoolType()),
        FieldDescriptor(0x83, "Discovered Sparrow",            '', BoolType()),
        FieldDescriptor(0x84, "Discovered Beg",                '', BoolType()),
        FieldDescriptor(0x85, "Discovered Eggplant King",      '', BoolType()),
    ),
    'Journal Items': (
        FieldDescriptor(0x86, "Discovered Rope Pile",         '', BoolType()),
        FieldDescriptor(0x87, "Discovered Bomb Bag",          '', BoolType()),
        FieldDescriptor(0x88, "Discovered Bomb Box",          '', BoolType()),
        FieldDescriptor(0x89, "Discovered Paste",             '', BoolType()),
        FieldDescriptor(0x8a, "Discovered Spectacles",        '', BoolType()),
        FieldDescriptor(0x8b, "Discovered Climbing Gloves",   '', BoolType()),
        FieldDescriptor(0x8c, "Discovered Pitcher's Mitt",    '', BoolType()),
        FieldDescriptor(0x8d, "Discovered Spring Shoes",      '', BoolType()),
        FieldDescriptor(0x8e, "Discovered Spike Shoes",       '', BoolType()),
        FieldDescriptor(0x8f, "Discovered Compass",           '', BoolType()),
        FieldDescriptor(0x90, "Discovered Alien Compass",     '', BoolType()),
        FieldDescriptor(0x91, "Discovered Parachute",         '', BoolType()),
        FieldDescriptor(0x92, "Discovered Udjat Eye",         '', BoolType()),
        FieldDescriptor(0x93, "Discovered Kapala",            '', BoolType()),
        FieldDescriptor(0x94, "Discovered Hedjet",            '', BoolType()),
        FieldDescriptor(0x95, "Discovered Crown",             '', BoolType()),
        FieldDescriptor(0x96, "Discovered Eggplant Crown",    '', BoolType()),
        FieldDescriptor(0x97, "Discovered The True Crown",    '', BoolType()),
        FieldDescriptor(0x98, "Discovered Ankh",              '', BoolType()),
        FieldDescriptor(0x99, "Discovered Tablet of Destiny", '', BoolType()),
        FieldDescriptor(0x9a, "Discovered Skeleton Key",      '', BoolType()),
        FieldDescriptor(0x9b, "Discovered Royal Jelly",       '', BoolType()),
        FieldDescriptor(0x9c, "Discovered Cape",              '', BoolType()),
        FieldDescriptor(0x9d, "Discovered Vlad's Cape",       '', BoolType()),
        FieldDescriptor(0x9e, "Discovered Jetpack",           '', BoolType()),
        FieldDescriptor(0x9f, "Discovered Telepack",          '', BoolType()),
        FieldDescriptor(0xa0, "Discovered Hoverpack",         '', BoolType()),
        FieldDescriptor(0xa1, "Discovered Powerpack",         '', BoolType()),
        FieldDescriptor(0xa2, "Discovered Webgun",            '', BoolType()),
        FieldDescriptor(0xa3, "Discovered Shotgun",           '', BoolType()),
        FieldDescriptor(0xa4, "Discovered Freeze Ray",        '', BoolType()),
        FieldDescriptor(0xa5, "Discovered Clone Gun",         '', BoolType()),
        FieldDescriptor(0xa6, "Discovered Crossbow",          '', BoolType()),
        FieldDescriptor(0xa7, "Discovered Camera",            '', BoolType()),
        FieldDescriptor(0xa8, "Discovered Teleporter",        '', BoolType()),
        FieldDescriptor(0xa9, "Discovered Mattock",           '', BoolType()),
        FieldDescriptor(0xaa, "Discovered Boomerang",         '', BoolType()),
        FieldDescriptor(0xab, "Discovered Machete",           '', BoolType()),
        FieldDescriptor(0xac, "Discovered Excalibure",        '', BoolType()),
        FieldDescriptor(0xad, "Discovered Broken Sword",      '', BoolType()),
        FieldDescriptor(0xae, "Discovered Plasma Cannon",     '', BoolType()),
        FieldDescriptor(0xaf, "Discovered Scepter",           '', BoolType()),
        FieldDescriptor(0xb0, "Discovered Hou Yi's Bow",      '', BoolType()),
        FieldDescriptor(0xb1, "Discovered Arrow of Light",    '', BoolType()),
        FieldDescriptor(0xb2, "Discovered Wooden Shield",     '', BoolType()),
        FieldDescriptor(0xb3, "Discovered Metal Shield",      '', BoolType()),
        FieldDescriptor(0xb4, "Discovered Idol",              '', BoolType()),
        FieldDescriptor(0xb5, "Discovered The Tusk Idol",     '', BoolType()),
        FieldDescriptor(0xb6, "Discovered Curse Pot",         '', BoolType()),
        FieldDescriptor(0xb7, "Discovered Ushabti",           '', BoolType()),
        FieldDescriptor(0xb8, "Discovered Eggplant",          '', BoolType()),
        FieldDescriptor(0xb9, "Discovered Cooked Turkey",     '', BoolType()),
        FieldDescriptor(0xba, "Discovered Elixir",            '', BoolType()),
        FieldDescriptor(0xbb, "Discovered Four-Leaf Clover",  '', BoolType()),
    ),
    'Journal Traps': (
        FieldDescriptor(0xbc, "Discovered Spikes",           '', BoolType()),
        FieldDescriptor(0xbd, "Discovered Arrow Trap",       '', BoolType()),
        FieldDescriptor(0xbe, "Discovered Bear Trap",        '', BoolType()),
        FieldDescriptor(0xbf, "Discovered Log Trap",         '', BoolType()),
        FieldDescriptor(0xc0, "Discovered Spear Trap",       '', BoolType()),
        FieldDescriptor(0xc1, "Discovered Thorny Vine",      '', BoolType()),
        FieldDescriptor(0xc2, "Discovered Snap Trap",        '', BoolType()),
        FieldDescriptor(0xc3, "Discovered Powder Box",       '', BoolType()),
        FieldDescriptor(0xc4, "Discovered Falling Platform", '', BoolType()),
        FieldDescriptor(0xc5, "Discovered Spikeball",        '', BoolType()),
        FieldDescriptor(0xc6, "Discovered Lion Trap",        '', BoolType()),
        FieldDescriptor(0xc7, "Discovered Giant Clam",       '', BoolType()),
        FieldDescriptor(0xc8, "Discovered Sliding Wall",     '', BoolType()),
        FieldDescriptor(0xc9, "Discovered Crush Trap",       '', BoolType()),
        FieldDescriptor(0xca, "Discovered Giant Crush Trap", '', BoolType()),
        FieldDescriptor(0xcb, "Discovered Boulder",          '', BoolType()),
        FieldDescriptor(0xcc, "Discovered Spring Trap",      '', BoolType()),
        FieldDescriptor(0xcd, "Discovered Landmine",         '', BoolType()),
        FieldDescriptor(0xce, "Discovered Laser Trap",       '', BoolType()),
        FieldDescriptor(0xcf, "Discovered Spark Trap",       '', BoolType()),
        FieldDescriptor(0xd0, "Discovered Frog Trap",        '', BoolType()),
        FieldDescriptor(0xd1, "Discovered Sticky Trap",      '', BoolType()),
        FieldDescriptor(0xd2, "Discovered Bone Drop",        '', BoolType()),
        FieldDescriptor(0xd3, "Discovered Egg Sac",          '', BoolType()),
    ),
    'Character Unlocks': (
        FieldDescriptor(0xe6, "Unlock field", '', FlagType(4, CharacterUnlockFlags)),
    ),
    'Shortcut Unlocks': (
        FieldDescriptor(0xeb, "Shortcut Progress", '', EnumType(1, ShortcutProgressEnum)),
    ),
    'Bestiary Defeated Counts': (
        FieldDescriptor(0x0ee, "Snake",             '', Int32Type()),
        FieldDescriptor(0x0f2, "Spider",            '', Int32Type()),
        FieldDescriptor(0x0f6, "Bat",               '', Int32Type()),
        FieldDescriptor(0x0fa, "Caveman",           '', Int32Type()),
        FieldDescriptor(0x0fe, "Skeleton",          '', Int32Type()),
        FieldDescriptor(0x102, "Horned Lizard",     '', Int32Type()),
        FieldDescriptor(0x106, "Moles",             '', Int32Type()),
        FieldDescriptor(0x10a, "Quillback",         '', Int32Type()),
        FieldDescriptor(0x10e, "Mantrap",           '', Int32Type()),
        FieldDescriptor(0x112, "Tiki Man",          '', Int32Type()),
        FieldDescriptor(0x116, "Witch Doctor",      '', Int32Type()),
        FieldDescriptor(0x11a, "Mosquito",          '', Int32Type()),
        FieldDescriptor(0x11e, "Monkey",            '', Int32Type()),
        FieldDescriptor(0x122, "Hang Spider",       '', Int32Type()),
        FieldDescriptor(0x126, "Giant Spider",      '', Int32Type()),
        FieldDescriptor(0x12a, "Magmar",            '', Int32Type()),
        FieldDescriptor(0x12e, "Robot",             '', Int32Type()),
        FieldDescriptor(0x132, "Fire Bug",          '', Int32Type()),
        FieldDescriptor(0x136, "Imp",               '', Int32Type()),
        FieldDescriptor(0x13a, "Lavamander",        '', Int32Type()),
        FieldDescriptor(0x13e, "Vampire",           '', Int32Type()),
        FieldDescriptor(0x142, "Vlad",              '', Int32Type()),
        FieldDescriptor(0x146, "Olmec",             '', Int32Type()),
        FieldDescriptor(0x14a, "Jiangshi",          '', Int32Type()),
        FieldDescriptor(0x14e, "Jiangshi Assassin", '', Int32Type()),
        FieldDescriptor(0x152, "Flying Fish",       '', Int32Type()),
        FieldDescriptor(0x156, "Octopy",            '', Int32Type()),
        FieldDescriptor(0x15a, "Hermit Crab",       '', Int32Type()),
        FieldDescriptor(0x15e, "Pangxie",           '', Int32Type()),
        FieldDescriptor(0x162, "Great Humphead",    '', Int32Type()),
        FieldDescriptor(0x166, "Kingu",             '', Int32Type()),
        FieldDescriptor(0x16a, "Crocman",           '', Int32Type()),
        FieldDescriptor(0x16e, "Cobra",             '', Int32Type()),
        FieldDescriptor(0x172, "Mummy",             '', Int32Type()),
        FieldDescriptor(0x176, "Sorceress",         '', Int32Type()),
        FieldDescriptor(0x17a, "Cat Mummy",         '', Int32Type()),
        FieldDescriptor(0x17e, "Necromancer",       '', Int32Type()),
        FieldDescriptor(0x182, "Anubis",            '', Int32Type()),
        FieldDescriptor(0x186, "Ammit",             '', Int32Type()),
        FieldDescriptor(0x18a, "Apep",              '', Int32Type()),
        FieldDescriptor(0x18e, "Anubis II",         '', Int32Type()),
        FieldDescriptor(0x192, "Osiris",            '', Int32Type()),
        FieldDescriptor(0x196, "Ufo",               '', Int32Type()),
        FieldDescriptor(0x19a, "Alien",             '', Int32Type()),
        FieldDescriptor(0x19e, "Yeti",              '', Int32Type()),
        FieldDescriptor(0x1a2, "Yeti King",         '', Int32Type()),
        FieldDescriptor(0x1a6, "Yeti Queen",        '', Int32Type()),
        FieldDescriptor(0x1aa, "Lahamu",            '', Int32Type()),
        FieldDescriptor(0x1ae, "Proto Shopkeeper",  '', Int32Type()),
        FieldDescriptor(0x1b2, "Olmite",            '', Int32Type()),
        FieldDescriptor(0x1b6, "Lamassu",           '', Int32Type()),
        FieldDescriptor(0x1ba, "Tiamat",            '', Int32Type()),
        FieldDescriptor(0x1be, "Tadpole",           '', Int32Type()),
        FieldDescriptor(0x1c2, "Frog",              '', Int32Type()),
        FieldDescriptor(0x1c6, "Fire Frog",         '', Int32Type()),
        FieldDescriptor(0x1ca, "Goliath Frog",      '', Int32Type()),
        FieldDescriptor(0x1ce, "Grub",              '', Int32Type()),
        FieldDescriptor(0x1d2, "Giant Fly",         '', Int32Type()),
        FieldDescriptor(0x1d6, "Hundun",            '', Int32Type()),
        FieldDescriptor(0x1da, "Eggplant Minister", '', Int32Type()),
        FieldDescriptor(0x1de, "Eggplup",           '', Int32Type()),
        FieldDescriptor(0x1e2, "Celestial Jelly",   '', Int32Type()),
        FieldDescriptor(0x1e6, "Scorpion",          '', Int32Type()),
        FieldDescriptor(0x1ea, "Bee",               '', Int32Type()),
        FieldDescriptor(0x1ee, "Queen Bee",         '', Int32Type()),
        FieldDescriptor(0x1f2, "Scarab",            '', Int32Type()),
        FieldDescriptor(0x1f6, "Golden Monkey",     '', Int32Type()),
        FieldDescriptor(0x1fa, "Leprechaun",        '', Int32Type()),
        FieldDescriptor(0x1fe, "Monty",             '', Int32Type()),
        FieldDescriptor(0x202, "Percy",             '', Int32Type()),
        FieldDescriptor(0x206, "Poochi",            '', Int32Type()),
        FieldDescriptor(0x20a, "Ghist",             '', Int32Type()),
        FieldDescriptor(0x20e, "Ghost",             '', Int32Type()),
        FieldDescriptor(0x212, "Cave Turkey",       '', Int32Type()),
        FieldDescriptor(0x216, "Rock Dog",          '', Int32Type()),
        FieldDescriptor(0x21a, "Axolotl",           '', Int32Type()),
        FieldDescriptor(0x21e, "Qilin",             '', Int32Type()),
        FieldDescriptor(0x222, "Mech Rider",        '', Int32Type()),
    ),
    'Bestiary Killed by Counts': (
        FieldDescriptor(0x226, "Snake",             '', Int32Type()),
        FieldDescriptor(0x22a, "Spider",            '', Int32Type()),
        FieldDescriptor(0x22e, "Bat",               '', Int32Type()),
        FieldDescriptor(0x232, "Caveman",           '', Int32Type()),
        FieldDescriptor(0x236, "Skeleton",          '', Int32Type()),
        FieldDescriptor(0x23a, "Horned Lizard",     '', Int32Type()),
        FieldDescriptor(0x23e, "Moles",             '', Int32Type()),
        FieldDescriptor(0x242, "Quillback",         '', Int32Type()),
        FieldDescriptor(0x246, "Mantrap",           '', Int32Type()),
        FieldDescriptor(0x24a, "Tiki Man",          '', Int32Type()),
        FieldDescriptor(0x24e, "Witch Doctor",      '', Int32Type()),
        FieldDescriptor(0x252, "Mosquito",          '', Int32Type()),
        FieldDescriptor(0x256, "Monkey",            '', Int32Type()),
        FieldDescriptor(0x25a, "Hang Spider",       '', Int32Type()),
        FieldDescriptor(0x25e, "Giant Spider",      '', Int32Type()),
        FieldDescriptor(0x262, "Magmar",            '', Int32Type()),
        FieldDescriptor(0x266, "Robot",             '', Int32Type()),
        FieldDescriptor(0x26a, "Fire Bug",          '', Int32Type()),
        FieldDescriptor(0x26e, "Imp",               '', Int32Type()),
        FieldDescriptor(0x272, "Lavamander",        '', Int32Type()),
        FieldDescriptor(0x276, "Vampire",           '', Int32Type()),
        FieldDescriptor(0x27a, "Vlad",              '', Int32Type()),
        FieldDescriptor(0x27e, "Olmec",             '', Int32Type()),
        FieldDescriptor(0x282, "Jiangshi",          '', Int32Type()),
        FieldDescriptor(0x286, "Jiangshi Assassin", '', Int32Type()),
        FieldDescriptor(0x28a, "Flying Fish",       '', Int32Type()),
        FieldDescriptor(0x28e, "Octopy",            '', Int32Type()),
        FieldDescriptor(0x292, "Hermit Crab",       '', Int32Type()),
        FieldDescriptor(0x296, "Pangxie",           '', Int32Type()),
        FieldDescriptor(0x29a, "Great Humphead",    '', Int32Type()),
        FieldDescriptor(0x29e, "Kingu",             '', Int32Type()),
        FieldDescriptor(0x2a2, "Crocman",           '', Int32Type()),
        FieldDescriptor(0x2a6, "Cobra",             '', Int32Type()),
        FieldDescriptor(0x2aa, "Mummy",             '', Int32Type()),
        FieldDescriptor(0x2ae, "Sorceress",         '', Int32Type()),
        FieldDescriptor(0x2b2, "Cat Mummy",         '', Int32Type()),
        FieldDescriptor(0x2b6, "Necromancer",       '', Int32Type()),
        FieldDescriptor(0x2ba, "Anubis",            '', Int32Type()),
        FieldDescriptor(0x2be, "Ammit",             '', Int32Type()),
        FieldDescriptor(0x2c2, "Apep",              '', Int32Type()),
        FieldDescriptor(0x2c6, "Anubis II",         '', Int32Type()),
        FieldDescriptor(0x2ca, "Osiris",            '', Int32Type()),
        FieldDescriptor(0x2ce, "Ufo",               '', Int32Type()),
        FieldDescriptor(0x2d2, "Alien",             '', Int32Type()),
        FieldDescriptor(0x2d6, "Yeti",              '', Int32Type()),
        FieldDescriptor(0x2da, "Yeti King",         '', Int32Type()),
        FieldDescriptor(0x2de, "Yeti Queen",        '', Int32Type()),
        FieldDescriptor(0x2e2, "Lahamu",            '', Int32Type()),
        FieldDescriptor(0x2e6, "Proto Shopkeeper",  '', Int32Type()),
        FieldDescriptor(0x2ea, "Olmite",            '', Int32Type()),
        FieldDescriptor(0x2ee, "Lamassu",           '', Int32Type()),
        FieldDescriptor(0x2f2, "Tiamat",            '', Int32Type()),
        FieldDescriptor(0x2f6, "Tadpole",           '', Int32Type()),
        FieldDescriptor(0x2fa, "Frog",              '', Int32Type()),
        FieldDescriptor(0x2fe, "Fire Frog",         '', Int32Type()),
        FieldDescriptor(0x302, "Goliath Frog",      '', Int32Type()),
        FieldDescriptor(0x306, "Grub",              '', Int32Type()),
        FieldDescriptor(0x30a, "Giant Fly",         '', Int32Type()),
        FieldDescriptor(0x30e, "Hundun",            '', Int32Type()),
        FieldDescriptor(0x312, "Eggplant Minister", '', Int32Type()),
        FieldDescriptor(0x316, "Eggplup",           '', Int32Type()),
        FieldDescriptor(0x31a, "Celestial Jelly",   '', Int32Type()),
        FieldDescriptor(0x31e, "Scorpion",          '', Int32Type()),
        FieldDescriptor(0x322, "Bee",               '', Int32Type()),
        FieldDescriptor(0x326, "Queen Bee",         '', Int32Type()),
        FieldDescriptor(0x32a, "Scarab",            '', Int32Type()),
        FieldDescriptor(0x32e, "Golden Monkey",     '', Int32Type()),
        FieldDescriptor(0x332, "Leprechaun",        '', Int32Type()),
        FieldDescriptor(0x336, "Monty",             '', Int32Type()),
        FieldDescriptor(0x33a, "Percy",             '', Int32Type()),
        FieldDescriptor(0x33e, "Poochi",            '', Int32Type()),
        FieldDescriptor(0x342, "Ghist",             '', Int32Type()),
        FieldDescriptor(0x346, "Ghost",             '', Int32Type()),
        FieldDescriptor(0x34a, "Cave Turkey",       '', Int32Type()),
        FieldDescriptor(0x34e, "Rock Dog",          '', Int32Type()),
        FieldDescriptor(0x352, "Axolotl",           '', Int32Type()),
        FieldDescriptor(0x356, "Qilin",             '', Int32Type()),
        FieldDescriptor(0x35a, "Mech Rider",        '', Int32Type()),
    ),
    'People Defeated Counts': (
        FieldDescriptor(0x3b2, "Hired Hand",         '', Int32Type()),
        FieldDescriptor(0x3b6, "Eggplant Child",     '', Int32Type()),
        FieldDescriptor(0x3ba, "Shopkeeper",         '', Int32Type()),
        FieldDescriptor(0x3be, "Tun",                '', Int32Type()),
        FieldDescriptor(0x3c2, "Yang",               '', Int32Type()),
        FieldDescriptor(0x3c6, "Madame Tusk",        '', Int32Type()),
        FieldDescriptor(0x3ca, "Tusk's Bodyguard",   '', Int32Type()),
        FieldDescriptor(0x3ce, "Waddler",            '', Int32Type()),
        FieldDescriptor(0x3d2, "Caveman Shopkeeper", '', Int32Type()),
        FieldDescriptor(0x3d6, "Ghist Shopkeeper",   '', Int32Type()),
        FieldDescriptor(0x3da, "Van Horsing",        '', Int32Type()),
        FieldDescriptor(0x3de, "Parsley",            '', Int32Type()),
        FieldDescriptor(0x3e2, "Parsnip",            '', Int32Type()),
        FieldDescriptor(0x3e6, "Parmesan",           '', Int32Type()),
        FieldDescriptor(0x3ea, "Sparrow",            '', Int32Type()),
        FieldDescriptor(0x3ee, "Beg",                '', Int32Type()),
        FieldDescriptor(0x3f2, "Eggplant King",      '', Int32Type()),
    ),
    'People Killed by Counts': (
        FieldDescriptor(0x44a, "Hired Hand",         '', Int32Type()),
        FieldDescriptor(0x44e, "Eggplant Child",     '', Int32Type()),
        FieldDescriptor(0x452, "Shopkeeper",         '', Int32Type()),
        FieldDescriptor(0x456, "Tun",                '', Int32Type()),
        FieldDescriptor(0x45a, "Yang",               '', Int32Type()),
        FieldDescriptor(0x45e, "Madame Tusk",        '', Int32Type()),
        FieldDescriptor(0x462, "Tusk's Bodyguard",   '', Int32Type()),
        FieldDescriptor(0x466, "Waddler",            '', Int32Type()),
        FieldDescriptor(0x46a, "Caveman Shopkeeper", '', Int32Type()),
        FieldDescriptor(0x46e, "Ghist Shopkeeper",   '', Int32Type()),
        FieldDescriptor(0x472, "Van Horsing",        '', Int32Type()),
        FieldDescriptor(0x476, "Parsley",            '', Int32Type()),
        FieldDescriptor(0x47a, "Parsnip",            '', Int32Type()),
        FieldDescriptor(0x47e, "Parmesan",           '', Int32Type()),
        FieldDescriptor(0x482, "Sparrow",            '', Int32Type()),
        FieldDescriptor(0x486, "Beg",                '', Int32Type()),
        FieldDescriptor(0x48a, "Eggplant King",      '', Int32Type()),
    ),
}

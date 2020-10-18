from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import IntFlag, auto
import struct

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
        return struct.unpack('<i', binary)[0]

    def to_binary(self, value):
        return struct.pack('<i', value)

class ByteType(Type):
    @property
    def size(self):
        return 1

    def from_binary(self, binary):
        return binary[0]

    def to_binary(self, value):
        return bytes([value])

class FlagType(Type):
    flag_definition = None

    @property
    def size(self):
        return 4

    def __init__(self, flag_definition):
        self.flag_definition = flag_definition

    def from_binary(self, binary):
        return self.flag_definition(struct.unpack('<i', binary)[0])

    def to_binary(self, value):
        return bytes([value])

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
        FieldDescriptor(0xe6, "Unlock field", '', FlagType(CharacterUnlockFlags)),
    ),
}

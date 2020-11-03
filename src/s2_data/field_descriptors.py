from dataclasses import dataclass
from enum import IntFlag, IntEnum
import typing
from .field_types import *

class CharacterUnlockFlags(IntFlag):
    Ana        = 1 << 0
    Margaret   = 1 << 1
    Colin      = 1 << 2
    Roffy      = 1 << 3
    Alto       = 1 << 4
    Liz        = 1 << 5
    Nekka      = 1 << 6
    LISE       = 1 << 7
    Coco       = 1 << 8
    Manfred    = 1 << 9
    Jay        = 1 << 10
    Tina       = 1 << 11
    Valerie    = 1 << 12
    Au         = 1 << 13
    Demi       = 1 << 14
    Pilot      = 1 << 15
    Airyn      = 1 << 16
    Dirk       = 1 << 17
    Guy        = 1 << 18
    ClassicGuy = 1 << 19

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

class CharacterSelectedEnum(IntEnum):
    Ana        = 0x00
    Margaret   = 0x01
    Colin      = 0x02
    Roffy      = 0x03
    Alto       = 0x04
    Liz        = 0x05
    Nekka      = 0x06
    LISE       = 0x07
    Coco       = 0x08
    Manfred    = 0x09
    Jay        = 0x0a
    Tina       = 0x0b
    Valerie    = 0x0c
    Au         = 0x0d
    Demi       = 0x0e
    Pilot      = 0x0f
    Airyn      = 0x10
    Dirk       = 0x11
    Guy        = 0x12
    ClassicGuy = 0x13

class StickerEnum(IntEnum):
    NoSticker = 0x00

    Ana        = 0xc1
    Margaret   = 0xc2
    Colin      = 0xc3
    Roffy      = 0xc4
    Alto       = 0xc5
    Liz        = 0xc6
    Nekka      = 0xc7
    LISE       = 0xc8
    Coco       = 0xc9
    Manfred    = 0xca
    Jay        = 0xcb
    Tina       = 0xcc
    Valerie    = 0xcd
    Au         = 0xce
    Demi       = 0xcf
    Pilot      = 0xd0
    Airyn      = 0xd1
    Dirk       = 0xd2
    Guy        = 0xd3
    ClassicGuy = 0xd4

    Caveman      = 0xe1
    Quillback    = 0xe7
    Vlad         = 0xf5
    Anubis       = 0xfc
    Osiris       = 0x100
    AlienQueen   = 0x10e
    Kingu        = 0x118
    Tiamat       = 0x119
    EggplantKing = 0x122
    Hundun       = 0x123
    Shopkeeper   = 0x127
    Tun          = 0x128
    Yang         = 0x129
    Parsley      = 0x12b
    Parsnip      = 0x12c
    Parmesan     = 0x12d
    VanHorsing   = 0x12e
    Sparrow      = 0x12f

    Idol = 0x163

    Paste           = 0x216
    ClimbingGloves  = 0x217
    SpikeShoes      = 0x218
    SpringShoes     = 0x219
    Kapala          = 0x21a
    Spectacles      = 0x21b
    PitchersMitt    = 0x21c
    UdjatEye        = 0x21d
    Parachute       = 0x21e
    Compass         = 0x21f
    AlienCompass    = 0x220
    Hedjet          = 0x221
    Crown           = 0x222
    EggplantCrown   = 0x223
    TrueCrown       = 0x224
    Ankh            = 0x225
    TabletOfDestiny = 0x226
    SkeletonKey     = 0x227

    Cape      = 0x229
    VladsCape = 0x22a
    Jetpack   = 0x22c
    Telepack  = 0x22f
    Hoverpack = 0x231
    Powerpack = 0x233

    Olmec = 0x25a

StickerType = EnumType(4, StickerEnum)

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
        'four_leaf_clover':  FieldDescriptor(0xbb, "Four-Leaf Clover",  BoolType()),
    }),
    'traps_discovered': Category('Journal: Traps Discovered', {
        'spikes':           FieldDescriptor(0xbc, "Spikes",           BoolType()),
        'arrow_trap':       FieldDescriptor(0xbd, "Arrow Trap",       BoolType()),
        'bear_trap':        FieldDescriptor(0xbe, "Totem Trap",       BoolType()),
        'log_trap':         FieldDescriptor(0xbf, "Log Trap",         BoolType()),
        'spear_trap':       FieldDescriptor(0xc0, "Spear Trap",       BoolType()),
        'thorny_vine':      FieldDescriptor(0xc1, "Thorny Vine",      BoolType()),
        'snap_trap':        FieldDescriptor(0xc2, "Bear Trap",        BoolType()),
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
    'area_deaths': Category('Area Death Counts', {
        'level_1_1':  FieldDescriptor(0x08b2, "1-1",  Int32Type()),
        'level_1_2':  FieldDescriptor(0x08b6, "1-2",  Int32Type()),
        'level_1_3':  FieldDescriptor(0x08ba, "1-3",  Int32Type()),
        'level_1_4':  FieldDescriptor(0x08be, "1-4",  Int32Type()),
        'level_2_1':  FieldDescriptor(0x0cae, "2-1",  Int32Type()),
        'level_2_2':  FieldDescriptor(0x0cb2, "2-2",  Int32Type()),
        'level_2_3':  FieldDescriptor(0x0cb6, "2-3",  Int32Type()),
        'level_2_4':  FieldDescriptor(0x0cba, "2-4",  Int32Type()),
        'level_3_1':  FieldDescriptor(0x10aa, "3-1",  Int32Type()),
        'level_4_1':  FieldDescriptor(0x14a6, "4-1",  Int32Type()),
        'level_4_2':  FieldDescriptor(0x14aa, "4-2",  Int32Type()),
        'level_4_3':  FieldDescriptor(0x14ae, "4-3",  Int32Type()),
        'level_4_4':  FieldDescriptor(0x14b2, "4-4",  Int32Type()),
        'level_5_1':  FieldDescriptor(0x18a2, "5-1",  Int32Type()),
        'level_6_1':  FieldDescriptor(0x1c9e, "6-1",  Int32Type()),
        'level_6_2':  FieldDescriptor(0x1ca2, "6-2",  Int32Type()),
        'level_6_3':  FieldDescriptor(0x1ca6, "6-3",  Int32Type()),
        'level_6_4':  FieldDescriptor(0x1caa, "6-4",  Int32Type()),
        'level_7_1':  FieldDescriptor(0x209a, "7-1",  Int32Type()),
        'level_7_2':  FieldDescriptor(0x209e, "7-2",  Int32Type()),
        'level_7_3':  FieldDescriptor(0x20a2, "7-3",  Int32Type()),
        'level_7_4':  FieldDescriptor(0x20a6, "7-4",  Int32Type()),
        'level_7_5':  FieldDescriptor(0x20aa, "7-5",  Int32Type()),
        'level_7_6':  FieldDescriptor(0x20ae, "7-6",  Int32Type()),
        'level_7_7':  FieldDescriptor(0x20b2, "7-7",  Int32Type()),
        'level_7_8':  FieldDescriptor(0x20b6, "7-8",  Int32Type()),
        'level_7_9':  FieldDescriptor(0x20ba, "7-9",  Int32Type()),
        'level_7_10': FieldDescriptor(0x20be, "7-10", Int32Type()),
        'level_7_11': FieldDescriptor(0x20c2, "7-11", Int32Type()),
        'level_7_12': FieldDescriptor(0x20c6, "7-12", Int32Type()),
        'level_7_13': FieldDescriptor(0x20ca, "7-13", Int32Type()),
        'level_7_14': FieldDescriptor(0x20ce, "7-14", Int32Type()),
        'level_7_15': FieldDescriptor(0x20d2, "7-15", Int32Type()),
        'level_7_16': FieldDescriptor(0x20d6, "7-16", Int32Type()),
        'level_7_17': FieldDescriptor(0x20da, "7-17", Int32Type()),
        'level_7_18': FieldDescriptor(0x20de, "7-18", Int32Type()),
        'level_7_19': FieldDescriptor(0x20e2, "7-19", Int32Type()),
        'level_7_20': FieldDescriptor(0x20e6, "7-20", Int32Type()),
        'level_7_21': FieldDescriptor(0x20ea, "7-21", Int32Type()),
        'level_7_22': FieldDescriptor(0x20ee, "7-22", Int32Type()),
        'level_7_23': FieldDescriptor(0x20f2, "7-23", Int32Type()),
        'level_7_24': FieldDescriptor(0x20f6, "7-24", Int32Type()),
        'level_7_25': FieldDescriptor(0x20fa, "7-25", Int32Type()),
        'level_7_26': FieldDescriptor(0x20fe, "7-26", Int32Type()),
        'level_7_27': FieldDescriptor(0x2102, "7-27", Int32Type()),
        'level_7_28': FieldDescriptor(0x2106, "7-28", Int32Type()),
        'level_7_29': FieldDescriptor(0x210a, "7-29", Int32Type()),
        'level_7_30': FieldDescriptor(0x210e, "7-30", Int32Type()),
        'level_7_31': FieldDescriptor(0x2112, "7-31", Int32Type()),
        'level_7_32': FieldDescriptor(0x2116, "7-32", Int32Type()),
        'level_7_33': FieldDescriptor(0x211a, "7-33", Int32Type()),
        'level_7_34': FieldDescriptor(0x211e, "7-34", Int32Type()),
        'level_7_35': FieldDescriptor(0x2122, "7-35", Int32Type()),
        'level_7_36': FieldDescriptor(0x2126, "7-36", Int32Type()),
        'level_7_37': FieldDescriptor(0x212a, "7-37", Int32Type()),
        'level_7_38': FieldDescriptor(0x212e, "7-38", Int32Type()),
        'level_7_39': FieldDescriptor(0x2132, "7-39", Int32Type()),
        'level_7_40': FieldDescriptor(0x2136, "7-40", Int32Type()),
        'level_7_41': FieldDescriptor(0x213a, "7-41", Int32Type()),
        'level_7_42': FieldDescriptor(0x213e, "7-42", Int32Type()),
        'level_7_43': FieldDescriptor(0x2142, "7-43", Int32Type()),
        'level_7_44': FieldDescriptor(0x2146, "7-44", Int32Type()),
        'level_7_45': FieldDescriptor(0x214a, "7-45", Int32Type()),
        'level_7_46': FieldDescriptor(0x214e, "7-46", Int32Type()),
        'level_7_47': FieldDescriptor(0x2152, "7-47", Int32Type()),
        'level_7_48': FieldDescriptor(0x2156, "7-48", Int32Type()),
        'level_7_49': FieldDescriptor(0x215a, "7-49", Int32Type()),
        'level_7_50': FieldDescriptor(0x215e, "7-50", Int32Type()),
        'level_7_51': FieldDescriptor(0x2162, "7-51", Int32Type()),
        'level_7_52': FieldDescriptor(0x2166, "7-52", Int32Type()),
        'level_7_53': FieldDescriptor(0x216a, "7-53", Int32Type()),
        'level_7_54': FieldDescriptor(0x216e, "7-54", Int32Type()),
        'level_7_55': FieldDescriptor(0x2172, "7-55", Int32Type()),
        'level_7_56': FieldDescriptor(0x2176, "7-56", Int32Type()),
        'level_7_57': FieldDescriptor(0x217a, "7-57", Int32Type()),
        'level_7_58': FieldDescriptor(0x217e, "7-58", Int32Type()),
        'level_7_59': FieldDescriptor(0x2182, "7-59", Int32Type()),
        'level_7_60': FieldDescriptor(0x2186, "7-60", Int32Type()),
        'level_7_61': FieldDescriptor(0x218a, "7-61", Int32Type()),
        'level_7_62': FieldDescriptor(0x218e, "7-62", Int32Type()),
        'level_7_63': FieldDescriptor(0x2192, "7-63", Int32Type()),
        'level_7_64': FieldDescriptor(0x2196, "7-64", Int32Type()),
        'level_7_65': FieldDescriptor(0x219a, "7-65", Int32Type()),
        'level_7_66': FieldDescriptor(0x219e, "7-66", Int32Type()),
        'level_7_67': FieldDescriptor(0x21a2, "7-67", Int32Type()),
        'level_7_68': FieldDescriptor(0x21a6, "7-68", Int32Type()),
        'level_7_69': FieldDescriptor(0x21aa, "7-69", Int32Type()),
        'level_7_70': FieldDescriptor(0x21ae, "7-70", Int32Type()),
        'level_7_71': FieldDescriptor(0x21b2, "7-71", Int32Type()),
        'level_7_72': FieldDescriptor(0x21b6, "7-72", Int32Type()),
        'level_7_73': FieldDescriptor(0x21ba, "7-73", Int32Type()),
        'level_7_74': FieldDescriptor(0x21be, "7-74", Int32Type()),
        'level_7_75': FieldDescriptor(0x21c2, "7-75", Int32Type()),
        'level_7_76': FieldDescriptor(0x21c6, "7-76", Int32Type()),
        'level_7_77': FieldDescriptor(0x21ca, "7-77", Int32Type()),
        'level_7_78': FieldDescriptor(0x21ce, "7-78", Int32Type()),
        'level_7_79': FieldDescriptor(0x21d2, "7-79", Int32Type()),
        'level_7_80': FieldDescriptor(0x21d6, "7-80", Int32Type()),
        'level_7_81': FieldDescriptor(0x21da, "7-81", Int32Type()),
        'level_7_82': FieldDescriptor(0x21de, "7-82", Int32Type()),
        'level_7_83': FieldDescriptor(0x21e2, "7-83", Int32Type()),
        'level_7_84': FieldDescriptor(0x21e6, "7-84", Int32Type()),
        'level_7_85': FieldDescriptor(0x21ea, "7-85", Int32Type()),
        'level_7_86': FieldDescriptor(0x21ee, "7-86", Int32Type()),
        'level_7_87': FieldDescriptor(0x21f2, "7-87", Int32Type()),
        'level_7_88': FieldDescriptor(0x21f6, "7-88", Int32Type()),
        'level_7_89': FieldDescriptor(0x21fa, "7-89", Int32Type()),
        'level_7_90': FieldDescriptor(0x21fe, "7-90", Int32Type()),
        'level_7_91': FieldDescriptor(0x2202, "7-91", Int32Type()),
        'level_7_92': FieldDescriptor(0x2206, "7-92", Int32Type()),
        'level_7_93': FieldDescriptor(0x220a, "7-93", Int32Type()),
        'level_7_94': FieldDescriptor(0x220e, "7-94", Int32Type()),
        'level_7_95': FieldDescriptor(0x2212, "7-95", Int32Type()),
        'level_7_96': FieldDescriptor(0x2216, "7-96", Int32Type()),
        'level_7_97': FieldDescriptor(0x221a, "7-97", Int32Type()),
        'level_7_98': FieldDescriptor(0x221e, "7-98", Int32Type()),
    }),
    'character_deaths': Category('Character Death Counts', {
        'ana_spelunky':      FieldDescriptor(0x289a, "Ana Spelunky",      Int32Type()),
        'margaret_tunnel':   FieldDescriptor(0x289e, "Margaret Tunnel",   Int32Type()),
        'colin_northward':   FieldDescriptor(0x28a2, "Colin Northward",   Int32Type()),
        'roffy_sloth':       FieldDescriptor(0x28a6, "Roffy D. Sloth",    Int32Type()),
        'alto_singh':        FieldDescriptor(0x28aa, "Alto Singh",        Int32Type()),
        'liz_mutton':        FieldDescriptor(0x28ae, "Liz Mutton",        Int32Type()),
        'nekka_the_eagle':   FieldDescriptor(0x28b2, "Nekka the Eagle",   Int32Type()),
        'lise_project':      FieldDescriptor(0x28b6, "Lise Project",      Int32Type()),
        'coco_von_diamonds': FieldDescriptor(0x28ba, "Coco von Diamonds", Int32Type()),
        'manfred_tunnel':    FieldDescriptor(0x28be, "Manfred Tunnel",    Int32Type()),
        'little_jay':        FieldDescriptor(0x28c2, "Little Jay",        Int32Type()),
        'tina_flan':         FieldDescriptor(0x28c6, "Tina Flan",         Int32Type()),
        'valerie_crump':     FieldDescriptor(0x28ca, "Valerie Crump",     Int32Type()),
        'au':                FieldDescriptor(0x28ce, "Au",                Int32Type()),
        'demi_von_diamonds': FieldDescriptor(0x28d2, "Demi von Diamonds", Int32Type()),
        'pilot':             FieldDescriptor(0x28d6, "Pilot",             Int32Type()),
        'princess_airyn':    FieldDescriptor(0x28da, "Princess Airyn",    Int32Type()),
        'dirk_yamaoka':      FieldDescriptor(0x28de, "Dirk Yamaoka",      Int32Type()),
        'guy_spelunky':      FieldDescriptor(0x28e2, "Guy Spelunky",      Int32Type()),
        'classic_spelunky':  FieldDescriptor(0x28e6, "Classic Spelunky",  Int32Type()),
    }),
    'completion': Category('Completion', {
        'normal':  FieldDescriptor(0x2901, "Completed the game (Normal)",                    BoolType()),
        'ironman': FieldDescriptor(0x2902, "Completed the game with no shortcuts (Ironman)", BoolType()),
        'hard':    FieldDescriptor(0x2903, "Completed the game (Hard)",                      BoolType()),
    }),
    'viewed_player_profile': Category('Viewed Player Profile', {
        'viewed': FieldDescriptor(0x2904, 'Viewed', BoolType()),
    }),
    'unlocked_seeded_runs': Category('Seeded Runs Unlocked', {
        'unlocked': FieldDescriptor(0x2905, 'Unlocked', BoolType()),
    }),
    'last_game_played': Category('Last Game Played', {
        'area':  FieldDescriptor(0x2906, 'Area',  ByteType()),
        'level': FieldDescriptor(0x2907, 'Level', ByteType()),
        'money': FieldDescriptor(0x290a, 'Money', Int32Type()),
        'time':  FieldDescriptor(0x290e, 'Time',  Int32Type()),
    }),
    'stickers': Category('Stickers', {
        'sticker_1': FieldDescriptor(0x2912, 'Sticker 1', StickerType),
        'sticker_2': FieldDescriptor(0x2916, 'Sticker 2', StickerType),
        'sticker_3': FieldDescriptor(0x291a, 'Sticker 3', StickerType),
        'sticker_4': FieldDescriptor(0x291e, 'Sticker 4', StickerType),
        'sticker_5': FieldDescriptor(0x2922, 'Sticker 5', StickerType),
        'sticker_6': FieldDescriptor(0x2926, 'Sticker 6', StickerType),
        'sticker_7': FieldDescriptor(0x292a, 'Sticker 7', StickerType),
        'sticker_8': FieldDescriptor(0x292e, 'Sticker 8', StickerType),
        'sticker_9': FieldDescriptor(0x2932, 'Sticker 9', StickerType),
    }),
    'character_selected': Category('Player - Character Selection', {
        'player_1': FieldDescriptor(0x2a7a, "Player 1", EnumType(1, CharacterSelectedEnum)),
        'player_2': FieldDescriptor(0x2a7b, "Player 2", EnumType(1, CharacterSelectedEnum)),
        'player_3': FieldDescriptor(0x2a7c, "Player 3", EnumType(1, CharacterSelectedEnum)),
        'player_4': FieldDescriptor(0x2a7d, "Player 4", EnumType(1, CharacterSelectedEnum)),
    }),
    'crc': Category('CRC32', {
        'crc': FieldDescriptor(0x359a, 'CRC32', UInt32Type())
    }),
}

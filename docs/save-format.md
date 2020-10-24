# Credits

The following people helped out tremendously in the Spelunky Community Discord:
https://mossranking.com/discord

 * dextercd#7326
    - Journal Entry Unlocks - https://pastebin.com/jEAGuxGD
    - Constellations - https://pastebin.com/0pZZPt9F
 * EngIo#7610
 * iojonmbnmb#8149
 * gary#9999


# TODO

 - [ ] Constellations
 - [ ] Last Played
   - [ ] Last Played Character
 - [ ] Format Raw Data


# Types

 * byte    - 1 Byte. Unknown type.
 * bool    - 1 Byte. 0x0 or 0x1
 * int     - 32 bit Integer. Little Endian
 * int64   - 64 bit Integer. Little Endian
 * float   - 32 bit Float. Little Endian
 * time    - 32 bit Integer. Multiply by 16.67 to get milliseconds.
 * time64  - 64 bit Integer. Multiply by 16.67 to get milliseconds.


# Save Format

## Magic Number

```
00: byte - 19
01: byte - 00
```

## Journal Entry Unlocks

### Places

```
02: bool - Discovered Dwelling
03: bool - Discovered Jungle
04: bool - Discovered Volcana
05: bool - Discovered Olmec's Lair
06: bool - Discovered Tide Pool
07: bool - Discovered Abzu
08: bool - Discovered Temple of Anubis
09: bool - Discovered The City of Gold
0a: bool - Discovered Duat
0b: bool - Discovered Ice Caves
0c: bool - Discovered Neo Babylon
0d: bool - Discovered Tiamat's Throne
0e: bool - Discovered Sunken City
0f: bool - Discovered Eggplant World
10: bool - Discovered Hundun's Hideaway
11: bool - Discovered Cosmic Ocean
```

### Bestiary
```
 12: bool - Discovered Snake
 13: bool - Discovered Spider
 14: bool - Discovered Bat
 15: bool - Discovered Caveman
 16: bool - Discovered Skeleton
 17: bool - Discovered Horned Lizard
 18: bool - Discovered Moles
 19: bool - Discovered Quillback
 1a: bool - Discovered Mantrap
 1b: bool - Discovered Tiki Man
 1c: bool - Discovered Witch Doctor
 1d: bool - Discovered Mosquito
 1e: bool - Discovered Monkey
 1f: bool - Discovered Hang Spider
 20: bool - Discovered Giant Spider
 21: bool - Discovered Magmar
 22: bool - Discovered Robot
 23: bool - Discovered Fire Bug
 24: bool - Discovered Imp
 25: bool - Discovered Lavamander
 26: bool - Discovered Vampire
 27: bool - Discovered Vlad
 28: bool - Discovered Olmec
 29: bool - Discovered Jiangshi
 2a: bool - Discovered Jiangshi Assassin
 2b: bool - Discovered Flying Fish
 2c: bool - Discovered Octopy
 2d: bool - Discovered Hermit Crab
 2e: bool - Discovered Pangxie
 2f: bool - Discovered Great Humphead
 30: bool - Discovered Kingu
 31: bool - Discovered Crocman
 32: bool - Discovered Cobra
 33: bool - Discovered Mummy
 34: bool - Discovered Sorceress
 35: bool - Discovered Cat Mummy
 36: bool - Discovered Necromancer
 37: bool - Discovered Anubis
 38: bool - Discovered Ammit
 39: bool - Discovered Apep
 3a: bool - Discovered Anubis II
 3b: bool - Discovered Osiris
 3c: bool - Discovered Ufo
 3d: bool - Discovered Alien
 3e: bool - Discovered Yeti
 3f: bool - Discovered Yeti King
 40: bool - Discovered Yeti Queen
 41: bool - Discovered Lahamu
 42: bool - Discovered Proto Shopkeeper
 43: bool - Discovered Olmite
 44: bool - Discovered Lamassu
 45: bool - Discovered Tiamat
 46: bool - Discovered Tadpole
 47: bool - Discovered Frog
 48: bool - Discovered Fire Frog
 49: bool - Discovered Goliath Frog
 4a: bool - Discovered Grub
 4b: bool - Discovered Giant Fly
 4c: bool - Discovered Hundun
 4d: bool - Discovered Eggplant Minister
 4e: bool - Discovered Eggplup
 4f: bool - Discovered Celestial Jelly
 50: bool - Discovered Scorpion
 51: bool - Discovered Bee
 52: bool - Discovered Queen Bee
 53: bool - Discovered Scarab
 54: bool - Discovered Golden Monkey
 55: bool - Discovered Leprechaun
 56: bool - Discovered Monty
 57: bool - Discovered Percy
 58: bool - Discovered Poochi
 59: bool - Discovered Ghist
 5a: bool - Discovered Ghost
 5b: bool - Discovered Cave Turkey
 5c: bool - Discovered Rock Dog
 5d: bool - Discovered Axolotl
 5e: bool - Discovered Qilin
 5f: bool - Discovered Mech Rider
```

### People

```
 60: bool - Discovered Ana Spelunky
 61: bool - Discovered Margaret Tunnel
 62: bool - Discovered Colin Northward
 63: bool - Discovered Roffy D. Sloth
 64: bool - Discovered Alto Singh
 65: bool - Discovered Liz Mutton
 66: bool - Discovered Nekka the Eagle
 67: bool - Discovered Lise Project
 68: bool - Discovered Coco von Diamonds
 69: bool - Discovered Manfred Tunnel
 6a: bool - Discovered Little Jay
 6b: bool - Discovered Tina Flan
 6c: bool - Discovered Valerie Crump
 6d: bool - Discovered Au
 6e: bool - Discovered Demi von Diamonds
 6f: bool - Discovered Pilot
 70: bool - Discovered Princess Airyn
 71: bool - Discovered Dirk Yamaoka
 72: bool - Discovered Guy Spelunky
 73: bool - Discovered Classic Spelunky
 74: bool - Discovered Terra Tunnel
 75: bool - Discovered Hired Hand
 76: bool - Discovered Eggplant Child
 77: bool - Discovered Shopkeeper
 78: bool - Discovered Tun
 79: bool - Discovered Yang
 7a: bool - Discovered Madame Tusk
 7b: bool - Discovered Tusk's Bodyguard
 7c: bool - Discovered Waddler
 7d: bool - Discovered Caveman Shopkeeper
 7e: bool - Discovered Ghist Shopkeeper
 7f: bool - Discovered Van Horsing
 80: bool - Discovered Parsley
 81: bool - Discovered Parsnip
 82: bool - Discovered Parmesan
 83: bool - Discovered Sparrow
 84: bool - Discovered Beg
 85: bool - Discovered Eggplant King
```

### Items

```
 86: bool - Discovered Rope Pile
 87: bool - Discovered Bomb Bag
 88: bool - Discovered Bomb Box
 89: bool - Discovered Paste
 8a: bool - Discovered Spectacles
 8b: bool - Discovered Climbing Gloves
 8c: bool - Discovered Pitcher's Mitt
 8d: bool - Discovered Spring Shoes
 8e: bool - Discovered Spike Shoes
 8f: bool - Discovered Compass
 90: bool - Discovered Alien Compass
 91: bool - Discovered Parachute
 92: bool - Discovered Udjat Eye
 93: bool - Discovered Kapala
 94: bool - Discovered Hedjet
 95: bool - Discovered Crown
 96: bool - Discovered Eggplant Crown
 97: bool - Discovered The True Crown
 98: bool - Discovered Ankh
 99: bool - Discovered Tablet of Destiny
 9a: bool - Discovered Skeleton Key
 9b: bool - Discovered Royal Jelly
 9c: bool - Discovered Cape
 9d: bool - Discovered Vlad's Cape
 9e: bool - Discovered Jetpack
 9f: bool - Discovered Telepack
 a0: bool - Discovered Hoverpack
 a1: bool - Discovered Powerpack
 a2: bool - Discovered Webgun
 a3: bool - Discovered Shotgun
 a4: bool - Discovered Freeze Ray
 a5: bool - Discovered Clone Gun
 a6: bool - Discovered Crossbow
 a7: bool - Discovered Camera
 a8: bool - Discovered Teleporter
 a9: bool - Discovered Mattock
 aa: bool - Discovered Boomerang
 ab: bool - Discovered Machete
 ac: bool - Discovered Excalibure
 ad: bool - Discovered Broken Sword
 ae: bool - Discovered Plasma Cannon
 af: bool - Discovered Scepter
 b0: bool - Discovered Hou Yi's Bow
 b1: bool - Discovered Arrow of Light
 b2: bool - Discovered Wooden Shield
 b3: bool - Discovered Metal Shield
 b4: bool - Discovered Idol
 b5: bool - Discovered The Tusk Idol
 b6: bool - Discovered Curse Pot
 b7: bool - Discovered Ushabti
 b8: bool - Discovered Eggplant
 b9: bool - Discovered Cooked Turkey
 ba: bool - Discovered Elixir
 bb: bool - Discovered Four-Leaf Clover
```

### Traps
```
 bc: bool - Discovered Spikes
 bd: bool - Discovered Arrow Trap
 be: bool - Discovered Bear Trap
 bf: bool - Discovered Log Trap
 c0: bool - Discovered Spear Trap
 c1: bool - Discovered Thorny Vine
 c2: bool - Discovered Snap Trap
 c3: bool - Discovered Powder Box
 c4: bool - Discovered Falling Platform
 c5: bool - Discovered Spikeball
 c6: bool - Discovered Lion Trap
 c7: bool - Discovered Giant Clam
 c8: bool - Discovered Sliding Wall
 c9: bool - Discovered Crush Trap
 ca: bool - Discovered Giant Crush Trap
 cb: bool - Discovered Boulder
 cc: bool - Discovered Spring Trap
 cd: bool - Discovered Landmine
 ce: bool - Discovered Laser Trap
 cf: bool - Discovered Spark Trap
 d0: bool - Discovered Frog Trap
 d1: bool - Discovered Sticky Trap
 d2: bool - Discovered Bone Drop
 d3: bool - Discovered Egg Sac
```

## Player Unlocks

Playable characters each have their own bit offset in the following 3 bytes.
Discovering characters in the Journal is not enough to unlock them as playable, they must have
a bit toggled here. A fully-unlocked save is `0xff 0xff 0x0f`.

Note: It is possibly to remove the default characters by editing these values.

> **:warning: Warning**: Unlocking characters without setting approriate Furthest Depth will result in characters spawning in walls as the camp size hasn't grown to accomodate the new characters.

```
e6: byte
    0 - Ana
    1 - Margaret
    2 - Colin
    3 - Roffy
    4 - Alto
    5 - Liz
    6 - Nekka
    7 - LISE

e7: byte
    0 - Coco
    1 - Manfred
    2 - Jay
    3 - Tina
    4 - Valerie
    5 - Au
    6 - Demi
    7 - Pilot

e8: byte
    0 - Airyn
    1 - Dirk
    2 - Guy
    3 - Classic Guy

```

## Shortcut Unlocks

A value from `00` to `0a` signifying which steps you've completed. Every item delivered increments the value by 1.

Larger values are accepted, but seemingly don't do anything.

```
eb: byte
    00 - Nothing Unlocked / Never met Terra
    01 - Met Terra                      - Yellow notice board will appear in hub
    02 - 1-4 Shortcut - Gave $2,000
    03 - 1-4 Shortcut - Gave 1 bomb
    04 - 1-4 Shortcut - Gave $10,000    - 1-4 Shortcut unlocked
    05 - 3-1 Shortcut - Gave 1 Rope
    06 - 3-1 Shortcut - Gave Weapon
    07 - 3-1 Shortcut - Gave Mount      - 3-1 Shortcut unlocked
    08 - 5-1 Shortcut - Gave $50,000
    09 - 5-1 Shortcut - Gave Hired Hand
    0a - 5-1 Shortcut - Gave Golden Key - 5-1 Shortcut unlocked
```


## Journal Entry Counts

### Bestiary - Defeated Counts

```
0ee: int - Snake
0f2: int - Spider
0f6: int - Bat
0fa: int - Caveman
0fe: int - Skeleton
102: int - Horned Lizard
106: int - Moles
10a: int - Quillback
10e: int - Mantrap
112: int - Tiki Man
116: int - Witch Doctor
11a: int - Mosquito
11e: int - Monkey
122: int - Hang Spider
126: int - Giant Spider
12a: int - Magmar
12e: int - Robot
132: int - Fire Bug
136: int - Imp
13a: int - Lavamander
13e: int - Vampire
142: int - Vlad
146: int - Olmec
14a: int - Jiangshi
14e: int - Jiangshi Assassin
152: int - Flying Fish
156: int - Octopy
15a: int - Hermit Crab
15e: int - Pangxie
162: int - Great Humphead
166: int - Kingu
16a: int - Crocman
16e: int - Cobra
172: int - Mummy
176: int - Sorceress
17a: int - Cat Mummy
17e: int - Necromancer
182: int - Anubis
186: int - Ammit
18a: int - Apep
18e: int - Anubis II
192: int - Osiris
196: int - Ufo
19a: int - Alien
19e: int - Yeti
1a2: int - Yeti King
1a6: int - Yeti Queen
1aa: int - Lahamu
1ae: int - Proto Shopkeeper
1b2: int - Olmite
1b6: int - Lamassu
1ba: int - Tiamat
1be: int - Tadpole
1c2: int - Frog
1c6: int - Fire Frog
1ca: int - Goliath Frog
1ce: int - Grub
1d2: int - Giant Fly
1d6: int - Hundun
1da: int - Eggplant Minister
1de: int - Eggplup
1e2: int - Celestial Jelly
1e6: int - Scorpion
1ea: int - Bee
1ee: int - Queen Bee
1f2: int - Scarab
1f6: int - Golden Monkey
1fa: int - Leprechaun
1fe: int - Monty
202: int - Percy
206: int - Poochi
20a: int - Ghist
20e: int - Ghost
212: int - Cave Turkey
216: int - Rock Dog
21a: int - Axolotl
21e: int - Qilin
222: int - Mech Rider
```

### Bestiary - Killed By Counts

```
226: int - Snake
22a: int - Spider
22e: int - Bat
232: int - Caveman
236: int - Skeleton
23a: int - Horned Lizard
23e: int - Moles
242: int - Quillback
246: int - Mantrap
24a: int - Tiki Man
24e: int - Witch Doctor
252: int - Mosquito
256: int - Monkey
25a: int - Hang Spider
25e: int - Giant Spider
262: int - Magmar
266: int - Robot
26a: int - Fire Bug
26e: int - Imp
272: int - Lavamander
276: int - Vampire
27a: int - Vlad
27e: int - Olmec
282: int - Jiangshi
286: int - Jiangshi Assassin
28a: int - Flying Fish
28e: int - Octopy
292: int - Hermit Crab
296: int - Pangxie
29a: int - Great Humphead
29e: int - Kingu
2a2: int - Crocman
2a6: int - Cobra
2aa: int - Mummy
2ae: int - Sorceress
2b2: int - Cat Mummy
2b6: int - Necromancer
2ba: int - Anubis
2be: int - Ammit
2c2: int - Apep
2c6: int - Anubis II
2ca: int - Osiris
2ce: int - Ufo
2d2: int - Alien
2d6: int - Yeti
2da: int - Yeti King
2de: int - Yeti Queen
2e2: int - Lahamu
2e6: int - Proto Shopkeeper
2ea: int - Olmite
2ee: int - Lamassu
2f2: int - Tiamat
2f6: int - Tadpole
2fa: int - Frog
2fe: int - Fire Frog
302: int - Goliath Frog
306: int - Grub
30a: int - Giant Fly
30e: int - Hundun
312: int - Eggplant Minister
316: int - Eggplup
31a: int - Celestial Jelly
31e: int - Scorpion
322: int - Bee
326: int - Queen Bee
32a: int - Scarab
32e: int - Golden Monkey
332: int - Leprechaun
336: int - Monty
33a: int - Percy
33e: int - Poochi
342: int - Ghist
346: int - Ghost
34a: int - Cave Turkey
34e: int - Rock Dog
352: int - Axolotl
356: int - Qilin
35a: int - Mech Rider
```

### People - Killed Counts

```
3b2: int - Hired Hand
3b6: int - Eggplant Child
3ba: int - Shopkeeper
3be: int - Tun
3c2: int - Yang
3c6: int - Madame Tusk
3ca: int - Tusk's Bodyguard
3ce: int - Waddler
3d2: int - Caveman Shopkeeper
3d6: int - Ghist Shopkeeper
3da: int - Van Horsing
3de: int - Parsley
3e2: int - Parsnip
3e6: int - Parmesan
3ea: int - Sparrow
3ee: int - Beg
3f2: int - Eggplant King
```


### People - Killed By Counts

```
44a: int - Hired Hand
44e: int - Eggplant Child
452: int - Shopkeeper
456: int - Tun
45a: int - Yang
45e: int - Madame Tusk
462: int - Tusk's Bodyguard
466: int - Waddler
46a: int - Caveman Shopkeeper
46e: int - Ghist Shopkeeper
472: int - Van Horsing
476: int - Parsley
47a: int - Parsnip
47e: int - Parmesan
482: int - Sparrow
486: int - Beg
48a: int - Eggplant King
```


## Player Profile

```
48e: int  - Plays
492: int  - Deaths
496: int  - Normal Wins
49a: int  - Hard Wins
49e: int  - Special Wins

4a2: int64 - Sum of Score
4aa: int   - Top Score
# Seems to record Area as 8 once in CO. This
# has impact on camp size.
4ae: byte - Deepest Area
4af: byte - Deepest Level

288e: time64 - Sum of Time
2896: time   - Best Time
```

## Area - Death Count

```
8b2: int - 1-1
8b6: int - 1-2
8ba: int - 1-3
8be: int - 1-4

cae: int - 2-1
cb2: int - 2-2
cb6: int - 2-3
cba: int - 2-4

10aa: int - 3-1

14a6: int - 4-1
14aa: int - 4-2
14ae: int - 4-3
14b2: int - 4-4

18a2: int - 5-1

1c9e: int - 6-1
1ca2: int - 6-2
1ca6: int - 6-3
1caa: int - 6-4

209a: int - 7-1
209e: int - 7-2
20a2: int - 7-3
20a6: int - 7-4
20aa: int - 7-5
20ae: int - 7-6
20b2: int - 7-7
20b6: int - 7-8
20ba: int - 7-9
20be: int - 7-10
20c2: int - 7-11
20c6: int - 7-12
20ca: int - 7-13
20ce: int - 7-14
20d2: int - 7-15
20d6: int - 7-16
20da: int - 7-17
20de: int - 7-18
20e2: int - 7-19
20e6: int - 7-20
20ea: int - 7-21
20ee: int - 7-22
20f2: int - 7-23
20f6: int - 7-24
20fa: int - 7-25
20fe: int - 7-26
2102: int - 7-27
2106: int - 7-28
210a: int - 7-29
210e: int - 7-30
2112: int - 7-31
2116: int - 7-32
211a: int - 7-33
211e: int - 7-34
2122: int - 7-35
2126: int - 7-36
212a: int - 7-37
212e: int - 7-38
2132: int - 7-39
2136: int - 7-40
213a: int - 7-41
213e: int - 7-42
2142: int - 7-43
2146: int - 7-44
214a: int - 7-45
214e: int - 7-46
2152: int - 7-47
2156: int - 7-48
215a: int - 7-49
215e: int - 7-50
2162: int - 7-51
2166: int - 7-52
216a: int - 7-53
216e: int - 7-54
2172: int - 7-55
2176: int - 7-56
217a: int - 7-57
217e: int - 7-58
2182: int - 7-59
2186: int - 7-60
218a: int - 7-61
218e: int - 7-62
2192: int - 7-63
2196: int - 7-64
219a: int - 7-65
219e: int - 7-66
21a2: int - 7-67
21a6: int - 7-68
21aa: int - 7-69
21ae: int - 7-70
21b2: int - 7-71
21b6: int - 7-72
21ba: int - 7-73
21be: int - 7-74
21c2: int - 7-75
21c6: int - 7-76
21ca: int - 7-77
21ce: int - 7-78
21d2: int - 7-79
21d6: int - 7-80
21da: int - 7-81
21de: int - 7-82
21e2: int - 7-83
21e6: int - 7-84
21ea: int - 7-85
21ee: int - 7-86
21f2: int - 7-87
21f6: int - 7-88
21fa: int - 7-89
21fe: int - 7-90
2202: int - 7-91
2206: int - 7-92
220a: int - 7-93
220e: int - 7-94
2212: int - 7-95
2216: int - 7-96
221a: int - 7-97
221e: int - 7-98
```

## Character - Death Counts

```
289a: int - Ana Spelunky
289e: int - Margaret Tunnel
28a2: int - Colin Northward
28a6: int - Roffy D. Sloth
28aa: int - Alto Singh
28ae: int - Liz Mutton
28b2: int - Nekka the Eagle
28b6: int - Lise Project
28ba: int - Coco von Diamonds
28be: int - Manfred Tunnel
28c2: int - Little Jay
28c6: int - Tina Flan
28ca: int - Valerie Crump
28ce: int - Au
28d2: int - Demi von Diamonds
28d6: int - Pilot
28da: int - Princess Airyn
28de: int - Dirk Yamaoka
28e2: int - Guy Spelunky
28e6: int - Classic Spelunky
```

## Completion

Booleans marking how you've beaten the game. Changes the appearance of the entrance.
```
2901: bool - Completed the game (Normal)
2902: bool - Completed the game with no shortcuts (Ironman)
2903: bool - Completed the game (Hard)
```

## Viewed Player Profile
Tracks whether you ever viewed the player profile. Used to determine if it should show you a message saying it doesn't track seeded and multiplayer runs.

```
2904: bool
```

## Seeded Runs Unlocked

```
2905: bool
```

## Last Game Played

```
2906: byte - Area
2907: byte - Level
290a: int  - Money
290e: time - Time
```

## Stickers

Here the stickers are numbered in the order that they appear in the save file,
but in game they are listed from the middle outwards. The first sticker is
placed in the middle, the second to the left of the first, the third sticker
appears to the right of the first, fourth is placed further to the left of the
first, etc..

```
0x2912: int - Sticker 1
0x2916: int - Sticker 2
0x291a: int - Sticker 3
0x291e: int - Sticker 4
0x2922: int - Sticker 5
0x2926: int - Sticker 6
0x292a: int - Sticker 7
0x292e: int - Sticker 8
0x2932: int - Sticker 9
```

Values in the range of 0-3fb have been tried out and documented, any value
within this range not listed below causes a 'rainbow' square to appear in the
spot a sticker would normally be in.

When Spelunky 2 sees NoSticker it will ignore any following sticker value.

Here's the list of values:

```
0x00 - NoSticker

0xc1 - Ana
0xc2 - Margaret
0xc3 - Colin
0xc4 - Roffy
0xc5 - Alto
0xc6 - Liz
0xc7 - Nekka
0xc8 - LISE
0xc9 - Coco
0xca - Manfred
0xcb - Jay
0xcc - Tina
0xcd - Valerie
0xce - Au
0xcf - Demi
0xd0 - Pilot
0xd1 - Airyn
0xd2 - Dirk
0xd3 - Guy
0xd4 - ClassicGuy

0xe1 - Caveman
0xe7 - Quillback
0xf5 - Vlad
0xfc - Anubis
0x100 - Osiris
0x10e - AlienQueen
0x118 - Kingu
0x119 - Tiamat
0x122 - EggplantKing
0x123 - Hundun
0x127 - Shopkeeper
0x128 - Tun
0x129 - Yang
0x12b - Parsley
0x12c - Parsnip
0x12d - Parmesan
0x12e - VanHorsing
0x12f - Sparrow

0x163 - Idol

0x216 - Paste
0x217 - ClimbingGloves
0x218 - SpikeShoes
0x219 - SpringShoes
0x21a - Kapala
0x21b - Spectacles
0x21c - PitchersMitt
0x21d - UdjatEye
0x21e - Parachute
0x21f - Compass
0x220 - AlienCompass
0x221 - Hedjet
0x222 - Crown
0x223 - EggplantCrown
0x224 - TrueCrown
0x225 - Ankh
0x226 - TabletOfDestiny
0x227 - SkeletonKey

0x229 - Cape
0x22a - VladsCape
0x22c - Jetpack
0x22f - Telepack
0x231 - Hoverpack
0x233 - Powerpack

0x25a - Olmec
```

## Player - Character Selection

```
2a7a: byte - Player 1
2a7b: byte - Player 2
2a7c: byte - Player 3
2a7d: byte - Player 4
```

Values: 

```
0x00 - Ana Spelunky
0x01 - Margaret Tunnel
0x02 - Colin Northward
0x03 - Roffy D. Sloth
0x04 - Alto Singh
0x05 - Liz Mutton
0x06 - Nekka the Eagle
0x07 - Lise Project
0x08 - Coco von Diamonds
0x09 - Manfred Tunnel
0x0a - Little Jay
0x0b - Tina Flan
0x0c - Valerie Crump
0x0d - Au
0x0e - Demi von Diamonds
0x0f - Pilot
0x10 - Princess Airyn
0x11 - Dirk Yamaoka
0x12 - Guy Spelunky
0x13 - Classic Spelunky
```

## CRC32

bit inverted CRC32 of all bytes between magic numbers (2 bytes) and this crc32 (4 bytes). 


Example:

```py
>>> ~zlib.crc32(exe[2:-4])
1819641176
>>> struct.unpack('<L', exe[-4:])[0]
1819641176
```

```
359a: int - CRC32
```


# Raw Data

```md


# Damsels Rescued
0x28ea through 0x28ec tracks damsels of each type rescued across all playthroughs, including seeded runs. Goes in the same order as options (dog, cat, hamster). Above a certain value (untested) it causes pets to always appear in camp. It seems pets can also appear regardless of this value if your camp is big enough but without that many characters unlocked.


# Best Tutorial Time
0xd6 is the best tutorial time record (seconds * 60)(edited)
My guess is it's 4 bytes like most of the values
Little-endian
08 07 nets you a time of exactly 30s

# Score
For some weird reason, score is stored as a signed integer, so the highest value possible is ff ff ff 7f. Larger values flip the sign integer and make it negative. This means with save editing you can give yourself a negative high score (which will be immediately overwritten the moment you play a daily or unseeded run)

# Note about camp spawns
If you unlock too many characters without setting a sufficient depth, the camp will remain at its current size (usually so small that NPCs will spawn inside a wall on the right and die instantly). The opposite is also true where if you set a large depth with no character unlocks, the camp will get bigger, but only damsels will inhabit it until you get more characters unlocked.

# Regarding Jungle in Tutorial

Kind of? I had to change 0xea to 04 and ensure Nekka was unlocked, but I still have no idea what the byte at 0xea does aside from that.

# Journal Pickups

0xe2: remaining pick-up journal
0xea: count of picked-up journal (initial tutorial + letter stuffs)

```

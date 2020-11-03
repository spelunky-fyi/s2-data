from dataclasses import dataclass

@dataclass
class Entry:
    id_: int
    name: str
    description: str


ENTRIES = {
    "places": [
        Entry(
            1, "Dwelling", "The air here is warm and dry. It smells of campfire smoke and bat guano.",
        ),
        Entry(
            2, "Jungle", "Despite all odds, this dense, tropical forest appears to be teeming with life.",
        ),
        Entry(
            3, "Volcana", "It's as hot as Hell in this lava-filled world! Who knew the Moon could have such a place inside it?",
        ),
        Entry(
            4, "Olmec's Lair", "A shrine dedicated to the mighty Olmec. There is a timeless quality to this place of worship.",
        ),
        Entry(
            5, "Tide Pool", "The ruins of an ancient empire lay here at the edge of a vast, underground ocean.",
        ),
        Entry(
            6, "Abzu", "This palatial sanctuary was built over the deepest part of the sea.",
        ),
        Entry(
            7, "Temple of Anubis", "A massive tomb build by powerful pharaohs. On its walls are carved the stories of the past, present, and future.",
        ),
        Entry(
            8, "The City of Gold", "A legendary place to all treasure hunters! Every brick is made from solid gold.",
        ),
        Entry(
            9, "Duat", "A desert of ash and fire, burning beneath an eternal blood moon. The domain of the god Osiris.",
        ),
        Entry(
            10, "Ice Caves", "Life still thrives within the frozen core of this giant meteorite.",
        ),
        Entry(
            11, "Neo Babylon", "The capital city of the Olmites, a place of high technology, untold wonders, and endless stimulation.",
        ),
        Entry(
            12, "Tiamat's Throne", "Where Queen Tiamat gave birth to the World. Now a seat of power from which she guides her unruly children.",
        ),
        Entry(
            13, "Sunken City", "In the bottom of the Well, the First City sleeps.",
        ),
        Entry(
            14, "Eggplant World", "Once the palace of a mighty tyrant, now overgrown with peaceful eggplants.",
        ),
        Entry(
            15, "Hundun's Hideaway", "At the lowest point of the Well is where the Great Dreamer muddles about, always felt but never known.",
        ),
        Entry(
            16, "Cosmic Ocean", "The roiling waters of creation that flow from Hundun's childish weeping. Here one may find the beginning and the end.",
        ),
    ],
    "people": [
        Entry(
            1, "Ana Spelunky", "She's come to the Moon to find her mom and dad. An easygoing young lady with the heart of a hero.",
        ),
        Entry(
            2, "Margaret Tunnel", "A fascination with the ocean led her away from the family business. Her dream is to buy her own pirate ship.",
        ),
        Entry(
            3, "Colin Northward", "An inquisitive artist and engineer who's obsessed with Olmec and the Curse of the Caves.",
        ),
        Entry(
            4, "Roffy D. Sloth", "He has a lot of deep thoughts, but not a lot that he wants to say out loud.",
        ),
        Entry(
            5, "Alto Singh", "He works in physical education and wants to make sure everyone's taking good care of their health and staying positive.",
        ),
        Entry(
            6, "Liz Mutton", "A tough-as-nails adventurer who is hard to warm up to and needs her solitude, but also cares deeply for her friends.",
        ),
        Entry(
            7, "Nekka the Eagle", "A ferocious warrior chief who wants to confront the gods and question them about the problems of the universe.",
        ),
        Entry(
            8, "LISE Project", "A robot designed to explore and enjoy herself. After 1000 years she'll return to her creators with the data she's collected.",
        ),
        Entry(
            9, "Coco Von Diamonds", "The creator of the world-famous Von Diamonds fashion and lifestyle brand. She's on vacation right now.",
        ),
        Entry(
            10, "Manfred Tunnel", "He's decided to finally try his hand at spelunking after many years of building shortcuts.",
        ),
        Entry(
            11, "Little Jay", "A self-proclaimed \"Spelunkyhead\" trying to become a famous explorer. Gets a little overly excited around his heroes.",
        ),
        Entry(
            12, "Tina Flan", "As a relatively unknown caver she managed to hit King Yama with an eggplant. She tries to downplay her fame!",
        ),
        Entry(
            13, "Valerie Crump", "An avid fan of music and video games. She's trying to find creative inspiration through travel.",
        ),
        Entry(
            14, "Au", "A monk with bright golden skin. By challenging his mind and body he's trying to find peace in a chaotic universe.",
        ),
        Entry(
            15, "Demi Von Diamonds", "The heiress to the Von Diamonds empire. She's lived a pampered life, but is eager to learn more about the world.",
        ),
        Entry(
            16, "Pilot", "A strange little spaceman from a far away planet. He can often be found muttering about his UFO, the Campanella.",
        ),
        Entry(
            17, "Princess Airyn", "A culinary expert, she travels the world looking for the most exquisite tastes to bring home to her kingdom of Heliotropia.",
        ),
        Entry(
            18, "Dirk Yamaoka", "A master ninja always looking to hone his skills. When the Moon called, he answered without hesitation.",
        ),
        Entry(
            19, "Guy Spelunky", "He's spent his life in pursuit of adventure (and treasure). A young man no longer, he's re-evaluating what's most important to him.",
        ),
        Entry(
            20, "Classic Guy", "A version of Guy Spelunky from a parallel universe made of large, flat blocks of colors.",
        ),
        Entry(
            21, "Terra Tunnel", "She met Manfred many years ago, when she rescued him from a cave-in. Together they've built a thriving shortcut-building business!",
        ),
        Entry(
            22, "Hired Hand", "He's been trapped in the caves for a very long time and is eager to be free once again.",
        ),
        Entry(
            23, "Eggplant Child", "Separated from their mother, they miss her dearly. The embodiment of curiosity and creative potential.",
        ),
        Entry(
            24, "Shopkeeper", "A card-carrying member of the Shopkeeper's Association. He HATES shoplifting above all else!",
        ),
        Entry(
            25, "Tun", "A mysterious young woman who keeps a close eye on what's happening in the Caves. Beg's sister.",
        ),
        Entry(
            26, "Yang", "The youngest of Yang's 12 sons, who are all named Yang. He loves turkeys.",
        ),
        Entry(
            27, "Madame Tusk", "The most famous resident of the caves, or at least she'd like to think so!",
        ),
        Entry(
            28, "Tusk's Bodyguard", "Madame Tusk pays them extremely well.",
        ),
        Entry(
            29, "Waddler", "He runs an item storage and transportation business. Customers have complained of getting their items back sticky.",
        ),
        Entry(
            30, "Caveman Shopkeeper", "An enterprising caveman trying to acquire more shiny things to show off to his friends.",
        ),
        Entry(
            31, "Ghist Shopkeeper", "In the darkest corners they peddle their wares, hoping to preserve some small shred of their former life.",
        ),
        Entry(
            32, "Van Horsing", "A veteran from the first adventure. He seeks revenge on Vlad for reasons unknown.",
        ),
        Entry(
            33, "Parsley", "The youngest of three sisters. She's cheery but has a quick temper.",
        ),
        Entry(
            34, "Parsnip", "The middle child of three sisters. She loves parties and cats.",
        ),
        Entry(
            35, "Parmesan", "The eldest of three sisters. She's shy and nurturing.",
        ),
        Entry(
            36, "Sparrow", "Hailing from a prominent ninja family, she defied her parents and turned to thievery to challenge authority.",
        ),
        Entry(
            37, "Beg", "In his insecurity he was drawn to Hundun and embraced Chaos. Tun's brother.",
        ),
        Entry(
            38, "Eggplant King", "He was a mighty king... until a brave explorer humbled him. Some might say he's even more powerful now.",
        ),
    ],
    "items": [
        Entry(
            1, "Rope Pile", "3 ropes to help you get to those hard-to-reach places.",
        ),
        Entry(
            2, "Bomb Bag", "A large sack filled with 3 bombs.",
        ),
        Entry(
            3, "Bomb Box", "A flame-resistant box of 12 bombs. The gift every adventurer wants to receive!",
        ),
        Entry(
            4, "Paste", "Made from spider's web. Lather it on your bombs to make them sticky!",
        ),
        Entry(
            5, "Spectacles", "Improves your vision and also makes you look slightly more intelligent.",
        ),
        Entry(
            6, "Climbing Gloves", "The grips of these gloves have small bristles all over them. Just lean into walls to cling to them!",
        ),
        Entry(
            7, "Pitcher's Mitt", "This classic American baseball glove makes you feel like you can throw like a pro.",
        ),
        Entry(
            8, "Spring Shoes", "A sturdy pair of boots equipped with alien spring technology.",
        ),
        Entry(
            9, "Spike Shoes", "A sturdy pair of boots with sharp spikes fitted to the bottom.",
        ),
        Entry(
            10, "Compass", "This classic explorer's tool will point you right to the exit. How convenient!",
        ),
        Entry(
            11, "Alien Compass", "A special compass designed by aliens to help them return home through the inky darkness of space.",
        ),
        Entry(
            12, "Parachute", "It will save your life when you least expect it!",
        ),
        Entry(
            13, "Udjat Eye", "The udjat eye is a symbol of great power. It represents the gods' watchful gaze.",
        ),
        Entry(
            14, "Kapala", "A skull cup bestowed upon Kali's most loyal devotees. Drinking blood from it can improve one's health and enlightenment.",
        ),
        Entry(
            15, "Hedjet", "A white pharaoh's crown, indicating the wearer's status as an envoy for the gods. It glows brilliantly.",
        ),
        Entry(
            16, "Crown", "This royal headgear exudes an aura of unquestionable authority. It's much heavier than it looks!",
        ),
        Entry(
            17, "Eggplant Crown", "The Eggplant King bequeathed his crown to me. I feel at peace with my place in the universe.",
        ),
        Entry(
            18, "The True Crown", "Also known as the cap and bells. A fitting crown for the followers of Hundun.",
        ),
        Entry(
            19, "Ankh", "This coveted amulet was created by the gods for followers deemed worthy enough to have their life extended.",
        ),
        Entry(
            20, "Tablet of Destiny", "A clay tablet on which many esoteric prophecies are written.",
        ),
        Entry(
            21, "Skeleton Key", "The tool of thieves. It opens any lock without breaking.",
        ),
        Entry(
            22, "Royal Jelly", "A delicacy that's highly sought after for its refined taste and healing properties.",
        ),
        Entry(
            23, "Cape", "This dashing fashion accessory can also be used to reduce one's speed while falling.",
        ),
        Entry(
            24, "Vlad's Cape", "The blood-red cape of Vlad the Impaler. It offers impressive mobility.",
        ),
        Entry(
            25, "Jetpack", "It's expensive, but many explorers swear by it. Just keep an eye on your fuel levels!",
        ),
        Entry(
            26, "Telepack", "Allows you to teleport while freeing up your hands! Requires your feet to be off the ground, however.",
        ),
        Entry(
            27, "Hoverpack", "A refinement of Olmite technology. It allows you to hover indefinitely.",
        ),
        Entry(
            28, "Powerpack", "Developed for military use, the power pack imbues its wearer with improved weapon handling abilities.",
        ),
        Entry(
            29, "Webgun", "It shoots synthetic webs that are so close to the real thing that even spiders can't tell the difference",
        ),
        Entry(
            30, "Shotgun", "A basic 12-gauge shotgun. Favored by shopkeepers for self-defense and hunting down shoplifters.",
        ),
        Entry(
            31, "Freeze Ray", "The say the mechanism behind its frozen blast was inspired by the sneezes of the now-extinct mammoth.",
        ),
        Entry(
            32, "Clone Gun", "A one-of-a-kind prototype! The technology required to build one is beyond any known civilization.",
        ),
        Entry(
            33, "Crossbow", "A ranged weapon favored by hunters. It's capable of firing arrows with incredible accuracy.",
        ),
        Entry(
            34, "Camera", "This fancy camera comes with the most powerful flash on the market right now.",
        ),
        Entry(
            35, "Teleporter", "A handheld teleportation device. It's still in beta after all these years!",
        ),
        Entry(
            36, "Mattock", "A useful digging tool that breaks easily. The Tunnel family prefers shovels.",
        ),
        Entry(
            37, "Boomerang", "A curved wooden weapon that will return to its owner after being thrown",
        ),
        Entry(
            38, "Machete", "Its long, broad blade is great for defense or chopping vegetables for dinner.",
        ),
        Entry(
            39, "Excalibur", "The sword of legend. Wielded by kings and queens in times of great calamity.",
        ),
        Entry(
            40, "Broken Sword", "Although perhaps it no longer contains its full strength, it's still a formidable weapon.",
        ),
        Entry(
            41, "Plasma Cannon", "It was built by aliens, but sadly the recoil proved to be too strong for them to use it easily.",
        ),
        Entry(
            42, "Scepter", "A magical tool used by the god Anubis to cleanse souls on their way to judgement.",
        ),
        Entry(
            43, "Hou Yi's Bow", "With this simple but refined bow, Hou Yi shot down the nine suns that scorched the Earth.",
        ),
        Entry(
            44, "Arrow of Light", "A ray of sun reflecting off the Moon's tears.",
        ),
        Entry(
            45, "Wooden Shield", "A flimsy wooden shield carried by Tikimen for some basic defense against the harsh Jungle environment.",
        ),
        Entry(
            46, "Metal Shield", "A highly durable knight's shield made of tempered steel.",
        ),
        Entry(
            47, "Idol", "This valuable golden idol can be brought to the exit or to shops in exchange for gold.",
        ),
        Entry(
            48, "The Tusk Idol", "A walrus idol carved from an extra-large diamond. One of Madame's most precious treasures.",
        ),
        Entry(
            49, "Curse Pot", "A clay pot filled with a toxic substance rumored to be a mixture of ectoplasm and cursed blood.",
        ),
        Entry(
            50, "Ushabti", "A funerary figurine created to accompany someone on their journey to the underworld.",
        ),
        Entry(
            51, "Eggplant", "It is fragile yet full of vigor, reminding us to treasure every one of life's moments.",
        ),
        Entry(
            52, "Cooked Turkey", "A turkey that has been cooked just right. The meat is tender and flavorful.",
        ),
        Entry(
            53, "Elixir", "A restorative potion said to cure any affliction. Royal jelly is mixed in to reduce the bitterness.",
        ),
        Entry(
            54, "Four-Leaf Clover", "A rare clover. It's prized by leprechauns for protection and good fortune.",
        ),
    ],
    "bestiary": [
        Entry(
            1, "Snake", "Be careful! It's liable to throw a hissy fit!",
        ),
        Entry(
            2, "Spider", "Much larger than the household variety. Don't let it get the drop on you!",
        ),
        Entry(
            3, "Bat", "A common cave resident that nonetheless thinks very highly of itself due to its cute appearance.",
        ),
        Entry(
            4, "Caveman", "One of our primitive ancestors. His simple life is somewhat enviable.",
        ),
        Entry(
            5, "Skeleton", "We all have one inside us... and yet they're still so spooky!",
        ),
        Entry(
            6, "Horned Lizard", "It still hasn't figured out how to stop rolling once it starts.",
        ),
        Entry(
            7, "Cave Mole", "Who's got teeth like spades and needs no shades? CAVE MOLE! CAVE MOLE!",
        ),
        Entry(
            8, "Quillback", "The leader of the cavemen. A big bully who wears the pelt of the last cave porcupine.",
        ),
        Entry(
            9, "Mantrap", "Once it tasted human flesh, it never looked back!",
        ),
        Entry(
            10, "Tiki man", "A masked Jungle-dweller who hunts with a large boomerang.",
        ),
        Entry(
            11, "Witch Doctor", "A Tiki Tribe elder who practices black magic. They use an effigy to attack intruders.",
        ),
        Entry(
            12, "Mosquito", "An annoying pest! Makes me mad just thinking about it.",
        ),
        Entry(
            13, "Monkey", "A mischievous forest trickster. It simply can't get enough of its own unfunny pranks!",
        ),
        Entry(
            14, "Hang Spider", "It could chase you if it had to but it'd rather not leave its web if possible.",
        ),
        Entry(
            15, "Giant Spider", "A frightening arachnid the size of a car. She squirts sticky webs to ensnare her prey.",
        ),
        Entry(
            16, "Magmar", "When an adventurer dies in lava, their spirit can become trapped inside the lava instead of going free.",
        ),
        Entry(
            17, "Robot", "They patrol Volcana aimlessly, awaiting instructions from long-dead masters",
        ),
        Entry(
            18, "Fire Bug", "A deadly insect that protects itself by igniting gas stored inside its body.",
        ),
        Entry(
            19, "Imp", "When Yama disappeared, these lowly servants emerged from Hell seeking employment",
        ),
        Entry(
            20, "Lavamander", "The blood of this lizard-like monster runs so cold that only the immense heat of lava can keep it going.",
        ),
        Entry(
            21, "Vampire", "A tortured soul who traded their humanity for eternal life.",
        ),
        Entry(
            22, "Vlad", "The dark lord of all vampires. He relocated to a large castle deep inside Volcana.",
        ),
        Entry(
            23, "Olmec", "Once thought to be the cause of a curse that trapped explorers in a cave... but maybe he was just a small part of it?",
        ),
        Entry(
            24, "Jiangshi", "A reanimated corpse. Its stiff legs force it to hop around.",
        ),
        Entry(
            25, "Jiangshi Assassin", "This wily jiang-shi was once an imperial assassin.",
        ),
        Entry(
            26, "Flying Fish", "A strange, thrill-seeking fish that will go out of its way to eat \"landfood\".",
        ),
        Entry(
            27, "Octopy", "It defends itself with a blinding ink attack and a crown of razor sharp barnacles.",
        ),
        Entry(
            28, "Hermit Crab", "An irritable loner who hates being disturbed. Its saliva is very poisonous!",
        ),
        Entry(
            29, "Pangxie", "One of Kingu's famous armored guards. His claws can crush wood and stone with ease.",
        ),
        Entry(
            30, "Great Humphead", "Endlessly he patrols the salty waters of the Great Lake, waiting for the Empress to return and feed him.",
        ),
        Entry(
            31, "Kingu", "Tiamat's loyal companion and unwavering protector. Her mighty shell once withstood the impact of a comet.",
        ),
        Entry(
            32, "Crocman", "Their powerful bite and teleportation magic makes them a dangerous foe.",
        ),
        Entry(
            33, "Cobra", "A hooded serpent with a rather rude habit.",
        ),
        Entry(
            34, "Mummy", "This frightening tomb lord emerges from its eternal slumber to protect the Temple from trespassers.",
        ),
        Entry(
            35, "Sorceress", "An expert magic user who wields the power of creation",
        ),
        Entry(
            36, "Cat Mummy", "The mummified felines are filled with terrible curses.",
        ),
        Entry(
            37, "Necromancer", "A master of the dark arts who dedicated his life to studying the Book of the Dead.",
        ),
        Entry(
            38, "Anubis", "This legendary jackal-headed god is tasked with guarding the Temple's most hallowed treasures.",
        ),
        Entry(
            39, "Ammit", "A terrifying underworld demon who eats the hearts of unclean souls, casuing them to die a second death.",
        ),
        Entry(
            40, "Apep", "A great snake god who slithers tirelessly throughout Duat, with scales of flint and a stomach full of hot ash.",
        ),
        Entry(
            41, "Anubis II", "Having been defeated at the Temple, Anubis returns to the underworld to beg forgiveness of his father, Osiris.",
        ),
        Entry(
            42, "Osiris", "The ruler of Duat and the ultimate judge of souls who make their way to him.",
        ),
        Entry(
            43, "UFO", "In alien society, being a flying saucer pilot is considered a lowly occupation.",
        ),
        Entry(
            44, "Alien", "Tiamat's firstborn. They harbor a deep jealousy of the Olmites, whom they think she favors.",
        ),
        Entry(
            45, "Yeti", "It loves to toss things and chew gum. But it doesn't know what gum is!",
        ),
        Entry(
            46, "Yeti King", "The king of the yetis is whichever one is biggest.",
        ),
        Entry(
            47, "Yeti Queen", "The queen of the yetis is whichever one can default the king in battle.",
        ),
        Entry(
            48, "Lahamu", "The eldest daughter of Tiamat. A jealous and vindictive warlord with powerful psychic abilities",
        ),
        Entry(
            49, "Proto Shopkeeper", "During the First Wars, Lahamu stole the Original Man to create clones of him with varying degrees of success.",
        ),
        Entry(
            50, "Olmite", "Tiamat's secondborn. An inquisitive race that excels at creation.",
        ),
        Entry(
            51, "Lamassu", "A mighty demigod created by the Olmites to help them guard Neo Babylon.",
        ),
        Entry(
            52, "Tiamat", "The Queen of the World. Though myth and legend hava separated her from her decendents, some still hear her call...",
        ),
        Entry(
            53, "Tadpole", "A baby frog. It's content to splash in the murky waters.",
        ),
        Entry(
            54, "Frog", "Over the aeons, these bloated amphibians have overrun the Sunken City.",
        ),
        Entry(
            55, "Fire Frog", "Some of the Sunken City frogs have developed an explosive personality.",
        ),
        Entry(
            56, "Goliath Frog", "A frog of legend. It carries its entire family within its mighty belly.",
        ),
        Entry(
            57, "Grub", "A lowly creature just trying to make it to the next part of its lifecycle.",
        ),
        Entry(
            58, "Giant Fly", "A fly of titanic proportions. It looks threatening but seems rather uninterested in us...",
        ),
        Entry(
            59, "Hundun", "The muddled dreamer Hundun. The cosmic egg Hundun. The majestic child Hundun. The unstoppable Hundun.",
        ),
        Entry(
            60, "Eggplant Minister", "The most loyal servants of the King of Hell, who continued to follow though commands no longer left his lips.",
        ),
        Entry(
            61, "Eggplup", "Once a fierce hound of hell, now a playful puppy.",
        ),
        Entry(
            62, "Celestial Jelly", "These mighty titan's roam the vast waters of the Cosmic Ocean, leaving behind them great ripples that alter time and space.",
        ),
        Entry(
            63, "Scorpion", "Sometimes you break open a pot and a nightmare comes out. This is that nightmare.",
        ),
        Entry(
            64, "Bee", "An important part of the cave ecosystem. However, it's much larger and more aggressive than the common honeybee.",
        ),
        Entry(
            65, "Queen Bee", "The matriarch of the hive. On her abdomen one might find a blob of delicious royal jelly.",
        ),
        Entry(
            66, "Scarab", "A jeweled flying beetle revered by the followers of Anubis and sought after by leprechauns and treasure hunters.",
        ),
        Entry(
            67, "Golden Monkey", "He struck out on adventure but a sorceress used magic to transform him into an idol.",
        ),
        Entry(
            68, "Leprechaun", "This greedy sprite seeks out heavy pockets to pilfer for his treasure stash.",
        ),
        Entry(
            69, "Monty", "A helpless pug adopted by Tina Flan after her first big adventure. Ana's somewhat faithful companion.",
        ),
        Entry(
            70, "Percy", "A helpless cat who snuck aboard Margaret Tunnel's spaceship looking for a warm place to sleep.",
        ),
        Entry(
            71, "Poochi", "A helpless hamster who Colin Northward brought to the Moon in the name of science. Unfortunately, she escaped.",
        ),
        Entry(
            72, "Ghist", "If in life the spirit is small and spiteful, in death its presence is weak and hard to know.",
        ),
        Entry(
            73, "Ghost", "This angry and relentless spirit chases down explorers for reasons unknown.",
        ),
        Entry(
            74, "Cave Turkey", "A large, meaty bird, best known for its fleshy wattle, also known as a snood.",
        ),
        Entry(
            75, "Rock Dog", "The skin of this fire-breathing canine is protected by a rock-hard plates, hence the name.",
        ),
        Entry(
            76, "Axolotl", "The empress encountered these curious creatures during her travels and brought some back as pets. They quickly escaped!",
        ),
        Entry(
            77, "Qilin", "A creature of myth, whose arrival is said to coincide with important events in the history of humans and gods.",
        ),
        Entry(
            78, "Mech Rider", "A MOYA-class mechanized armor designed by aliens to combat the Olmites during the Second Wars.",
        ),

    ],
    "traps": [
        Entry(
            1, "Spikes", "Ah, spikes! The classic trap. They come in many shapes and sizes, all painful.",
        ),
        Entry(
            2, "Arrow Trap", "An ancient trap of unknown origin. It's responsible for the death of many an explorer.",
        ),
        Entry(
            3, "Totem Trap", "Quillback built these to train his followers, although they mostly serve to put them \"to sleep\".",
        ),
        Entry(
            4, "Log Trap", "The trunk of a massive tree, carved by Quillback and strung up to protect his treasure.",
        ),
        Entry(
            5, "Spear Trap", "These wooden spear traps can be hard to spot amidst the Jungle foliage.",
        ),
        Entry(
            6, "Thorny Vine", "The thorns of these thick vines aren't long enough to impale, but they're sharp enough to deliver a nasty poke.",
        ),
        Entry(
            7, "Bear Trap", "The slightest pressure will cause its powerful steel jaws to snap shut, causing massive damage.",
        ),
        Entry(
            8, "Powder Box", "A wooden box hastily filled with black powder. It will explode at the slightest provocation.",
        ),
        Entry(
            9, "Falling Platform", "A rickety outcropping of rock that won't take very much weight...",
        ),
        Entry(
            10, "Spikeball", "A large ball-and-chain that was designed for crushing rock.",
        ),
        Entry(
            11, "Lion Trap", "It's said that the Empress successfully deflected a barbarian horde using only these golden lions.",
        ),
        Entry(
            12, "Giant Clam", "Over the years, the Empress's treasure has made its way to the ocean and into the mouths of these oversized molluscs.",
        ),
        Entry(
            13, "Sliding Wall", "A door-like mechanism that is activated by a switch.",
        ),
        Entry(
            14, "Crush Trap", "A solid block of stone designed by the pharaohs to flatten would-be tomb robbers.",
        ),
        Entry(
            15, "Giant Crush Trap", "An extra large edition of the crush trap, for discerning pharaohs who want that extra crushing power.",
        ),
        Entry(
            16, "Boulder", "A frosty boulder released to smash treasure hunters that make it to the Ice Caves.",
        ),
        Entry(
            17, "Spring Trap", "In alien society, bouncing up and down is a common form of recreation and exercise.",
        ),
        Entry(
            18, "Landmine", "An explosive device triggered by proximity. Disable it before it's too late!",
        ),
        Entry(
            19, "Laser Trap", "A fixed laser gun triggered by a motion detector.",
        ),
        Entry(
            20, "Spark Trap", "The enormous amount of excess energy generated by Neo Babylon is channeled into dangerous contraptions such as these.",
        ),
        Entry(
            21, "Frog Trap", "The spear is so huge that it's hard to imagine that it was meant to be used against human beings...",
        ),
        Entry(
            22, "Sticky Trap", "A strange growth, whose fleshy protuberance is reminiscent of a uvula.",
        ),
        Entry(
            23, "Bone Drop", "This mass of bones is so large that it's starting to burst out of the ground.",
        ),
        Entry(
            24, "Egg Sac", "Beneath the thin membrane you can see something writhing around vigorously.",
        ),
    ],
}

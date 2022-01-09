# dmpreview.tok

## Description

There are `40` total Arena levels represented in the `dmpreview.tok` file. Each arena preview
consists of `450` bytes used to represent a 30 x 15 grid of tiles, 30 bytes per line. The mapping
of byte value to symbol is documented in the Tiles section below.

## Tiles

* `0x00` - Floor
* `0x01` - Push Block
* `0x02` - Crate
* `0x03` - Ladder
* `0x04` - 
* `0x05` - 
* `0x06` - 
* `0x07` - Spikes
* `0x08` - 
* `0x09` - 
* `0x0a` - 
* `0x0b` - 
* `0x0c` - 
* `0x0d` - 
* `0x0e` - 
* `0x0f` - Water
* `0x10` - 
* `0x11` - 
* `0x12` - 
* `0x13` - 
* `0x14` - 
* `0x15` - 
* `0x16` - 
* `0x17` - Regen
* `0x18` - Tubes
* `0x19` - 
* `0x1a` - 
* `0xff` - Empty

## Rooms

### Dwelling - Boneyard (Small)
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 ff ff ff ff ff 00 00 09 09 00 00 ff ff ff ff ff 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 09 09 ff ff ff 09 09 ff ff ff 09 09 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 09 09 00 ff ff 09 09 ff ff 00 09 09 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 ff ff 09 09 00 00 ff 09 09 ff 00 00 09 09 ff ff 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 09 09 00 00 00 09 09 00 00 00 09 09 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Dwelling - Ladders (Small)
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 03 ff ff 03 ff ff ff ff 03 ff ff 03 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 03 ff ff 03 00 00 00 00 03 ff ff 03 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 03 ff ff 03 00 00 00 00 03 ff ff 03 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 03 ff ff 03 ff ff ff ff 03 ff ff 03 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 03 ff ff 03 ff ff ff ff 03 ff ff 03 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 03 ff ff 03 ff ff ff ff 03 ff ff 03 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 03 ff ff 03 00 00 00 00 03 ff ff 03 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Dwelling - The Boss Room (Large)
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 00 00 03 ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff 03 00 00 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff 09 09 ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 00 00 03 ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff 03 00 00 00
00 00 ff 03 ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff 03 ff 00 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Dwelling - The Dig (Large)
```
00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00
00 00 ff ff ff 00 00 00 00 ff ff ff 03 ff ff ff ff 03 ff ff ff 00 00 00 00 ff ff ff 00 00
00 ff ff ff ff ff ff ff ff ff ff ff 03 00 00 00 00 03 ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff 03 ff ff ff ff 03 ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff 03 ff 03 03 ff 03 ff ff ff ff ff ff ff ff 03 ff ff 00
00 00 00 03 00 00 00 00 00 00 00 00 00 00 03 03 00 00 00 00 00 00 00 00 00 00 03 00 00 00
00 09 00 03 00 09 00 00 00 09 00 00 00 00 03 03 00 00 00 00 09 00 00 00 09 00 03 00 09 00
00 00 00 03 09 09 09 00 00 00 00 00 02 00 03 03 00 02 00 00 00 00 00 09 09 09 03 00 00 00
00 00 00 03 00 09 09 00 00 00 00 00 00 00 03 03 00 00 00 00 00 00 00 09 09 00 03 00 00 00
00 00 ff 03 00 00 00 00 ff ff 00 ff ff 00 03 03 00 ff ff 00 ff ff 00 00 00 00 03 ff 00 00
00 ff ff 03 ff ff ff ff ff ff ff ff ff ff 03 03 ff ff ff ff ff ff ff ff ff ff 03 ff ff 00
00 ff ff 03 ff ff 00 ff ff ff ff ff ff ff 03 03 ff ff ff ff ff ff ff 00 ff ff 03 ff ff 00
00 00 ff 03 ff ff 00 00 ff ff ff ff ff ff 03 03 ff ff ff ff ff ff 00 00 ff ff 03 ff 00 00
00 00 00 00 00 00 00 00 00 00 00 00 ff ff 03 03 ff ff 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Dwelling - Apartments (Large)
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 ff ff 00 00 00 00 00 01 00 00 03 ff ff ff ff 03 00 00 01 00 00 00 00 00 ff ff 00 00
00 ff ff ff ff ff 00 00 00 00 00 00 03 00 00 00 00 03 00 00 00 00 00 00 ff ff ff ff ff 00
00 ff ff ff ff ff 01 ff ff ff ff 00 03 00 00 00 00 03 00 ff ff ff ff 01 ff ff ff ff ff 00
00 ff 00 00 00 00 00 00 ff ff ff ff 03 ff 00 00 ff 03 ff ff ff ff 00 00 00 00 00 00 ff 00
00 ff ff ff ff ff ff 01 ff ff ff ff 03 ff ff ff ff 03 ff ff ff ff 01 ff ff ff ff ff ff 00
00 ff ff 03 ff ff ff 00 00 00 00 00 03 00 ff ff 00 03 00 00 00 00 00 ff ff ff 03 ff ff 00
00 00 00 03 00 00 ff 00 00 00 00 00 03 00 ff ff 00 03 00 00 00 00 00 ff 00 00 03 00 00 00
00 00 00 03 00 00 ff 00 00 00 00 00 03 ff ff ff ff 03 00 00 00 00 00 ff 00 00 03 00 00 00
00 00 ff 03 ff ff ff ff ff ff 02 01 03 00 ff ff 00 03 01 02 ff ff ff ff ff ff 03 ff 00 00
00 ff ff 03 ff 00 00 00 ff 00 00 00 03 00 ff ff 00 03 00 00 00 ff 00 00 00 ff 03 ff ff 00
00 ff ff 03 ff 00 ff ff ff 00 ff ff 03 ff ff ff ff 03 ff ff 00 ff ff ff 00 ff 03 ff ff 00
00 ff ff 03 ff ff ff ff ff ff ff ff 03 00 ff ff 00 03 ff ff ff ff ff ff ff ff 03 ff ff 00
00 00 ff 03 00 00 00 00 00 00 ff ff ff 00 00 00 00 ff ff ff 00 00 00 00 00 00 03 ff 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Jungle - Vines (Small)
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 04 00 00 00 04 00 00 00 00 04 00 00 00 04 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 00 00 00 04 ff ff ff ff 04 00 00 00 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff 04 ff ff ff 04 ff ff ff ff 04 ff ff ff 04 ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 0a 00 00 0a 00 00 0a 00 00 0a 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Jungle - 
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 04 ff ff ff ff ff ff ff ff ff ff 04 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 04 ff ff ff ff ff ff ff ff ff ff 04 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 04 ff ff ff ff ff ff ff ff ff ff 04 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 04 ff ff 00 00 ff ff 00 00 ff ff 04 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 04 ff ff 00 ff ff ff ff 00 ff ff 04 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 04 ff ff 00 00 ff ff 00 00 ff ff 04 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 ff ff ff 01 02 ff ff 02 01 ff ff ff 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Jungle - 
```
00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00
00 ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff 00
00 ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff 00
00 00 ff 00 00 00 00 ff 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 ff 00 00 00 00 ff 00 00
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff 1a ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 1a ff ff
ff ff 19 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 19 ff ff
ff ff 19 ff ff ff ff 1a ff ff ff ff ff 1a ff ff 1a ff ff ff ff ff 1a ff ff ff ff 19 ff ff
ff ff 19 ff ff ff ff 19 ff ff ff ff ff 19 ff ff 19 ff ff ff ff ff 19 ff ff ff ff 19 ff ff
ff 00 00 00 ff ff ff 19 ff ff ff ff ff 19 00 00 19 ff ff ff ff ff 19 ff ff ff 00 00 00 ff
ff ff 00 ff ff ff ff 19 ff ff ff ff ff 19 00 00 19 ff ff ff ff ff 19 ff ff ff ff 00 ff ff
ff ff ff ff ff ff 00 00 00 00 ff ff ff 00 00 00 00 ff ff ff 00 00 00 00 ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Jungle - 
```
00 ff ff ff ff 04 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 04 ff ff ff ff 00
00 ff ff ff ff 04 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 04 ff ff ff ff 00
00 ff 1a ff ff 04 ff ff ff ff ff 00 00 02 03 03 02 00 00 ff ff ff ff ff 04 ff ff 1a ff 00
00 ff 19 ff ff 04 ff ff ff ff ff 00 00 00 03 03 00 00 00 ff ff ff ff ff 04 ff ff 19 ff 00
00 ff 19 ff ff 04 ff ff ff ff ff 00 00 ff 03 03 ff 00 00 ff ff ff ff ff 04 ff ff 19 ff 00
00 00 19 ff ff 04 ff ff ff ff ff 01 ff ff 03 03 ff ff 01 ff ff ff ff ff 04 ff ff 19 00 00
00 00 00 00 ff 04 ff ff ff ff 1a 00 00 00 03 03 00 00 00 1a ff ff ff ff 04 ff 00 00 00 00
00 ff ff ff ff 04 ff ff ff ff 19 00 00 ff 03 03 ff 00 00 19 ff ff ff ff 04 ff ff ff ff 00
00 ff ff ff ff 04 ff ff ff ff 19 00 00 ff 03 03 ff 00 00 19 ff ff ff ff 04 ff ff ff ff 00
00 ff ff ff ff 04 ff ff ff ff 19 00 00 00 03 03 00 00 00 19 ff ff ff ff 04 ff ff ff ff 00
00 ff ff ff 1a 04 ff ff 1a ff 00 00 00 00 03 03 00 00 00 00 ff 1a ff ff 04 1a ff ff ff 00
00 ff ff ff 19 ff ff ff 19 ff ff ff 01 ff 03 03 ff 01 ff ff ff 19 ff ff ff 19 ff ff ff 00
00 ff ff ff 19 ff ff ff 19 ff 00 00 00 ff 03 03 ff 00 00 00 ff 19 ff ff ff 19 ff ff ff 00
00 ff ff ff 19 ff ff ff 19 00 00 00 00 00 ff ff 00 00 00 00 00 19 ff ff ff 19 ff ff ff 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Jungle - 
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 04 00 00 00 04 00 00 00 00 00 04 00 00 04 00 00 00 00 00 04 00 00 00 04 00 00 00
00 ff ff 04 ff ff ff 04 ff ff ff ff ff 04 ff ff 04 ff ff ff ff ff 04 ff ff ff 04 ff ff 00
00 ff ff 04 ff ff ff 04 ff ff ff ff ff 04 02 02 04 ff ff ff ff ff 04 ff ff ff 04 ff ff 00
00 ff ff 04 ff ff ff 04 00 00 00 ff ff 04 00 00 04 ff ff 00 00 00 04 ff ff ff 04 ff ff 00
00 ff ff 04 0a ff ff 04 00 00 00 ff ff 04 00 00 04 ff ff 00 00 00 04 ff ff 0a 04 ff ff 00
00 ff 00 04 00 ff 00 04 00 00 00 ff ff 04 ff ff 04 ff ff 00 00 00 04 00 ff 00 04 00 ff 00
00 ff 00 04 00 ff 00 04 00 00 00 ff ff 04 ff ff 04 ff ff 00 00 00 04 00 ff 00 04 00 ff 00
00 ff ff 04 ff ff ff 04 00 00 00 ff ff 04 ff ff 04 ff ff 00 00 00 04 ff ff ff 04 ff ff 00
00 ff ff 04 ff ff ff 1a ff ff ff ff ff 04 ff ff 04 ff ff ff ff ff 1a ff ff ff 04 ff ff 00
00 00 ff 1a ff ff ff 19 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 19 ff ff ff 1a ff 00 00
00 00 ff 19 ff ff ff 19 ff ff ff 0a 00 00 00 00 00 00 0a ff ff ff 19 ff ff ff 19 ff 00 00
00 00 00 19 00 00 00 19 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 00 00 00 19 00 00 00
00 00 00 19 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 19 00 00 00
```

### Volcana -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 0f 0f 0f 0f 0f 0f 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff 00 0f 0f 0f 0f 0f 0f 00 ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff 00 00 00 00 00 00 00 00 ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff 0c 0c 0d 0d ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff 0c 0c 00 00 00 00 0d 0d ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff 0c 0c 00 00 00 00 00 00 00 00 0d 0d ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Volcana -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff 0c ff ff 0d ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 0b 0b 0d 0b 0b 0b 0b 0b 0b 0b 0b 0c 0b 0b 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f ff ff ff ff ff
ff ff ff ff ff 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Volcana -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 05 ff ff ff 00 ff ff ff ff 00 00 0f 0f 0f 0f 0f 0f 00 00 ff ff ff ff 00 ff ff ff 05 00
00 05 ff ff ff ff ff ff ff ff 0e 00 0f 0f 0f 0f 0f 0f 00 0e ff ff ff ff ff ff ff ff 05 00
00 05 00 00 0b 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 0b 00 00 05 00
00 05 00 ff ff ff 00 ff ff ff ff ff ff 0e 00 00 0e ff ff ff ff ff ff 00 ff ff ff 00 05 00
00 ff 00 ff ff ff ff ff ff ff ff ff ff 00 00 00 00 ff ff ff ff ff ff ff ff ff ff 00 ff 00
00 ff 00 00 00 00 00 0b 0d 0d 0d 0d ff 00 00 00 00 ff 0c 0c 0c 0c 0b 00 00 00 00 00 ff 00
00 ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff 00
00 ff 00 0f 0f 00 0e ff ff ff ff ff 00 ff ff ff ff 00 ff ff ff ff ff 0e 00 0f 0f 00 ff 00
00 ff 00 0f 0f 00 00 ff 0c 0c 0c 0c 00 0b 0b 0b 0b 00 0d 0d 0d 0d ff 00 00 0f 0f 00 ff 00
00 ff 00 00 00 00 00 ff ff ff 00 00 00 ff ff ff ff 00 00 00 ff ff ff 00 00 00 00 00 ff 00
00 ff ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff ff ff 00
00 ff ff ff ff ff 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 ff ff ff ff ff 00
00 00 00 ff 00 00 00 00 00 00 00 0d 0d ff ff ff ff 0c 0c 00 00 00 00 00 00 00 ff 00 00 00
0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f
```

### Volcana -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 05 ff ff 05 ff ff ff ff ff ff 05 05 ff ff ff ff ff ff 05 ff ff 05 00 00 00 00
00 ff ff ff 05 ff ff 05 ff ff 0d 0d 0d ff 05 05 ff 0c 0c 0c ff ff 05 ff ff 05 ff ff ff 00
00 ff ff ff 05 ff ff 05 ff ff ff 00 00 ff 05 05 ff 00 00 ff ff ff 05 ff ff 05 ff ff ff 00
00 00 00 00 05 ff ff 05 ff ff ff ff ff ff 05 05 ff ff ff ff ff ff 05 ff ff 05 00 00 00 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff 0c 0c 0c ff ff ff ff 0d 0d 0d ff ff ff ff ff ff ff ff ff 00
00 00 00 00 ff ff ff ff ff ff 00 00 00 ff 00 00 ff 00 00 00 ff ff ff ff ff ff 00 00 00 00
00 ff ff ff ff ff 00 00 00 ff ff 02 05 ff ff ff ff 05 02 ff ff 00 00 00 ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff 00 05 ff ff ff ff 05 00 ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff 05 ff ff ff ff 05 ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff 05 ff 00 00 ff 05 ff ff ff ff ff ff ff ff ff ff ff 00
00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00
0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f
```

### Volcana -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff ff 00
00 ff ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff ff 00
00 0d 0d ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff 0c 0c 00
00 ff ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff 05 ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00
00 0d 0d ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 0c 0c 00
00 ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff ff 05 ff ff 05 ff ff ff ff ff ff ff ff ff ff ff ff ff
00 ff ff ff ff ff ff ff ff ff ff ff ff 05 ff ff 05 ff ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff 00 ff ff ff ff ff ff ff 05 ff ff 05 ff ff ff ff ff ff ff 00 ff ff ff ff 00
00 00 00 ff ff 00 ff ff ff ff ff ff ff 05 ff ff 05 ff ff ff ff ff ff ff 00 ff ff 00 00 00
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f
0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f
```

### Tide Pool -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 ff ff 06 ff ff ff ff ff ff ff ff ff ff 06 ff ff 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 06 ff ff ff ff ff ff ff ff ff ff 06 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 06 ff ff ff ff 00 00 ff ff ff ff 06 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff 06 ff 00 00 00 00 00 00 00 00 ff 06 ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 06 ff ff ff ff ff ff ff ff ff ff 06 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff 06 ff ff ff ff ff ff ff ff ff ff 06 ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff 06 ff ff ff ff ff ff ff ff ff ff 06 ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 ff 0f 0f 0f 0f ff 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Tide Pool -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff 00 00 ff ff ff ff 00 00 ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 0f 0f 0f 0f 0f ff 0f 0f ff 0f 0f ff 0f 0f ff 0f 0f 0f 0f 0f ff ff ff ff ff
ff ff ff ff ff 02 0f 0f 0f 0f 0f 0f 0f 00 0f 0f 00 0f 0f 0f 0f 0f 0f 0f 02 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Tide Pool -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff 00
00 ff 06 ff 00 00 ff 06 ff 00 ff ff 06 ff ff ff ff 06 ff ff 00 ff 06 ff 00 00 ff 06 ff 00
00 00 06 00 00 00 00 06 00 00 ff ff 06 ff 00 00 ff 06 ff ff 00 00 06 00 00 00 00 06 00 00
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff ff ff 06 ff ff
ff ff 00 ff ff ff ff 00 ff ff ff ff 00 ff ff ff ff 00 ff ff ff ff 00 ff ff ff ff 00 ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Tide Pool -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff 00 00 ff ff ff 00 06 ff ff ff ff ff ff ff ff 06 00 ff ff ff 00 00 ff ff ff 00
00 ff ff ff 00 00 ff ff ff 00 06 00 ff ff ff ff ff ff 00 06 00 ff ff ff 00 00 ff ff ff 00
00 00 ff 00 00 00 00 ff 00 00 06 00 ff ff 0f 0f ff ff 00 06 00 00 ff 00 00 00 00 ff 00 00
ff ff ff ff ff ff ff ff ff ff 06 00 00 0f ff ff 0f 00 00 06 ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff 06 00 ff 0f 00 00 0f ff 00 06 ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff 06 00 0f 0f 0f 0f 0f 0f 00 06 ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff 06 00 00 00 00 00 00 00 00 06 ff ff ff ff ff ff ff ff ff ff
00 00 ff 00 00 00 00 ff 00 00 06 00 00 00 00 00 00 00 00 06 00 00 ff 00 00 00 00 ff 00 00
00 ff ff ff ff ff ff ff 00 00 06 ff ff ff ff ff ff ff ff 06 00 00 ff ff ff ff ff ff ff 00
00 00 ff 00 00 00 00 ff ff ff 06 ff ff ff ff ff ff ff ff 06 ff ff ff 00 00 00 00 ff 00 00
00 ff ff ff ff ff ff ff ff ff 06 ff ff ff ff ff ff ff ff 06 ff ff ff ff ff ff ff ff ff 00
02 ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff 02
00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Tide Pool -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff ff ff ff ff ff ff ff ff ff 00 0f 0f 00 ff ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff 06 ff ff 00 0f 0f 00 ff ff 06 ff ff ff ff ff ff ff ff ff 00
00 00 ff ff ff ff ff ff ff ff 06 ff 00 00 0f 0f 00 00 ff 06 ff ff ff ff ff ff ff ff 00 00
00 ff ff ff ff ff ff ff ff ff 06 ff 00 0f ff ff 0f 00 ff 06 ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff 00 ff ff ff 06 ff 00 0f 0f 0f 0f 00 ff 06 ff ff ff 00 ff ff ff ff ff 00
00 00 00 ff ff ff 00 ff ff ff 06 ff ff 0f 0f 0f 0f ff ff 06 ff ff ff 00 ff ff ff 00 00 00
00 00 00 00 ff ff 00 00 00 00 06 00 00 00 00 00 00 00 00 06 00 00 00 00 ff ff 00 00 00 00
00 00 00 00 ff ff 00 00 00 00 06 00 00 ff ff ff ff 00 00 06 00 00 00 00 ff ff 00 00 00 00
00 ff ff 00 ff ff ff ff ff 00 06 00 00 00 02 02 00 00 00 06 00 ff ff ff ff ff 00 ff ff 00
00 02 ff ff ff ff ff ff ff ff 06 00 00 00 00 00 00 00 00 06 ff ff ff ff ff ff ff ff 02 00
00 00 00 00 00 00 ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff 00 00 00 00 00 00
00 00 00 00 ff ff ff ff ff 00 ff ff ff 00 00 00 00 ff ff ff 00 ff ff ff ff ff 00 00 00 00
00 00 ff ff ff ff ff ff ff ff ff ff 02 00 00 00 00 02 ff ff ff ff ff ff ff ff ff ff 00 00
00 00 00 00 00 ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff 00 00 00 00 00
```

### Temple of Anubis -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 10 10 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff 00 ff ff ff ff ff ff 10 10 ff ff ff ff ff ff 00 ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff 00 00 ff ff ff ff 00 00 ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Temple of Anubis -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 ff ff ff ff ff 00 00 ff ff ff ff ff 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff 00 00 00 00 ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff 00 00 00 00 00 00 ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 02 02 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Temple of Anubis -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
11 ff ff ff ff ff ff ff ff 00 09 09 09 09 10 10 09 09 09 09 00 ff ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff ff ff ff 09 09 09 09 00 00 09 09 09 09 ff ff ff ff ff ff ff ff ff 11
11 00 00 00 00 ff ff ff ff ff 09 09 09 09 ff ff 09 09 09 09 ff ff ff ff ff 00 00 00 00 11
11 00 00 00 00 00 ff ff ff ff 09 09 10 10 09 09 10 10 09 09 ff ff ff ff 00 00 00 00 00 11
11 00 00 00 00 00 00 ff ff ff 09 09 10 10 09 09 10 10 09 09 ff ff ff 00 00 00 00 00 00 11
11 11 11 ff ff ff ff ff ff ff 00 00 00 00 09 09 00 00 00 00 ff ff ff ff ff ff ff 11 11 11
11 11 11 ff ff ff ff ff ff 00 00 00 00 00 09 09 00 00 00 00 00 ff ff ff ff ff ff 11 11 11
11 11 11 ff ff ff ff ff ff 00 00 00 00 00 09 09 00 00 00 00 00 ff ff ff ff ff ff 11 11 11
11 00 00 00 00 00 ff ff ff ff 09 09 10 10 09 09 10 10 09 09 ff ff ff ff 00 00 00 00 00 11
11 00 00 00 00 00 00 ff ff ff 09 09 10 10 09 09 10 10 09 09 ff ff ff 00 00 00 00 00 00 11
11 00 00 00 00 00 00 00 ff ff 09 09 09 09 02 02 09 09 09 09 ff ff 00 00 00 00 00 00 00 11
11 ff ff ff ff ff ff ff ff ff 09 09 09 09 00 00 09 09 09 09 ff ff ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff ff ff 00 09 09 09 09 10 10 09 09 09 09 00 ff ff ff ff ff ff ff ff 11
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Temple of Anubis -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 ff ff ff ff 00 00 10 00 00 10 00 00 10 00 00 10 00 00 ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff 00 00 00 ff 00 00 ff 00 00 ff 00 00 ff 00 00 00 ff ff ff 00 00 00 00
10 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 10
00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 00 00
10 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 10
00 00 00 00 ff ff ff ff ff ff ff ff 00 ff 00 00 ff 00 ff ff ff ff ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff ff ff ff ff 00 00 ff 00 00 ff 00 00 ff ff ff ff ff ff ff 00 00 00 00
10 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 10
00 00 00 00 ff ff ff ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff 00 00 ff ff ff ff 00 00 00 00
00 00 00 00 ff ff ff 00 00 00 10 00 00 10 00 00 10 00 00 10 00 00 00 ff ff ff 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Temple of Anubis -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
11 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 11
11 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 11
11 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 11
11 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff 11
11 00 00 00 00 00 ff ff ff ff 00 00 ff ff ff ff ff ff 00 00 ff ff ff ff 00 00 00 00 00 11
11 00 00 00 00 00 00 ff ff ff 00 00 ff ff ff ff ff ff 00 00 ff ff ff 00 00 00 00 00 00 11
11 ff ff ff ff ff ff ff ff 00 00 00 11 11 11 11 11 11 00 00 00 ff ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff ff 00 00 00 00 11 11 11 11 11 11 00 00 00 00 ff ff ff ff ff ff ff 11
11 ff ff ff ff ff ff 00 00 00 00 11 11 11 11 11 11 11 11 00 00 00 00 ff ff ff ff ff ff 11
11 ff ff ff ff ff 00 00 00 11 11 11 11 11 11 11 11 11 11 11 11 00 00 00 ff ff ff ff ff 11
11 ff ff ff ff 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 11 ff ff ff ff 11
00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

### Ice Caves -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff 12 12 12 12 12 12 ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff 12 12 ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff 12 ff ff ff ff ff ff ff 12 12 ff ff ff ff ff ff ff 12 ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff 12 12 12 12 12 12 ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff 12 ff ff ff ff ff ff ff ff ff ff 12 ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff 12 12 12 12 12 12 ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 12 ff ff ff ff ff ff ff ff 12 12 ff ff ff ff ff ff ff ff 12 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff 12 12 ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff 12 ff ff ff 12 12 12 12 12 12 ff ff ff 12 ff ff ff ff ff ff ff ff
ff ff ff ff ff 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Ice Caves -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff 0b ff ff 0b ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff 0b ff ff ff ff ff ff ff ff 0b ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 13 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Ice Caves -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00
00 ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff ff 00
00 00 00 0b ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 0b 00 00 00
00 ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00
00 00 00 ff ff ff ff ff ff ff ff ff ff 0b 12 12 0b ff ff ff ff ff ff ff ff ff ff 00 00 00
00 ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff 00
ff ff ff ff ff ff ff ff 13 ff ff ff ff ff ff ff ff ff ff ff ff 13 ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff
ff ff ff ff 13 ff ff ff ff ff ff 13 ff ff ff ff ff ff 13 ff ff ff ff ff ff 13 ff ff ff ff
ff ff ff ff 00 ff ff ff ff ff ff 00 ff ff ff ff ff ff 00 ff ff ff ff ff ff 00 ff ff ff ff
ff 13 ff ff 00 ff ff ff ff ff ff ff ff 13 ff ff 13 ff ff ff ff ff ff ff ff 00 ff ff 13 ff
00 00 ff ff ff ff ff ff ff ff ff ff ff 00 ff ff 00 ff ff ff ff ff ff ff ff ff ff ff 00 00
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Ice Caves -
```
12 12 12 12 12 12 12 12 12 12 12 12 00 00 00 00 00 00 12 12 12 12 12 12 12 12 12 12 12 12
12 ff ff ff 12 12 ff ff ff 12 ff ff ff ff ff ff ff ff ff ff 12 ff ff ff 12 12 ff ff ff 12
00 ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff 00
00 00 ff 00 00 00 00 ff 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 ff 00 00 00 00 ff 00 00
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 12 ff ff
ff ff ff ff ff ff ff 00 00 00 12 12 12 12 12 12 12 12 12 12 00 00 00 ff ff ff ff ff ff ff
ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Ice Caves -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
12 ff ff ff ff ff 12 12 12 12 12 12 ff ff ff ff ff ff 12 12 12 12 12 12 ff ff ff ff ff 12
12 12 12 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 12 12 12
12 12 ff ff ff ff ff ff ff ff ff ff ff 12 ff ff 12 ff ff ff ff ff ff ff ff ff ff ff 12 12
12 12 ff ff ff ff ff ff ff ff ff ff ff 12 ff ff 12 ff ff ff ff ff ff ff ff ff ff ff 12 12
12 12 ff ff ff ff ff ff ff ff ff ff ff 12 00 00 12 ff ff ff ff ff ff ff ff ff ff ff 12 12
12 ff ff ff 13 ff ff ff ff ff ff ff 13 12 12 12 12 13 ff ff ff ff ff ff ff 13 ff ff ff 12
12 ff ff ff 00 ff ff ff ff ff ff ff 00 12 12 12 12 00 ff ff ff ff ff ff ff 00 ff ff ff 12
12 12 ff ff ff ff ff ff ff ff ff 12 12 12 00 00 12 12 12 ff ff ff ff ff ff ff ff ff 12 12
00 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 00
08 08 ff ff ff ff ff 12 12 ff ff ff ff ff 12 12 ff ff ff ff ff 12 12 ff ff ff ff ff 08 08
ff ff ff ff ff ff ff ff 12 12 ff ff ff 00 00 00 00 ff ff ff 12 12 ff ff ff ff ff ff ff ff
ff ff 12 ff 13 ff ff ff 12 12 13 ff ff 12 12 12 12 ff ff 13 12 12 ff ff ff 13 ff 12 ff ff
13 13 00 00 00 00 00 00 12 12 00 00 00 12 12 12 12 00 00 00 12 12 00 00 00 00 00 00 13 13
00 00 00 00 00 00 00 12 12 12 12 00 12 12 12 12 12 12 00 12 12 12 12 00 00 00 00 00 00 00
```

### Neo Babylon -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff
ff ff ff ff ff 00 15 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 15 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 15 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 15 00 ff ff ff ff ff
ff ff ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Neo Babylon -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff 1a ff ff 1a ff ff 1a ff ff 1a ff ff 1a ff ff 1a ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff 19 ff ff 19 ff ff 19 ff ff 19 ff ff 19 ff ff 19 ff 00 ff ff ff ff ff
ff ff ff ff ff 00 ff 19 ff ff 19 00 ff 19 ff ff 19 ff 00 19 ff ff 19 ff 00 ff ff ff ff ff
ff ff ff ff ff 00 00 19 ff ff 19 00 00 19 ff ff 19 00 00 19 ff ff 19 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Neo Babylon -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00
ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff
ff 00 00 00 ff ff ff ff ff ff ff ff 00 00 ff ff 00 00 ff ff ff ff ff ff ff ff 00 00 00 ff
ff 00 ff ff ff ff ff ff ff ff ff 00 00 00 ff ff 00 00 00 ff ff ff ff ff ff ff ff ff 00 ff
ff ff ff ff ff ff 1a ff ff ff 00 00 00 00 ff ff 00 00 00 00 ff ff ff 1a ff ff ff ff ff ff
ff 00 00 00 ff ff 19 ff ff 00 00 00 00 00 ff ff 00 00 00 00 00 ff ff 19 ff ff 00 00 00 ff
ff 00 00 ff ff ff 19 ff 00 00 00 00 ff 00 ff ff 00 ff 00 00 00 00 ff 19 ff ff ff 00 00 ff
ff ff ff ff ff ff 19 00 00 00 00 00 02 ff ff ff ff 02 00 00 00 00 00 19 ff ff ff ff ff ff
ff ff ff ff ff ff 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 00 ff ff ff ff ff
ff ff ff ff 00 00 00 00 15 00 00 00 00 00 ff ff 00 00 00 00 00 15 00 00 00 00 ff ff ff ff
ff ff ff 00 00 00 00 00 ff 00 00 00 00 00 ff ff 00 00 00 00 00 ff 00 00 00 00 00 ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
14 00 00 00 00 00 00 00 15 00 00 00 00 00 14 14 00 00 00 00 00 15 00 00 00 00 00 00 00 14
```

### Neo Babylon -
```
15 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 15
ff 00 00 15 00 ff ff ff ff ff 00 15 00 00 00 00 00 00 15 00 ff ff ff ff ff 00 15 00 00 ff
ff 00 ff ff ff ff ff ff ff ff ff ff ff 00 ff ff 00 ff ff ff ff ff ff ff ff ff ff ff 00 ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff 15 00 ff ff ff ff ff 00 15 ff ff ff ff ff ff 15 00 ff ff ff ff ff 00 15 ff ff ff
ff ff ff 00 00 00 00 00 00 00 00 00 ff ff 00 00 ff ff 00 00 00 00 00 00 00 00 00 ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff 00 00 00 00 00 00 00 00 00 ff ff ff ff ff ff 00 00 00 00 00 00 00 00 00 ff ff ff
ff ff 00 15 00 ff ff ff ff ff 00 15 ff ff ff ff ff ff 15 00 ff ff ff ff ff 00 15 00 ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff 14 ff 15 00 ff ff ff ff ff 00 15 00 14 ff ff 14 00 15 00 ff ff ff ff ff 00 15 ff 14 ff
ff 00 ff 00 00 00 00 00 00 00 00 00 00 00 ff ff 00 00 00 00 00 00 00 00 00 00 00 ff 00 ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
15 00 00 00 00 00 00 00 00 00 00 00 00 00 14 14 00 00 00 00 00 00 00 00 00 00 00 00 00 15
```

### Neo Babylon -
```
ff 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ff
ff 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff 00 ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff 16 ff ff 16 ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff 16 ff ff 16 ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff 16 ff ff 16 ff ff 00 00 00 00 00 00 00 00 00 00 00 00 ff ff 16 ff ff 16 ff ff ff
ff ff ff ff ff ff ff ff ff 00 15 00 00 15 00 00 15 00 00 15 00 ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff 1a ff ff 16 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 16 ff ff 1a ff ff ff
14 ff ff 19 ff ff ff 1a ff ff ff ff ff ff ff ff ff ff ff ff ff ff 1a ff ff ff 19 ff ff 14
00 02 ff 19 ff ff ff 19 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 19 ff ff ff 19 ff 02 00
00 00 ff 19 ff ff ff 19 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 19 ff ff ff 19 ff 00 00
00 00 00 00 00 00 00 19 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 19 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 15 14 14 15 14 14 15 14 14 15 00 00 00 00 00 00 00 00 00 00
```

### Sunken City -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 00 00 00 17 17 17 17 00 00 00 00 00 00 17 17 17 17 00 00 00 ff ff ff ff ff
ff ff ff ff ff 17 00 00 00 17 00 17 17 00 17 17 00 17 17 00 17 00 00 00 17 ff ff ff ff ff
ff ff ff ff ff 17 ff ff ff ff 17 17 17 ff 17 17 ff 17 17 17 ff ff ff ff 17 ff ff ff ff ff
ff ff ff ff ff 00 17 ff ff ff ff ff ff ff 17 17 ff ff ff ff ff ff ff 17 00 ff ff ff ff ff
ff ff ff ff ff 17 17 ff ff ff ff ff ff ff 17 17 ff ff ff ff ff ff ff 17 17 ff ff ff ff ff
ff ff ff ff ff 17 ff ff ff ff ff ff ff ff 17 17 ff ff ff ff ff ff ff ff 17 ff ff ff ff ff
ff ff ff ff ff 17 ff ff ff ff ff 17 ff ff 17 17 ff ff 17 ff ff ff ff ff 17 ff ff ff ff ff
ff ff ff ff ff 17 00 ff ff ff ff 17 17 17 17 17 17 17 17 ff ff ff ff 00 17 ff ff ff ff ff
ff ff ff ff ff 00 00 00 17 00 00 17 17 00 00 00 00 17 17 00 00 17 00 00 00 ff ff ff ff ff
ff ff ff ff ff 00 00 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 17 00 00 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Sunken City -
```
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff 18 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 18 ff ff ff ff ff
ff ff ff ff ff 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 ff ff ff ff ff
ff ff ff ff ff 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 ff ff ff ff ff
ff ff ff ff ff 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 ff ff ff ff ff
ff ff ff ff ff 18 17 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 17 18 ff ff ff ff ff
ff ff ff ff ff 18 ff ff ff ff ff ff ff ff 17 17 ff ff ff ff ff ff ff ff 18 ff ff ff ff ff
ff ff ff ff ff 18 ff ff ff ff ff 00 ff ff ff ff ff ff 00 ff ff ff ff ff 18 ff ff ff ff ff
ff ff ff ff ff 18 00 ff ff ff ff 00 00 ff ff ff ff 00 00 ff ff ff ff 00 18 ff ff ff ff ff
ff ff ff ff ff 18 00 00 00 00 18 00 00 00 00 00 00 00 00 18 00 00 00 00 18 ff ff ff ff ff
ff ff ff ff ff 18 18 18 18 18 18 00 00 00 00 00 00 00 00 18 18 18 18 18 18 ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff
```

### Sunken City -
```
18 18 18 18 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 18 18 18 18
18 ff ff ff 18 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 0f 18 ff ff ff 18
18 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 18
18 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 18
18 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 18
18 ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff 18
18 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 00 00 ff ff ff ff ff ff ff ff ff ff 00 00 18
18 ff ff ff ff ff ff ff ff ff ff ff 00 00 00 00 00 00 ff ff ff ff ff ff ff ff ff ff ff 18
18 ff ff ff ff ff ff ff ff ff 17 17 00 00 00 00 00 00 17 17 ff ff ff ff ff ff ff ff ff 18
18 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 18
18 ff ff ff 17 17 17 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 17 17 17 ff ff ff 18
18 ff ff ff ff ff ff ff ff ff ff ff ff ff 17 17 ff ff ff ff ff ff ff ff ff ff ff ff ff 18
18 18 ff ff ff ff ff ff ff ff ff 17 17 ff ff ff ff 17 17 ff ff ff ff ff ff ff ff ff 18 18
00 00 00 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 00 00 00
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```

### Sunken City -
```
00 ff ff 18 18 18 18 18 18 18 18 18 18 ff ff ff ff 18 18 18 18 18 18 18 18 18 18 ff ff 00
00 ff ff 18 ff 00 00 00 0f 0f 17 17 ff ff ff ff ff ff 17 17 0f 0f 00 00 00 ff 18 ff ff 00
00 ff ff ff ff 18 18 18 0f 0f 00 00 00 18 07 07 18 00 00 00 0f 0f 18 18 18 ff ff ff ff 00
00 18 02 ff ff 00 ff 18 ff 18 18 18 00 18 00 00 18 00 18 18 18 ff 18 ff 00 ff ff 02 18 00
00 18 00 00 18 00 ff ff ff 17 00 18 00 18 00 00 18 00 18 00 17 ff ff ff 00 18 00 00 18 00
ff 18 ff 00 18 00 00 00 00 ff 00 18 18 0f ff ff 0f 18 18 00 ff 00 00 00 00 18 00 ff 18 ff
ff ff ff 00 18 00 00 00 ff ff 00 ff ff 0f 00 00 0f ff ff 00 ff ff 00 00 00 18 00 ff ff ff
18 ff ff 00 18 18 18 ff ff ff 18 18 18 0f 0f 0f 0f 18 18 18 ff ff ff 18 18 18 00 ff ff 18
18 00 18 00 00 00 00 ff ff 17 17 ff ff 0f 0f 0f 0f ff ff 17 17 ff ff 00 00 00 00 18 00 18
18 00 18 18 ff ff 00 00 00 00 18 18 18 0f 0f 0f 0f 18 18 18 00 00 00 00 ff ff 18 18 00 18
18 00 00 00 17 ff ff 18 18 18 18 00 00 0f 0f 0f 0f 00 00 18 18 18 18 ff ff 17 00 00 00 18
18 ff 18 18 ff ff ff 17 0f 0f 00 00 00 18 0f 0f 18 00 00 00 0f 0f 17 ff ff ff 18 18 ff 18
ff ff 18 00 00 18 00 00 0f 0f 18 18 18 18 0f 0f 18 18 18 18 0f 0f 00 00 18 00 00 18 ff ff
02 ff ff 00 00 18 00 00 ff ff ff 17 17 0f 0f 0f 0f 17 17 ff ff ff 00 00 18 00 00 ff ff 02
00 ff ff 00 00 18 18 18 18 18 18 18 18 18 07 07 18 18 18 18 18 18 18 18 18 00 00 ff ff 00
```

### Sunken City -
```
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
18 18 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 18 18
18 ff ff ff ff 17 17 ff ff ff ff 18 18 ff ff ff ff 18 18 ff ff ff ff 17 17 ff ff ff ff 18
18 17 00 00 00 00 00 00 00 00 00 00 18 00 00 00 00 18 00 00 00 00 00 00 00 00 00 00 17 18
18 18 18 ff ff ff ff ff ff ff 17 ff ff ff 00 00 ff ff ff 17 ff ff ff ff ff ff ff 18 18 18
ff 00 17 17 ff ff ff ff ff ff 00 ff ff ff 18 18 ff ff ff 00 ff ff ff ff ff ff 17 17 00 ff
ff 00 00 ff ff ff 17 17 ff ff 00 00 18 00 00 00 00 18 00 00 ff ff 17 17 ff ff ff 00 00 ff
ff 00 00 ff ff ff 17 17 ff ff 00 00 18 00 00 00 00 18 00 00 ff ff 17 17 ff ff ff 00 00 ff
ff 00 17 17 ff ff ff ff ff ff 00 ff ff ff 00 00 ff ff ff 00 ff ff ff ff ff ff 17 17 00 ff
18 18 18 ff ff ff ff ff ff ff 17 ff ff ff 17 17 ff ff ff 17 ff ff ff ff ff ff ff 18 18 18
18 17 00 00 00 00 00 00 00 00 00 00 18 00 00 00 00 18 00 00 00 00 00 00 00 00 00 00 17 18
18 ff ff ff ff 17 17 ff ff ff ff 18 18 ff ff ff ff 18 18 ff ff ff ff 17 17 ff ff ff ff 18
18 18 ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff 18 18
17 17 17 00 00 00 00 00 00 17 17 17 17 00 00 00 00 17 17 17 17 00 00 00 00 00 00 17 17 17
07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
```
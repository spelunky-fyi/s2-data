
# File Access and Info

http://cdn.spelunky2.net/static/YYYYMMDD appears to be a CDN in front of http://cosmic-ocean.spelunky2.net/static/YYYYMMDD where YYYYMMDD represents the date of the leaderboards being requested. e.g. 20201016 for October 16, 2020.

* Compression: zstd
* Uncompressed File Size: 67,000,008 bytes

The data consists of what appears to be 7 aligned arrays of data. An index in one array is related to that same index in the other arrays.

Note: The first 2 entries in each array appear to always be empty.

# Format

A types specified below are in little endian byte order.

## Header

```
00: u64 - Number of Entries
```

## Data

| Offset | Type | Notes |
| ------ | ---- | ----- |
| 0x0000008 | u64 | User ID |
| 0x07A1208 | 33 bytes. Fixed width string buffer. utf-8 | Usernames |
| 0x2719C48 | u8, u8 | (Platform, Character)
| 0x29020C8 | u32, u32 | (Number of frames, Ending)
| 0x30A32C8 | u32, u32 | (Scores, Level)
| 0x38444C8 | 4 bytes | Unknown
| 0x3c14dC8 | 4 bytes | Unknown

### Platforms

```
Steam: 0x12
PS4:   0x30
```

### Characters

```
Ana:         0x00
Margaret:    0x01
Colin:       0x02
Roffy:       0x03
Alto:        0x04
Liz:         0x05
Nekka:       0x06
LISE:        0x07
Coco:        0x08
Manfred:     0x09
Jay:         0x0A
Tina:        0x0B
Valerie:     0x0C
Au:          0x0D
Demi:        0x0E
Pilot:       0x0F
Airyn:       0x10
Dirk:        0x11
Guy:         0x12
Classic Guy: 0x13
```

### Ending

Specifies whether you've completed the game, and in which way, during the run.

```
Normal Win:  0x02ED
Hard Win:    0x01E9
Special Win: 0x008A
```

# Credits

The following resources were helpful building this information

 * https://www.reddit.com/r/spelunky/comments/j4wbfk/spelunky_2_leaderboard_format/
 * https://github.com/VDZx/Spelunky2LeaderboardGenerator

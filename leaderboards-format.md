# Credits
 * https://www.reddit.com/r/spelunky/comments/j4wbfk/spelunky_2_leaderboard_format/

# File Access and Info

http://cdn.spelunky2.net/static/YYYYMMDD appears to be a CDN in front of http://cosmic-ocean.spelunky2.net/static/YYYYMMDD where YYYYMMDD represents the date of the leaderboards being requested. e.g. 20201016 for October 16, 2020.

* Compression: zstd
* Uncompressed File Size: 67,000,008 bytes

The data consists of what appears to be 7 aligned arrays of data. An index in one array is related to that same index in the other arrays.

Note: The first 2 entries in each array appear to always be empty.

# Save Format

## Header

```
00: uint32  - Number of Entries
04: 8 bytes - Padding
```

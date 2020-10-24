from struct import pack, unpack
from PIL import Image
import io

from .chacha import Key, filename_hash, decrypt_data, encrypt_data

KNOWN_ASSETS = [
    b"Data/Fonts/fontdebug.fnb",
    b"Data/Fonts/fontfirasans.fnb",
    b"Data/Fonts/fontmono.fnb",
    b"Data/Fonts/fontyorkten.fnb",
    b"Data/Levels/abzu.lvl",
    b"Data/Levels/Arena/dm1-1.lvl",
    b"Data/Levels/Arena/dm1-2.lvl",
    b"Data/Levels/Arena/dm1-3.lvl",
    b"Data/Levels/Arena/dm1-4.lvl",
    b"Data/Levels/Arena/dm1-5.lvl",
    b"Data/Levels/Arena/dm2-1.lvl",
    b"Data/Levels/Arena/dm2-2.lvl",
    b"Data/Levels/Arena/dm2-3.lvl",
    b"Data/Levels/Arena/dm2-4.lvl",
    b"Data/Levels/Arena/dm2-5.lvl",
    b"Data/Levels/Arena/dm3-1.lvl",
    b"Data/Levels/Arena/dm3-2.lvl",
    b"Data/Levels/Arena/dm3-3.lvl",
    b"Data/Levels/Arena/dm3-4.lvl",
    b"Data/Levels/Arena/dm3-5.lvl",
    b"Data/Levels/Arena/dm4-1.lvl",
    b"Data/Levels/Arena/dm4-2.lvl",
    b"Data/Levels/Arena/dm4-3.lvl",
    b"Data/Levels/Arena/dm4-4.lvl",
    b"Data/Levels/Arena/dm4-5.lvl",
    b"Data/Levels/Arena/dm5-1.lvl",
    b"Data/Levels/Arena/dm5-2.lvl",
    b"Data/Levels/Arena/dm5-3.lvl",
    b"Data/Levels/Arena/dm5-4.lvl",
    b"Data/Levels/Arena/dm5-5.lvl",
    b"Data/Levels/Arena/dm6-1.lvl",
    b"Data/Levels/Arena/dm6-2.lvl",
    b"Data/Levels/Arena/dm6-3.lvl",
    b"Data/Levels/Arena/dm6-4.lvl",
    b"Data/Levels/Arena/dm6-5.lvl",
    b"Data/Levels/Arena/dm7-1.lvl",
    b"Data/Levels/Arena/dm7-2.lvl",
    b"Data/Levels/Arena/dm7-3.lvl",
    b"Data/Levels/Arena/dm7-4.lvl",
    b"Data/Levels/Arena/dm7-5.lvl",
    b"Data/Levels/Arena/dm8-1.lvl",
    b"Data/Levels/Arena/dm8-2.lvl",
    b"Data/Levels/Arena/dm8-3.lvl",
    b"Data/Levels/Arena/dm8-4.lvl",
    b"Data/Levels/Arena/dm8-5.lvl",
    b"Data/Levels/Arena/dmpreview.tok",
    b"Data/Levels/babylonarea.lvl",
    b"Data/Levels/basecamp_garden.lvl",
    b"Data/Levels/basecamp.lvl",
    b"Data/Levels/basecamp_shortcut_discovered.lvl",
    b"Data/Levels/basecamp_shortcut_undiscovered.lvl",
    b"Data/Levels/basecamp_shortcut_unlocked.lvl",
    b"Data/Levels/basecamp_surface.lvl",
    b"Data/Levels/basecamp_tutorial.lvl",
    b"Data/Levels/basecamp_tv_room_locked.lvl",
    b"Data/Levels/basecamp_tv_room_unlocked.lvl",
    b"Data/Levels/beehive.lvl",
    b"Data/Levels/blackmarket.lvl",
    b"Data/Levels/cavebossarea.lvl",
    b"Data/Levels/challenge_moon.lvl",
    b"Data/Levels/challenge_star.lvl",
    b"Data/Levels/challenge_sun.lvl",
    b"Data/Levels/cityofgold.lvl",
    b"Data/Levels/cosmicocean_babylon.lvl",
    b"Data/Levels/cosmicocean_dwelling.lvl",
    b"Data/Levels/cosmicocean_icecavesarea.lvl",
    b"Data/Levels/cosmicocean_jungle.lvl",
    b"Data/Levels/cosmicocean_sunkencity.lvl",
    b"Data/Levels/cosmicocean_temple.lvl",
    b"Data/Levels/cosmicocean_tidepool.lvl",
    b"Data/Levels/cosmicocean_volcano.lvl",
    b"Data/Levels/duat.lvl",
    b"Data/Levels/dwellingarea.lvl",
    b"Data/Levels/eggplantarea.lvl",
    b"Data/Levels/ending.lvl",
    b"Data/Levels/generic.lvl",
    b"Data/Levels/hallofushabti.lvl",
    b"Data/Levels/hundun.lvl",
    b"Data/Levels/icecavesarea.lvl",
    b"Data/Levels/junglearea.lvl",
    b"Data/Levels/lake.lvl",
    b"Data/Levels/lakeoffire.lvl",
    b"Data/Levels/olmecarea.lvl",
    b"Data/Levels/palaceofpleasure.lvl",
    b"Data/Levels/sunkencityarea.lvl",
    b"Data/Levels/templearea.lvl",
    b"Data/Levels/testingarea.lvl",
    b"Data/Levels/tiamat.lvl",
    b"Data/Levels/tidepoolarea.lvl",
    b"Data/Levels/vladscastle.lvl",
    b"Data/Levels/volcanoarea.lvl",
    b"Data/Textures/base_eggship2.png",
    b"Data/Textures/base_eggship3.png",
    b"Data/Textures/base_eggship.png",
    b"Data/Textures/base_skynight.png",
    b"Data/Textures/base_surface2.png",
    b"Data/Textures/base_surface.png",
    b"Data/Textures/bayer8.png",
    b"Data/Textures/bg_babylon.png",
    b"Data/Textures/bg_beehive.png",
    b"Data/Textures/bg_cave.png",
    b"Data/Textures/bg_duat2.png",
    b"Data/Textures/bg_duat.png",
    b"Data/Textures/bg_eggplant.png",
    b"Data/Textures/bg_gold.png",
    b"Data/Textures/bg_ice.png",
    b"Data/Textures/bg_jungle.png",
    b"Data/Textures/bg_mothership.png",
    b"Data/Textures/bg_stone.png",
    b"Data/Textures/bg_sunken.png",
    b"Data/Textures/bg_temple.png",
    b"Data/Textures/bg_tidepool.png",
    b"Data/Textures/bg_vlad.png",
    b"Data/Textures/bg_volcano.png",
    b"Data/Textures/border_main.png",
    b"Data/Textures/char_black.png",
    b"Data/Textures/char_blue.png",
    b"Data/Textures/char_cerulean.png",
    b"Data/Textures/char_cinnabar.png",
    b"Data/Textures/char_cyan.png",
    b"Data/Textures/char_eggchild.png",
    b"Data/Textures/char_gold.png",
    b"Data/Textures/char_gray.png",
    b"Data/Textures/char_green.png",
    b"Data/Textures/char_hired.png",
    b"Data/Textures/char_iris.png",
    b"Data/Textures/char_khaki.png",
    b"Data/Textures/char_lemon.png",
    b"Data/Textures/char_lime.png",
    b"Data/Textures/char_magenta.png",
    b"Data/Textures/char_olive.png",
    b"Data/Textures/char_orange.png",
    b"Data/Textures/char_pink.png",
    b"Data/Textures/char_red.png",
    b"Data/Textures/char_violet.png",
    b"Data/Textures/char_white.png",
    b"Data/Textures/char_yellow.png",
    b"Data/Textures/coffins.png",
    b"Data/Textures/credits.png",
    b"Data/Textures/deco_babylon.png",
    b"Data/Textures/deco_basecamp.png",
    b"Data/Textures/deco_cave.png",
    b"Data/Textures/deco_cosmic.png",
    b"Data/Textures/deco_eggplant.png",
    b"Data/Textures/deco_extra.png",
    b"Data/Textures/deco_gold.png",
    b"Data/Textures/deco_ice.png",
    b"Data/Textures/deco_jungle.png",
    b"Data/Textures/deco_sunken.png",
    b"Data/Textures/deco_temple.png",
    b"Data/Textures/deco_tidepool.png",
    b"Data/Textures/deco_tutorial.png",
    b"Data/Textures/deco_volcano.png",
    b"Data/Textures/floor_babylon.png",
    b"Data/Textures/floor_cave.png",
    b"Data/Textures/floor_eggplant.png",
    b"Data/Textures/floor_ice.png",
    b"Data/Textures/floor_jungle.png",
    b"Data/Textures/floormisc.png",
    b"Data/Textures/floorstyled_babylon.png",
    b"Data/Textures/floorstyled_beehive.png",
    b"Data/Textures/floorstyled_duat.png",
    b"Data/Textures/floorstyled_gold_normal.png",
    b"Data/Textures/floorstyled_gold.png",
    b"Data/Textures/floorstyled_guts.png",
    b"Data/Textures/floorstyled_mothership.png",
    b"Data/Textures/floorstyled_pagoda.png",
    b"Data/Textures/floorstyled_palace.png",
    b"Data/Textures/floorstyled_stone.png",
    b"Data/Textures/floorstyled_sunken.png",
    b"Data/Textures/floorstyled_temple.png",
    b"Data/Textures/floorstyled_vlad.png",
    b"Data/Textures/floorstyled_wood.png",
    b"Data/Textures/floor_sunken.png",
    b"Data/Textures/floor_surface.png",
    b"Data/Textures/floor_temple.png",
    b"Data/Textures/floor_tidepool.png",
    b"Data/Textures/floor_volcano.png",
    b"Data/Textures/fontdebug.png",
    b"Data/Textures/fontfirasans.png",
    b"Data/Textures/fontmono.png",
    b"Data/Textures/fontyorkten.png",
    b"Data/Textures/fx_ankh.png",
    b"Data/Textures/fx_big.png",
    b"Data/Textures/fx_explosion.png",
    b"Data/Textures/fx_rubble.png",
    b"Data/Textures/fx_small2.png",
    b"Data/Textures/fx_small3.png",
    b"Data/Textures/fx_small.png",
    b"Data/Textures/hud_controller_buttons.png",
    b"Data/Textures/hud.png",
    b"Data/Textures/hud_text.png",
    b"Data/Textures/items.png",
    b"Data/Textures/items_ushabti.png",
    b"Data/Textures/journal_back.png",
    b"Data/Textures/journal_elements.png",
    b"Data/Textures/journal_entry_bg.png",
    b"Data/Textures/journal_entry_items.png",
    b"Data/Textures/journal_entry_mons_big.png",
    b"Data/Textures/journal_entry_mons.png",
    b"Data/Textures/journal_entry_people.png",
    b"Data/Textures/journal_entry_place.png",
    b"Data/Textures/journal_entry_traps.png",
    b"Data/Textures/journal_pageflip.png",
    b"Data/Textures/journal_pagetorn.png",
    b"Data/Textures/journal_select.png",
    b"Data/Textures/journal_stickers.png",
    b"Data/Textures/journal_story.png",
    b"Data/Textures/journal_top_entry.png",
    b"Data/Textures/journal_top_gameover.png",
    b"Data/Textures/journal_top_main.png",
    b"Data/Textures/journal_top_profile.png",
    b"Data/Textures/loading.png",
    b"Data/Textures/lut_backlayer.png",
    b"Data/Textures/lut_blackmarket.png",
    b"Data/Textures/lut_icecaves.png",
    b"Data/Textures/lut_original.png",
    b"Data/Textures/lut_vlad.png",
    b"Data/Textures/main_body.png",
    b"Data/Textures/main_dirt.png",
    b"Data/Textures/main_doorback.png",
    b"Data/Textures/main_doorframe.png",
    b"Data/Textures/main_door.png",
    b"Data/Textures/main_fore1.png",
    b"Data/Textures/main_fore2.png",
    b"Data/Textures/main_head.png",
    b"Data/Textures/menu_basic.png",
    b"Data/Textures/menu_brick1.png",
    b"Data/Textures/menu_brick2.png",
    b"Data/Textures/menu_cave1.png",
    b"Data/Textures/menu_cave2.png",
    b"Data/Textures/menu_chardoor.png",
    b"Data/Textures/menu_charsel.png",
    b"Data/Textures/menu_deathmatch2.png",
    b"Data/Textures/menu_deathmatch3.png",
    b"Data/Textures/menu_deathmatch4.png",
    b"Data/Textures/menu_deathmatch5.png",
    b"Data/Textures/menu_deathmatch6.png",
    b"Data/Textures/menu_deathmatch.png",
    b"Data/Textures/menu_disp.png",
    b"Data/Textures/menu_generic.png",
    b"Data/Textures/menu_header.png",
    b"Data/Textures/menu_leader.png",
    b"Data/Textures/menu_online.png",
    b"Data/Textures/menu_titlegal.png",
    b"Data/Textures/menu_title.png",
    b"Data/Textures/menu_tunnel.png",
    b"Data/Textures/monsters01.png",
    b"Data/Textures/monsters02.png",
    b"Data/Textures/monsters03.png",
    b"Data/Textures/monstersbasic01.png",
    b"Data/Textures/monstersbasic02.png",
    b"Data/Textures/monstersbasic03.png",
    b"Data/Textures/monstersbig01.png",
    b"Data/Textures/monstersbig02.png",
    b"Data/Textures/monstersbig03.png",
    b"Data/Textures/monstersbig04.png",
    b"Data/Textures/monstersbig05.png",
    b"Data/Textures/monstersbig06.png",
    b"Data/Textures/monsters_ghost.png",
    b"Data/Textures/monsters_hundun.png",
    b"Data/Textures/monsters_olmec.png",
    b"Data/Textures/monsters_osiris.png",
    b"Data/Textures/monsters_pets.png",
    b"Data/Textures/monsters_tiamat.png",
    b"Data/Textures/monsters_yama.png",
    b"Data/Textures/mounts.png",
    b"Data/Textures/noise0.png",
    b"Data/Textures/noise1.png",
    b"Data/Textures/OldTextures/ai.png",
    b"Data/Textures/placeholder",
    b"Data/Textures/saving.png",
    b"Data/Textures/shadows.png",
    b"Data/Textures/shine.png",
    b"Data/Textures/splash0.png",
    b"Data/Textures/splash1.png",
    b"Data/Textures/splash2.png",
    b"shaders.hlsl",
    b"soundbank.bank",
    b"soundbank.strings.bank",
    b"strings00.str",
    b"strings01.str",
    b"strings02.str",
    b"strings03.str",
    b"strings04.str",
    b"strings05.str",
    b"strings06.str",
    b"strings07.str",
]


class Asset(object):
    def __init__(
        self, name_hash, name_len, asset_len, encrypted, offset, data_offset, data_size
    ):
        self.name_hash = name_hash
        self.name_len = name_len
        self.asset_len = asset_len
        self.encrypted = encrypted
        self.offset = offset
        self.data_offset = data_offset
        self.data_size = data_size

    @property
    def total_size(self):
        return 8 + self.name_len + self.data_size

    def __repr__(self):
        return (
            "Asset("
            "name_hash={!r}, name_len={!r}, asset_len={!r}, encrypted={!r}, "
            "offset={}, data_offset={}, data_size={!r}"
            ")"
        ).format(
            self.name_hash,
            self.name_len,
            self.asset_len,
            self.encrypted,
            hex(self.offset),
            hex(self.data_offset),
            self.data_size,
        )

    def match_hash(self, hash):
        l = min(len(hash), self.name_len)
        return hash[:l] == self.name_hash[:l]

    def extract(self, filename, handle, key):
        handle.seek(self.data_offset)
        data = handle.read(self.data_size)
        if self.encrypted:
            try:
                data = decrypt_data(filename, data, key)
            except Exception as exc:
                print(exc)
                return None

        if filename.endswith(b".png"):
            width, height = unpack(b"<II", data[:8])
            image = Image.frombytes("RGBA", (width, height), data[8:], "raw")
            new_data = io.BytesIO()
            image.save(new_data, format="PNG")
            data = new_data.getvalue()

        return data


class AssetStore(object):
    def __init__(self, exe_handle):
        self.assets = []
        self.exe_handle = exe_handle
        self.key = Key()
        self._load_assets()

    def find_asset(self, filename):
        name_hash = filename_hash(filename, self.key.key)
        for asset in self.assets:
            if asset.match_hash(name_hash):
                return asset
        return None

    def pack_asset(self, filename, new_data):
        asset = self.find_asset(filename)

        if asset.encrypted:
            size_raw = len(new_data)
            new_data = encrypt_data(filename, new_data, self.key.key)
            print(
                'Encrypting data for "{}" ({} bytes -> {} bytes)'.format(
                    filename, size_raw, len(new_data)
                )
            )

        old_size = asset.data_size
        new_size = len(new_data)

        if new_size > old_size:
            print(
                'Asset "{}" is larger than original ({} bytes > {} bytes), replacing currently not possible'.format(
                    filename, new_size, old_size
                )
            )
            return False
        elif new_size == old_size:
            print(
                'Replacing asset "{}" with same size ({} bytes)'.format(
                    filename, new_size
                )
            )
            self.exe_handle.seek(asset.data_offset)
            self.exe_handle.write(new_data)
        elif new_size < old_size:
            print(
                'Replacing asset "{}" with smaller size ({} bytes < {} bytes)'.format(
                    filename, new_size, old_size
                )
            )
            self.exe_handle.seek(asset.data_offset)
            self.exe_handle.write(new_data)

            diff = old_size - new_size
            if diff < 10:
                print(
                    "Difference is less than 10 bytes, not enoguh space to insert a padding asset. Things might break"
                )
            else:
                # Old/Replaced asset size
                self.exe_handle.seek(asset.offset)
                self.exe_handle.write(pack("<I", new_size + 1))
                # New padding asset size (with name_len = 1)
                self.exe_handle.seek(asset.data_offset + new_size)
                self.exe_handle.write(pack("<II", diff - 9, 1))

        return True

    def _load_assets(self, offset=0x400):
        self.exe_handle.seek(offset)

        while True:
            offset = self.exe_handle.tell()
            asset_len, name_len = unpack(b"<II", self.exe_handle.read(8))
            if (asset_len, name_len) == (0, 0):
                break
            assert asset_len > 0

            name_hash = self.exe_handle.read(name_len)
            encrypted = self.exe_handle.read(1) == b"\x01"
            data_offset = self.exe_handle.tell()
            data_size = asset_len - 1

            self.exe_handle.seek(data_size, 1)
            self.key.update(asset_len)

            self.assets.append(
                Asset(
                    name_hash=name_hash,
                    name_len=name_len,
                    asset_len=asset_len,
                    encrypted=encrypted,
                    offset=offset,
                    data_offset=data_offset,
                    data_size=data_size,
                )
            )

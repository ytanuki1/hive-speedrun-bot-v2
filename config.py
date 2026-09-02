import os

# プロジェクトのルートディレクトリ
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BOT_NAME = "Hive Speedrun Leaderboard"
BOT_VERSION = "2.0.0"
BOT_ACTIVITY_TEXT = "/speedrun | Gravity Leaderboard\nby Yytanuki"

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN", "")
DEV_GUILD_ID = os.environ.get("DEV_GUILD_ID", "")

# GAS環境変数は不要になりましたが、互換性のため残しています
GAS_WEBAPP_URL = os.environ.get("GAS_WEBAPP_URL", "")
GAS_API_SECRET = os.environ.get("GAS_API_SECRET", "")

DEFAULT_BACKGROUND_URL = os.environ.get(
    "DEFAULT_BACKGROUND_URL", "https://i.imgur.com/1gY2pA4.png"
)

# ------------------------------------------------------------
# 部門 / マップ設定
# ------------------------------------------------------------
DIVISIONS = {
    # --- 総合（固定選択肢） ---
    "5maps": {
        "label": "5 Maps",
        "background_url": "https://i.imgur.com/1gY2pA4.png",
        "variable_value_name": "5 maps",
    },
    "nocustom": {
        "label": "5 Maps No Custom Server",
        "background_url": "https://i.imgur.com/xfFhLxa.png",
        "variable_value_name": "5 maps (no custom server)",
    },
    # --- 個別マップ (Easy) ---
    "abstract_easy": {
        "label": "Abstract (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_abstract.jpg",
        "variable_value_name": "Abstract (Easy)"
    },
    "apartments_easy": {
        "label": "Apartments (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_apartments.jpg",
        "variable_value_name": "Apartments (Easy)"
    },
    "beanstalk_easy": {
        "label": "Beanstalk (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_beanstalk.jpg",
        "variable_value_name": "Beanstalk (Easy)"
    },
    "beehive_easy": {
        "label": "Beehive (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_beehive.jpg",
        "variable_value_name": "Beehive (Easy)"
    },
    "concrete_easy": {
        "label": "Concrete (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_concrete.jpg",
        "variable_value_name": "Concrete (Easy)"
    },
    "cyberpunk_easy": {
        "label": "Cyberpunk (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_cyberpunk.jpg",
        "variable_value_name": "Cyberpunk (Easy)"
    },
    "data_easy": {
        "label": "Data (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_beehive.jpg",
        "variable_value_name": "Data (Easy)"
    },
    "depths_easy": {
        "label": "Depths (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_depth.jpg",
        "variable_value_name": "Depths (Easy)"
    },
    "glitched_easy": {
        "label": "Glitched (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_glitched.jpg",
        "variable_value_name": "Glitched (Easy)"
    },
    "groovy_easy": {
        "label": "Groovy (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_groovy.jpg",
        "variable_value_name": "Groovy (Easy)"
    },
    "jungle_easy": {
        "label": "Jungle (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_jungle.jpg",
        "variable_value_name": "Jungle (Easy)"
    },
    "lava_easy": {
        "label": "Lava (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_lava.jpg",
        "variable_value_name": "Lava (Easy)"
    },
    "pixels_easy": {
        "label": "Pixels (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_pixels.jpg",
        "variable_value_name": "Pixels (Easy)"
    },
    "shapes_easy": {
        "label": "Shapes (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_shapes.jpg",
        "variable_value_name": "Shapes (Easy)"
    },
    "shelves_easy": {
        "label": "Shelves (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_shelves.jpg",
        "variable_value_name": "Shelves (Easy)"
    },
    "shrine_easy": {
        "label": "Shrine (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_shrine.jpg",
        "variable_value_name": "Shrine (Easy)"
    },
    "stairs_easy": {
        "label": "Stairs (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_stairs.jpg",
        "variable_value_name": "Stairs (Easy)"
    },
    "toxic_easy": {
        "label": "Toxic (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_toxic.jpg",
        "variable_value_name": "Toxic (Easy)"
    },
    "waterways_easy": {
        "label": "Waterways (Easy)",
        "background_url": "https://cdn.playhive.com/maps/grav_waterways.jpg",
        "variable_value_name": "Waterways (Easy)"
    },
    "clockwork_medium": {
        "label": "Clockwork (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_clockwork.jpg",
        "variable_value_name": "Clockwork (Medium)"
    },
    "construction_medium": {
        "label": "Construction (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_construction.jpg",
        "variable_value_name": "Construction (Medium)"
    },
    "daisies_medium": {
        "label": "Daisies (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_daisies.jpg",
        "variable_value_name": "Daisies (Medium)"
    },
    "deepscape_medium": {
        "label": "Deepscape (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_deepscape.jpg",
        "variable_value_name": "Deepscape (Medium)"
    },
    "dimensions_medium": {
        "label": "Dimensions (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_dimensions.jpg",
        "variable_value_name": "Dimensions (Medium)"
    },
    "dungeon_medium": {
        "label": "Dungeon (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_dungeon.jpg",
        "variable_value_name": "Dungeon (Medium)"
    },
    "labrinth_medium": {
        "label": "Labrinth (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_labyrinth.jpg",
        "variable_value_name": "Labrinth (Medium)"
    },
    "lilypads_medium": {
        "label": "Lilypads (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_lilypads.jpg",
        "variable_value_name": "Lilypads (Medium)"
    },
    "new_orleans_medium": {
        "label": "New Orleans (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_neworleans.jpg",
        "variable_value_name": "New Orleans (Medium)"
    },
    "post_office_medium": {
        "label": "Post office (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_postoffice.jpg",
        "variable_value_name": "Post office (Medium)"
    },
    "roadtrip_medium": {
        "label": "Roadtrip (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_roadtrip.jpg",
        "variable_value_name": "Roadtrip (Medium)"
    },
    "stained_glass_medium": {
        "label": "Stained Glass (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_stainedglass.jpg",
        "variable_value_name": "Stained Glass (Medium)"
    },
    "tomes_medium": {
        "label": "Tomes (Medium)",
        "background_url": "https://cdn.playhive.com/maps/grav_tomes.jpg",
        "variable_value_name": "Tomes (Medium)"
    },
    "burrow_hard": {
        "label": "Burrow (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_burrow.jpg",
        "variable_value_name": "Burrow (Hard)"
    },
    "circuit_board_hard": {
        "label": "Circuit Board (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_circuitboard.jpg",
        "variable_value_name": "Circuit Board (Hard)"
    },
    "geometric_hard": {
        "label": "Geometric (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_geometric.jpg",
        "variable_value_name": "Geometric (Hard)"
    },
    "shanty_town_hard": {
        "label": "Shanty Town (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_shantytown.jpg",
        "variable_value_name": "Shanty Town (Hard)"
    },
    "space_hard": {
        "label": "Space (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_space.jpg",
        "variable_value_name": "Space (Hard)"
    },
    "triangles_hard": {
        "label": "Triangles (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_triangles.jpg",
        "variable_value_name": "Triangles (Hard)"
    },
    "twisted_hard": {
        "label": "Twisted (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_twisted.jpg",
        "variable_value_name": "Twisted (Hard)"
    },
    "under_the_sea_hard": {
        "label": "Under The Sea (Hard)",
        "background_url": "https://cdn.playhive.com/maps/grav_underthesea.jpg",
        "variable_value_name": "Under The Sea (Hard)"
    }
}

GAME_NAME = "The Hive"
GAME_ID = "hive"
CATEGORY_NAME = "Gravity"

_jp_whitelist_raw = os.environ.get(
    "JP_WHITELIST",
    "tanukiYy,AmonHive,AlmondCellar,Suriipu,StoodBird84586,MintGamesYT,maikuragenzin,spring861,TouTubeTomaTV,iroha0515",
)
JP_WHITELIST = {
    name.strip().lower() for name in _jp_whitelist_raw.split(",") if name.strip()
}
JP_COUNTRY_CODE = "JP"

CACHE_DIR = os.environ.get("CACHE_DIR", os.path.join(BASE_DIR, "cache"))
CACHE_TTL_MINUTES = 60

FONT_DIR = os.environ.get("FONT_DIR", os.path.join(BASE_DIR, "fonts"))
FONT_MOJANGLES = os.path.join(FONT_DIR, "Mojangles.ttf")
FONT_UNIFONT = os.path.join(FONT_DIR, "Unifont.ttf")

IMAGE_WIDTH = 1010
ROW_HEIGHT = 68
HEADER_HEIGHT = 170
FOOTER_HEIGHT = 30
PADDING = 14
ROWS_PER_PAGE = 10
MAX_ROWS_WORLD_DISPLAY = 40
MAX_ROWS_JP_DISPLAY = 20

LOGO_URL = os.environ.get(
    "LOGO_URL", "https://playhive.com/_next/static/media/Hive.9ce7fa58.png"
)
LOGO_HEIGHT = 34
BACKGROUND_BLUR_RADIUS = 4
BACKGROUND_DARKEN_ALPHA = 130

COLORS = {
    "panel_bg": (14, 18, 28, 235),
    "panel_border": (40, 46, 58, 255),
    "row_bg_a": (30, 38, 52, 200),
    "row_bg_b": (22, 28, 40, 200),
    "header_tab_bg": (18, 22, 32, 255),
    "header_tab_border": (60, 66, 80, 255),
    "title_cyan": (85, 210, 235, 255),
    "title_green": (85, 220, 100, 255),
    "col_header_pos": (240, 140, 130, 255),
    "col_header_white": (255, 255, 255, 255),
    "col_header_green": (95, 220, 105, 255),
    "col_header_red": (225, 90, 90, 255),
    "text_white": (240, 240, 240, 255),
    "rank_gold": (255, 215, 60, 255),
    "rank_silver": (200, 205, 210, 255),
    "rank_bronze": (190, 120, 70, 255),
    "rank_other": (235, 140, 140, 255),
    "player_name": (230, 230, 235, 255),
    "time_lightgreen": (150, 230, 90, 255),
    "date_darkgreen": (60, 140, 75, 255),
    "platform_red": (215, 80, 80, 255),
    "shadow": (0, 0, 0, 160),
}

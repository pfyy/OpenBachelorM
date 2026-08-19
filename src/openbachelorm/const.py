from enum import StrEnum

TMP_DIRPATH = "tmp/"

ASSET_DIRPATH = "asset/"

MOD_DIRPATH = "mod/"


class KnownTable(StrEnum):
    ACTIVITY_TABLE = "activity_table"
    AUDIO_DATA = "audio_data"
    BATTLE_EQUIP_TABLE = "battle_equip_table"
    BUFF_TABLE = "buff_table"
    BUILDING_DATA = "building_data"
    BUILDING_LOCAL_DATA = "building_local_data"
    CAMPAIGN_TABLE = "campaign_table"
    CHAPTER_TABLE = "chapter_table"
    CHARACTER_TABLE = "character_table"
    CHARM_TABLE = "charm_table"
    CHARWORD_TABLE = "charword_table"
    CHAR_MASTER_TABLE = "char_master_table"
    CHAR_META_TABLE = "char_meta_table"
    CHAR_PATCH_TABLE = "char_patch_table"
    CHECKIN_TABLE = "checkin_table"
    CLIMB_TOWER_TABLE = "climb_tower_table"
    CLUE_DATA = "clue_data"
    COOPERATE_BATTLE_TABLE = "cooperate_battle_table"
    CRISIS_TABLE = "crisis_table"
    CRISIS_V2_TABLE = "crisis_v2_table"
    DISPLAY_META_TABLE = "display_meta_table"
    ENEMY_DATABASE = "enemy_database"
    ENEMY_HANDBOOK_TABLE = "enemy_handbook_table"
    EP_BREAKBUFF_TABLE = "ep_breakbuff_table"
    EXTRA_BATTLELOG_TABLE = "extra_battlelog_table"
    FAVOR_TABLE = "favor_table"
    GACHA_TABLE = "gacha_table"
    GAMEDATA_CONST = "gamedata_const"
    HANDBOOK_INFO_TABLE = "handbook_info_table"
    HANDBOOK_TEAM_TABLE = "handbook_team_table"
    HOTUPDATE_META_TABLE = "hotupdate_meta_table"
    INIT_TEXT = "init_text"
    ITEM_TABLE = "item_table"
    LEGION_MODE_BUFF_TABLE = "legion_mode_buff_table"
    LEVEL_SCRIPT_TABLE = "level_script_table"
    MAIN_TEXT = "main_text"
    MEDAL_TABLE = "medal_table"
    META_UI_TABLE = "meta_ui_table"
    MISSION_TABLE = "mission_table"
    OPEN_SERVER_TABLE = "open_server_table"
    REPLICATE_TABLE = "replicate_table"
    RETRO_TABLE = "retro_table"
    ROGUELIKE_TOPIC_TABLE = "roguelike_topic_table"
    SANDBOX_PERM_TABLE = "sandbox_perm_table"
    SHOP_CLIENT_TABLE = "shop_client_table"
    SKILL_TABLE = "skill_table"
    SKIN_TABLE = "skin_table"
    SPECIAL_OPERATOR_TABLE = "special_operator_table"
    STAGE_TABLE = "stage_table"
    STORY_REVIEW_META_TABLE = "story_review_meta_table"
    STORY_REVIEW_TABLE = "story_review_table"
    STORY_TABLE = "story_table"
    TIP_TABLE = "tip_table"
    TOKEN_TABLE = "token_table"
    UNIEQUIP_TABLE = "uniequip_table"
    ZONE_TABLE = "zone_table"
    ARKVENT_TABLE = "arkvent_table"

    HANDBOOK_TABLE = "handbook_table"
    PLAYER_AVATAR_TABLE = "player_avatar_table"
    RANGE_TABLE = "range_table"
    ROGUELIKE_TABLE = "roguelike_table"
    SANDBOX_TABLE = "sandbox_table"
    TECH_BUFF_TABLE = "tech_buff_table"
    UNIEQUIP_DATA = "uniequip_data"

    BATTLE_MISC_TABLE = "battle_misc_table"

    BUFF_TEMPLATE_DATA = "buff_template_data"

    DATA_VERSION = "data_version"


def get_last_res_version_android(client_version: str) -> str:
    match client_version:
        case "2.7.61":
            return "26-08-17-11-25-42_dbc172"
        case "2.7.51":
            return "26-07-20-09-52-12_5d4a43"
        case "2.7.41":
            return "26-07-01-15-26-52_d3376d"
        case "2.7.31":
            return "26-05-20-12-59-09_e8f456"
        case "2.7.21":
            return "26-04-22-10-22-20_1d417a"
        case "2.7.11":
            return "26-03-31-05-42-28_7d7f67"
        case "2.7.01":
            return "26-02-28-10-42-20_2bc282"
        case "2.6.91":
            return "26-02-02-04-52-41_58bd30"
        case "2.6.82":
            return "25-12-30-07-42-27_86bc9a"
        case "2.6.71":
            return "25-11-21-15-21-44_ee1197"
        case "2.6.61":
            return "25-10-23-13-35-37_3d4b91"
        case "2.6.41":
            return "25-09-28-12-13-16_6485b3"
        case "2.6.21":
            return "25-08-25-23-45-59_81c7ff"
        case "2.6.01":
            return "25-07-19-05-16-54_1e71a6"
        case "2.5.80":
            return "25-06-26-04-47-55_47709b"
        case "2.5.60":
            return "25-05-20-12-36-22_4803e1"
        case "2.5.04":
            return "25-04-25-08-42-16_acb2f8"
        case "2.4.61":
            return "25-03-27-16-19-10-4d4819"
        case "2.4.41":
            return "25-02-19-09-21-28-ba1f4e"
        case "2.4.21":
            return "25-01-08-07-44-44-3d8742"
        case "2.4.01":
            return "24-11-21-11-04-45-bae23b"
        case "2.3.81":
            return "24-10-24-14-30-30-b63a02"
        case "2.3.61":
            return "24-09-23-11-27-19-c6564b"
        case "2.3.21":
            return "24-08-26-16-10-17-fd946e"
        case "2.3.01":
            return "24-07-23-15-16-02-a53606"
        case "2.2.81":
            return "24-06-21-09-33-59-503529"
        case "2.2.61":
            return "24-05-22-06-44-01-4a3244"
        case "2.2.41":
            return "24-04-26-09-22-08-413e02"
        case "2.2.21":
            return "24-03-29-14-33-44-5002d2"
        case "2.2.01":
            return "24-02-26-08-28-19-0f351f"
        case "2.1.41":
            return "24-01-12-07-52-32-80033a"
        case "2.1.21":
            return "23-11-17-08-48-31-26d599"
        case "2.1.01":
            return "23-10-18-08-57-00-a2b96e"
        case "2.0.81":
            return "23-09-20-13-28-42-486799"
        case "2.0.61":
            return "23-08-25-11-36-41-12f55f"
        case "2.0.40":
            return "23-07-24-13-21-30-90fb63"
        case "2.0.11":
            return "23-06-25-13-09-13-327c56"
        case "2.0.01":
            return "23-05-25-08-29-42-5bba8f"
        case "1.9.91":
            return "23-04-23-15-07-53-24a81c"
        case "1.9.81":
            return "23-03-27-11-50-38-b42880"
        case "1.9.62":
            return "23-02-22-22-37-04-ef2150"
        case "1.9.42":
            return "23-01-11-12-54-27-873b47"
        case "1.9.21":
            return "22-11-29-10-38-08-99d7db"
        case "1.9.01":
            return "22-10-21-22-14-51-ba22f3"
        case "1.8.81":
            return "22-09-19-15-00-59-ae77d7"
        case "1.8.61":
            return "22-08-29-13-56-31-95a9a4"
        case _:
            raise ValueError(f"unknown client_version {client_version}")


def get_last_res_version_windows(client_version: str) -> str:
    match client_version:
        case "2.7.61":
            return "26-08-17-11-22-14_59d37d"
        case "2.7.51":
            return "26-07-20-09-52-01_970b78"
        case "2.7.41":
            return "26-07-01-15-25-07_7886d5"
        case "2.7.31":
            return "26-05-20-14-05-50_24a03e"
        case "2.7.21":
            return "26-04-22-09-33-12_01a3a2"
        case "2.7.11":
            return "26-03-31-05-51-38_1cc8a5"
        case "2.7.01":
            return "26-02-28-11-16-12_689e5e"
        case "2.6.91":
            return "26-02-02-05-12-37_d6d557"
        case _:
            raise ValueError(f"unknown client_version {client_version}")


def get_last_res_version(client_version: str, platform_name: str = "Android") -> str:
    match platform_name:
        case "Android":
            return get_last_res_version_android(client_version)

        case "Windows":
            return get_last_res_version_windows(client_version)

        case _:
            raise ValueError(f"unknown platform_name {platform_name}")

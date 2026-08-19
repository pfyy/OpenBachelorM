import UnityPy

from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger
from openbachelorm.const import get_last_res_version_windows
from openbachelorm.helper import (
    get_known_table_decorator_lst,
    get_mod_level_decorator_lst,
    get_known_table_asset_name_prefix,
)
from openbachelorm.const import KnownTable


def do_mod_character_table(character_table):
    for char in character_table["characters"]:
        if char["key"] == "trap_296_iznsbr":
            char["value"]["talents"][0]["candidates"][0]["blackboard"][0][
                "valueStr"
            ] = "enemy_2126_dycyue"
    return character_table


def do_mod_level(level):
    level["enemyDbRefs"].append(
        {
            "useDb": True,
            "id": "enemy_2126_dycyue",
        }
    )
    level["enemyDbRefs"].append(
        {
            "useDb": True,
            "id": "enemy_2130_dyswrd",
        }
    )

    found = False
    for card in level["predefines"]["tokenCards"]:
        if card["inst"]["characterKey"] == "trap_296_iznsbr":
            found = True
            card["initialCnt"] = 99
            break

    if not found:
        level["predefines"]["tokenCards"].append(
            {
                "initialCnt": 99,
                "inst": {"characterKey": "trap_296_iznsbr", "level": 1},
                "skillIndex": -1,
                "mainSkillLvl": 1,
                "skinId": "",
            },
        )

    level["predefines"]["tokenCards"].append(
        {
            "initialCnt": 0,
            "inst": {"characterKey": "trap_790_dytswd", "level": 1},
            "skillIndex": -1,
            "mainSkillLvl": 1,
            "skinId": "",
        }
    )

    level["bgmEvent"] = "rl5boss5"

    return level


def main():
    res = Resource("2.7.61", get_last_res_version_windows("2.7.61"), "Windows")

    mgr = ManifestMerger(
        "april_shuo",
        res,
        [
            Resource("2.7.21", get_last_res_version_windows("2.7.21"), "Windows"),
        ],
        "Windows",
    )

    mgr.merge_src_res()

    mgr.merge_special_anon_bundle()

    mgr.merge_act_asset_map()

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    # ----------

    res.mod_table(
        KnownTable.CHARACTER_TABLE.value,
        do_mod_character_table,
        get_known_table_decorator_lst(
            KnownTable.CHARACTER_TABLE, res.client_version, res.res_version
        ),
        table_asset_name_prefix=get_known_table_asset_name_prefix(
            KnownTable.CHARACTER_TABLE
        ),
    )

    ab_filename = mgr.get_merger_bundle_filepath(
        "anon/3848542ff281bdbee51286c81ce549d2.bin"
    )
    asset_env = UnityPy.load(ab_filename.as_posix())
    for i in range(1, 7):
        level_id = f"level_act7fun_0{i}"
        res.mod_level_ab(
            asset_env,
            level_id,
            do_mod_level,
            get_mod_level_decorator_lst(level_id, res.client_version, res.res_version),
        )
    ab_filename.write_bytes(asset_env.file.save())

    # ----------

    mgr.build_mod()


if __name__ == "__main__":
    main()

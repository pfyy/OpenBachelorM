from openbachelorm.resource import Resource
from openbachelorm.helper import (
    get_known_table_decorator_lst,
    get_mod_level_decorator_lst,
    get_known_table_asset_name_prefix,
)
from openbachelorm.const import KnownTable

IMMUNE_FLAG = True

IMMUNE_LST = [
    "stunImmune",
    "silenceImmune",
    "sleepImmune",
    "frozenImmune",
    "levitateImmune",
    "disarmedCombatImmune",
    "fearedImmune",
    "palsyImmune",
    "attractImmune",
]

ATK_FLAG = True

DEF_FLAG = True


def do_mod_enemy_database(enemy_database):
    for enemy_obj in enemy_database["enemies"]:
        for enemy_value in enemy_obj["Value"]:
            enemy_data = enemy_value["enemyData"]

            enemy_data["lifePointReduce"] = {"m_defined": True, "m_value": 0}

            enemy_attr = enemy_data["attributes"]

            if IMMUNE_FLAG:
                for k in IMMUNE_LST:
                    enemy_attr[k] = {"m_defined": True, "m_value": True}

                enemy_attr["massLevel"] = {"m_defined": True, "m_value": 100}

            if ATK_FLAG:
                if enemy_attr.get("atk"):
                    if enemy_attr["atk"].get("m_defined"):
                        old_atk = enemy_attr["atk"].get("m_value", 0)

                        enemy_attr["atk"] = {
                            "m_defined": True,
                            "m_value": 10000 + 1000 * old_atk,
                        }

            if DEF_FLAG:
                if enemy_attr.get("def"):
                    if enemy_attr["def"].get("m_defined"):
                        old_def = enemy_attr["def"].get("m_value", 0)

                        enemy_attr["def"] = {
                            "m_defined": True,
                            "m_value": 10000 + 1000 * old_def,
                        }

                for k in ["magicResistance", "epDamageResistance", "epResistance"]:
                    enemy_attr[k] = {"m_defined": True, "m_value": 1000}

    return enemy_database


def build_sample_mod(client_version: str, res_version: str):
    res = Resource(client_version, res_version)

    res.mod_table(
        KnownTable.ENEMY_DATABASE.value,
        do_mod_enemy_database,
        get_known_table_decorator_lst(
            KnownTable.ENEMY_DATABASE, client_version, res_version
        ),
        table_asset_name_prefix=get_known_table_asset_name_prefix(
            KnownTable.ENEMY_DATABASE
        ),
    )

    res.build_mod("ak_2077")


def main():
    build_sample_mod("2.6.91", "26-02-02-04-52-41_58bd30")


if __name__ == "__main__":
    main()

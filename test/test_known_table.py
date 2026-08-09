from openbachelorm.resource import Resource
from openbachelorm.helper import (
    nop_mod_table_func,
    get_known_table_decorator_lst,
    is_known_table_available,
    get_known_table_asset_name_prefix,
)
from openbachelorm.const import KnownTable
from openbachelorm.const import (
    get_last_res_version_android,
    get_last_res_version_windows,
)


def load_known_table(
    client_version: str, res_version: str, platform_name: str = "Android"
):
    res = Resource(client_version, res_version, platform_name)

    for known_table in KnownTable:
        if not is_known_table_available(known_table, client_version):
            continue
        res.mod_table(
            known_table.value,
            nop_mod_table_func,
            get_known_table_decorator_lst(known_table, client_version, res_version),
            table_asset_name_prefix=get_known_table_asset_name_prefix(known_table),
        )


def test_known_table():
    load_known_table("2.4.01", get_last_res_version_android("2.4.01"))
    load_known_table("2.4.21", get_last_res_version_android("2.4.21"))
    load_known_table("2.4.41", get_last_res_version_android("2.4.41"))
    load_known_table("2.4.61", get_last_res_version_android("2.4.61"))
    load_known_table("2.5.04", get_last_res_version_android("2.5.04"))
    load_known_table("2.5.60", get_last_res_version_android("2.5.60"))
    load_known_table("2.5.80", get_last_res_version_android("2.5.80"))
    load_known_table("2.6.01", get_last_res_version_android("2.6.01"))
    load_known_table("2.6.21", get_last_res_version_android("2.6.21"))
    load_known_table("2.6.41", get_last_res_version_android("2.6.41"))
    load_known_table("2.6.61", get_last_res_version_android("2.6.61"))
    load_known_table("2.6.71", get_last_res_version_android("2.6.71"))
    load_known_table("2.6.82", get_last_res_version_android("2.6.82"))
    load_known_table("2.6.91", get_last_res_version_android("2.6.91"))
    load_known_table("2.7.01", get_last_res_version_android("2.7.01"))
    load_known_table("2.7.11", get_last_res_version_android("2.7.11"))
    load_known_table("2.7.21", get_last_res_version_android("2.7.21"))
    load_known_table("2.7.31", get_last_res_version_android("2.7.31"))
    load_known_table("2.7.41", get_last_res_version_android("2.7.41"))
    load_known_table("2.7.51", get_last_res_version_android("2.7.51"))
    load_known_table("2.7.61", get_last_res_version_android("2.7.61"))


def test_known_table_windows():
    load_known_table("2.6.91", get_last_res_version_windows("2.6.91"), "Windows")
    load_known_table("2.7.01", get_last_res_version_windows("2.7.01"), "Windows")
    load_known_table("2.7.11", get_last_res_version_windows("2.7.11"), "Windows")
    load_known_table("2.7.21", get_last_res_version_windows("2.7.21"), "Windows")
    load_known_table("2.7.31", get_last_res_version_windows("2.7.31"), "Windows")
    load_known_table("2.7.41", get_last_res_version_windows("2.7.41"), "Windows")
    load_known_table("2.7.51", get_last_res_version_windows("2.7.51"), "Windows")
    load_known_table("2.7.61", get_last_res_version_windows("2.7.61"), "Windows")

from functools import wraps
from packaging.version import Version
import json

import flatbuffers
import bson

from .fbs_codegen.v2_6_91 import (
    prts___levels_generated as prts___levels_v2_6_91,
)
from .fbs_codegen.v2_6_82 import (
    prts___levels_generated as prts___levels_v2_6_82,
)
from .fbs_codegen.v2_6_71 import (
    prts___levels_generated as prts___levels_v2_6_71,
)
from .fbs_codegen.v2_6_61 import (
    prts___levels_generated as prts___levels_v2_6_61,
)
from .fbs_codegen.v2_6_41 import (
    prts___levels_generated as prts___levels_v2_6_41,
)
from .fbs_codegen.v2_6_21 import (
    prts___levels_generated as prts___levels_v2_6_21,
)
from .fbs_codegen.v2_6_01 import (
    prts___levels_generated as prts___levels_v2_6_01,
)
from .fbs_codegen.v2_5_80 import (
    prts___levels_generated as prts___levels_v2_5_80,
)
from .fbs_codegen.v2_5_60 import (
    prts___levels_generated as prts___levels_v2_5_60,
)
from .fbs_codegen.v2_5_04 import (
    prts___levels_generated as prts___levels_v2_5_04,
)
from .fbs_codegen.v2_4_61 import (
    prts___levels_generated as prts___levels_v2_4_61,
)


from .helper import (
    script_decorator,
    header_decorator,
    json_decorator,
    dump_table_decorator,
    encode_flatc,
    decode_flatc,
    nop_mod_table_func,
    get_mod_level_decorator_lst,
    apply_decorator_lst,
    script_to_bytes,
    bytes_to_script,
    remove_header,
    add_header,
    dump_table,
    decrypt_data,
)


def get_prts___levels(client_version: str):
    match client_version:
        case "2.6.91":
            return prts___levels_v2_6_91

        case "2.6.82":
            return prts___levels_v2_6_82

        case "2.6.71":
            return prts___levels_v2_6_71

        case "2.6.61":
            return prts___levels_v2_6_61

        case "2.6.41":
            return prts___levels_v2_6_41

        case "2.6.21":
            return prts___levels_v2_6_21

        case "2.6.01":
            return prts___levels_v2_6_01

        case "2.5.80":
            return prts___levels_v2_5_80

        case "2.5.60":
            return prts___levels_v2_5_60

        case "2.5.04":
            return prts___levels_v2_5_04

        case "2.4.61":
            return prts___levels_v2_4_61

        case _:
            raise ValueError(f"fbs codegen not found for {client_version}")


def migrate_flatc_decorator(
    src_client_version: str, dst_client_version: str, fbs_name: str
):
    def _migrate_flatc_decorator(func):
        @wraps(func)
        def wrapper(data):
            return encode_flatc(
                func(
                    decode_flatc(
                        data,
                        src_client_version,
                        fbs_name,
                    )
                ),
                dst_client_version,
                fbs_name,
            )

        return wrapper

    return _migrate_flatc_decorator


def get_migrate_level_decorator_lst(
    level_id: str, src_client_version: str, dst_client_version: str, res_version: str
):
    return [
        script_decorator,
        header_decorator,
        migrate_flatc_decorator(
            src_client_version, dst_client_version, "prts___levels"
        ),
        json_decorator,
        dump_table_decorator(f"{level_id}_{res_version}_migrate"),
    ]


def get_codegen_migrate_level_decorator_lst():
    return [
        script_decorator,
        header_decorator,
    ]


def handle_obj_in_level(obj, prts___levels):
    if isinstance(obj, prts___levels.clz_Torappu_EnemyDatabase_AttributesDataT):
        if hasattr(obj, "palsyImmune") and obj.palsyImmune is None:
            obj.palsyImmune = prts___levels.clz_Torappu_Undefinable_1_System_Boolean_T()

        if hasattr(obj, "attractImmune") and obj.attractImmune is None:
            obj.attractImmune = (
                prts___levels.clz_Torappu_Undefinable_1_System_Boolean_T()
            )

        if hasattr(obj, "epBreakRecoverSpeed") and obj.epBreakRecoverSpeed is None:
            obj.epBreakRecoverSpeed = (
                prts___levels.clz_Torappu_Undefinable_1_System_Single_T()
            )

        if hasattr(obj, "disarmedCombatImmune") and obj.disarmedCombatImmune is None:
            obj.disarmedCombatImmune = (
                prts___levels.clz_Torappu_Undefinable_1_System_Boolean_T()
            )

        if hasattr(obj, "fearedImmune") and obj.fearedImmune is None:
            obj.fearedImmune = (
                prts___levels.clz_Torappu_Undefinable_1_System_Boolean_T()
            )

        if hasattr(obj, "damageHitratePhysical") and obj.damageHitratePhysical is None:
            obj.damageHitratePhysical = (
                prts___levels.clz_Torappu_Undefinable_1_System_Single_T()
            )

        if hasattr(obj, "damageHitrateMagical") and obj.damageHitrateMagical is None:
            obj.damageHitrateMagical = (
                prts___levels.clz_Torappu_Undefinable_1_System_Single_T()
            )

        if hasattr(obj, "epDamageResistance") and obj.epDamageResistance is None:
            obj.epDamageResistance = (
                prts___levels.clz_Torappu_Undefinable_1_System_Single_T()
            )

        if hasattr(obj, "epResistance") and obj.epResistance is None:
            obj.epResistance = prts___levels.clz_Torappu_Undefinable_1_System_Single_T()

        return

    if isinstance(obj, prts___levels.clz_Torappu_EnemyDatabase_EnemyDataT):
        if hasattr(obj, "applyWay") and obj.applyWay is None:
            obj.applyWay = (
                prts___levels.clz_Torappu_Undefinable_1_Torappu_SourceApplyWay_T()
            )

        if hasattr(obj, "motion") and obj.motion is None:
            obj.motion = prts___levels.clz_Torappu_Undefinable_1_Torappu_MotionMode_T()

        if hasattr(obj, "enemyTags") and obj.enemyTags is None:
            obj.enemyTags = prts___levels.clz_Torappu_Undefinable_1_System_String___T()

        if hasattr(obj, "notCountInTotal") and obj.notCountInTotal is None:
            obj.notCountInTotal = (
                prts___levels.clz_Torappu_Undefinable_1_System_Boolean_T()
            )

        if hasattr(obj, "viewRadius") and obj.viewRadius is None:
            obj.viewRadius = prts___levels.clz_Torappu_Undefinable_1_System_Single_T()

        return


def recursive_handle_obj_in_level(obj, prts___levels):
    handle_obj_in_level(obj, prts___levels)

    if isinstance(obj, list):
        for i in obj:
            recursive_handle_obj_in_level(
                i,
                prts___levels,
            )
        return

    if not hasattr(obj, "__dict__"):
        return

    for i in obj.__dict__.values():
        recursive_handle_obj_in_level(
            i,
            prts___levels,
        )


def get_codegen_migrate_func(
    dst_client_version: str,
):
    def _codegen_migrate_func(level_bytes: bytes) -> bytes:
        prts___levels = get_prts___levels(dst_client_version)

        level_obj = prts___levels.clz_Torappu_LevelDataT.InitFromPackedBuf(level_bytes)

        recursive_handle_obj_in_level(level_obj, prts___levels)

        builder = flatbuffers.Builder()
        builder.Finish(level_obj.Pack(builder))
        level_bytes = bytes(builder.Output())

        return level_bytes

    return _codegen_migrate_func


def convert_legacy_json_level_mapData(level):
    if "mapData" not in level:
        return

    level["mapData"].pop("width", None)
    level["mapData"].pop("height", None)

    if "map" not in level["mapData"]:
        return

    old_map = level["mapData"]["map"]
    new_map = {}

    row_size = len(old_map)
    column_size = len(old_map[0])
    matrix_data = sum(old_map, [])

    new_map = {
        "row_size": row_size,
        "column_size": column_size,
        "matrix_data": matrix_data,
    }

    level["mapData"]["map"] = new_map


def convert_legacy_json_level_waves(level):
    if "waves" not in level:
        return

    for wave_obj in level["waves"]:
        wave_obj.pop("name", None)

        for fragment_obj in wave_obj.get("fragments", []):
            fragment_obj.pop("name", None)


def convert_legacy_json_level_routes(level):
    if "routes" not in level:
        return

    for i in range(len(level["routes"])):
        if level["routes"][i] is None:
            level["routes"][i] = {}


def convert_legacy_json_level_extraRoutes(level):
    if "extraRoutes" not in level:
        return

    for i in range(len(level["extraRoutes"])):
        if level["extraRoutes"][i] is None:
            level["extraRoutes"][i] = {}


def convert_legacy_json_level_branches(level):
    if level.get("branches", None) is None:
        return

    old_branches = level["branches"]
    new_branches = []

    for k, v in old_branches.items():
        new_branches.append(
            {
                "key": k,
                "value": v,
            }
        )

    level["branches"] = new_branches


def convert_legacy_json_bossrush_level(level):
    for wave in level.get("waves", []):
        for fragment in wave.get("fragments", []):
            actions = fragment.get("actions", [])

            del_idx_lst: list[int] = []

            for i, action in enumerate(actions):
                k: str = action.get("key", "")

                if (
                    k.startswith("trap_091_brctrl#")
                    and (":" in k and not k.endswith(":empty"))
                ) or (k.startswith("trap_090_recodr#") and (":" in k)):
                    del_idx_lst.append(i)

            if not del_idx_lst:
                continue

            for i in reversed(del_idx_lst):
                actions.pop(i)


def convert_legacy_json_level(level_id: str, level):
    convert_legacy_json_level_mapData(level)
    convert_legacy_json_level_waves(level)
    convert_legacy_json_level_routes(level)
    convert_legacy_json_level_extraRoutes(level)
    convert_legacy_json_level_branches(level)

    if level_id.startswith("level_bossrush"):
        convert_legacy_json_bossrush_level(level)


def migrate_legacy_json_level(
    level_str: str,
    level_id: str,
    src_client_version: str,
    dst_client_version: str,
    res_version: str,
) -> str:
    try:
        level = bson.decode(remove_header(script_to_bytes(level_str)))
    except Exception:
        level = json.loads(decrypt_data(script_to_bytes(level_str)).decode("utf-8"))

    dump_table(level, f"{level_id}_{res_version}_migrate_json_pre.json")

    convert_legacy_json_level(level_id, level)

    dump_table(level, f"{level_id}_{res_version}_migrate_json_post.json")

    level_str = bytes_to_script(
        add_header(
            encode_flatc(
                json.dumps(level, ensure_ascii=False, indent=4),
                dst_client_version,
                "prts___levels",
            )
        )
    )

    return level_str


def migrate_level(
    level_id: str,
    src_client_version: str,
    dst_client_version: str,
    res_version: str,
    level_str: str,
) -> str:
    if Version(src_client_version) < Version("2.0.40"):
        is_legacy_json_level = True
    else:
        is_legacy_json_level = False

    if is_legacy_json_level:
        level_str = migrate_legacy_json_level(
            level_str, level_id, src_client_version, dst_client_version, res_version
        )
    else:
        migrate_level_decorator_lst = get_migrate_level_decorator_lst(
            level_id, src_client_version, dst_client_version, res_version
        )

        migrate_func = nop_mod_table_func

        migrate_func = apply_decorator_lst(migrate_func, migrate_level_decorator_lst)

        level_str = migrate_func(level_str)

    # ----------

    codegen_migrate_level_decorator_lst = get_codegen_migrate_level_decorator_lst()

    codegen_migrate_func = get_codegen_migrate_func(dst_client_version)

    codegen_migrate_func = apply_decorator_lst(
        codegen_migrate_func, codegen_migrate_level_decorator_lst
    )

    level_str = codegen_migrate_func(level_str)

    # ----------

    log_decorator_lst = get_mod_level_decorator_lst(
        level_id, dst_client_version, res_version
    )

    log_func = nop_mod_table_func

    log_func = apply_decorator_lst(log_func, log_decorator_lst)

    level_str = log_func(level_str)

    return level_str

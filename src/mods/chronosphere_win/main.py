from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger
from openbachelorm.const import get_last_res_version_windows


def main():
    mgr = ManifestMerger(
        "chronosphere_win",
        Resource("2.7.61", get_last_res_version_windows("2.7.61"), "Windows"),
        [
            Resource("2.7.51", get_last_res_version_windows("2.7.51"), "Windows"),
            Resource("2.7.41", get_last_res_version_windows("2.7.41"), "Windows"),
            Resource("2.7.31", get_last_res_version_windows("2.7.31"), "Windows"),
            Resource("2.7.21", get_last_res_version_windows("2.7.21"), "Windows"),
            Resource("2.7.11", get_last_res_version_windows("2.7.11"), "Windows"),
            Resource("2.7.01", get_last_res_version_windows("2.7.01"), "Windows"),
            Resource("2.6.91", get_last_res_version_windows("2.6.91"), "Windows"),
        ],
        "Windows",
    )

    mgr.merge_src_res()

    mgr.merge_special_anon_bundle()

    mgr.merge_act_asset_map()

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    mgr.build_mod()


if __name__ == "__main__":
    main()

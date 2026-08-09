from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger
from openbachelorm.const import get_last_res_version_android


def main():
    mgr = ManifestMerger(
        "chronosphere",
        Resource("2.7.61", get_last_res_version_android("2.7.61")),
        [
            Resource("2.7.51", get_last_res_version_android("2.7.51")),
            Resource("2.7.41", get_last_res_version_android("2.7.41")),
            Resource("2.7.31", get_last_res_version_android("2.7.31")),
            Resource("2.7.21", get_last_res_version_android("2.7.21")),
            Resource("2.7.11", get_last_res_version_android("2.7.11")),
            Resource("2.7.01", get_last_res_version_android("2.7.01")),
            Resource("2.6.91", get_last_res_version_android("2.6.91")),
            Resource("2.6.82", get_last_res_version_android("2.6.82")),
            Resource("2.6.71", get_last_res_version_android("2.6.71")),
            Resource("2.6.61", get_last_res_version_android("2.6.61")),
            Resource("2.6.41", get_last_res_version_android("2.6.41")),
            Resource("2.6.21", get_last_res_version_android("2.6.21")),
            Resource("2.6.01", get_last_res_version_android("2.6.01")),
            Resource("2.5.80", get_last_res_version_android("2.5.80")),
            Resource("2.5.60", get_last_res_version_android("2.5.60")),
            Resource("2.5.04", get_last_res_version_android("2.5.04")),
        ],
    )

    mgr.merge_src_res()

    mgr.merge_special_anon_bundle()

    mgr.merge_act_asset_map()

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    mgr.build_mod()


if __name__ == "__main__":
    main()

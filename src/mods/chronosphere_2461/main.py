from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger
from openbachelorm.const import get_last_res_version_android


def main():
    mgr = ManifestMerger(
        "chronosphere_2461",
        Resource("2.4.61", get_last_res_version_android("2.4.61")),
        [
            Resource("2.4.41", get_last_res_version_android("2.4.41")),
            Resource("2.4.21", get_last_res_version_android("2.4.21")),
            Resource("2.4.01", get_last_res_version_android("2.4.01")),
            Resource("2.3.81", get_last_res_version_android("2.3.81")),
            Resource("2.3.61", get_last_res_version_android("2.3.61")),
            Resource("2.3.21", get_last_res_version_android("2.3.21")),
            Resource("2.3.01", get_last_res_version_android("2.3.01")),
            Resource("2.2.81", get_last_res_version_android("2.2.81")),
            Resource("2.2.61", get_last_res_version_android("2.2.61")),
            Resource("2.2.41", get_last_res_version_android("2.2.41")),
            Resource("2.2.21", get_last_res_version_android("2.2.21")),
            Resource("2.2.01", get_last_res_version_android("2.2.01")),
            Resource("2.1.41", get_last_res_version_android("2.1.41")),
            Resource("2.1.21", get_last_res_version_android("2.1.21")),
            Resource("2.1.01", get_last_res_version_android("2.1.01")),
            Resource("2.0.81", get_last_res_version_android("2.0.81")),
            Resource("2.0.61", get_last_res_version_android("2.0.61")),
            Resource("2.0.40", get_last_res_version_android("2.0.40")),
            # ----------
            # too legacy, and therefore selective
            # act24side
            Resource("1.9.81", get_last_res_version_android("1.9.81")),
            # act14mini
            Resource("1.9.62", get_last_res_version_android("1.9.62")),
            # act2bossrush
            Resource("1.9.42", get_last_res_version_android("1.9.42")),
            # act13mini, act12mini
            Resource("1.8.81", get_last_res_version_android("1.8.81")),
            # act1bossrush
            Resource("1.8.61", get_last_res_version_android("1.8.61")),
        ],
    )

    mgr.merge_src_res()

    mgr.merge_act_asset_map()

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    mgr.build_mod()


if __name__ == "__main__":
    main()

from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger


def main():
    mgr = ManifestMerger(
        "chronosphere_win",
        Resource("2.7.51", "26-07-10-13-52-38_fcd8ed", "Windows"),
        [
            Resource("2.7.41", "26-07-01-15-25-07_7886d5", "Windows"),
            Resource("2.7.31", "26-05-20-14-05-50_24a03e", "Windows"),
            Resource("2.7.21", "26-04-22-09-33-12_01a3a2", "Windows"),
            Resource("2.7.11", "26-03-31-05-51-38_1cc8a5", "Windows"),
            Resource("2.7.01", "26-02-28-11-16-12_689e5e", "Windows"),
            Resource("2.6.91", "26-02-02-05-12-37_d6d557", "Windows"),
        ],
        "Windows",
    )

    mgr.merge_src_res()

    mgr.merge_special_anon_bundle()

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    mgr.build_mod()


if __name__ == "__main__":
    main()

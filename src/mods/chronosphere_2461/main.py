from openbachelorm.resource import Resource
from openbachelorm.manifest import ManifestMerger


def main():
    mgr = ManifestMerger(
        "chronosphere_2461",
        Resource("2.4.61", "25-03-27-16-19-10-4d4819"),
        [
            Resource("2.4.41", "25-02-19-09-21-28-ba1f4e"),
            Resource("2.4.21", "25-01-08-07-44-44-3d8742"),
            Resource("2.4.01", "24-11-21-11-04-45-bae23b"),
            Resource("2.3.81", "24-10-24-14-30-30-b63a02"),
            Resource("2.3.61", "24-09-23-11-27-19-c6564b"),
            Resource("2.3.21", "24-08-26-16-10-17-fd946e"),
            Resource("2.3.01", "24-07-23-15-16-02-a53606"),
            Resource("2.2.81", "24-06-21-09-33-59-503529"),
            Resource("2.2.61", "24-05-22-06-44-01-4a3244"),
            Resource("2.2.41", "24-04-26-09-22-08-413e02"),
            Resource("2.2.21", "24-03-29-14-33-44-5002d2"),
            Resource("2.2.01", "24-02-26-08-28-19-0f351f"),
            Resource("2.1.41", "24-01-12-07-52-32-80033a"),
            Resource("2.1.21", "23-11-17-08-48-31-26d599"),
            Resource("2.1.01", "23-10-18-08-57-00-a2b96e"),
            Resource("2.0.81", "23-09-20-13-28-42-486799"),
            Resource("2.0.61", "23-08-25-11-36-41-12f55f"),
            Resource("2.0.40", "23-07-24-13-21-30-90fb63"),
            # ----------
            # too legacy, and therefore selective
            # act24side
            Resource("1.9.81", "23-03-27-11-50-38-b42880"),
            # act14mini
            Resource("1.9.62", "23-02-22-22-37-04-ef2150"),
            # act2bossrush
            Resource("1.9.42", "23-01-11-12-54-27-873b47"),
            # act13mini, act12mini
            Resource("1.8.81", "22-09-19-15-00-59-ae77d7"),
            # act1bossrush
            Resource("1.8.61", "22-08-29-13-56-31-95a9a4"),
        ],
    )

    mgr.merge_src_res()

    mgr.copy_zonemap_node()

    mgr.copy_merger_tree_node(
        "activity/[uc]act24side/zonemap/zone_map_act24side_zone1",
        "ui/zonemaps/zone_map_act24side_zone1",
    )

    mgr.prep_merger_bundle()

    mgr.migrate_level()

    mgr.build_mod()


if __name__ == "__main__":
    main()

import networkx as nx

import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import ScenarioContainer, StaticTarget


def _construct_falklands_ship(above_ground_m: float) -> nx.Graph:
    wp_1 = g.WayPoint(1, -59.3261, -51.1776)
    wp_2 = g.WayPoint(2, -59.3014, -51.2653)
    wp_3 = g.WayPoint(3, -59.5047, -51.1362)
    wp_4 = g.WayPoint(4, -60.6939, -51.1845)
    wp_5 = g.WayPoint(5, -60.9356, -51.5360)
    wp_6 = g.WayPoint(6, -61.3064, -51.5224)
    wp_7 = g.WayPoint(7, -60.7873, -51.7542)
    wp_8 = g.WayPoint(8, -61.5151, -51.8459)
    wp_9 = g.WayPoint(9, -60.6582, -52.3118)
    wp_10 = g.WayPoint(10, -60.0512, -52.2177)
    wp_11 = g.WayPoint(11, -60.3945, -52.3839)

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8, wp_9, wp_10, wp_11])
    for wp in graph.nodes:
        wp.alt_m = wp.ground_m + above_ground_m
        wp.is_point_of_interest = True

    # edges
    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_1, wp_3)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_4, wp_6)
    graph.add_edge(wp_5, wp_7)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_7)
    graph.add_edge(wp_6, wp_8)
    graph.add_edge(wp_8, wp_9)
    graph.add_edge(wp_9, wp_10)
    graph.add_edge(wp_9, wp_11)
    graph.add_edge(wp_10, wp_11)

    return graph


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        # Port Howard SFPH
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-59.50651585, -51.62629475, 1), 0),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(-59.52009521, -51.63214343, 1), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-59.51432636, -51.61269427, 17), 0, 2),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-59.52070372, -51.61498746, 7), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-59.52368429, -51.61193519, 18), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-59.50628052, -51.61192936, 1), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-59.50338468, -51.62123505, 1), 0, 3),

        # Chartres SFCS
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.06014292, -51.71829692, 10), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-60.06904195, -51.71512290, 6), 0),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(-60.05780592, -51.72231465, 7), 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(-60.05508825, -51.72659592, 2), 0, 1),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.06391101, -51.73510859, 81), 0),

        # Dunnose Head SFDH
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(-60.41455806, -51.75474579, 9), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.41779578, -51.75019133, 19), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.40498462, -51.75773028, 1), 0, 2),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.41800430, -51.76342062, 5), 0),

        # Shallow Harbour SFSW
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.52336272, -51.76004950, 16), 0),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(-60.52216032, -51.75124282, 40), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.51654578, -51.74090384, 111), 0, 2),

        # Spring Point SFSP
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.45442221, -51.83032886, 19), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.44393529, -51.83290163, 17), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-60.46448109, -51.83920252, 1), 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(-60.48275161, -51.83544599, 10), 0, 1),

        # Port Stephens SFPS
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(-60.83463924, -52.07935587, 18), 0),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.85245786, -52.09274383, 17), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.84476475, -52.10766650, 1), 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(-60.84253921, -52.08965744, 22), 0, 2),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-60.84506353, -52.12238839, 1), 0),

        # West Point SFWP
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.66546029, -51.35547304, 3), 0, 1),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.64381050, -51.34636112, 12), 0, 3),
        StaticTarget(mpt.MPTarget.LIGHT_HANGAR, g.Position(-60.69391652, -51.34264992, 12), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.68366466, -51.34916960, 10), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-60.63344255, -51.37084483, 16), 0),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.69487360, -51.37863192, 2), 0),

        # Crodendle House SFCH
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-60.26388741, -51.52671908, 38), 0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(-60.25399085, -51.53174845, 30), 0, 3),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.25744850, -51.54523981, 46), 0),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.25824423, -51.51302880, 56), 0),

        # Hill Cove SFHC
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.14780072, -51.50589489, 17), 0),
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(-60.13912595, -51.50633961, 18), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.15864713, -51.48810510, 1), 0, 3),

        # North Arm SFNA
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-59.37846855, -52.12489388, 14), 0),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-59.36832970, -52.12551483, 8), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-59.37492797, -52.14119141, 7), 1),
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-59.35872516, -52.13147986, 7), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(-59.38594129, -52.13293278, 12), 0),

        # Fox Bay SFFB
        StaticTarget(mpt.MPTarget.GASOMETER, g.Position(-60.06258578, -51.93542851, 29), 0),
        StaticTarget(mpt.MPTarget.WAREHOUSE, g.Position(-60.05899565, -51.95788521, 9), 0),
        StaticTarget(mpt.MPTarget.DEPOT, g.Position(-60.06694972, -51.92370182, 26), 0),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(-60.07676724, -51.93897830, 6), 1),
    ]
    scenario = ScenarioContainer('falklands', 'Falklands',
                                 'Cf. http://opredflag.com/events/923128?event_instance_id=15944889',
                                 (-61., -52.5), (-57.5, -51.2),
                                 'EGYP', None, 60)
    scenario.add_static_targets(static_targets)
    scenario.add_ships(2, 0, 3, _construct_falklands_ship(0.), [mpt.oprf_frigate])
    return scenario

import networkx as nx

import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import OPFOR_defaults, ScenarioContainer, StaticTarget, default_ships_list


def _construct_northern_mariana_ship(above_ground_m: float) -> nx.Graph:
    wp_1 = g.WayPoint(1, 145.541739, 15.029769)
    wp_2 = g.WayPoint(2, 145.547782, 15.091035)
    wp_3 = g.WayPoint(3, 145.615004, 15.139890)
    wp_4 = g.WayPoint(4, 145.631621, 15.217889)
    wp_5 = g.WayPoint(5, 145.719237, 15.234651)
    wp_6 = g.WayPoint(6, 145.778906, 15.308972)
    wp_7 = g.WayPoint(7, 145.865012, 15.297316)
    wp_8 = g.WayPoint(8, 145.883139, 15.263800)
    wp_9 = g.WayPoint(9, 145.814406, 15.203312)
    wp_10 = g.WayPoint(10, 145.824980, 15.130412)
    wp_11 = g.WayPoint(11, 145.787970, 15.098328)
    wp_12 = g.WayPoint(12, 145.815161, 15.041440)
    wp_13 = g.WayPoint(13, 145.892958, 15.048005)
    wp_14 = g.WayPoint(14, 145.894469, 14.971403)
    wp_15 = g.WayPoint(15, 145.800055, 14.964836)
    # wp_0 = g.WayPoint(, 145.813651, 15.043628)
    wp_17 = g.WayPoint(17, 145.756247, 15.057487)
    wp_18 = g.WayPoint(18, 145.707907, 15.098328)
    # wp_0 = g.WayPoint(0, 145.615759, 15.137703)
    wp_20 = g.WayPoint(20, 145.681471, 15.093223)
    wp_21 = g.WayPoint(21, 145.712439, 15.046546)
    wp_22 = g.WayPoint(22, 145.723769, 14.973592)
    wp_23 = g.WayPoint(23, 145.688269, 14.914481)
    wp_24 = g.WayPoint(24, 145.620291, 14.894044)
    wp_25 = g.WayPoint(25, 145.593855, 14.923969)
    wp_26 = g.WayPoint(26, 145.522856, 14.886014)
    wp_27 = g.WayPoint(27, 145.489623, 14.953890)
    wp_28 = g.WayPoint(28, 145.540984, 14.979429)
    # wp_0 = g.WayPoint(0, 145.593100, 14.925429)
    # wp_0 = g.WayPoint(0, 145.542494, 15.030498)

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8, wp_9, wp_10,
                          wp_11, wp_12, wp_13, wp_14, wp_15, wp_17, wp_18,
                          wp_20, wp_21, wp_22, wp_23, wp_24, wp_26, wp_27, wp_28])
    for wp in graph.nodes:
        wp.alt_m = wp.ground_m + above_ground_m
        wp.is_point_of_interest = True

    # edges
    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_7)
    graph.add_edge(wp_7, wp_8)
    graph.add_edge(wp_8, wp_9)
    graph.add_edge(wp_9, wp_10)
    graph.add_edge(wp_10, wp_11)
    graph.add_edge(wp_11, wp_12)
    graph.add_edge(wp_12, wp_13)
    graph.add_edge(wp_13, wp_14)
    graph.add_edge(wp_14, wp_15)
    graph.add_edge(wp_15, wp_12)
    graph.add_edge(wp_12, wp_17)
    graph.add_edge(wp_17, wp_18)
    graph.add_edge(wp_18, wp_3)
    graph.add_edge(wp_3, wp_20)
    graph.add_edge(wp_20, wp_21)
    graph.add_edge(wp_21, wp_22)
    graph.add_edge(wp_22, wp_23)
    graph.add_edge(wp_23, wp_24)
    graph.add_edge(wp_24, wp_25)
    graph.add_edge(wp_25, wp_26)
    graph.add_edge(wp_26, wp_27)
    graph.add_edge(wp_27, wp_28)
    graph.add_edge(wp_28, wp_25)
    graph.add_edge(wp_25, wp_1)
    graph.add_edge(wp_27, wp_1)
    graph.add_edge(wp_28, wp_1)
    graph.add_edge(wp_15, wp_22)
    graph.add_edge(wp_22, wp_17)
    graph.add_edge(wp_17, wp_11)

    return graph


def build_scenario(path: str) -> ScenarioContainer:
    static_targets = [
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(145.66579653, 14.95363634, 2.8763), 0, 2),
        StaticTarget(mpt.MPTarget.S_300, g.Position(145.65159095, 14.95604869, 182.8701), 0, 1),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(145.55179930, 14.84919640, 157.4966), 0, 2),
        StaticTarget(mpt.MPTarget.BUK_M2, g.Position(145.62759909, 15.04078500, 154.6720), 0, 2),
        StaticTarget(mpt.MPTarget.S_300, g.Position(145.63128228, 15.01646323, 83.5844), 240.0, 1),
        StaticTarget(mpt.MPTarget.TOWER, g.Position(145.72406157, 15.12155346, 65.5575), 85.0),
        # StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(145.72547640, 15.12485989, 63.1279), 0),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(145.7267, 15.1258, 63.1279), 0),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(145.72545999, 15.12391426, 63.6506), 0),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(145.72694381, 15.12315665, 65.5359), 0),
        StaticTarget(mpt.MPTarget.DOUBLE_SHELTER, g.Position(145.72666452, 15.12467371, 63.6134), 0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(145.72881483, 15.12316435, 66.2967), 204.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(145.72949293, 15.12345911, 66.3027), 204.0),
        StaticTarget(mpt.MPTarget.BUNKER, g.Position(145.73020012, 15.12377071, 66.3147), 204.0),
        StaticTarget(mpt.MPTarget.RADAR_STATION, g.Position(145.72379214, 15.12331304, 62.7219), 292.0),
        StaticTarget(mpt.MPTarget.S_300, g.Position(145.72582705, 15.12042629, 67.4474), 148.0)
    ]
    scenario = ScenarioContainer('northern_mariana', 'Northern Mariana',
                                 'http://opredflag.com/events/929815?event_instance_id=16025063',
                                 OPFOR_defaults,
                                 (143.75, 14.76), (146, 15.375),
                                 'PGSN', 0.3, None, 60)
    scenario.add_static_targets(static_targets)
    scenario.add_ships(3, 0, 0, _construct_northern_mariana_ship(0.), default_ships_list)
    return scenario

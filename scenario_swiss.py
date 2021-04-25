import networkx as nx

import hunter.geometry as g
import hunter.mp_targets as mpt
from hunter.scenarios import OPFOR_defaults, ScenarioContainer, StaticTarget, create_circle_points, load_network, default_helis_list


def _construct_dammastock_circle() -> nx.DiGraph:
    return create_circle_points(8.42, 46.643, 10000, int(g.feet_to_metres(12000)), 18)


def _construct_alpnach_see_speedboat_track() -> nx.Graph:
    wp_1 = g.WayPoint(1, 8.28858, 46.9573, alt_m=433.995)
    wp_2 = g.WayPoint(2, 8.28507, 46.9558, alt_m=433.998)
    wp_3 = g.WayPoint(3, 8.28111, 46.9566, alt_m=433.997)
    wp_4 = g.WayPoint(4, 8.28604, 46.9598, alt_m=433.997)
    wp_5 = g.WayPoint(5, 8.28903, 46.9602, alt_m=433.994)
    wp_6 = g.WayPoint(6, 8.29531, 46.9631, alt_m=433.988)
    wp_7 = g.WayPoint(7, 8.31209, 46.968, alt_m=433.996)
    wp_8 = g.WayPoint(8, 8.29588, 46.9534, alt_m=433.988)
    wp_9 = g.WayPoint(9, 8.31757, 46.9624, alt_m=433.99)
    wp_10 = g.WayPoint(10, 8.32711, 46.9673, alt_m=433.988)
    wp_11 = g.WayPoint(11, 8.33434, 46.9718, alt_m=433.995)
    wp_12 = g.WayPoint(12, 8.33426, 46.975, alt_m=433.997)
    wp_13 = g.WayPoint(13, 8.33218, 46.976, alt_m=433.999)
    wp_14 = g.WayPoint(14, 8.33128, 46.9729, alt_m=433.997)
    wp_15 = g.WayPoint(15, 8.32346, 46.9693, alt_m=433.988)

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8, wp_9,
                          wp_10, wp_11, wp_12, wp_13, wp_14, wp_15])

    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_7)
    graph.add_edge(wp_7, wp_15)
    graph.add_edge(wp_1, wp_6)
    graph.add_edge(wp_1, wp_8)
    graph.add_edge(wp_8, wp_9)
    graph.add_edge(wp_9, wp_15)
    graph.add_edge(wp_9, wp_10)
    graph.add_edge(wp_10, wp_11)
    graph.add_edge(wp_10, wp_15)
    graph.add_edge(wp_10, wp_14)
    graph.add_edge(wp_11, wp_12)
    graph.add_edge(wp_12, wp_13)
    graph.add_edge(wp_13, wp_14)
    graph.add_edge(wp_14, wp_15)

    return graph


def _construct_lsmi_truck_track() -> nx.Graph:
    wp_1 = g.WayPoint(1, 7.88845, 46.6828, alt_m=572.326)
    wp_2 = g.WayPoint(2, 7.88614, 46.6843, alt_m=569.999)
    wp_3 = g.WayPoint(3, 7.8842, 46.6848, alt_m=569.318)
    wp_4 = g.WayPoint(4, 7.88334, 46.6835, alt_m=570.203)
    wp_5 = g.WayPoint(5, 7.88326, 46.6832, alt_m=570.407)
    wp_6 = g.WayPoint(6, 7.88692, 46.6818, alt_m=572.526)
    wp_7 = g.WayPoint(7, 7.88103, 46.6827, alt_m=570.745)
    wp_8 = g.WayPoint(8, 7.88007, 46.6827, alt_m=570.853)
    wp_9 = g.WayPoint(9, 7.8793, 46.6835, alt_m=570.49)
    wp_10 = g.WayPoint(10, 7.87698, 46.6834, alt_m=571.04)
    # North East corner taken out due to buildings in OSM
    # wp_11 = g.WayPoint(11, 7.87729, 46.6842, alt_m=570.46)
    # wp_12 = g.WayPoint(12, 7.87822, 46.6847, alt_m=569.882)
    # wp_13 = g.WayPoint(13, 7.87955, 46.6851, alt_m=569.374)
    wp_14 = g.WayPoint(14, 7.87752, 46.682, alt_m=571.763)
    wp_15 = g.WayPoint(15, 7.87841, 46.6811, alt_m=572.15)
    wp_16 = g.WayPoint(16, 7.8768, 46.6765, alt_m=575.292)
    wp_17 = g.WayPoint(17, 7.87794, 46.6758, alt_m=575.804)
    wp_18 = g.WayPoint(18, 7.86908, 46.6712, alt_m=579.742)
    wp_19 = g.WayPoint(19, 7.8698, 46.6703, alt_m=580.24)
    wp_20 = g.WayPoint(20, 7.87131, 46.6697, alt_m=580.715)
    wp_21 = g.WayPoint(21, 7.87328, 46.6702, alt_m=580.383)
    wp_22 = g.WayPoint(22, 7.881, 46.6761, alt_m=576.162)
    wp_23 = g.WayPoint(23, 7.87908, 46.6766, alt_m=575.25)
    wp_24 = g.WayPoint(24, 7.88472, 46.6798, alt_m=573.606)
    wp_25 = g.WayPoint(25, 7.88529, 46.6807, alt_m=572.983)

    graph = nx.Graph()
    graph.add_nodes_from([wp_1, wp_2, wp_3, wp_4, wp_5, wp_6, wp_7, wp_8, wp_9,
                          wp_10, wp_14, wp_15, wp_16, wp_17, wp_18, wp_19,  # , wp_11, wp_12, wp_13
                          wp_20, wp_21, wp_22, wp_23, wp_24, wp_25])

    graph.add_edge(wp_1, wp_2)
    graph.add_edge(wp_2, wp_3)
    graph.add_edge(wp_3, wp_4)
    graph.add_edge(wp_4, wp_5)
    graph.add_edge(wp_5, wp_6)
    graph.add_edge(wp_6, wp_1)
    graph.add_edge(wp_5, wp_7)
    graph.add_edge(wp_7, wp_8)
    graph.add_edge(wp_8, wp_9)
    graph.add_edge(wp_9, wp_4)
    graph.add_edge(wp_9, wp_10)
    # graph.add_edge(wp_10, wp_11)
    # graph.add_edge(wp_11, wp_12)
    # graph.add_edge(wp_12, wp_13)
    # graph.add_edge(wp_13, wp_3)
    graph.add_edge(wp_10, wp_14)
    graph.add_edge(wp_14, wp_15)
    graph.add_edge(wp_15, wp_16)
    graph.add_edge(wp_16, wp_17)
    graph.add_edge(wp_16, wp_18)
    graph.add_edge(wp_18, wp_19)
    graph.add_edge(wp_19, wp_20)
    graph.add_edge(wp_20, wp_21)
    graph.add_edge(wp_21, wp_22)
    graph.add_edge(wp_22, wp_23)
    graph.add_edge(wp_22, wp_24)
    graph.add_edge(wp_24, wp_25)
    graph.add_edge(wp_25, wp_6)
    graph.add_edge(wp_25, wp_23)
    graph.add_edge(wp_23, wp_17)
    graph.add_edge(wp_17, wp_19)

    return graph


def build_scenario() -> ScenarioContainer:
    static_targets = [
        # Axalp
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(8.0547, 46.7057, 2180), 70),  # Grätli left
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(8.0551, 46.7051, 2165), 60),  # Grätli right
        StaticTarget(mpt.MPTarget.HILL_TARGET, g.Position(8.05934685, 46.70961520, 2237), 0),  # Axalphorn
        StaticTarget(mpt.MPTarget.CLIFF_TARGET, g.Position(8.0617, 46.7011, 2230), 165),  # Felswand
        StaticTarget(mpt.MPTarget.WATER_TARGET, g.Position(6.88, 46.88, 419), 130)  # Forel
    ]
    # A truck driving on the runway and taxiway as LSMI
    lsmi_graph = _construct_lsmi_truck_track()
    origin_lsmi = g.Position(7.88845, 46.6828)  # same as WP_1
    lsmi_truck = mpt.MPTargetTrips.create_random_target(mpt.MPTarget.TRUCK, lsmi_graph, origin_lsmi,
                                                        mpt.MPTargetTrips.STATIC_HP, 5, 10000, 0)
    # A random trip speedboat on Alpnach Lake
    lsma_graph = _construct_alpnach_see_speedboat_track()
    origin_lsma = g.Position(8.28858, 46.9573)
    lsma_speedboat = mpt.MPTargetTrips.create_random_target(mpt.MPTarget.SPEEDBOAT, lsma_graph, origin_lsma,
                                                            mpt.MPTargetTrips.STATIC_HP, 5, 10000, 0)
    # a convoy of trucks close to LSMP
    # network created with road_network.py: TEST/params.py -b *6.75_46.75_7_46.875 -o swiss_lsmp_roads.pkl
    lsmp_trip_graph = load_network('swiss_lsmp_roads.pkl')
    origin_trip_lsmp = g.Position(6.7813, 46.8112)  # Cheyres
    dests_lsmp = [g.Position(6.9595, 46.8387),  # Corcelles
                  g.Position(6.8319, 46.7803),  # Nuvilly
                  g.Position(6.9280, 46.8721),  # Grandcour
                  g.Position(6.9387, 46.7542)  # Chatonnaye
                  ]
    lsmp_convoy = mpt.MPTargetTrips.create_routed_convoy_targets(mpt.MPTarget.TRUCK,
                                                                 lsmp_trip_graph, origin_trip_lsmp,
                                                                 mpt.MPTargetTrips.STATIC_HP, 5, dests_lsmp, True,
                                                                 30, 3, 2)

    # a convoy of trucks running around lake Murten
    # network created with road_network.py: -f TEST/params.py -b *7.018_46.9_7.148_46.97 -o swiss_murten_roads.pkl
    murten_trip_graph = load_network('swiss_murten_roads.pkl')
    origin_trip_murten = g.Position(7.0253, 46.9200)  # Salavaux
    dests_murten = [g.Position(7.0752, 46.9083),  # Faoug
                    g.Position(7.1339, 46.9396),  # Muntelier
                    g.Position(7.1139, 46.9628),  # Sugiez
                    g.Position(7.0253, 46.9200)  # Salavaux
                    ]
    murten_convoy = mpt.MPTargetTrips.create_routed_convoy_targets(mpt.MPTarget.TRUCK,
                                                                   murten_trip_graph, origin_trip_murten,
                                                                   mpt.MPTargetTrips.STATIC_HP, 0, dests_murten, True,
                                                                   40, 5, 2)

    trip_targets = [lsmi_truck, lsma_speedboat]
    trip_targets.extend(lsmp_convoy)
    trip_targets.extend(murten_convoy)

    # network created with heli_network.py: -f TEST/params.py -b *8_46.75_8.75_47.125 -o swiss_helis.pkl
    heli_network = load_network('swiss_helis.pkl')

    scenario = ScenarioContainer('swiss', 'Swiss', 'Swiss Air Force shooting range Axalp and other training targets',
                                 OPFOR_defaults,
                                 (6.7, 46.5), (8.8, 47.1),
                                 'LSMM', 2.5, None, 60)
    scenario.add_static_targets(static_targets)
    scenario.add_targets_with_trips(trip_targets)
    scenario.add_towed_targets(2, mpt.pc9, 500, 120, _construct_dammastock_circle())
    scenario.add_helicopters(3, 5, heli_network, default_helis_list)
    return scenario

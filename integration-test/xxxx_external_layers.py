# -*- encoding: utf-8 -*-
import json
import os
import shutil

import dsl
from shapely.wkt import loads as wkt_loads

from . import FixtureTest


class ExternalLayers(FixtureTest):
    def test_no_external_layer_building_merge(self):
        """
        First make sure that even if there is no external layer everything still loads fine and the buildings do merge
        """
        # just in case a failed test didnt cleanup
        shutil.rmtree('external_layers', ignore_errors=True)

        # get two adjacent buildings there so they will merge
        self.generate_fixtures(dsl.way(777, wkt_loads('POLYGON ((0 0, 0 .001, .001 .001, .001 0, 0 0))'),
                                       {u'building': u'yes', u'layer': u'2', u'name': u'foo'}),
                               dsl.way(778, wkt_loads('POLYGON ((.001 0, .001 .001, .002 .001, .002 0, .001 0))'),
                                       {u'building': u'yes', u'layer': u'2', u'name': u'bar'}),
                               )

        # prove they merged, there should be 1 building there
        self.assert_n_matching_features(15, 16384, 16383, 'buildings', {'kind': 'building'}, 1)

        # prove there are no auxiliary buildings pois
        self.assert_no_matching_feature(15, 16384, 16383, 'auxiliary_buildings', {})

    def test_external_layer_blocks_building_merge(self):
        # we can temporarily add the external layer, here we build a square structure over the center of the map
        # note that the origin of the feature is in the upper right quadrant but should appear in all quadrants
        null_island = {
            "type": "FeatureCollection",
            "name": "foo",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::3857"}},
            "features": [
                {"type": "Feature",
                 "properties": {"name": "null island hut", "superseded": True, "baz": "qux", "origin": [1, 1], "id": 42},
                 "geometry": {"type": "Polygon", "coordinates":
                     [[[111, 111], [-111, 111],  [-111, -111], [111, -111], [111, 111]]]}}
            ]
        }

        # write it to disk
        shutil.rmtree('external_layers', ignore_errors=True)
        os.makedirs('external_layers')
        with open('external_layers/auxiliary_buildings.geojson', 'w') as f:
            json.dump(null_island, f)

        # get a building or two in there right next to each other so they will merge
        self.generate_fixtures(dsl.way(777, wkt_loads('POLYGON ((0 0, 0 .001, .001 .001, .001 0, 0 0))'),
                                       {u'building': u'yes', u'layer': u'2', u'name': u'foo'}),
                               dsl.way(778, wkt_loads('POLYGON ((.001 0, .001 .001, .002 .001, .002 0, .001 0))'),
                                       {u'building': u'yes', u'layer': u'2', u'name': u'bar'}),
                               )

        # prove they didnt merge, there should still be 2 buildings there
        self.assert_n_matching_features(15, 16384, 16383, 'buildings', {'kind': 'building'}, 2)

        # check that the property was copied to the right building
        self.assert_has_feature(17, 65536, 65535, 'buildings', {'superseded': 'true', 'name': 'foo'})

        # check that the pois made it in properly mutated from the original feature
        self.assert_has_feature(15, 16383, 16383, 'auxiliary_buildings', {'baz': 'qux'})
        self.assert_feature_geom_type(15, 16383, 16383, 'auxiliary_buildings', '42', 'Point')
        self.assert_has_feature(15, 16384, 16383, 'auxiliary_buildings', {'baz': 'qux'})
        self.assert_feature_geom_type(15, 16384, 16383, 'auxiliary_buildings', '42', 'Point')
        self.assert_has_feature(15, 16383, 16384, 'auxiliary_buildings', {'baz': 'qux'})
        self.assert_feature_geom_type(15, 16383, 16384, 'auxiliary_buildings', '42', 'Point')
        self.assert_has_feature(15, 16384, 16384, 'auxiliary_buildings', {'baz': 'qux'})
        self.assert_feature_geom_type(15, 16384, 16384, 'auxiliary_buildings', '42', 'Point')

        # clean up external layer
        shutil.rmtree('external_layers')
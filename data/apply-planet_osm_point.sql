DO $$
BEGIN

--------------------------------------------------------------------------------
-- planet_osm_point
--------------------------------------------------------------------------------

-- the coalesce here is just an optimisation, as the poi level
-- will always be NULL if all of the arguments are NULL.
UPDATE planet_osm_point SET
    mz_poi_min_zoom = mz_calculate_min_zoom_pois(planet_osm_point.*)
    WHERE mz_calculate_min_zoom_pois(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_water_min_zoom = mz_calculate_min_zoom_water(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_water(planet_osm_point.*) IS NOT NULL;

UPDATE planet_osm_point
  SET mz_places_min_zoom = mz_calculate_min_zoom_places(planet_osm_point.*)
  WHERE mz_calculate_min_zoom_places(planet_osm_point.*) IS NOT NULL;

CREATE INDEX planet_osm_point_min_zoom_way_9_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_way_12_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_way_15_index ON planet_osm_point USING gist(way) WHERE mz_poi_min_zoom <= 15;

CREATE INDEX planet_osm_point_min_zoom_water_9_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_water_12_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_water_15_index ON planet_osm_point USING gist(way) WHERE mz_water_min_zoom <= 15;

CREATE INDEX planet_osm_point_min_zoom_places_9_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 9;
CREATE INDEX planet_osm_point_min_zoom_places_12_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 12;
CREATE INDEX planet_osm_point_min_zoom_places_15_index ON planet_osm_point USING gist(way) WHERE mz_places_min_zoom <= 15;

END $$;

ANALYZE planet_osm_point;

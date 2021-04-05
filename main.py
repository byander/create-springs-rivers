import argparse
import geopandas as gpd
from collections import Counter
from shapely.geometry import Point
from pathlib import Path

# Round coordinates. Tested only UTM coordinates.
TOLERANCE = 5


class CreateSprings:

    def __init__(self):
        description = 'Create points from springs from rivers.'

        parser = argparse.ArgumentParser(description=description)

        parser.add_argument('-i', '--input', type=str, required=True,
                            help='Name (with extension) and path of the rivers '
                                 'shapefile')

        parser.add_argument('-o', '--output', type=str, required=True,
                            help='Output - Name (without extension) of '
                                 'springs points')

        args = vars(parser.parse_args())

        self.rivers_path = args['input']
        self.springs = args['output']
        self.list_points = []
        self.points = None

    def run(self):
        if not self.check_if_file_exist(self.rivers_path):
            return

        self.rivers = gpd.read_file(self.rivers_path)

        self.springs_points = Path(Path(self.rivers_path).parent,
                                   self.springs + '.shp')

        print('Finding springs points...')
        self.get_points()
        self.remove_duplicates()
        self.write_file()

    def check_if_file_exist(self, filepath):
        if Path(filepath).is_file():
            return True
        else:
            print('File not exits')
            return False

    def get_points(self):
        """Create springs points from rivers
        :param geopackage:
        :param rivers:
        :return:
        """
        for i, ft in self.rivers.iterrows():
            if ft.geometry.type == 'MultiLineString':
                for g in ft.geometry:
                    pt_ini = [round(g.coords[0][0], TOLERANCE),
                              round(g.coords[0][1], TOLERANCE)]

                    pt_end = [round(g.coords[-1][0], TOLERANCE),
                              round(g.coords[-1][1], TOLERANCE)]

                    self.list_points.append(pt_ini)
                    self.list_points.append(pt_end)

            elif ft.geometry.type == 'LineString':
                pt_ini = [round(list(ft['geometry'].coords)[0][0], TOLERANCE),
                          round(list(ft['geometry'].coords)[0][1], TOLERANCE)]

                pt_end = [round(list(ft['geometry'].coords)[-1][0], TOLERANCE),
                          round(list(ft['geometry'].coords)[-1][1], TOLERANCE)]

                self.list_points.append(pt_ini)
                self.list_points.append(pt_end)

    def remove_duplicates(self):
        """Remove duplicate points
        Source:
        # https://stackoverflow.com/questions/52452286/python-remove-all-duplicates-from-a-large-list-of-lists-efficiently-and-elegant
         """
        nodups = {k for k, cnt in Counter(map(tuple, self.list_points)).items()
                  if cnt == 1}
        list_points_nodup = [list(k) for k in map(tuple, self.list_points) if
                             k in nodups]

        self.points = gpd.GeoSeries([Point(list(xy)) for xy in
                                     list_points_nodup])

    def write_file(self):
        self.points.to_file(self.springs_points, layer='nascentes',
                            crs=self.rivers.crs)


if __name__ == '__main__':
    cs = CreateSprings()
    cs.run()

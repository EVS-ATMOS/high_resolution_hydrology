#!/usr/bin/env python

import matplotlib
matplotlib.use('agg')
import pyart
from matplotlib import pyplot as plt

from netCDF4 import num2date, date2num
import numpy as np
from time import time
import os
#here is the key import!
from IPython.parallel import Client
from time import sleep

def do_grid_map_gates_to_grid(radar_fname):
    import pyart
    from matplotlib import pyplot as plt
    from netCDF4 import num2date, date2num
    import numpy as np
    from time import time
    import os
    md = '/lcrc/group/earthscience/radar/chicago_stationary/'
    try:
        radar = pyart.io.read(radar_fname)
        rain_z = radar.fields['reflectivity']['data'].copy()
        z_lin = 10.0**(radar.fields['reflectivity']['data']/10.)
        rain_z = (z_lin/300.0)**(1./1.4)  #Z=300 R1.4
        radar.add_field_like('reflectivity', 'rain_z',  rain_z, replace_existing = True)
        radar.fields['rain_z']['units'] = 'mm/h'
        radar.fields['rain_z']['standard_name'] = 'rainfall_rate'
        radar.fields['rain_z']['long_name'] = 'rainfall_rate_from_z'
        radar.fields['rain_z']['valid_min'] = 0
        radar.fields['rain_z']['valid_max'] = 500
        grid = pyart.map.grid_from_radars(
             (radar,), grid_shape=(1, 501, 501),
            grid_limits=((0, 0),(-50000, 50000), (-50000, 50000)),
            fields=radar.fields.keys(), gridding_algo="map_gates_to_grid",
            weighting_function='BARNES')
        dts = num2date(grid.axes['time']['data'], grid.axes['time']['units'])
        sstr = dts[0].strftime('%Y%m%d_%H%M%S')
        pyart.io.write_grid(md + 'grid_250_'+sstr+'.nc', grid)
        myd = pyart.graph.RadarMapDisplay(radar)
        fig = plt.figure(figsize = [18,10])
        myd.plot_ppi_map( 'rain_z', vmin = 0, vmax = 100,
                         resolution = 'h', max_lat = 41.8,
                         min_lat = 41.25, min_lon = -88.3, max_lon = -87.5)
        m = myd.basemap
        m.drawparallels(np.linspace(41, 42, 9),labels=[1,0,0,0])
        m.drawmeridians(np.linspace(-88.4, -87, 8),labels=[0,0,0,1])
        m.drawrivers()
        m.drawcounties()
        m.drawstates()
        m.drawmapscale(-88., 41.55, -88.,
                41.55, 10, barstyle='fancy', fontcolor='k',
                fillcolor1='b', fillcolor2='k')
        myd.plot_point( -87.9706,41.6815,
                label_text = 'Argonne Lab', label_offset = (0.0,0.0) )
        plt.savefig(md+ 'radar_'+sstr+'.png')
        plt.close(fig)
        fig = plt.figure(figsize = [15,15])
        max_lat = 43
        min_lat = 41.5
        min_lon = -88.3
        max_lon = -87.5
        display = pyart.graph.GridMapDisplay(grid)
        display.plot_basemap(lat_lines=np.arange(min_lat,max_lat,.1),
                             lon_lines=np.arange(min_lon, max_lon, .1),
                             resolution='h')
        display.plot_grid('rain_z', vmin=0, vmax=100)
        xcf,ycf = display.basemap(-87.9706,41.6815)
        display.basemap.plot(xcf,ycf,'ro')
        plt.text(xcf+2000.,ycf+2000., 'Argonne Lab')
        display.basemap.drawcounties()
        display.basemap.drawrivers()

        display.basemap.drawmapscale(-88., 41.55, -88., 41.55, 10, barstyle='fancy', fontcolor='k', fillcolor1='b', fillcolor2='k')
        display.plot_colorbar()
        plt.savefig(md+ 'mapped_250_'+sstr+'.png')
        plt.close(fig)
        del(radar)
        del(grid)
    except:
        pass
    return 0

print('Exex')

md = '/lcrc/group/earthscience/radar/chicago_stationary/'
idir = md
filelist = os.listdir(md)
good_files = []
for fl in filelist:
    if 'KLOT' in fl:
        good_files.append(idir + fl)
good_files.sort()
state = 0
while state == 0:
    try:
        My_Cluster = Client()
        My_View = My_Cluster[:]
        state = 1
    except:
        state = 0
        print('Cluster not ready for me')
    sleep(10)

print My_View
print len(My_View)

#Turn off blocking so all engines can work async
My_View.block = False

#on all engines do an import of Py-ART
My_View.execute('import matplotlib')
My_View.execute('matplotlib.use("agg")')




#Map the code and input to all workers
result = My_View.map_async(do_grid_map_gates_to_grid, good_files)

#Reduce the result to get a list of output
qvps = result.get()



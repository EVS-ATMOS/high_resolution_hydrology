#!/usr/bin/env python

import matplotlib
matplotlib.use('agg')
import pyart
from matplotlib import pyplot as plt

from netCDF4 import num2date, date2num
import numpy as np
from time import time, sleep
import os
#here is the key import!
from IPython.parallel import Client


def do_grid_map_gates_to_grid(radar_fname):
    import pyart
    from matplotlib import pyplot as plt
    from netCDF4 import num2date, date2num
    import numpy as np
    from time import time
    import os
    md = '/lcrc/group/earthscience/radar/maine_out/'
    try:
        tf = md + radar_fname.split('/')[-1]+'.status'
        fh = open(tf, 'w')
        fh.write('READING' + radar_fname + ' \n')
        fh.close()
        radar = pyart.io.read(radar_fname)
        fh = open(tf, 'w')
        fh.write('Calcs \n')
        fh.close()
        gatefilter = pyart.correct.GateFilter(radar)
        gatefilter.exclude_masked('reflectivity')
        #gatefilter.exclude_below('cross_correlation_ratio', 0.75)
        rain_z = radar.fields['reflectivity']['data'].copy()
        z_lin = 10.0**(radar.fields['reflectivity']['data']/10.)
        rain_z = (z_lin/300.0)**(1./1.4)  #Z=300 R1.4
        radar.add_field_like('reflectivity', 'rain_z',  rain_z, replace_existing = True)
        radar.fields['rain_z']['units'] = 'mm/h'
        radar.fields['rain_z']['standard_name'] = 'rainfall_rate'
        radar.fields['rain_z']['long_name'] = 'rainfall_rate_from_z'
        radar.fields['rain_z']['valid_min'] = 0
        radar.fields['rain_z']['valid_max'] = 500
        min_lat = 43
        min_lon = -72
        max_lon = -69
        max_lat = 45
        fh = open(tf, 'w')
        fh.write('GRIDDING \n')
        fh.close()
        grid = pyart.map.grid_from_radars(
             (radar,), grid_shape=(1, 501, 501),
            grid_limits=((0, 0),(-50000, 50000), (-50000, 50000)),
            fields=radar.fields.keys(), gridding_algo="map_gates_to_grid",
            weighting_function='BARNES', gatefilters = (gatefilter,))
        dts = num2date(grid.axes['time']['data'], grid.axes['time']['units'])
        sstr = dts[0].strftime('%Y%m%d_%H%M%S')
        pyart.io.write_grid(md + 'grid_250_'+sstr+'.nc', grid)
        fh = open(tf, 'w')
        fh.write('PLOTTING PPI \n')
        fh.close()
        myd = pyart.graph.RadarMapDisplay(radar)
        fig = plt.figure(figsize = [18,10])
        myd.plot_ppi_map( 'rain_z', vmin = 0, vmax = 100, 
                         resolution = 'h', max_lat = max_lat, 
                         min_lat = min_lat, min_lon = min_lon, max_lon = max_lon)
        m = myd.basemap
        m.drawparallels(np.arange(min_lat,max_lat, 1),labels=[1,0,0,0])
        m.drawmeridians(np.arange(min_lon,max_lon, 1),labels=[0,0,0,1])
        m.drawrivers()
        m.drawcounties()
        m.drawstates()
        plt.savefig(md+ 'radar_'+sstr+'.png')
        plt.close(fig)
        fig = plt.figure(figsize = [15,15])
        display = pyart.graph.GridMapDisplay(grid)
        display.plot_basemap(lat_lines=np.arange(min_lat,max_lat,.1),
                             lon_lines=np.arange(min_lon, max_lon, .1),
                             resolution='h')
        display.plot_grid('rain_z', vmin=0, vmax=100)
        display.basemap.drawcounties()
        display.basemap.drawrivers()
        plt.savefig(md+ 'mapped_250_'+sstr+'.png')
        plt.close(fig)
        max_r = grid.fields['rain_z']['data'].max()
        mean_r = grid.fields['rain_z']['data'].mean()
        stttr = '{} {}'.format(max_r, mean_r)
        fh = open(tf, 'w')
        fh.write(stttr + ' \n')
        fh.close()
        del(radar)
        del(grid)
    except:
        pass
    return 0

md = '/lcrc/group/earthscience/radar/nexrad/maine/'
idir = md
filelist = os.listdir(md)
good_files = []
for fl in filelist:
    if 'KGYX' in fl:
        good_files.append(idir + fl)
good_files.sort()

good = False
while not good:
    try:
        My_Cluster = Client()
        My_View = My_Cluster[:]
        print My_View
        print len(My_View)
        good = True
    except:
        print('no!')
        sleep(5)
        good = False

#Turn off blocking so all engines can work async
My_View.block = False

#on all engines do an import of Py-ART
My_View.execute('import matplotlib')
My_View.execute('matplotlib.use("agg")')




#Map the code and input to all workers
result = My_View.map_async(do_grid_map_gates_to_grid, good_files)

#Reduce the result to get a list of output
qvps = result.get()



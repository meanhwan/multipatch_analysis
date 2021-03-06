from collections import OrderedDict

all_connections = {((None,'sim1'), (None,'sim1')): ['1490642434.41', 3, 5],
                   ((None,'tlx3'), (None,'tlx3')): ['1492545925.15', 8, 5],
               ((None, 'sim1'), (None, 'pvalb')): ['1495574744.01', 8, 4],
               ((None, 'tlx3'), (None, 'pvalb')): ['1496699390.01', 8, 2],
               ((None, 'tlx3'), (None, 'sst')): ['1497653267.74', 3, 4],
               ((None, 'pvalb'), (None, 'sim1')): ['1495574744.01', 4, 8],
               ((None, 'pvalb'), (None, 'tlx3')): ['1503953399.15', 2, 8],
               ((None, 'pvalb'), (None, 'pvalb')): ['1491597493.27', 2, 6],
               ((None, 'pvalb'), (None, 'sst')): ['1493765516.34', 8, 3],
               ((None, 'pvalb'), (None, 'vip')): ['1487796524.54', 3, 6],
               ((None, 'sst'), (None, 'tlx3')): ['1504300627.31', 8, 2],
               ((None, 'sst'), (None, 'pvalb')): ['1493765516.34', 3, 8],
               ((None, 'sst'), (None, 'sst')): ['1493765516.34', 2, 3],
               ((None, 'sst'), (None, 'vip')): ['1494632512.34', 5, 4],
               ((None, 'vip'), (None, 'sst')): ['1490997794.08', 7, 8],
               ((None, 'vip'), (None, 'vip')): ['1500408589.73', 8, 1],
               (('2/3', 'unknown'), ('2/3', 'unknown')): ['1501101571.17', 1, 5],
               ((None,'rorb'), (None,'rorb')): ['1502301827.80', 6, 8],
               ((None,'ntsr1'), (None,'ntsr1')): ['1504737622.52', 8, 2],
               ((None,'slc17a8'), (None,'slc17a8')): ['1495833911.11', 1, 8],
               (('2', 'unknown'), ('2', 'unknown')): ['1504052194.49', 1, 5],
               (('3', 'unknown'), ('3', 'unknown')): ['1503372117.27', 6, 4],
               (('4', 'unknown'), ('4', 'unknown')): ['1497585824.83', 6, 8],
               (('5', 'unknown'), ('5', 'unknown')): ['1503376975.16', 2, 4]}

human_connections = OrderedDict([((('2', 'unknown'), ('2', 'unknown')), ['1504052194.49', 1, 5]),
                                 ((('3', 'unknown'), ('3', 'unknown')), ['1503372117.27', 6, 4]),
                                 ((('4', 'unknown'), ('4', 'unknown')), ['1497585824.83', 6, 8]),
                                 ((('5', 'unknown'), ('5', 'unknown')), ['1512513429.49', 8, 1])])

ee_connections = OrderedDict([((('2/3', 'unknown'), ('2/3', 'unknown')), ['1501101571.17', 1, 5]),
                              (((None,'rorb'), (None,'rorb')), ['1502301827.80', 6, 8]),
                              (((None,'sim1'), (None,'sim1')), ['1490642434.41', 3, 5]),
                              (((None,'tlx3'), (None,'tlx3')), ['1492545925.15', 8, 5]),
                              #(((None,'slc17a8'), (None,'slc17a8')), ['1495833911.11', 1, 8]),
                              (((None,'ntsr1'), (None,'ntsr1')), ['1504737622.52', 8, 2])])
ii_connections = {((None, 'pvalb'), (None, 'pvalb')): ['1491597493.27', 2, 6],
                  ((None, 'pvalb'), (None, 'sst')): ['1493765516.34', 8, 3],
                  ((None, 'pvalb'), (None, 'vip')): ['1487796524.54', 3, 6],
                  ((None, 'sst'), (None, 'pvalb')): ['1493765516.34', 3, 8],
                  ((None, 'sst'), (None, 'sst')): ['1493765516.34', 2, 3],
                  ((None, 'sst'), (None, 'vip')): ['1494632512.34', 5, 4],
                  ((None, 'vip'), (None, 'sst')): ['1490997794.08', 7, 8],
                  ((None, 'vip'), (None, 'vip')): ['1500408589.73', 8, 1],
                  }

ei_connections = {((None, 'sim1'), (None, 'pvalb')): ['1495574744.01', 8, 4],
                  ((None, 'tlx3'), (None, 'pvalb')): ['1496699390.01', 8, 2],
                  ((None, 'tlx3'), (None, 'sst')): ['1497653267.74', 3, 4],
                  }

ie_connections = {((None, 'pvalb'), (None, 'sim1')): ['1495574744.01', 4, 8],
                  ((None, 'pvalb'), (None, 'tlx3')): ['1503953399.15', 2, 8],
                  ((None, 'sst'), (None, 'tlx3')): ['1504300627.31', 8, 2],
                  }

no_include = [['1513748435.90', 7, 5]]
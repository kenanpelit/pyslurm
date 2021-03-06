#!/usr/bin/env python

from __future__ import print_function

import pyslurm
import sys
from time import gmtime, strftime

steps = pyslurm.jobstep()
a = steps.get()
if a:
    for job, job_step in sorted(a.iteritems()):


        print("Job: {0}".format(job))
        for step, step_data in sorted(job_step.iteritems()):

            print("\tStep: {0}".format(step))
            for step_item, item_data in sorted(step_data.iteritems()):

                if 'start_time' in step_item:
                    ddate = pyslurm.epoch2date(item_data)
                    print("\t\t{0:<15} : {1}".format(step_item, ddate))
                else:
                    print("\t\t{0:<15} : {1}".format(step_item, item_data))

            layout = steps.layout(job, step)
            print("\t\tLayout:")
            for name, value in sorted(layout.iteritems()):
                print("\t\t\t{0:<15} : {1}".format(name, value))

    print('{0:*^80}'.format(''))
else:
    print("No jobsteps found !")


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2021-03-15

@author: cook
"""
import numpy as np
import os

from lbl.core import base
from lbl.core import base_classes
from lbl.core import io
from lbl.instruments import select
from lbl.science import general

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'lbl_compile.py'
__STRNAME__ = 'LBL Compil'
__version__ = base.__version__
__date__ = base.__date__
__authors__ = base.__authors__
# get classes
InstrumentsList = select.InstrumentsList
InstrumentsType = select.InstrumentsType
ParamDict = base_classes.ParamDict
LblException = base_classes.LblException
log = base_classes.log
# add arguments (must be in parameters.py)
ARGS = [# core
        'INSTRUMENT', 'CONFIG_FILE',
        # directory
        'DATA_DIR', 'LBLRV_SUBDIR', 'LBLRDB_SUBDIR',
        # science
        'OBJECT_SCIENCE', 'OBJECT_TEMPLATE',
        # plotting
        'PLOT',
        # other
        'SKIP_DONE', 'RDB_SUFFIX'
        ]
# TODO: Etienne - Fill out
DESCRIPTION = 'Use this code to compile the LBL rdb file'


# =============================================================================
# Define functions
# =============================================================================
def main(**kwargs):
    """
    Wrapper around __main__ recipe code (deals with errors and loads instrument
    profile)

    :param kwargs: kwargs to parse to instrument - anything in params can be
                   parsed (overwrites instrumental and default parameters)
    :return:
    """
    # deal with parsing arguments
    args = select.parse_args(ARGS, kwargs, DESCRIPTION)
    # load instrument
    inst = select.load_instrument(args)
    # print splash
    select.splash(name=__STRNAME__, instrument=inst.name)
    # run __main__
    try:
        return __main__(inst)
    except LblException as e:
        raise LblException(e.message)
    except Exception as e:
        emsg = 'Unexpected Error: {0}: {1}'
        eargs = [type(e), str(e)]
        raise LblException(emsg.format(*eargs))


def __main__(inst: InstrumentsType, **kwargs):
    """
    The main recipe function - all code dealing with recipe functionality
    should go here

    :param inst: Instrument instance
    :param kwargs: kwargs to parse to instrument (only use if inst is None)
                   anything in params can be parsed (overwrites instrumental
                   and default parameters)

    :return: all variables in local namespace
    """
    # -------------------------------------------------------------------------
    # deal with debug
    if inst is None or inst.params is None:
        # deal with parsing arguments
        args = select.parse_args(ARGS, kwargs, DESCRIPTION)
        # load instrument
        inst = select.load_instrument(args)
        # assert inst type
        amsg = 'inst must be a valid Instrument class'
        assert isinstance(inst, InstrumentsList), amsg
    # -------------------------------------------------------------------------
    # Step 1: Set up data directory
    # -------------------------------------------------------------------------
    # get data directory
    data_dir = inst.params['DATA_DIR']
    # make lblrv directory
    lblrv_dir = io.make_dir(data_dir, inst.params['LBLRV_SUBDIR'], 'LBL RV')
    # make lbl rdb directory
    lbl_rdb_dir = io.make_dir(data_dir, inst.params['LBLREFTAB_SUBDIR'],
                              'LBL rdb')
    # -------------------------------------------------------------------------
    # Step 2: set filenames
    # -------------------------------------------------------------------------
    # get all lblrv files for this object_science and object_template
    lblrv_files = inst.get_lblrv_files(lblrv_dir)
    # get rdb files for this object_science and object_template
    rdbfile1, rdbfile2 = inst.get_lblrdb_files(lbl_rdb_dir)

    # -------------------------------------------------------------------------
    # Step 3: Produce RDB file
    # -------------------------------------------------------------------------
    if os.path.exists(rdbfile1) and inst.params['SKIP_DONE']:
        # log file exists and we are skipping
        msg = 'File {0} exists, we will read it. To regenerate use --skip'
        margs = [rdbfile1]
        log.general(msg.format(*margs))
        # read the rdb file
        rdb_table = inst.load_lblrdb_file(rdbfile1)

    # else we generate the rdb file
    else:
        rdb_table = general.make_rdb_table(inst, rdbfile1, lblrv_files)

    # -------------------------------------------------------------------------
    # Step 4: Produce binned (per-epoch) RDB file
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Step 5: Produce drift file(s)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # return local namespace
    # -------------------------------------------------------------------------
    return locals()


# =============================================================================
# Start of code
# =============================================================================
if __name__ == "__main__":
    # print hello world
    ll = main()

# =============================================================================
# End of code
# =============================================================================

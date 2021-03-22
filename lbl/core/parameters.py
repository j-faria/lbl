#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Default parameters (non-instrument specific)

Created on 2021-03-15

@author: cook
"""
from lbl.core import base
from lbl.core import base_classes

# =============================================================================
# Define variables
# =============================================================================
__NAME__ = 'core.parameters.py'
__version__ = base.__version__
__date__ = base.__date__
__authors__ = base.__authors__
# set up parameter dictionary
params = base_classes.ParamDict()

# =============================================================================
# Define general parameters
# =============================================================================
# add default params - can be None
params.set(key='CONFIG_FILE', value=None, source=__NAME__,
           desc='Config file for user settings (absolute path)',
           arg='--config', dtype=str)

# add main data directory (structure assumed below)
params.set(key='DATA_DIR', value=None, source=__NAME__,
           desc='Main data directory (absolute path)',
           arg='--datadir', dtype=str, not_none=True)

# add masks sub directory (relative to data directory)
params.set(key='MASK_SUBDIR', value='masks', source=__NAME__,
           desc='mask sub directory (relative to data directory)',
           arg='--maskdir', dtype=str)

# add template sub directory (relative to data directory)
params.set(key='TEMPLATE_SUBDIR', value='templates', source=__NAME__,
           desc='template sub directory (relative to data directory)',
           arg='--templatedir', dtype=str)

# add calib sub directory (relative to data directory)
params.set(key='CALIB_SUBDIR', value='calib', source=__NAME__,
           desc='calib sub directory (relative to data directory)',
           arg='--calibdir', dtype=str)

# add science sub directory (relative to data directory)
params.set(key='SCIENCE_SUBDIR', value='science', source=__NAME__,
           desc='science sub directory (relative to data directory)',
           arg='--scidir', dtype=str)

# add lblrv sub directory (relative to data directory)
params.set(key='LBLRV_SUBDIR', value='lblrv', source=__NAME__,
           desc='LBL RV sub directory (relative to data directory)',
           arg='--lblrvdir', dtype=str)

# add lblreftable sub directory (relative to data directory)
params.set(key='LBLREFTAB_SUBDIR', value='lblreftable', source=__NAME__,
           desc='LBL ref table sub directory (relative to data directory)',
           arg='--lblreftabdir', dtype=str)

# add lblrdb sub directory (relative to data directory)
params.set(key='LBLRDB_SUBDIR', value='lblrdb', source=__NAME__,
           desc='LBL RDB sub directory (relative to data directory)',
           arg='--lblrdbdir', dtype=str)

# add instrument
params.set(key='INSTRUMENT', value=None, source=__NAME__,
           desc='The instrument to use', options=base.INSTRUMENTS,
           arg='--instrument', dtype=str, not_none=True)

# Define whether to skip done files
params.set(key='SKIP_DONE', value=True, source=__NAME__,
           desc='Whether to skip done files',
           arg='--skip', dtype=bool, options=[True, False])

# =============================================================================
# Define common parameters (between compute / compil)
# =============================================================================
# The object name for the compute function
params.set(key='OBJECT_SCIENCE', value=None, source=__NAME__,
           desc='The object name for the compute function',
           arg='--obj_sci', dtype=str, not_none=True)

# The object name to use for the template
params.set(key='OBJECT_TEMPLATE', value=None, source=__NAME__,
           desc='The object name to use for the template '
                '(If None set to OBJECT_SCIENCE)',
           arg='--obj_template', dtype=str)

# =============================================================================
# Define compute parameters
# =============================================================================
# Define blaze file - can be None
params.set(key='BLAZE_FILE', value=None, source=__NAME__,
           desc='Blaze file to use (must be present in the CALIB directory)',
           arg='--blaze', dtype=str)

# Template file to use (if not defined will try to find template for OBJECT)
#   - can be None
params.set(key='TEMPLATE_FILE', value=None, source=__NAME__,
           desc='Template file to use (if not defined will try to find'
                ' template for OBJECT_TEMPLATE) must be present in the'
                'TEMPLATES directory',
           arg='--template', dtype=str)

# define the input files
params.set(key='INPUT_FILE', value=None, source=__NAME__,
           desc='The input file expression to use (i.e. *e2dsff*AB.fits)',
           arg='--input_file', dtype=str,
           not_none=True)

# Define ref table format
params.set(key='REF_TABLE_FMT', value='csv', source=__NAME__,
           desc='Ref table format (i.e. csv)')

# define the High pass width [km/s]
params.set(key='HP_WIDTH', value=None, source=__NAME__,
           desc='The High pass width [km/s]', not_none=True)

# define the SNR cut off threshold
params.set(key='SNR_THRESHOLD', value=None, source=__NAME__,
           desc='The SNR cut off threshold', not_none=True)

# define switch whether to use noise model for RMS calculation
params.set(key='USE_NOISE_MODEL', value=False, source=__NAME__,
           desc='Switch whether to use noise model or not for the RMS '
                'calculation', options=[True, False])

# define the rough CCF rv minimum limit in m/s
params.set(key='ROUGH_CCF_MIN_RV', value=-3e5, source=__NAME__,
           desc='The rough CCF rv minimum limit in m/s')

# define the rough CCF rv maximum limit in m/s
params.set(key='ROUGH_CCF_MAX_RV', value=3e5, source=__NAME__,
           desc='The rough CCF rv maximum limit in m/s')

# define the rough CCF rv step in m/s
params.set(key='ROUGH_CCF_RV_STEP', value=500, source=__NAME__,
           desc='The rough CCF rv step in m/s')

# define the rough CCF ewidth guess for fit in m/s
params.set(key='ROUGH_CCF_EWIDTH_GUESS', value=2000, source=__NAME__,
           desc='The rough CCF ewidth guess for fit in m/s')

# define the number of iterations to do to converge during compute rv
params.set(key='COMPUTE_RV_N_ITERATIONS', value=10, source=__NAME__,
           desc='The number of iterations to do to converge during compute RV')

# define the plot order for compute rv model plot
params.set(key='COMPUTE_MODEL_PLOT_ORDERS', value=None, source=__NAME__,
           desc='The plot orders for compute rv model plot', not_none=True)

# define the minimum line width (in pixels) to consider line valid
params.set(key='COMPUTE_LINE_MIN_PIX_WIDTH', value=5, source=__NAME__,
           desc='The minimum line width (in pixels) to consider line valid')

# define the threshold in sigma on nsig (dv / dvrms) to keep valid
params.set(key='COMPUTE_LINE_NSIG_THRES', value=8, source=__NAME__,
           desc='The threshold in sigma on nsig (dv / dvrms) to keep valid')

# define the fraction of the bulk error the rv mean must be above for compute
#   rv to have converged
params.set(key='COMPUTE_RV_BULK_ERROR_CONVERGENCE', value=0.2, source=__NAME__,
           desc='fraction of the bulk error the rv mean must be above for '
                'compute rv to have converged')

# define the maximum number of iterations deemed to lead to a good RV
params.set(key='COMPUTE_RV_MAX_N_GOOD_ITERS', value=8, source=__NAME__,
           desc='The maximum number of iterations deemed to lead to a good RV')

# =============================================================================
# Define compil parameters
# =============================================================================
# define the suffix to give the rdb files
params.set(key='RDB_SUFFIX', value='', source=__NAME__,
           desc='The suffix to give the rdb files',
           arg='--subbfix_rdb', dtype=str)

# define the plot order for the compute rv model plot
params.set('COMPUTE_MODEL_PLOT_ORDERS', value=None, source=__NAME__,
           desc='define the plot order for the compute rv model plot'
                'this can be an integer of a list of integers')

# define the compil minimum wavelength allowed for lines [nm]
params.set('COMPIL_WAVE_MIN', None, source=__NAME__,
           desc='define the compil minimum wavelength allowed for lines [nm]',
           not_none=True)

# define the compil maximum wavelength allowed for lines [nm]
params.set('COMPIL_WAVE_MAX', None, source=__NAME__,
           desc='define the compil maximum wavelength allowed for lines [nm]',
           not_none=True)

# define the maximum pixel width allowed for lines [pixels]
params.set('COMPIL_MAX_PIXEL_WIDTH', None, source=__NAME__,
           desc='define the maximum pixel width allowed for lines [pixels]',
           not_none=True)

# =============================================================================
# Define plot parameters
# =============================================================================
# Define whether to do any plots
params.set(key='PLOT', value=False, source=__NAME__,
           desc='Whether to do plots for the compute function',
           arg='--plot', dtype=bool, options=[True, False])

# Define whether to do the compute ccf plot
params.set(key='PLOT_COMPUTE_CCF', value=False, source=__NAME__,
           desc='Whether to do the compute ccf plot',
           arg='--plotccf', dtype=bool, options=[True, False])

# Define whether to do the compute line plot
params.set(key='PLOT_COMPUTE_LINES', value=False, source=__NAME__,
           desc='Whether to do the compute line plot',
           arg='--plotline', dtype=bool, options=[True, False])

# Define whether to do the compil cumulative plot
params.set(key='PLOT_COMPIL_CUMUL', value=False, source=__NAME__,
           desc='Whether to do the compute ccf plot',
           arg='--plotcumul', dtype=bool, options=[True, False])




# =============================================================================
# Define header keys
# =============================================================================
# Wave coefficients header key
params.set(key='KW_WAVECOEFFS', value=None, source=__NAME__,
           desc='Wave coefficients header key', not_none=True)

# define wave num orders key in header
params.set(key='KW_WAVEORDN', value=None, source=__NAME__,
           desc='wave num orders key in header', not_none=True)

# define wave degree key in header
params.set(key='KW_WAVEDEGN', value=None, source=__NAME__,
           desc='wave degree key in header', not_none=True)

# define the key that gives the mid exposure time in MJD
params.set(key='KW_MID_EXP_TIME', value=None, source=__NAME__,
           desc='mid exposure time in MJD', not_none=True)

# define snr keyword
params.set(key='KW_SNR', value=None, source=__NAME__,
           desc='snr key in header', not_none=True)

# define the BERV keyword
params.set(key='KW_BERV', value=None, source=__NAME__,
           desc='the barycentric correction keyword', not_none=True)

# define the Blaze calibration file
params.set(key='KW_BLAZE_FILE', value=None, source=__NAME__,
           desc='The Blaze calibration file', not_none=True)

# define the number of iterations
params.set(key='KW_NITERATIONS', value='ITE_RV', source=__NAME__,
           desc='the number of iterations',
           comment='Num iterations to reach sigma accuracy')

# define the systemic velocity in m/s
params.set(key='KW_SYSTEMIC_VELO', value='SYSTVELO', source=__NAME__,
           desc='the systemic velocity in m/s',
           comment='systemic velocity in m/s')

# define the rms to photon noise ratio
params.set(key='KW_RMS_RATIO', value='RMSRATIO', source=__NAME__,
           desc='the rms to photon noise ratio',
           comment='RMS vs photon noise')

# define the e-width of LBL CCF
params.set(key='KW_CCF_EW', value='CCF_EW', source=__NAME__,
           desc='the e-width of LBL CCF',
           comment='e-width of LBL CCF in m/s')

# define the high-pass LBL width [km/s]
params.set(key='KW_HP_WIDTH', value='HP_WIDTH', source=__NAME__,
           desc='the high-pass LBL width [km/s]',
           comment='high-pass LBL width in km/s')

# define the LBL version
params.set(key='KW_VERSION', value='LBL_VERS', source=__NAME__,
           desc='the LBL version',
           comment='LBL code version')

# define the LBL date
params.set(key='KW_VDATE', value='LBLVDATE', source=__NAME__,
           desc='the LBL version',
           comment='LBL version date')

# define the process date
params.set(key='KW_PDATE', value='LBLPDATE', source=__NAME__,
           desc='the LBL processed date',
           comment='LBL processed date')

# define the lbl instrument was used
params.set(key='KW_INSTRUMENT', value='LBLINSTR', source=__NAME__,
           desc='the LBL processed date',
           comment='LBL instrument used')

# define the start time of the observation key
params.set(key='KW_MJDATE', value=None, source=__NAME__, not_none=False,
           desc='the start time of the observation')

# define the exposure time of the observation
params.set(key='KW_EXPTIME', value=None, source=__NAME__, not_none=False,
           desc='the exposure time of the observation')

# define the airmass of the observation
params.set(key='KW_AIRMASS', value=None, source=__NAME__, not_none=False,
           desc='the airmass of the observation')

# define the filename of the observation
params.set(key='KW_FILENAME', value=None, source=__NAME__, not_none=False,
           desc='the filename of the observation')

# define the human date of the observation
params.set(key='KW_DATE', value=None, source=__NAME__, not_none=False,
           desc='the human date of the observation')

# define the tau_h20 of the observation
params.set(key='KW_TAU_H2O', value=None, source=__NAME__, not_none=False,
           desc='the tau_h20 of the observation')

# define the tau_other of the observation
params.set(key='KW_TAU_OTHERS', value=None, source=__NAME__, not_none=False,
           desc='the tau_other of the observation')

# define the DPRTYPE of the observation
params.set(key='KW_DPRTYPE', value=None, source=__NAME__, not_none=False,
           desc='the DPRTYPE of the observation')

# define the observation time (mjd) of the wave solution
params.set(key='KW_WAVETIME', value=None, source=__NAME__, not_none=False,
           desc='the observation time (mjd) of the wave solution')

# define the filename of the wave solution
params.set(key='KW_WAVEFILE', value=None, source=__NAME__, not_none=False,
           desc='the filename of the wave solution')

# define the telluric preclean velocity of water absorbers
params.set(key='KW_TLPDVH2O', value=None, source=__NAME__, not_none=False,
           desc='the telluric preclean velocity of water absorbers')

# define the telluric preclean velocity of other absorbers
params.set(key='KW_TLPDVOTR', value=None, source=__NAME__, not_none=False,
           desc='the telluric preclean velocity of other absorbers')

# define the wave solution calibration filename
params.set(key='KW_CDBWAVE', value=None, source=__NAME__, not_none=False,
           desc='the wave solution used')

# define the original object name
params.set(key='KW_OBJNAME', value=None, source=__NAME__, not_none=False,
           desc='the original object name')

# define the rhomb 1 predefined position
params.set(key='KW_RHOMB1', value=None, source=__NAME__, not_none=False,
           desc='the rhomb 1 predefined position')

# define the rhomb 2 predefined position
params.set(key='KW_RHOMB2', value=None, source=__NAME__, not_none=False,
           desc='the rhomb 2 predefined position')

# define the calib-reference density
params.set(key='KW_CDEN_P', value=None, source=__NAME__, not_none=False,
           desc='the calib-reference density')

# define the SNR goal per pixel per frame
params.set(key='KW_SNRGOAL', value=None, source=__NAME__, not_none=False,
           desc='the SNR goal per pixel per frame')

# define the SNR in chosen order
params.set(key='KW_EXT_SNR', value=None, source=__NAME__, not_none=False,
           desc='the SNR in chosen order')

# define the barycentric julian date
params.set(key='KW_BJD', value=None, source=__NAME__, not_none=False,
           desc='The barycentric julian date')

# define the shape code dx value
params.set(key='KW_SHAPE_DX', value=None, source=__NAME__, not_none=False,
           desc='The shape code dx value')

# define the shape code dy value
params.set(key='KW_SHAPE_DY', value=None, source=__NAME__, not_none=False,
           desc='The shape code dy value')

# define the shape code A value
params.set(key='KW_SHAPE_A', value=None, source=__NAME__, not_none=False,
           desc='The shape code A value')

# define the shape code B value
params.set(key='KW_SHAPE_B', value=None, source=__NAME__, not_none=False,
           desc='The shape code B value')

# define the shape code C value
params.set(key='KW_SHAPE_C', value=None, source=__NAME__, not_none=False,
           desc='The shape code C value')

# define the shape code D value
params.set(key='KW_SHAPE_D', value=None, source=__NAME__, not_none=True,
           desc='The shape code D value')



# =============================================================================
# Start of code
# =============================================================================
if __name__ == "__main__":
    # print hello world
    print('Hello World')

# =============================================================================
# End of code
# =============================================================================

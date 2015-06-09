# Configuration file for ipcluster.

c = get_config()

#------------------------------------------------------------------------------
# IPClusterStart configuration
#------------------------------------------------------------------------------

# IPClusterStart will inherit config from: IPClusterEngines,
# BaseParallelApplication, BaseIPythonApplication, Application

# The class for launching a Controller. Change this value if you want your
# controller to also be launched by a batch system, such as PBS,SGE,MPI,etc.
#
# Each launcher class has its own set of configuration options, for making sure
# it will work in your environment.
#
# Note that using a batch launcher for the controller *does not* put it in the
# same batch job as the engines, so they will still start separately.
#
# IPython's bundled examples include:
#
#     Local : start engines locally as subprocesses
#     MPI : use mpiexec to launch the controller in an MPI universe
#     PBS : use PBS (qsub) to submit the controller to a batch queue
#     SGE : use SGE (qsub) to submit the controller to a batch queue
#     LSF : use LSF (bsub) to submit the controller to a batch queue
#     HTCondor : use HTCondor to submit the controller to a batch queue
#     SSH : use SSH to start the controller
#     WindowsHPC : use Windows HPC
#
# If you are using one of IPython's builtin launchers, you can specify just the
# prefix, e.g:
#
#     c.IPClusterStart.controller_launcher_class = 'SSH'
#
# or:
#
#     ipcluster start --controller=MPI
# c.IPClusterStart.controller_launcher_class = 'LocalControllerLauncher'

# The class for launching a set of Engines. Change this value to use various
# batch systems to launch your engines, such as PBS,SGE,MPI,etc. Each launcher
# class has its own set of configuration options, for making sure it will work
# in your environment.
#
# You can also write your own launcher, and specify it's absolute import path,
# as in 'mymodule.launcher.FTLEnginesLauncher`.
#
# IPython's bundled examples include:
#
#     Local : start engines locally as subprocesses [default]
#     MPI : use mpiexec to launch engines in an MPI environment
#     PBS : use PBS (qsub) to submit engines to a batch queue
#     SGE : use SGE (qsub) to submit engines to a batch queue
#     LSF : use LSF (bsub) to submit engines to a batch queue
#     SSH : use SSH to start the controller
#                 Note that SSH does *not* move the connection files
#                 around, so you will likely have to do this manually
#                 unless the machines are on a shared file system.
#     HTCondor : use HTCondor to submit engines to a batch queue
#     WindowsHPC : use Windows HPC
#
# If you are using one of IPython's builtin launchers, you can specify just the
# prefix, e.g:
#
#     c.IPClusterEngines.engine_launcher_class = 'SSH'
#
# or:
#
#     ipcluster start --engines=MPI
# c.IPClusterStart.engine_launcher_class = 'LocalEngineSetLauncher'

# String id to add to runtime files, to prevent name collisions when using
# multiple clusters with a single profile simultaneously.
#
# When set, files will be named like: 'ipcontroller-<cluster_id>-engine.json'
#
# Since this is text inserted into filenames, typical recommendations apply:
# Simple character strings are ideal, and spaces are not recommended (but should
# generally work).
# c.IPClusterStart.cluster_id = ''

# Deprecated, use controller_launcher_class
# c.IPClusterStart.controller_launcher = None

# The date format used by logging formatters for %(asctime)s
# c.IPClusterStart.log_datefmt = '%Y-%m-%d %H:%M:%S'

# Whether to overwrite existing config files when copying
# c.IPClusterStart.overwrite = False

# Set the log level by value or name.
# c.IPClusterStart.log_level = 30

# Set the working dir for the process.
# c.IPClusterStart.work_dir = u'/fusion/gpfs/home/scollis'

# Path to an extra config file to load.
#
# If specified, load this config file in addition to any other IPython config.
# c.IPClusterStart.extra_config_file = u''

# whether to create the profile_dir if it doesn't exist
# c.IPClusterStart.auto_create = True

# delay (in s) between starting the controller and the engines
# c.IPClusterStart.delay = 1.0

# The IPython profile to use.
# c.IPClusterStart.profile = u'default'

# The ZMQ URL of the iplogger to aggregate logging.
# c.IPClusterStart.log_url = ''

# whether to log to a file
# c.IPClusterStart.log_to_file = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.IPClusterStart.ipython_dir = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPClusterStart.copy_config_files = False

# Deprecated, use engine_launcher_class
# c.IPClusterStart.engine_launcher = None

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPClusterStart.verbose_crash = False

# Whether to reset config files as part of '--create'.
# c.IPClusterStart.reset = False

# The number of engines to start. The default is to use one for each CPU on your
# machine
# c.IPClusterStart.n = 16

# The timeout (in seconds)
# c.IPClusterStart.early_shutdown = 30

# whether to cleanup old logs before starting
# c.IPClusterStart.clean_logs = True

# Daemonize the ipcluster program. This implies --log-to-file. Not available on
# Windows.
# c.IPClusterStart.daemonize = False

# The Logging format template
# c.IPClusterStart.log_format = '[%(name)s]%(highlevel)s %(message)s'

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
#
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
#
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# IPClusterEngines configuration
#------------------------------------------------------------------------------

# IPClusterEngines will inherit config from: BaseParallelApplication,
# BaseIPythonApplication, Application

# The IPython profile to use.
# c.IPClusterEngines.profile = u'default'

# Path to an extra config file to load.
#
# If specified, load this config file in addition to any other IPython config.
# c.IPClusterEngines.extra_config_file = u''

# Set the log level by value or name.
# c.IPClusterEngines.log_level = 30

# Set the working dir for the process.
# c.IPClusterEngines.work_dir = u'/fusion/gpfs/home/scollis'

# whether to log to a file
# c.IPClusterEngines.log_to_file = False

# Daemonize the ipcluster program. This implies --log-to-file. Not available on
# Windows.
# c.IPClusterEngines.daemonize = False

# The ZMQ URL of the iplogger to aggregate logging.
# c.IPClusterEngines.log_url = ''

# The class for launching a set of Engines. Change this value to use various
# batch systems to launch your engines, such as PBS,SGE,MPI,etc. Each launcher
# class has its own set of configuration options, for making sure it will work
# in your environment.
#
# You can also write your own launcher, and specify it's absolute import path,
# as in 'mymodule.launcher.FTLEnginesLauncher`.
#
# IPython's bundled examples include:
#
#     Local : start engines locally as subprocesses [default]
#     MPI : use mpiexec to launch engines in an MPI environment
#     PBS : use PBS (qsub) to submit engines to a batch queue
#     SGE : use SGE (qsub) to submit engines to a batch queue
#     LSF : use LSF (bsub) to submit engines to a batch queue
#     SSH : use SSH to start the controller
#                 Note that SSH does *not* move the connection files
#                 around, so you will likely have to do this manually
#                 unless the machines are on a shared file system.
#     HTCondor : use HTCondor to submit engines to a batch queue
#     WindowsHPC : use Windows HPC
#
# If you are using one of IPython's builtin launchers, you can specify just the
# prefix, e.g:
#
#     c.IPClusterEngines.engine_launcher_class = 'SSH'
#
# or:
#
#     ipcluster start --engines=MPI
c.IPClusterEngines.engine_launcher_class = 'MPIEngineSetLauncher'

# Whether to create profile dir if it doesn't exist
# c.IPClusterEngines.auto_create = False

# The timeout (in seconds)
# c.IPClusterEngines.early_shutdown = 30

# whether to cleanup old logfiles before starting
# c.IPClusterEngines.clean_logs = False

# The number of engines to start. The default is to use one for each CPU on your
# machine
# c.IPClusterEngines.n = 16

# String id to add to runtime files, to prevent name collisions when using
# multiple clusters with a single profile simultaneously.
#
# When set, files will be named like: 'ipcontroller-<cluster_id>-engine.json'
#
# Since this is text inserted into filenames, typical recommendations apply:
# Simple character strings are ideal, and spaces are not recommended (but should
# generally work).
# c.IPClusterEngines.cluster_id = ''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPClusterEngines.copy_config_files = False

# The date format used by logging formatters for %(asctime)s
# c.IPClusterEngines.log_datefmt = '%Y-%m-%d %H:%M:%S'

# Deprecated, use engine_launcher_class
# c.IPClusterEngines.engine_launcher = None

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPClusterEngines.verbose_crash = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.IPClusterEngines.ipython_dir = u''

# The Logging format template
# c.IPClusterEngines.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Whether to overwrite existing config files when copying
# c.IPClusterEngines.overwrite = False

#------------------------------------------------------------------------------
# LocalControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller as a regular external process.

# command-line args to pass to ipcontroller
# c.LocalControllerLauncher.controller_args = ['--log-to-file', '--log-level=20']

# Popen command to launch ipcontroller.
# c.LocalControllerLauncher.controller_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.controller']

#------------------------------------------------------------------------------
# LocalEngineLauncher configuration
#------------------------------------------------------------------------------

# Launch a single engine as a regular externall process.

# command-line arguments to pass to ipengine
# c.LocalEngineLauncher.engine_args = ['--log-to-file', '--log-level=20']

# command to launch the Engine.
# c.LocalEngineLauncher.engine_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.engine']

#------------------------------------------------------------------------------
# LocalEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch a set of engines as regular external processes.

# LocalEngineSetLauncher will inherit config from: LocalEngineLauncher

# delay (in seconds) between starting each engine after the first. This can help
# force the engines to get their ids in order, or limit process flood when
# starting many engines.
# c.LocalEngineSetLauncher.delay = 0.1

# command-line arguments to pass to ipengine
# c.LocalEngineSetLauncher.engine_args = ['--log-to-file', '--log-level=20']

# command to launch the Engine.
# c.LocalEngineSetLauncher.engine_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.engine']

#------------------------------------------------------------------------------
# MPILauncher configuration
#------------------------------------------------------------------------------

# Launch an external process using mpiexec.

# The command line arguments to pass to mpiexec.
# c.MPILauncher.mpi_args = []

# The mpiexec command to use in starting the process.
# c.MPILauncher.mpi_cmd = ['mpiexec']

#------------------------------------------------------------------------------
# MPIControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller using mpiexec.

# MPIControllerLauncher will inherit config from: MPILauncher

# The command line arguments to pass to mpiexec.
# c.MPIControllerLauncher.mpi_args = []

# The mpiexec command to use in starting the process.
# c.MPIControllerLauncher.mpi_cmd = ['mpiexec']

# command-line args to pass to ipcontroller
# c.MPIControllerLauncher.controller_args = ['--log-to-file', '--log-level=20']

# Popen command to launch ipcontroller.
# c.MPIControllerLauncher.controller_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.controller']

#------------------------------------------------------------------------------
# MPIEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch engines using mpiexec

# MPIEngineSetLauncher will inherit config from: MPILauncher

# The command line arguments to pass to mpiexec.
# c.MPIEngineSetLauncher.mpi_args = []

# The mpiexec command to use in starting the process.
# c.MPIEngineSetLauncher.mpi_cmd = ['mpiexec']

# command-line arguments to pass to ipengine
# c.MPIEngineSetLauncher.engine_args = ['--log-to-file', '--log-level=20']

# command to launch the Engine.
# c.MPIEngineSetLauncher.engine_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.engine']

#------------------------------------------------------------------------------
# SSHLauncher configuration
#------------------------------------------------------------------------------

# A minimal launcher for ssh.
#
# To be useful this will probably have to be extended to use the ``sshx`` idea
# for environment variables.  There could be other things this needs as well.

# hostname on which to launch the program
# c.SSHLauncher.hostname = ''

# command for starting ssh
# c.SSHLauncher.ssh_cmd = ['ssh']

# user@hostname location for ssh in one setting
# c.SSHLauncher.location = ''

# List of (local, remote) files to send before starting
# c.SSHLauncher.to_send = []

# command for sending files
# c.SSHLauncher.scp_cmd = ['scp']

# List of (remote, local) files to fetch after starting
# c.SSHLauncher.to_fetch = []

# args to pass to ssh
# c.SSHLauncher.ssh_args = ['-tt']

# username for ssh
# c.SSHLauncher.user = ''

#------------------------------------------------------------------------------
# SSHControllerLauncher configuration
#------------------------------------------------------------------------------

# SSHControllerLauncher will inherit config from: SSHClusterLauncher,
# SSHLauncher

# hostname on which to launch the program
# c.SSHControllerLauncher.hostname = ''

# Popen command to launch ipcontroller.
# c.SSHControllerLauncher.controller_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.controller']

# command-line args to pass to ipcontroller
# c.SSHControllerLauncher.controller_args = ['--log-to-file', '--log-level=20']

# command for starting ssh
# c.SSHControllerLauncher.ssh_cmd = ['ssh']

# The remote profile_dir to use.
#
# If not specified, use calling profile, stripping out possible leading homedir.
# c.SSHControllerLauncher.remote_profile_dir = ''

# user@hostname location for ssh in one setting
# c.SSHControllerLauncher.location = ''

# List of (local, remote) files to send before starting
# c.SSHControllerLauncher.to_send = []

# command for sending files
# c.SSHControllerLauncher.scp_cmd = ['scp']

# List of (remote, local) files to fetch after starting
# c.SSHControllerLauncher.to_fetch = []

# args to pass to ssh
# c.SSHControllerLauncher.ssh_args = ['-tt']

# username for ssh
# c.SSHControllerLauncher.user = ''

#------------------------------------------------------------------------------
# SSHEngineLauncher configuration
#------------------------------------------------------------------------------

# SSHEngineLauncher will inherit config from: SSHClusterLauncher, SSHLauncher

# hostname on which to launch the program
# c.SSHEngineLauncher.hostname = ''

# command to launch the Engine.
# c.SSHEngineLauncher.engine_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.engine']

# command-line arguments to pass to ipengine
# c.SSHEngineLauncher.engine_args = ['--log-to-file', '--log-level=20']

# command for starting ssh
# c.SSHEngineLauncher.ssh_cmd = ['ssh']

# The remote profile_dir to use.
#
# If not specified, use calling profile, stripping out possible leading homedir.
# c.SSHEngineLauncher.remote_profile_dir = ''

# user@hostname location for ssh in one setting
# c.SSHEngineLauncher.location = ''

# List of (local, remote) files to send before starting
# c.SSHEngineLauncher.to_send = []

# command for sending files
# c.SSHEngineLauncher.scp_cmd = ['scp']

# List of (remote, local) files to fetch after starting
# c.SSHEngineLauncher.to_fetch = []

# args to pass to ssh
# c.SSHEngineLauncher.ssh_args = ['-tt']

# username for ssh
# c.SSHEngineLauncher.user = ''

#------------------------------------------------------------------------------
# SSHEngineSetLauncher configuration
#------------------------------------------------------------------------------

# SSHEngineSetLauncher will inherit config from: LocalEngineSetLauncher,
# LocalEngineLauncher

# delay (in seconds) between starting each engine after the first. This can help
# force the engines to get their ids in order, or limit process flood when
# starting many engines.
# c.SSHEngineSetLauncher.delay = 0.1

# command-line arguments to pass to ipengine
# c.SSHEngineSetLauncher.engine_args = ['--log-to-file', '--log-level=20']

# dict of engines to launch.  This is a dict by hostname of ints, corresponding
# to the number of engines to start on that host.
# c.SSHEngineSetLauncher.engines = {}

# command to launch the Engine.
# c.SSHEngineSetLauncher.engine_cmd = ['/homes/scollis/anaconda/bin/python', '-m', 'IPython.parallel.engine']

#------------------------------------------------------------------------------
# SSHProxyEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launcher for calling `ipcluster engines` on a remote machine.
#
# Requires that remote profile is already configured.

# SSHProxyEngineSetLauncher will inherit config from: SSHClusterLauncher,
# SSHLauncher

#
# c.SSHProxyEngineSetLauncher.ipcluster_cmd = ['ipcluster']

# hostname on which to launch the program
# c.SSHProxyEngineSetLauncher.hostname = ''

# command for starting ssh
# c.SSHProxyEngineSetLauncher.ssh_cmd = ['ssh']

# The remote profile_dir to use.
#
# If not specified, use calling profile, stripping out possible leading homedir.
# c.SSHProxyEngineSetLauncher.remote_profile_dir = ''

# user@hostname location for ssh in one setting
# c.SSHProxyEngineSetLauncher.location = ''

# List of (local, remote) files to send before starting
# c.SSHProxyEngineSetLauncher.to_send = []

# command for sending files
# c.SSHProxyEngineSetLauncher.scp_cmd = ['scp']

# List of (remote, local) files to fetch after starting
# c.SSHProxyEngineSetLauncher.to_fetch = []

# args to pass to ssh
# c.SSHProxyEngineSetLauncher.ssh_args = ['-tt']

# username for ssh
# c.SSHProxyEngineSetLauncher.user = ''

#------------------------------------------------------------------------------
# WindowsHPCLauncher configuration
#------------------------------------------------------------------------------

# A regular expression used to get the job id from the output of the
# submit_command.
# c.WindowsHPCLauncher.job_id_regexp = '\\d+'

# The filename of the instantiated job script.
# c.WindowsHPCLauncher.job_file_name = u'ipython_job.xml'

# The command for submitting jobs.
# c.WindowsHPCLauncher.job_cmd = 'job'

# The hostname of the scheduler to submit the job to.
# c.WindowsHPCLauncher.scheduler = ''

#------------------------------------------------------------------------------
# WindowsHPCControllerLauncher configuration
#------------------------------------------------------------------------------

# WindowsHPCControllerLauncher will inherit config from: WindowsHPCLauncher

# A regular expression used to get the job id from the output of the
# submit_command.
# c.WindowsHPCControllerLauncher.job_id_regexp = '\\d+'

# WinHPC xml job file.
# c.WindowsHPCControllerLauncher.job_file_name = u'ipcontroller_job.xml'

# The command for submitting jobs.
# c.WindowsHPCControllerLauncher.job_cmd = 'job'

# The hostname of the scheduler to submit the job to.
# c.WindowsHPCControllerLauncher.scheduler = ''

#------------------------------------------------------------------------------
# WindowsHPCEngineSetLauncher configuration
#------------------------------------------------------------------------------

# WindowsHPCEngineSetLauncher will inherit config from: WindowsHPCLauncher

# A regular expression used to get the job id from the output of the
# submit_command.
# c.WindowsHPCEngineSetLauncher.job_id_regexp = '\\d+'

# jobfile for ipengines job
# c.WindowsHPCEngineSetLauncher.job_file_name = u'ipengineset_job.xml'

# The command for submitting jobs.
# c.WindowsHPCEngineSetLauncher.job_cmd = 'job'

# The hostname of the scheduler to submit the job to.
# c.WindowsHPCEngineSetLauncher.scheduler = ''

#------------------------------------------------------------------------------
# PBSLauncher configuration
#------------------------------------------------------------------------------

# A BatchSystemLauncher subclass for PBS.

# PBSLauncher will inherit config from: BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.PBSLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.PBSLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.PBSLauncher.queue = u''

# The string that is the batch script template itself.
# c.PBSLauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.PBSLauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.PBSLauncher.delete_command = ['qdel']

# The filename of the instantiated batch script.
# c.PBSLauncher.batch_file_name = u'batch_script'

# The file that contains the batch template.
# c.PBSLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# PBSControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller using PBS.

# PBSControllerLauncher will inherit config from: PBSLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.PBSControllerLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.PBSControllerLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.PBSControllerLauncher.queue = u''

# The string that is the batch script template itself.
# c.PBSControllerLauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.PBSControllerLauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.PBSControllerLauncher.delete_command = ['qdel']

# batch file name for the controller job.
# c.PBSControllerLauncher.batch_file_name = u'pbs_controller'

# The file that contains the batch template.
# c.PBSControllerLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# PBSEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch Engines using PBS

# PBSEngineSetLauncher will inherit config from: PBSLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.PBSEngineSetLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.PBSEngineSetLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.PBSEngineSetLauncher.queue = u''

# The string that is the batch script template itself.
# c.PBSEngineSetLauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.PBSEngineSetLauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.PBSEngineSetLauncher.delete_command = ['qdel']

# batch file name for the engine(s) job.
# c.PBSEngineSetLauncher.batch_file_name = u'pbs_engines'

# The file that contains the batch template.
# c.PBSEngineSetLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# SGELauncher configuration
#------------------------------------------------------------------------------

# Sun GridEngine is a PBS clone with slightly different syntax

# SGELauncher will inherit config from: PBSLauncher, BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.SGELauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.SGELauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.SGELauncher.queue = u''

# The string that is the batch script template itself.
# c.SGELauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.SGELauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.SGELauncher.delete_command = ['qdel']

# The filename of the instantiated batch script.
# c.SGELauncher.batch_file_name = u'batch_script'

# The file that contains the batch template.
# c.SGELauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# SGEControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller using SGE.

# SGEControllerLauncher will inherit config from: SGELauncher, PBSLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.SGEControllerLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.SGEControllerLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.SGEControllerLauncher.queue = u''

# The string that is the batch script template itself.
# c.SGEControllerLauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.SGEControllerLauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.SGEControllerLauncher.delete_command = ['qdel']

# batch file name for the ipontroller job.
# c.SGEControllerLauncher.batch_file_name = u'sge_controller'

# The file that contains the batch template.
# c.SGEControllerLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# SGEEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch Engines with SGE

# SGEEngineSetLauncher will inherit config from: SGELauncher, PBSLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.SGEEngineSetLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.SGEEngineSetLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.SGEEngineSetLauncher.queue = u''

# The string that is the batch script template itself.
# c.SGEEngineSetLauncher.batch_template = ''

# The PBS submit command ['qsub']
# c.SGEEngineSetLauncher.submit_command = ['qsub']

# The PBS delete command ['qsub']
# c.SGEEngineSetLauncher.delete_command = ['qdel']

# batch file name for the engine(s) job.
# c.SGEEngineSetLauncher.batch_file_name = u'sge_engines'

# The file that contains the batch template.
# c.SGEEngineSetLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# LSFLauncher configuration
#------------------------------------------------------------------------------

# A BatchSystemLauncher subclass for LSF.

# LSFLauncher will inherit config from: BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.LSFLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.LSFLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.LSFLauncher.queue = u''

# The string that is the batch script template itself.
# c.LSFLauncher.batch_template = ''

# The PBS submit command ['bsub']
# c.LSFLauncher.submit_command = ['bsub']

# The PBS delete command ['bkill']
# c.LSFLauncher.delete_command = ['bkill']

# The filename of the instantiated batch script.
# c.LSFLauncher.batch_file_name = u'batch_script'

# The file that contains the batch template.
# c.LSFLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# LSFControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller using LSF.

# LSFControllerLauncher will inherit config from: LSFLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.LSFControllerLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.LSFControllerLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.LSFControllerLauncher.queue = u''

# The string that is the batch script template itself.
# c.LSFControllerLauncher.batch_template = ''

# The PBS submit command ['bsub']
# c.LSFControllerLauncher.submit_command = ['bsub']

# The PBS delete command ['bkill']
# c.LSFControllerLauncher.delete_command = ['bkill']

# batch file name for the controller job.
# c.LSFControllerLauncher.batch_file_name = u'lsf_controller'

# The file that contains the batch template.
# c.LSFControllerLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# LSFEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch Engines using LSF

# LSFEngineSetLauncher will inherit config from: LSFLauncher,
# BatchSystemLauncher

# Regular expresion for identifying the job ID [r'\d+']
# c.LSFEngineSetLauncher.job_id_regexp = '\\d+'

# The group we wish to match in job_id_regexp (0 to match all)
# c.LSFEngineSetLauncher.job_id_regexp_group = 0

# The PBS Queue.
# c.LSFEngineSetLauncher.queue = u''

# The string that is the batch script template itself.
# c.LSFEngineSetLauncher.batch_template = ''

# The PBS submit command ['bsub']
# c.LSFEngineSetLauncher.submit_command = ['bsub']

# The PBS delete command ['bkill']
# c.LSFEngineSetLauncher.delete_command = ['bkill']

# batch file name for the engine(s) job.
# c.LSFEngineSetLauncher.batch_file_name = u'lsf_engines'

# The file that contains the batch template.
# c.LSFEngineSetLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# HTCondorLauncher configuration
#------------------------------------------------------------------------------

# A BatchSystemLauncher subclass for HTCondor.
#
# HTCondor requires that we launch the ipengine/ipcontroller scripts rather that
# the python instance but otherwise is very similar to PBS.  This is because
# HTCondor destroys sys.executable when launching remote processes - a launched
# python process depends on sys.executable to effectively evaluate its module
# search paths. Without it, regardless of which python interpreter you launch
# you will get the to built in module search paths.
#
# We use the ip{cluster, engine, controller} scripts as our executable to
# circumvent  this - the mechanism of shebanged scripts means that the python
# binary will be  launched with argv[0] set to the *location of the ip{cluster,
# engine, controller}  scripts on the remote node*. This means you need to take
# care that:
#
# a. Your remote nodes have their paths configured correctly, with the ipengine and ipcontroller
#    of the python environment you wish to execute code in having top precedence.
# b. This functionality is untested on Windows.
#
# If you need different behavior, consider making you own template.

# HTCondorLauncher will inherit config from: BatchSystemLauncher

# Regular expression for identifying the job ID [r'(\d+)\.$']
# c.HTCondorLauncher.job_id_regexp = '(\\d+)\\.$'

# The group we wish to match in job_id_regexp [1]
# c.HTCondorLauncher.job_id_regexp_group = 1

# The PBS Queue.
# c.HTCondorLauncher.queue = u''

# The string that is the batch script template itself.
# c.HTCondorLauncher.batch_template = ''

# The HTCondor submit command ['condor_submit']
# c.HTCondorLauncher.submit_command = ['condor_submit']

# The HTCondor delete command ['condor_rm']
# c.HTCondorLauncher.delete_command = ['condor_rm']

# The filename of the instantiated batch script.
# c.HTCondorLauncher.batch_file_name = u'batch_script'

# The file that contains the batch template.
# c.HTCondorLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# HTCondorControllerLauncher configuration
#------------------------------------------------------------------------------

# Launch a controller using HTCondor.

# HTCondorControllerLauncher will inherit config from: HTCondorLauncher,
# BatchSystemLauncher

# Regular expression for identifying the job ID [r'(\d+)\.$']
# c.HTCondorControllerLauncher.job_id_regexp = '(\\d+)\\.$'

# The group we wish to match in job_id_regexp [1]
# c.HTCondorControllerLauncher.job_id_regexp_group = 1

# The PBS Queue.
# c.HTCondorControllerLauncher.queue = u''

# The string that is the batch script template itself.
# c.HTCondorControllerLauncher.batch_template = ''

# The HTCondor submit command ['condor_submit']
# c.HTCondorControllerLauncher.submit_command = ['condor_submit']

# The HTCondor delete command ['condor_rm']
# c.HTCondorControllerLauncher.delete_command = ['condor_rm']

# batch file name for the controller job.
# c.HTCondorControllerLauncher.batch_file_name = u'htcondor_controller'

# The file that contains the batch template.
# c.HTCondorControllerLauncher.batch_template_file = u''

#------------------------------------------------------------------------------
# HTCondorEngineSetLauncher configuration
#------------------------------------------------------------------------------

# Launch Engines using HTCondor

# HTCondorEngineSetLauncher will inherit config from: HTCondorLauncher,
# BatchSystemLauncher

# Regular expression for identifying the job ID [r'(\d+)\.$']
# c.HTCondorEngineSetLauncher.job_id_regexp = '(\\d+)\\.$'

# The group we wish to match in job_id_regexp [1]
# c.HTCondorEngineSetLauncher.job_id_regexp_group = 1

# The PBS Queue.
# c.HTCondorEngineSetLauncher.queue = u''

# The string that is the batch script template itself.
# c.HTCondorEngineSetLauncher.batch_template = ''

# The HTCondor submit command ['condor_submit']
# c.HTCondorEngineSetLauncher.submit_command = ['condor_submit']

# The HTCondor delete command ['condor_rm']
# c.HTCondorEngineSetLauncher.delete_command = ['condor_rm']

# batch file name for the engine(s) job.
# c.HTCondorEngineSetLauncher.batch_file_name = u'htcondor_engines'

# The file that contains the batch template.
# c.HTCondorEngineSetLauncher.batch_template_file = u''

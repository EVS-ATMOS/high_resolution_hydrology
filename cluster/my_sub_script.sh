#!/bin/bash
#PBS -l nodes=4:ppn=12
#PBS -l walltime=00:10:00
#PBS -j oe
#PBS -V
#PBS -N IPythonMPI0

ipcluster start --n=48 --profile=mpi0


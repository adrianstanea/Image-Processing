#!/bin/bash

# Define variables
INITIAL_PATH=$(pwd)
DATA_DIR=data
GH_REPO='https://github.com/xingchenzhang/MFIF'

if [ -d "$DATA_DIR" ]; then
    rm -rf $DATA_DIR
fi

mkdir $DATA_DIR
cd $DATA_DIR
git clone $GH_REPO
cd MFIF/input
mv * ../../
cd ../..
rm -rf MFIF

cd $INITIAL_PATH
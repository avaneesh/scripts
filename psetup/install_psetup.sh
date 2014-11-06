#!/bin/bash

PSETUP_DIR=~/psetup
SRC_PSETUP_DIR=.

USER_BIN_DIR=~/bin
SRC_BIN_DIR=~avkadam/bin

if [[ ! -d $PSETUP_DIR ]]; then
    mkdir $PSETUP_DIR
fi

cp $SRC_PSETUP_DIR/README* $PSETUP_DIR/. 

cp $SRC_PSETUP_DIR/psetuprc ~/.

if [[ ! -d $USER_BIN_DIR ]]; then
    mkdir $USER_BIN_DIR
fi

ln -sf $SRC_BIN_DIR/psetup $USER_BIN_DIR/psetup
ln -sf $SRC_BIN_DIR/psetup.bleeding $USER_BIN_DIR/psetup.bleeding
ln -sf $SRC_BIN_DIR/ptelnet $USER_BIN_DIR/ptelnet
ln -sf $SRC_BIN_DIR/pltelnet $USER_BIN_DIR/pltelnet

echo "=================="
echo "==> Congratulations!!! psetup is ready to use.. <=="
echo "==> Please ensure $USER_BIN_DIR is in your PATH <=="
echo "==> Go ahead and change ~/.psetuprc as per your choice <=="
echo "=================="

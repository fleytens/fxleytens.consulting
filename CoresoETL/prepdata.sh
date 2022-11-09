#!/usr/bin/bash

echo "Recolting raw UCTE data from AT, BE, CH, IT, NL, PT"

mkdir ./intl
mkdir ./lines
mkdir ./nodes
mkdir ./pst
mkdir ./regulators
mkdir ./transformers
mkdir ./ucte

cp ./UCT_Source/20221102_1230_FO3_AT0.uct ./ucte/at.UCT
cp ./UCT_Source/20221102_1230_FO3_BE1.uct ./ucte/be.UCT
cp ./UCT_Source/20221102_1230_FO3_CH0.UCT ./ucte/ch.UCT
cp ./UCT_Source/20221102_1230_FO3_IT1.uct ./ucte/it.UCT
cp ./UCT_Source/20221102_1230_FO3_NL1.uct ./ucte/nl.UCT
cp ./UCT_Source/20221102_1230_FO3_PT0.UCT ./ucte/pt.UCT


./extractUCTE-AT.py

echo "Austria done"

./extractUCTE-BE.py

echo "Belgium done"

./extractUCTE-CH.py

echo "Switzerland done"

./extractUCTE-IT.py

echo "Italy done"

./extractUCTE-PT.py

echo "Portugal done"

./extractUCTE-NL.py

echo "Netherland done "
echo "Process finished."
echo "-----------------"


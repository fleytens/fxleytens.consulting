#!/usr/bin/bash

echo "Recolting raw UCTE data from AT, BE, CH, IT, NL, PT"

cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_AT0.uct ./ucte/at.UCT
cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_BE1.uct ./ucte/be.UCT
cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_CH0.UCT ./ucte/ch.UCT
cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_IT1.uct ./ucte/it.UCT
cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_NL1.uct ./ucte/nl.UCT
cp /home/fxleytens/Downloads/Merging_DACF_20221102_1230/20221102_1230_FO3_PT0.UCT ./ucte/pt.UCT


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

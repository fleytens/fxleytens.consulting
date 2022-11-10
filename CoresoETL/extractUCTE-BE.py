#!/usr/bin/python3

# This script is to export all data in the Swiss UCTE file into different
# CSV file for better ETL and insertion into a database
#
# Writen by Francois X. LEYTENS
# Date : 2022/11/09

# Import various libraries 
# - CSV to export in comma delimited file
# - NUMPY to write an array directly into CSV
# - DATETIME to manipulate the string date

import csv
import numpy as np
from datetime import datetime


# Opening various file
#
# switzerland = Swiss UCTE file in read mode
# nodeFile = Extract of all nodes into a CSV file
# line file = extract of all lines into a CSV file
# and so on for transformes, regulators, phase shifter etc.
#
# The prginal UCTE file has been renamed into ch.UCT
# Path tp the file must be adapted

belgium = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/ucte/be.UCT', 'r')

nodeFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/nodes/nodebe.csv', 'w+')
write = csv.writer(nodeFile)
write.writerow(['date','country','node','geoNode','status','nodeType','voltage','activeLoad','reactiveLoad','activePowerMW','reactivePowerMVar','minGenMW','maxGenMWminGenVar','maxGenVar','primCtrl%','nomPowerPrimCtrlMW','shortCircuitPowerMVar','XR_Ratio','plantType'])

lineFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/lines/linebe.csv', 'w+')
write = csv.writer(lineFile)
write.writerow(['date','country','node1','node2','orderCode','status','resistR','reactX','susceptanceB','currentLimA','elementName'])

transformerFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/transformers/transformerbe.csv', 'w+')
write = csv.writer(transformerFile)
write.writerow(['date','country','node1','node2','orderCode','status','ratedVoltNRW','ratedVoltRW','nomPower','restR','reactX','susceptanceB','conductanceG','currentLimA','elementName'])

regulatorFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/regulators/regulatorbe.csv', 'w+')
write = csv.writer(regulatorFile)
write.writerow(['date','country','node1','node2','orderCode','phRegulU','phRegulN','phRegulNprime','U','angleRegulU','angleRegulD','angleRegulN','angleRegulNprime','angleRegulP','type'])

phaseshifterFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/pst/phaseshifterbe.csv', 'w+')
write = csv.writer(phaseshifterFile)
write.writerow(['date','country','node1','node2','orderCode','tapPos','resistR','reactX','deltaUtapN','phaseShiftAngle'])

exchangeFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/CoresoETL/intl/exchangebe.csv', 'w+')
write = csv.writer(exchangeFile)
write.writerow(['date','country','countryIso1','countryIso2','powerExchange','comments'])


# Create the Lines object of all lines in the file ch.UCT

Lines = belgium.readlines()


# Set some global variables
  
count = 0                   # line number
procDate = ""               # file processing date
country = "BE"                # Country of origin
nodeBloc = 10000            # Bloc of lines for Nodes
lineBloc = 10000            # Bloc of lines for Lines
transformerBloc = 100000    # Bloc of lines for Transformes
regulatorBloc = 100000      # Bloc of lines for Regulators
phaseshifterBloc=1000000    # Bloc of lines for Phase Shifter
exchangeBloc = 100000       # Bloc of lines for Exchange devices


# Reading of the object (ch.UCT) line by line

for line in Lines:
 
    node = []               # Create an empty array


# get the file processing date from the file data

    if(count == 0 ):
        procDate = datetime.strptime(line[4:14], '%Y.%m.%d').date()


# look for the Node bloc

    if(line[0:3] == '##N'):
        nodeBloc = count + 1


# look for the Lines bloc

    if(line[0:3] == '##L'):
        lineBloc = count


# look for the Transformer bloc

    if(line[0:3] == '##T'):
        # print(line[0:3] + " - " + str(count))
        transformerBloc = count


# Look for teh Regulator bloc

    if(line[0:3] == '##R'):
        regulatorBloc = count


# Look for the Phase Shifter bloc

    if(line[0:4] == '##TT'):
        # print(line[0:3] + " - " + str(count))
        phaseshifterBloc = count


# Look for the Exchange device bloc

    if(line[0:3] == '##E'):
        # print(line[0:3] + " - " + str(count))
        exchangeBloc = count


# Look for the Comment bloc (often the end of device bloc) and reset the bloc count

    if(line[0:3] == '##C'):
        # print(line[0:3] + " - " + str(count))
        nodeBloc = 100000
        lineBloc = 100000
        transformerBloc = 100000
        regulatorBloc = 100000
        phaseshifterBloc=1000000
        exchangeBloc = 1000000


# Set the XX country code (no idea why)

#   if(line[0:5] == '##ZXX'):
#        # print(line[0:5] + " - " + 'XX')
#        country = 'XX'


# Extract all delimited value from the UCT file to create an array for each Node

    if(count > nodeBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:8].strip())
        node.append(line[9:21].strip())
        node.append(line[22:23].strip())
        node.append(line[24:25].strip())
        node.append(line[26:32].strip())
        node.append(line[33:40].strip())
        node.append(line[41:48].strip())
        node.append(line[49:56].strip())
        node.append(line[57:64].strip())
        node.append(line[65:72].strip())
        node.append(line[73:80].strip())
        node.append(line[81:88].strip())
        node.append(line[89:96].strip())
        node.append(line[96:102].strip())
        node.append(line[103:110].strip())
        node.append(line[111:118].strip())
        node.append(line[119:126].strip())
        node.append(line[127:128].strip())
            
        # Uncomment to print on the console the output (debugging)
        
        # print(node)

        # Writes the array to the file

        write = csv.writer(nodeFile)
        write.writerow(node)


# Extract all delimited value from the UCT file to create an array for each Lines

    if(count > lineBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:8].strip())
        node.append(line[9:17].strip())
        node.append(line[18:19].strip())
        node.append(line[20:21].strip())
        node.append(line[22:28].strip())
        node.append(line[29:35].strip())
        node.append(line[36:44].strip())
        node.append(line[45:51].strip())
        node.append(line[52:64].strip())

        # Uncomment to print on the console the output (debugging)

        # print(node)

        # Writes the array to the file

        write = csv.writer(lineFile)
        write.writerow(node)


# Extract all delimited value from the UCT file to create an array for each Transformers

    if(count > transformerBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:8].strip())
        node.append(line[9:17].strip())
        node.append(line[18:19].strip())
        node.append(line[20:21].strip())
        node.append(line[22:27].strip())
        node.append(line[28:33].strip())
        node.append(line[34:39].strip())
        node.append(line[40:46].strip())
        node.append(line[47:53].strip())
        node.append(line[54:62].strip())
        node.append(line[63:69].strip())
        node.append(line[70:76].strip())
        node.append(line[77:89].strip())

        # Uncomment to print on the console the output (debugging)

        # print(node)

        # Writes the array to the file

        write = csv.writer(transformerFile)
        write.writerow(node)


# Extract all delimited value from the UCT file to create an array for each Regulator

    if(count > regulatorBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:8].strip())
        node.append(line[9:17].strip())
        node.append(line[18:19].strip())
        node.append(line[20:25].strip())
        node.append(line[26:28].strip())
        node.append(line[29:32].strip())
        node.append(line[33:38].strip())
        node.append(line[39:44].strip())
        node.append(line[45:50].strip())
        node.append(line[51:53].strip())
        node.append(line[54:57].strip())
        node.append(line[58:63].strip())
        node.append(line[64:68].strip())

        # Uncomment to print on the console the output (debugging)

        # print(node)

        # Writes the array to the file

        write = csv.writer(regulatorFile)
        write.writerow(node)


# Extract all delimited value from the UCT file to create an array for each Phase Shifter

    if(count > phaseshifterBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:8].strip())
        node.append(line[9:17].strip())
        node.append(line[18:19].strip())
        node.append(line[22:25].strip())
        node.append(line[26:32].strip())
        node.append(line[33:39].strip())
        node.append(line[40:45].strip())
        node.append(line[46:51].strip())

        # Uncomment to print on the console the output (debugging)

        # print(node)

        # Writes the array to the file

        write = csv.writer(phaseshifterFile)
        write.writerow(node)


# Extract all delimited value from the UCT file to create an array for each Exchange Devices

    if(count > exchangeBloc):
        node.append(procDate)
        node.append(country)
        node.append(line[0:2].strip())
        node.append(line[3:5].strip())
        node.append(line[6:13].strip())
        node.append(line[14:26].strip())

        # Uncomment to print on the console the output (debugging)

        # print(node)

        # Writes the array to the file

        write = csv.writer(exchangeFile)
        write.writerow(node)

    count += 1



   
    

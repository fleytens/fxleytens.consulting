#!/usr/bin/python3

import csv
import numpy as np
from datetime import datetime
import os
import shutil
import time

startScript  = time.time()

# folder path
dir_path = r'/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCT_Source/'
processed_path = r'/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCT_Processed/'

nodeFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMnode.csv', 'a')
write = csv.writer(nodeFile)
# write.writerow(['date','country','node','geoNode','status','nodeType','voltage','activeLoad','reactiveLoad','activePowerMW','reactivePowerMVar','minGenMW','maxGenMWminGenVar','maxGenVar','primCtrl%','nomPowerPrimCtrlMW','shortCircuitPowerMVar','XR_Ratio','plantType'])

lineFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMline.csv', 'a')
write = csv.writer(lineFile)
# write.writerow(['date','country','node1','node2','orderCode','status','resistR','reactX','susceptanceB','currentLimA','elementName'])

transformerFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMtransformer.csv', 'a')
write = csv.writer(transformerFile)
# write.writerow(['date','country','node1','node2','orderCode','status','ratedVoltNRW','ratedVoltRW','nomPower','restR','reactX','susceptanceB','conductanceG','currentLimA','elementName'])

regulatorFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMregulator.csv', 'a')
write = csv.writer(regulatorFile)
# write.writerow(['date','country','node1','node2','orderCode','phRegulU','phRegulN','phRegulNprime','U','angleRegulU','angleRegulD','angleRegulN','angleRegulNprime','angleRegulP','type'])

phaseshifterFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMphaseshifter.csv', 'a')
write = csv.writer(phaseshifterFile)
# write.writerow(['date','country','node1','node2','orderCode','tapPos','resistR','reactX','deltaUtapN','phaseShiftAngle'])

exchangeFile = open('/home/fxleytens/GITPerso/fxleytens.consulting/myETL/UCTExtract/CGMexchange.csv', 'a')
write = csv.writer(exchangeFile)
# write.writerow(['date','country','countryIso1','countryIso2','powerExchange','comments'])

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)

for uctFile in res :
    country = ''
    nodeBlock = False
    lineBlock = False
    transformerBlock = False
    regulatorBlock = False
    phaseshifterBlock = False
    exchangeBlock = False

    num_lines = sum(1 for line in open(dir_path + uctFile))


    f = open(dir_path + uctFile, "r")

    

    for i in range(0,num_lines):
        uctLine=(f.readline())

        # if uctLine[0:3] == '##C' and uctLine[4:14] != '':
        #    procDate = datetime.strptime(uctLine[4:14], '%Y.%m.%d').date()
        procDate = '2022-11-30'

        if len(uctLine) == 0 :
            uctLine=(f.readline())
            nodeBlock = False
            lineBlock = False
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = False

        
        if uctLine[0:3] == '##C' :
            nodeBlock = False
            lineBlock = False
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = False

        if uctLine[0:3] == '##N' :
            nodeBlock = True
            lineBlock = False
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = False
            uctLine=(f.readline())
            country = uctLine[3:5]
            uctLine=(f.readline())

        # if uctLine[0:5] == '##ZXX' :
        #     country = uctLine[3:5]
        #     uctLine=(f.readline())
        
        if nodeBlock == True :
            
            node = []
            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:8].strip())
            node.append(uctLine[9:21].strip())
            node.append(uctLine[22:23].strip())
            node.append(uctLine[24:25].strip())
            node.append(uctLine[26:32].strip())
            node.append(uctLine[33:40].strip())
            node.append(uctLine[41:48].strip())
            node.append(uctLine[49:56].strip())
            node.append(uctLine[57:64].strip())
            node.append(uctLine[65:72].strip())
            node.append(uctLine[73:80].strip())
            node.append(uctLine[81:88].strip())
            node.append(uctLine[89:96].strip())
            node.append(uctLine[96:102].strip())
            node.append(uctLine[103:110].strip())
            node.append(uctLine[111:118].strip())
            node.append(uctLine[119:126].strip())
            node.append(uctLine[127:128].strip())

            if node[3] != '':
                print(node)

                write = csv.writer(nodeFile)
                write.writerow(node)

        
        if uctLine[0:3] == '##L' :
            nodeBlock = False
            lineBlock = True
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = False
            uctLine=(f.readline())
        
        if lineBlock == True:

            node = []


            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:8].strip())
            node.append(uctLine[9:17].strip())
            node.append(uctLine[18:19].strip())
            node.append(uctLine[20:21].strip())
            node.append(uctLine[22:28].strip())
            node.append(uctLine[29:35].strip())
            node.append(uctLine[36:44].strip())
            node.append(uctLine[45:51].strip())
            node.append(uctLine[52:64].strip())

            if node[3] != '':
                print(node)

                write = csv.writer(lineFile)
                write.writerow(node)

        if uctLine[0:3] == '##T' and len(uctLine) == 4 :
            nodeBlock = False
            lineBlock = False
            transformerBlock = True
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = False
            uctLine=(f.readline())

        if transformerBlock == True :

            node = []

            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:8].strip())
            node.append(uctLine[9:17].strip())
            node.append(uctLine[18:19].strip())
            node.append(uctLine[20:21].strip())
            node.append(uctLine[22:27].strip())
            node.append(uctLine[28:33].strip())
            node.append(uctLine[34:39].strip())
            node.append(uctLine[40:46].strip())
            node.append(uctLine[47:53].strip())
            node.append(uctLine[54:62].strip())
            node.append(uctLine[63:69].strip())
            node.append(uctLine[70:76].strip())
            node.append(uctLine[77:89].strip())

            if node[3] != '':
                print(node)

                write = csv.writer(transformerFile)
                write.writerow(node)

        if uctLine[0:3] == '##R'  :
            nodeBlock = False
            lineBlock = False
            transformerBlock = False
            regulatorBlock = True
            phaseshifterBlock = False
            exchangeBlock = False
            uctLine=(f.readline())

        if regulatorBlock == True :

            node = []

            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:8].strip())
            node.append(uctLine[9:17].strip())
            node.append(uctLine[18:19].strip())
            node.append(uctLine[20:25].strip())
            node.append(uctLine[26:28].strip())
            node.append(uctLine[29:32].strip())
            node.append(uctLine[33:38].strip())
            node.append(uctLine[39:44].strip())
            node.append(uctLine[45:50].strip())
            node.append(uctLine[51:53].strip())
            node.append(uctLine[54:57].strip())
            node.append(uctLine[58:63].strip())
            node.append(uctLine[64:68].strip())

            if node[3] != '':
                print(node)

                write = csv.writer(regulatorFile)
                write.writerow(node)


        if uctLine[0:4] == '##TT' :
            nodeBlock = False
            lineBlock = False
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = True
            exchangeBlock = False
            uctLine=(f.readline())

        if phaseshifterBlock == True :

            node = []

            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:8].strip())
            node.append(uctLine[9:17].strip())
            node.append(uctLine[18:19].strip())
            node.append(uctLine[22:25].strip())
            node.append(uctLine[26:32].strip())
            node.append(uctLine[33:39].strip())
            node.append(uctLine[40:45].strip())
            node.append(uctLine[46:51].strip())

            if node[3] != '':
                print(node)

                write = csv.writer(phaseshifterFile)
                write.writerow(node)

        if uctLine[0:3] == '##E' :
            nodeBlock = False
            lineBlock = False
            transformerBlock = False
            regulatorBlock = False
            phaseshifterBlock = False
            exchangeBlock = True
            uctLine=(f.readline())

        if exchangeBlock == True :

            node = []

            node.append(procDate)
            node.append(country)
            node.append(uctLine[0:2].strip())
            node.append(uctLine[3:5].strip())
            node.append(uctLine[6:13].strip())
            node.append(uctLine[14:26].strip())

            if node[3] != '':
            
                print(node)

                write = csv.writer(exchangeFile)
                write.writerow(node)

endScript = time.time()

#Subtract Start Time from The End Time
total_time = endScript - startScript
print("Total elapsed time = \n"+ str(total_time))





        






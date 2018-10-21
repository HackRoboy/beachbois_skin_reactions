import serial # if you have not already done so
import time


ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)



while(True):

    index_array = []
    for i in range(10000):
        f = open("index.txt", "r")
        line = f.readlines()
        if line != []:
            #print(line[0])
            index_array.append(line[0])


    index_array_status = True
    length_of_array = len(index_array)
    print("Lenth of array ", length_of_array)

    if length_of_array != 0:
        index_in_array = index_array[0]


        for j in range(length_of_array):
            if index_array[j] != index_in_array:
                index_array_status = False
                break

        if index_array_status == True:
            ser.write(bytes(index_array[0], 'utf-8'))
            print("values sent ",index_array[0])


    time.sleep(5)

    '''if line != []:
        index = line[0]

        bindex = bytes(index, 'utf-8')

        print(index)

        ser.write(bindex)
        time.sleep(2)

#    print("done")'''




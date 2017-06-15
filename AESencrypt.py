from BitVector import *#use BitVector class created by Avinash Kak (kak@purdue.edu) at https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html
from AESfunc import *

if len(sys.argv) is not 3:  # takes in two arguments for plaintext.txt and ciphertext.txt
    sys.exit("Error, script needs two command-line arguments. (Plaintext.txt File and Ciphertext.txt File)")

PassPhrase = "Thats my Kung Fu"#set static pass for now 16 char * 8 bits = 128 bits strength

# open message to encrypt
file = open(sys.argv[1], "r")
message = (file.read())
print("Inside your plaintext message is: %s" % message)
start = 0
end = 0
outputhex = ""
# add round key
for y in range(1, (len(message)//16)+1):  # loop to encrypt all parts of the message
    eightbit = message[start:end + 16]
    print("The round key string is : %s" % PassPhrase)
    print("The part of the message to be encrypted is : %s" % eightbit)
    bv1 = BitVector(textstring=eightbit)
    print("The plaintext message in hex is : %s" % bv1.get_bitvector_in_hex())
    bv2 = BitVector(textstring=PassPhrase)
    print("The password in hex/ roundkey one is : %s" % bv2.get_bitvector_in_hex())
    resultbv=bv1^bv2
    roundkey=findroundkey(bv2.get_bitvector_in_hex(),1)
    print("The round key one is : %s" % roundkey)
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The initial adding round key output is : %s" % myhexstring)

    for x in range(1, 10):  # loop through 9 rounds
        # sub byte
        print("Round: %i" % x)
        myhexstring = resultbv.get_bitvector_in_hex()

        temp2=subbyte(myhexstring)
        print("The subbyte output is: %s" % temp2)
        # shift rows

        temp3=shiftrow(temp2)


        print("The shiftrow output is: %s" % temp3)

        # mix column
        bv3 = BitVector(hexstring=temp3)

        bv01 = (bv3[0:8])
        bv23 = (bv3[8:16])
        bv45 = (bv3[16:24])
        bv67 = (bv3[24:32])
        bv89 = (bv3[32:40])
        bv1011 = (bv3[40:48])
        bv1213 = (bv3[48:56])
        bv1415 = (bv3[56:64])
        bv1617 = (bv3[64:72])
        bv1819 = (bv3[72:80])
        bv2021 = (bv3[80:88])
        bv2223 = (bv3[88:96])
        bv2425 = (bv3[96:104])
        bv2627 = (bv3[104:112])
        bv2829 = (bv3[112:120])
        bv3031 = (bv3[120:128])

        eightlim = BitVector(bitstring='100011011')
        one = BitVector(bitstring='0001')
        two = BitVector(bitstring='0010')
        three = BitVector(bitstring='0011')

        tempbv1 = bv01.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv23.gf_multiply_modular(three, eightlim, 8)
        newbv01 = tempbv1 ^ tempbv2 ^ bv45 ^ bv67

        tempbv2 = bv23.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv45.gf_multiply_modular(three, eightlim, 8)
        newbv23 = bv01 ^ tempbv2 ^ tempbv3 ^ bv67

        tempbv3 = bv45.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(three, eightlim, 8)
        newbv45 = bv01 ^ bv23 ^ tempbv3 ^ tempbv4

        tempbv1 = bv01.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv67.gf_multiply_modular(two, eightlim, 8)
        newbv67 = tempbv1 ^ bv23 ^ bv45 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv1011.gf_multiply_modular(three, eightlim, 8)
        newbv89 = tempbv1 ^ tempbv2 ^ bv1213 ^ bv1415

        tempbv2 = bv1011.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv1213.gf_multiply_modular(three, eightlim, 8)
        newbv1011 = bv89 ^ tempbv2 ^ tempbv3 ^ bv1415

        tempbv3 = bv1213.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(three, eightlim, 8)
        newbv1213 = bv89 ^ bv1011 ^ tempbv3 ^ tempbv4

        tempbv1 = bv89.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv1415.gf_multiply_modular(two, eightlim, 8)
        newbv1415 = tempbv1 ^ bv1011 ^ bv1213 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv1819.gf_multiply_modular(three, eightlim, 8)
        newbv1617 = tempbv1 ^ tempbv2 ^ bv2021 ^ bv2223

        tempbv2 = bv1819.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv2021.gf_multiply_modular(three, eightlim, 8)
        newbv1819 = bv1617 ^ tempbv2 ^ tempbv3 ^ bv2223

        tempbv3 = bv2021.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(three, eightlim, 8)
        newbv2021 = bv1617 ^ bv1819 ^ tempbv3 ^ tempbv4

        tempbv1 = bv1617.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv2223.gf_multiply_modular(two, eightlim, 8)
        newbv2223 = tempbv1 ^ bv1819 ^ bv2021 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(two, eightlim, 8)
        tempbv2 = bv2627.gf_multiply_modular(three, eightlim, 8)
        newbv2425 = tempbv1 ^ tempbv2 ^ bv2829 ^ bv3031

        tempbv2 = bv2627.gf_multiply_modular(two, eightlim, 8)
        tempbv3 = bv2829.gf_multiply_modular(three, eightlim, 8)
        newbv2627 = bv2425 ^ tempbv2 ^ tempbv3 ^ bv3031

        tempbv3 = bv2829.gf_multiply_modular(two, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(three, eightlim, 8)
        newbv2829 = bv2425 ^ bv2627 ^ tempbv3 ^ tempbv4

        tempbv1 = bv2425.gf_multiply_modular(three, eightlim, 8)
        tempbv4 = bv3031.gf_multiply_modular(two, eightlim, 8)
        newbv3031 = tempbv1 ^ bv2627 ^ bv2829 ^ tempbv4

        newbv = newbv01 + newbv23 + newbv45 + newbv67 + newbv89 + newbv1011 + newbv1213 + newbv1415 + newbv1617 + newbv1819 + newbv2021 + newbv2223 + newbv2425 + newbv2627 + newbv2829 + newbv3031
        newbvashex = newbv.get_bitvector_in_hex()
        print("The Mixcolumn Output is: %s" % newbvashex)

        #add roundkey
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkey)
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()
        print("The output after adding the round key: %s" % myhexresult)
        roundkey=findroundkey(roundkey,x+1)
        print("The round key %i is " %(x+1) + roundkey)


        # sub byte round 10
    print("Round 10:")
    myhexstring = resultbv.get_bitvector_in_hex()

    loop = 0
    loop2 = 0
    temp2 = ""
    for loop in range(0, 16):
        temp = myhexstring[loop2:loop2 + 2]
        if temp == "00":
            temp = "63"
        elif temp == "01":
            temp = "7c"
        elif temp == "02":
            temp = "77"
        elif temp == "03":
            temp = "7b"
        elif temp == "04":
            temp = "f2"
        elif temp == "05":
            temp = "6b"
        elif temp == "06":
            temp = "6f"
        elif temp == "07":
            temp = "c5"
        elif temp == "08":
            temp = "30"
        elif temp == "09":
            temp = "01"
        elif temp == "0a":
            temp = "67"
        elif temp == "0b":
            temp = "2b"
        elif temp == "0c":
            temp = "fe"
        elif temp == "0d":
            temp = "d7"
        elif temp == "0e":
            temp = "ab"
        elif temp == "0f":
            temp = "76"

        elif temp == "10":
            temp = "ca"
        elif temp == "11":
            temp = "82"
        elif temp == "12":
            temp = "c9"
        elif temp == "13":
            temp = "7d"
        elif temp == "14":
            temp = "fa"
        elif temp == "15":
            temp = "59"
        elif temp == "16":
            temp = "47"
        elif temp == "17":
            temp = "f0"
        elif temp == "18":
            temp = "ad"
        elif temp == "19":
            temp = "d4"
        elif temp == "1a":
            temp = "a2"
        elif temp == "1b":
            temp = "af"
        elif temp == "1c":
            temp = "9c"
        elif temp == "1d":
            temp = "a4"
        elif temp == "1e":
            temp = "72"
        elif temp == "1f":
            temp = "c0"

        elif temp == "20":
            temp = "b7"
        elif temp == "21":
            temp = "fd"
        elif temp == "22":
            temp = "93"
        elif temp == "23":
            temp = "26"
        elif temp == "24":
            temp = "36"
        elif temp == "25":
            temp = "3f"
        elif temp == "26":
            temp = "f7"
        elif temp == "27":
            temp = "cc"
        elif temp == "28":
            temp = "34"
        elif temp == "29":
            temp = "a5"
        elif temp == "2a":
            temp = "e5"
        elif temp == "2b":
            temp = "f1"
        elif temp == "2c":
            temp = "71"
        elif temp == "2d":
            temp = "d8"
        elif temp == "2e":
            temp = "31"
        elif temp == "2f":
            temp = "15"

        elif temp == "30":
            temp = "04"
        elif temp == "31":
            temp = "c7"
        elif temp == "32":
            temp = "23"
        elif temp == "33":
            temp = "c3"
        elif temp == "34":
            temp = "18"
        elif temp == "35":
            temp = "96"
        elif temp == "36":
            temp = "05"
        elif temp == "37":
            temp = "9a"
        elif temp == "38":
            temp = "07"
        elif temp == "39":
            temp = "12"
        elif temp == "3a":
            temp = "80"
        elif temp == "3b":
            temp = "e2"
        elif temp == "3c":
            temp = "eb"
        elif temp == "3d":
            temp = "27"
        elif temp == "3e":
            temp = "b2"
        elif temp == "3f":
            temp = "75"

        elif temp == "40":
            temp = "09"
        elif temp == "41":
            temp = "83"
        elif temp == "42":
            temp = "2c"
        elif temp == "43":
            temp = "1a"
        elif temp == "44":
            temp = "1b"
        elif temp == "45":
            temp = "6e"
        elif temp == "46":
            temp = "5a"
        elif temp == "47":
            temp = "a0"
        elif temp == "48":
            temp = "52"
        elif temp == "49":
            temp = "3b"
        elif temp == "4a":
            temp = "d6"
        elif temp == "4b":
            temp = "b3"
        elif temp == "4c":
            temp = "29"
        elif temp == "4d":
            temp = "e3"
        elif temp == "4e":
            temp = "2f"
        elif temp == "4f":
            temp = "84"

        elif temp == "50":
            temp = "53"
        elif temp == "51":
            temp = "d1"
        elif temp == "52":
            temp = "00"
        elif temp == "53":
            temp = "ed"
        elif temp == "54":
            temp = "20"
        elif temp == "55":
            temp = "fc"
        elif temp == "56":
            temp = "b1"
        elif temp == "57":
            temp = "5b"
        elif temp == "58":
            temp = "6a"
        elif temp == "59":
            temp = "cb"
        elif temp == "5a":
            temp = "be"
        elif temp == "5b":
            temp = "39"
        elif temp == "5c":
            temp = "4a"
        elif temp == "5d":
            temp = "4c"
        elif temp == "5e":
            temp = "58"
        elif temp == "5f":
            temp = "cf"

        elif temp == "60":
            temp = "d0"
        elif temp == "61":
            temp = "ef"
        elif temp == "62":
            temp = "aa"
        elif temp == "63":
            temp = "fb"
        elif temp == "64":
            temp = "43"
        elif temp == "65":
            temp = "4d"
        elif temp == "66":
            temp = "33"
        elif temp == "67":
            temp = "85"
        elif temp == "68":
            temp = "45"
        elif temp == "69":
            temp = "f9"
        elif temp == "6a":
            temp = "02"
        elif temp == "6b":
            temp = "7f"
        elif temp == "6c":
            temp = "50"
        elif temp == "6d":
            temp = "3c"
        elif temp == "6e":
            temp = "9f"
        elif temp == "6f":
            temp = "a8"

        elif temp == "70":
            temp = "51"
        elif temp == "71":
            temp = "a3"
        elif temp == "72":
            temp = "40"
        elif temp == "73":
            temp = "8f"
        elif temp == "74":
            temp = "92"
        elif temp == "75":
            temp = "9d"
        elif temp == "76":
            temp = "38"
        elif temp == "77":
            temp = "f5"
        elif temp == "78":
            temp = "bc"
        elif temp == "79":
            temp = "b6"
        elif temp == "7a":
            temp = "da"
        elif temp == "7b":
            temp = "21"
        elif temp == "7c":
            temp = "10"
        elif temp == "7d":
            temp = "ff"
        elif temp == "7e":
            temp = "f3"
        elif temp == "7f":
            temp = "d2"

        elif temp == "80":
            temp = "cd"
        elif temp == "81":
            temp = "0c"
        elif temp == "82":
            temp = "13"
        elif temp == "83":
            temp = "ec"
        elif temp == "84":
            temp = "5f"
        elif temp == "85":
            temp = "97"
        elif temp == "86":
            temp = "44"
        elif temp == "87":
            temp = "17"
        elif temp == "88":
            temp = "c4"
        elif temp == "89":
            temp = "a7"
        elif temp == "8a":
            temp = "7e"
        elif temp == "8b":
            temp = "3d"
        elif temp == "8c":
            temp = "64"
        elif temp == "8d":
            temp = "5d"
        elif temp == "8e":
            temp = "19"
        elif temp == "8f":
            temp = "73"

        elif temp == "90":
            temp = "60"
        elif temp == "91":
            temp = "81"
        elif temp == "92":
            temp = "4f"
        elif temp == "93":
            temp = "dc"
        elif temp == "94":
            temp = "22"
        elif temp == "95":
            temp = "2a"
        elif temp == "96":
            temp = "90"
        elif temp == "97":
            temp = "88"
        elif temp == "98":
            temp = "46"
        elif temp == "99":
            temp = "ee"
        elif temp == "9a":
            temp = "b8"
        elif temp == "9b":
            temp = "14"
        elif temp == "9c":
            temp = "de"
        elif temp == "9d":
            temp = "5e"
        elif temp == "9e":
            temp = "0b"
        elif temp == "9f":
            temp = "db"

        elif temp == "a0":
            temp = "e0"
        elif temp == "a1":
            temp = "32"
        elif temp == "a2":
            temp = "3a"
        elif temp == "a3":
            temp = "0a"
        elif temp == "a4":
            temp = "49"
        elif temp == "a5":
            temp = "06"
        elif temp == "a6":
            temp = "24"
        elif temp == "a7":
            temp = "5c"
        elif temp == "a8":
            temp = "c2"
        elif temp == "a9":
            temp = "d3"
        elif temp == "aa":
            temp = "ac"
        elif temp == "ab":
            temp = "62"
        elif temp == "ac":
            temp = "91"
        elif temp == "ad":
            temp = "95"
        elif temp == "ae":
            temp = "e4"
        elif temp == "af":
            temp = "79"

        elif temp == "b0":
            temp = "e7"
        elif temp == "b1":
            temp = "c8"
        elif temp == "b2":
            temp = "37"
        elif temp == "b3":
            temp = "6d"
        elif temp == "b4":
            temp = "8d"
        elif temp == "b5":
            temp = "d5"
        elif temp == "b6":
            temp = "4e"
        elif temp == "b7":
            temp = "a9"
        elif temp == "b8":
            temp = "6c"
        elif temp == "b9":
            temp = "56"
        elif temp == "ba":
            temp = "f4"
        elif temp == "bb":
            temp = "ea"
        elif temp == "bc":
            temp = "65"
        elif temp == "bd":
            temp = "7a"
        elif temp == "be":
            temp = "ae"
        elif temp == "bf":
            temp = "08"

        elif temp == "c0":
            temp = "ba"
        elif temp == "c1":
            temp = "78"
        elif temp == "c2":
            temp = "25"
        elif temp == "c3":
            temp = "2e"
        elif temp == "c4":
            temp = "1c"
        elif temp == "c5":
            temp = "a6"
        elif temp == "c6":
            temp = "b4"
        elif temp == "c7":
            temp = "c6"
        elif temp == "c8":
            temp = "e8"
        elif temp == "c9":
            temp = "dd"
        elif temp == "ca":
            temp = "74"
        elif temp == "cb":
            temp = "1f"
        elif temp == "cc":
            temp = "4b"
        elif temp == "cd":
            temp = "bd"
        elif temp == "ce":
            temp = "8b"
        elif temp == "cf":
            temp = "8a"

        elif temp == "d0":
            temp = "70"
        elif temp == "d1":
            temp = "3e"
        elif temp == "d2":
            temp = "b5"
        elif temp == "d3":
            temp = "66"
        elif temp == "d4":
            temp = "48"
        elif temp == "d5":
            temp = "03"
        elif temp == "d6":
            temp = "f6"
        elif temp == "d7":
            temp = "0e"
        elif temp == "d8":
            temp = "61"
        elif temp == "d9":
            temp = "35"
        elif temp == "da":
            temp = "57"
        elif temp == "db":
            temp = "b9"
        elif temp == "dc":
            temp = "86"
        elif temp == "dd":
            temp = "c1"
        elif temp == "de":
            temp = "1d"
        elif temp == "df":
            temp = "9e"

        elif temp == "e0":
            temp = "e1"
        elif temp == "e1":
            temp = "f8"
        elif temp == "e2":
            temp = "98"
        elif temp == "e3":
            temp = "11"
        elif temp == "e4":
            temp = "69"
        elif temp == "e5":
            temp = "d9"
        elif temp == "e6":
            temp = "8e"
        elif temp == "e7":
            temp = "94"
        elif temp == "e8":
            temp = "9b"
        elif temp == "e9":
            temp = "1e"
        elif temp == "ea":
            temp = "87"
        elif temp == "eb":
            temp = "e9"
        elif temp == "ec":
            temp = "ce"
        elif temp == "ed":
            temp = "55"
        elif temp == "ee":
            temp = "28"
        elif temp == "ef":
            temp = "df"

        elif temp == "f0":
            temp = "8c"
        elif temp == "f1":
            temp = "a1"
        elif temp == "f2":
            temp = "89"
        elif temp == "f3":
            temp = "0d"
        elif temp == "f4":
            temp = "bf"
        elif temp == "f5":
            temp = "e6"
        elif temp == "f6":
            temp = "42"
        elif temp == "f7":
            temp = "68"
        elif temp == "f8":
            temp = "41"
        elif temp == "f9":
            temp = "99"
        elif temp == "fa":
            temp = "2d"
        elif temp == "fb":
            temp = "0f"
        elif temp == "fc":
            temp = "b0"
        elif temp == "fd":
            temp = "54"
        elif temp == "fe":
            temp = "bb"
        elif temp == "ff":
            temp = "16"

        loop2 = loop2 + 2
        temp2 = temp2 + temp
    print("The subbyte output of round 10 is: %s" % temp2)

    # shift rows
    shiftrow = temp2

    temp3 = temp2[0] + temp2[1]

    temp3 = temp3 + temp2[10]
    temp3 = temp3 + temp2[11]
    temp3 = temp3 + temp2[20]
    temp3 = temp3 + temp2[21]
    temp3 = temp3 + temp2[30]
    temp3 = temp3 + temp2[31]
    temp3 = temp3 + temp2[8]
    temp3 = temp3 + temp2[9]
    temp3 = temp3 + temp2[18]
    temp3 = temp3 + temp2[19]
    temp3 = temp3 + temp2[28]
    temp3 = temp3 + temp2[29]
    temp3 = temp3 + temp2[6]
    temp3 = temp3 + temp2[7]
    temp3 = temp3 + temp2[16]
    temp3 = temp3 + temp2[17]
    temp3 = temp3 + temp2[26]
    temp3 = temp3 + temp2[27]
    temp3 = temp3 + temp2[4]
    temp3 = temp3 + temp2[5]
    temp3 = temp3 + temp2[14]
    temp3 = temp3 + temp2[15]
    temp3 = temp3 + temp2[24]
    temp3 = temp3 + temp2[25]
    temp3 = temp3 + temp2[2]
    temp3 = temp3 + temp2[3]
    temp3 = temp3 + temp2[12]
    temp3 = temp3 + temp2[13]
    temp3 = temp3 + temp2[22]
    temp3 = temp3 + temp2[23]

    print("The output after shiftrow is: %s" % temp3)
    # addround key
    newbv = BitVector(hexstring=temp3)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkey)
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The output after adding the roundkey is: %s" % myhexstring)

    outputhextemp = resultbv.get_hex_string_from_bitvector()
    print("The outputhex value for this part of the message is: %s" % outputhextemp)
    outputhex = outputhex + outputhextemp
    start = start + 16
    end = end + 16

# output encrypted to file
print("The outputhex value for the entire message is: %s" % outputhex)
FILEOUT = open(sys.argv[2], 'w')
FILEOUT.write(outputhex)
FILEOUT.close()

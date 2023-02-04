import hashlib
import json
import os

# class ของ CommercialBuildingBlock ระบุรายละเอียดของอาคารพาณิชย์
class CommercialBuildingBlock:
    def __init__(
        self, blockID, owner, address, sub_district, district, province, title_deed_number, 
        land_size, floor_area, detail, year_built, prv_block_hash
    ) :
        self.blockID = blockID
        self.owner = owner
        self.address = address
        self.sub_district = sub_district
        self.district = district
        self.province = province
        self.title_deed_number = title_deed_number 
        self.land_size = land_size
        self.floor_area = floor_area
        self.detail = detail
        self.year_built = year_built
        self.prv_block_hash = prv_block_hash
        self.block_hash = self.hash()
        
    #hash of the block using SHA-256
    def hash(self): 
        sha = hashlib.sha256()
        sha.update(str(self.blockID).encode('utf-8') + 
                   str(self.owner).encode('utf-8') + 
                   str(self.address).encode('utf-8') + 
                   str(self.sub_district).encode('utf-8') + 
                   str(self.district).encode('utf-8') + 
                   str(self.province).encode('utf-8') + 
                   str(self.title_deed_number).encode('utf-8') + 
                   str(self.land_size).encode('utf-8') + 
                   str(self.floor_area).encode('utf-8') + 
                   str(self.detail).encode('utf-8') + 
                   str(self.year_built).encode('utf-8') + 
                   str(self.prv_block_hash).encode('utf-8'))
        return sha.hexdigest()

# บันทึกข้อมูลลง block
def record_data():
    inputOwner = input("ชื่อเจ้าของ/owner: ")
    inputProvince = input("จังหวัด/province: ")
    inputDistrict = input("อำเภอ/district: ")
    inputSubDistrict = input("ตำบล/sub district: ")
    inputAddress = input("บ้านเลขที่/address: ")
    inputTitleDeedNumber = input("เลขโฉนดที่ดิน/title deed number: ")
    inputLandSize = input("ขนาดที่ดิน/land size (km^2): ")
    inputFloorArea = input("พื้นที่ใช้สอย/floor area (km^2): ")
    inputDetail = input("ลักษณะอาคาร/detail: ")
    inputYearBuilt = input("ปีที่สร้างเสร็จ/year built: ")

    currentBlock = CommercialBuildingBlock(
        blockID, inputOwner, inputAddress, inputSubDistrict, inputDistrict, inputProvince, 
        inputTitleDeedNumber, inputLandSize, inputFloorArea, inputDetail, inputYearBuilt, prv_hash
    )
    j = open("data.json", "w")
    bid = "{\"blockID\": \"" + blockID + "\","
    pr = "\"prv_block_hash\": \"" + prv_hash + "\","
    bh = "\"block_hash\": \"" + currentBlock.block_hash + "\","
    ow = "\"owner\": \"" + inputOwner + "\","
    ad = "\"address\": \"" + inputAddress + "\","
    sd = "\"sub_district\": \"" + inputSubDistrict + "\","
    di = "\"district\": \"" + inputDistrict + "\","
    pv = "\"province\": \"" + inputProvince + "\","
    td = "\"title_deed_number\": \"" + inputTitleDeedNumber + "\","
    ls = "\"land_size\": \"" + inputLandSize + "\","
    fa = "\"floor_area\": \"" + inputFloorArea + "\","
    dt = "\"detail\": \"" + inputDetail + "\","
    yb = "\"year_built\": \"" + inputYearBuilt + "\"}"
    blockchain_data = json.loads(bid+pr+bh+ad+ow+sd+di+pv+td+ls+fa+dt+yb)
    jsonData.append(blockchain_data)
    json.dump(jsonData, j, sort_keys=False, indent=4)



# function สร้าง genesis_block
def genesis_block():
    inputOwner = input("ชื่อเจ้าของ/owner: ")
    inputProvince = input("จังหวัด/province: ")
    inputDistrict = input("อำเภอ/district: ")
    inputSubDistrict = input("ตำบล/sub district: ")
    inputAddress = input("บ้านเลขที่/address: ")
    inputTitleDeedNumber = input("เลขโฉนดที่ดิน/title deed number: ")
    inputLandSize = input("ขนาดที่ดิน/land size (km^2): ")
    inputFloorArea = input("พื้นที่ใช้สอย/floor area (km^2): ")
    inputDetail = input("ลักษณะอาคาร/detail: ")
    inputYearBuilt = input("ปีที่สร้างเสร็จ/year built: ")

    currentBlock = CommercialBuildingBlock(fID, inputOwner, inputAddress, inputSubDistrict, inputDistrict, inputProvince, 
        inputTitleDeedNumber, inputLandSize, inputFloorArea, inputDetail, inputYearBuilt, "Commercial Building")
    j = open("data.json", "w")
    blockchain_data = [currentBlock.__dict__]
    json.dump(blockchain_data, j, sort_keys=False, indent=4)

# function hash ข้อมูลทั้งหมดใน blockchain
def update_block_hash():
    for i in range(0, len(jsonData)-1):
        ID = "blockID"
        current_block = str(i)
        for item in jsonData:
            if ID in item and item[ID] == current_block:
                block_data = (
                    item["blockID"] + item["owner"] + item["address"] + item["sub_district"] +
                    item["district"] + item["province"] + item["title_deed_number"] + item["land_size"] +
                    item["floor_area"] + item["detail"] + item["year_built"] + item["prv_block_hash"]
                )
                item["block_hash"] = hashlib.sha256(block_data.encode()).hexdigest()
    with open('data.json', 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)
    return 

# function ยืนยันข้อมูลทั้งหมดใน blockchain
def data_verification():
    for i in range(0, len(jsonData)-1):
        current_block = jsonData[i]
        prevent_block = jsonData[i+1]
        if prevent_block["prv_block_hash"] != current_block["block_hash"]:
            print("\nInvalid!!!! blockID: " + current_block["blockID"])
            print("block_hash    (blockID "+current_block["blockID"]+ "): " + current_block["block_hash"])
            print("prevent_block (blockID "+prevent_block["blockID"]+ "): " + prevent_block["prv_block_hash0"])
            print("")
            return False
    return 

# ค้นหาข้อมูลอาคารพาณิชย์จากชื่อ
def find_building():
    name = input("owner name: ")
    value = "owner"
    for item in jsonData:
        if value in item and item[value] == name:
            print("\n"+name+"'s commercial building")
            print(f"BlockID: {item['blockID']}")
            print(f"Owned by: {item['owner']}")
            print(f"Address: {item['address']} {item['sub_district']} {item['district']} {item['province']}")
            print(f"Detail: {item['detail']}")
            print(f"Floor area: {item['floor_area']} km^2")
            print("")
    else:
        print("Can't find this person's commercial building.")

# main
# เช็ค block ใน json
if os.path.exists("data.json"): 
    with open("data.json", "r") as file:
        jsonData = json.load(file)
# ถ้าไม่มี block มาก่อนต้องเริ่มจากสร้าง genesis block
else:
    print("START CREATE FIRST THE BLOCK")
    prv_hash = "Commercial Building"
    fID = "0"
    genesis_block()
    with open("data.json", "r") as file:
        jsonData = json.load(file)

while True :
    for item in jsonData:
        prv_hash = item["block_hash"]
        blockID = str(int(item["blockID"]) + 1)
    update_block_hash()
    data_verification()

    print("Please select an item")
    print("press 1 to record Commercial Building.")
    print("press 2 to Find a commercial building owner.")
    print("press 0 to exit")
    x = input()
    if x == "1":
        record_data()
    elif x == "2":
        find_building()
    elif x == "0":
        print("finish")
        break

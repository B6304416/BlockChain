import hashlib
import json
import os

# class ของ CommercialBuildingBlock ระบุรายละเอียดของอาคารพาณิชย์
class CommercialBuildingBlock:
    def __init__(
        self, blockID, owner, house_number, village_number, sub_district, district, province, title_deed_number, 
        land_size, floor_area, detail, year_built, prv_block_hash
    ) :
        self.blockID = blockID
        self.owner = owner
        self.house_number = house_number
        self.village_number = village_number
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
                   str(self.house_number).encode('utf-8') + 
                   str(self.village_number).encode('utf-8') + 
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
    inputHouseNumber = input("บ้านเลขที่/house No.: ")
    inputVillageNumber = input("หมู่/village No.: ")
    inputSubDistrict = input("ตำบล/sub district: ")
    inputDistrict = input("อำเภอ/district: ")
    inputProvince = input("จังหวัด/province: ")
    inputTitleDeedNumber = input("เลขโฉนดที่ดิน/title deed number: ")
    inputLandSize = input("ขนาดที่ดิน/land size (km^2): ")
    inputFloorArea = input("พื้นที่ใช้สอย/floor area (km^2): ")
    inputDetail = input("ลักษณะอาคาร/detail: ")
    inputYearBuilt = input("ปีที่สร้างเสร็จ/year built: ")

    currentBlock = CommercialBuildingBlock(
        blockID, inputOwner, inputHouseNumber, inputVillageNumber, inputSubDistrict, inputDistrict, inputProvince, 
        inputTitleDeedNumber, inputLandSize, inputFloorArea, inputDetail, inputYearBuilt, prv_hash
    )
    j = open("data.json", "w")
    bid = "{\"blockID\": \"" + blockID + "\","
    pr = "\"prv_block_hash\": \"" + prv_hash + "\","
    bh = "\"block_hash\": \"" + currentBlock.block_hash + "\","
    ow = "\"owner\": \"" + inputOwner + "\","
    hn = "\"house_number\": \"" + inputHouseNumber + "\","
    vn = "\"village_number\": \"" + inputVillageNumber + "\","
    sd = "\"sub_district\": \"" + inputSubDistrict + "\","
    di = "\"district\": \"" + inputDistrict + "\","
    pv = "\"province\": \"" + inputProvince + "\","
    td = "\"title_deed_number\": \"" + inputTitleDeedNumber + "\","
    ls = "\"land_size\": \"" + inputLandSize + "\","
    fa = "\"floor_area\": \"" + inputFloorArea + "\","
    dt = "\"detail\": \"" + inputDetail + "\","
    yb = "\"year_built\": \"" + inputYearBuilt + "\"}"
    blockchain_data = json.loads(bid+pr+bh+ow+hn+vn+sd+di+pv+td+ls+fa+dt+yb)
    jsonData.append(blockchain_data)
    json.dump(jsonData, j, sort_keys=False, indent=4)


# function สร้าง genesis_block
def genesis_block():
    inputOwner = input("ชื่อเจ้าของ/owner: ")
    inputHouseNumber = input("บ้านเลขที่/house No.: ")
    inputVillageNumber = input("หมู่/village No.: ")
    inputSubDistrict = input("ตำบล/sub district: ")
    inputDistrict = input("อำเภอ/district: ")
    inputProvince = input("จังหวัด/province: ")
    inputTitleDeedNumber = input("เลขโฉนดที่ดิน/title deed number: ")
    inputLandSize = input("ขนาดที่ดิน/land size (km^2): ")
    inputFloorArea = input("พื้นที่ใช้สอย/floor area (km^2): ")
    inputDetail = input("ลักษณะอาคาร/detail: ")
    inputYearBuilt = input("ปีที่สร้างเสร็จ/year built: ")

    currentBlock = CommercialBuildingBlock(fID, inputOwner, inputHouseNumber, inputVillageNumber, inputSubDistrict, inputDistrict, 
        inputProvince, inputTitleDeedNumber, inputLandSize, inputFloorArea, inputDetail, inputYearBuilt, "Commercial Building")
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
                    item["blockID"] + item["owner"] + item["house_number"] + item["village_number"] + item["sub_district"] +
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
            print("prevent_block (blockID "+prevent_block["blockID"]+ "): " + prevent_block["prv_block_hash"])
            print("")
            return False
    return 

# ค้นหาข้อมูลอาคารพาณิชย์จากชื่อ
def find_building():
    name = input("owner name: ")
    found = False
    num = 1
    for item in jsonData:
        if item.get("owner") == name:
            latest = True
            for check in jsonData:
                if (item["house_number"] == check["house_number"] and
                    item["title_deed_number"] == check["title_deed_number"]):
                    if item["blockID"] < check["blockID"]:
                        latest = False
                        print(item["blockID"] +"<"+ check["blockID"])
                        break
            if latest:
                found = True
                print("")
                print(f"{num}. BlockID: {item['blockID']}")
                print(f"Owned by: {item['owner']}")
                print(f"Address: {item['house_number']} Moo.{item['village_number']}, {item['sub_district']}, {item['district']}, {item['province']}")
                print(f"Detail: {item['detail']}")
                print(f"Floor area: {item['floor_area']} km^2")
                print("")
                num += 1
    if not found:
        print("Can't find this person's commercial building.")
        print("")


# ค้นหาข้อมูลอาคารพาณิชย์จากชื่อ
def find_owner():
    house = input("House No.: ")
    deed = input("Title deed No.: ")
    valueh = "house_number"
    valued = "title_deed_number"
    found = False
    num = 1
    for item in jsonData:
        if item[valueh] == house and item[valued] == deed:
            print("")
            print(str(num)+". "+ f"BlockID: {item['blockID']}")
            print(f"Owned by: {item['owner']}")
            print("")
            found = True
            num += 1
    if not found:
        print("Can't find this person's commercial building.")
        print("")

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
    print("press 1 to record commercial building.")
    print("press 2 to Find a commercial building.")
    print("press 3 to Find a commercial building trading history.")
    print("press 0 to exit")
    x = input()
    if x == "1":
        record_data()
    elif x == "2":
        find_building()
    elif x == "3":
        find_owner()
    elif x == "0":
        print("finish")
        break

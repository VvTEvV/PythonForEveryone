product = {'ดินสอกดpentel':{'ราคา':50,'สี':'แดง'},
           'ยางลบ':{'ราคา':50,'สี':'เขียว'},
           'ดินสอสี':{'ราคา':30,'สี':'ส้ม'}}
while True:#ทำเพื่อเราสามารถทำซ้ำได้เรื่อยๆ
    print('------กรุณากรอกข้อมูลสินค้า------')
    p = input('ชื่อสินค้า: ')
    q = int(input('จำนวน: '))
    print('-------')
    if p in product:
        print(f'สินค้า: {p} \nราคา: {product[p]['ราคา']} บาท \nสี: {product[p]['สี']}')
        print(f'จำนวน: {q} ชิ้น \nรวมทั้งหมด: {product[p]['ราคา'] * q } บาท')
    else:
        print('ไม่มีสินค้าในระบบ')
    #ออกจาก loop โดยการกด ctrl = c (ตอนที่รัยแล้ว)
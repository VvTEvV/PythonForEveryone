#tile = 10
#row = 3 #3 ชิ้นต่อแถว

#total_row = tile // row
#remain_tile = tile%row
#print(total_row,remain_tile)
#buy_more = row - remain_tile
#print(f'ใช้กระเบื้องทั้งหมด: {total_row} แผ่น',f'เหลือเศษหระเบื้อง: {remain_tile} แผ่น',f'ต้องซื้อเพิ่ม : {buy_more} แผ่น')
#print('ต้องปูกระเบื้อง {} แถว'.format(total_row))
#ลูกค้าต้องซื้อกระเบื้องเพิ่มกี่แผ่น
cat_color = {'black':100, 'white': 200,'brown':90}
try:
    price_cat = int(input('ป้อนราคาแมว: '))
    my_monney = int(input('ป้อนจำนวนเงินที่มี: '))#ต้องแปลงข้อมูลจากข้อความเป็นตัวเลข
    color = input('แมวสีอะไร? [black/white/brown]: ')
except:
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น!')
    price_cat = int(input('ป้อนราคาแมว: '))
    my_monney = int(input('ป้อนจำนวนเงินที่มี: '))
    color = input('แมวสีอะไร? [black/white/brown]: ')
print('-----โปรแกรมคำนวนเงินทอน-------')
price_cat_addon = price_cat * cat_color[color]
number_cat = my_monney//price_cat_addon
cash_back = my_monney - (number_cat*price_cat_addon)

print(f'ซื้อแมวได้ทั้งหมด: {number_cat} ตัว')
print(f'ได้เงินทอน: {cash_back} บาท')



      
    

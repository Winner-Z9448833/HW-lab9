class Data:
    def __init__(self, data):
        self.data = data

    def show(self):
        return self.data

    def add(self, item):
        self.data.append(item)

class mySet(Data):
    def __init__(self, data):
        super().__init__(data)

    def show(self):
        new = []
        for i in super().show():
            if i not in new:
                new.append(i)
        return new

    def delete(self, d):
        new = self.data.copy()
        if d in new:
            while d in new:
                new.remove(d)
            self.data = new 
        else:
            print(f"\n[!] ไม่พบ '{d}' ใน mySet")

class myBag(Data):
    def __init__(self, data):
        super().__init__(data)

    def show(self):
        return super().show()

    def delete(self, d):
        new = self.data.copy()
        if d in new:
            new.remove(d)
            self.data = new 
        else:
            print(f"\n[!] ไม่พบ '{d}' ใน myBag")

class myQueue(Data):
    def __init__(self, data):
        super().__init__(data)

    def show(self):
        return super().show()

    def delete(self):
        new = self.data.copy()
        if len(new) > 0:
            removed = new.pop(0) 
            print(f"\n[Dequeue]: '{removed}' ออกจากคิวเรียบร้อย")
            self.data = new  # อัปเดตข้อมูลจริง
        else:
            print('\n[!] ไม่มีข้อมูลใน Queue')

dt = ['gay', 5, 23, 'ohio', 5, 'ohio']

s = mySet(dt)
b = myBag(dt)
Q = myQueue(dt)

while True:
    print("\n----------------------------------------")
    print(f'Data (Raw):\t{dt}')
    print(f'1) mySet:\t{s.show()}')
    print(f'2) myBag:\t{b.show()}')
    print(f'3) myQueue:\t{Q.show()}')

    try:
        q = int(input('\nwanna add or delete?\n1) add\n2) delete\n3) exit\nnumber: '))
    except ValueError:
        print('กรุณากรอกเฉพาะตัวเลข!')
        continue

    # 1. เพิ่มข้อมูล
    if q == 1:
        ad = input('add: ')
        try:
            ad = int(ad)
        except ValueError:
            pass
        s.add(ad)

    # 2. ลบข้อมูล
    elif q == 2:
        try:
            q2 = int(input('delete in?\n1) mySet\n2) myBag\n3) myQueue\nnumber: '))
        except ValueError:
            print('กรุณากรอกเฉพาะตัวเลข!')
            continue

        if q2 == 1:
            de = input('delete from Set: ')
            try:
                de = int(de)
            except ValueError:
                pass
            s.delete(de)

        elif q2 == 2:
            de = input('delete from Bag: ')
            try:
                de = int(de)
            except ValueError:
                pass
            b.delete(de)

        elif q2 == 3:
            Q.delete()

        else:
            print('ตัวเลือกไม่ถูกต้อง')

    # 3. ออกจากโปรแกรม
    elif q == 3:
        print('จบการทำงาน!')
        break

    else:
        print('ตัวเลือกไม่ถูกต้อง')
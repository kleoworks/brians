function SList() {

    this.head = null;
    this.removeBack = removeBack;

}

function Nodey(val) {

    this.val = val;
    this.next = null;

}

function removeBack() {

    obj = this.head;

    if (!obj.next) {

        this.head = null;
        return this;

    } else {

        while (true) {

            if (obj.next) {
                last = obj;
                obj = obj.next;
            } else {
                last.next = null;
                return this;
            }
        }
    }
}

list = new SList();
obj1 = new Nodey(1);
obj2 = new Nodey(2);
obj3 = new Nodey(3);

list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;

console.log(list.removeBack());

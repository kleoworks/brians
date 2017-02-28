function SList() {

    this.head = null;
    this.length = length;

}

function Obj(name) {

    this.name = name;
    this.next = null;
}

function length() {

    count = 0;
    obj = this.head;

    while(true) {

        if (obj) {
            count ++;
            obj = obj.next;

        } else {

            return count;

        }
    }
}


// test
list = new SList();
list2 = new SList();
obj1 = new Obj('billy bob');
obj2 = new Obj('jelly ray');
obj3 = new Obj('jordy porgy');
list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;

console.log(list.length());
console.log(list2.length());

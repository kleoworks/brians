function SList() {

    this.head = null;
    this.min = min;

}

function Nodey(val) {

    this.val = val;
    this.next = null;

}

function min() {

    var runner = this.head;
    var min = null;

    while (runner) {

        if (runner.val < min) {

            min = runner.val;

        }

        runner = runner.next;

    }

    return min;

}

// test
list = new SList();
obj1 = new Nodey(1);
obj2 = new Nodey(1);
obj3 = new Nodey(100);
obj4 = new Nodey(10);
obj5 = new Nodey(-1);
obj6 = new Nodey(0);
list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;
obj3.next = obj4;
obj4.next = obj5;
obj5.next = obj6;
console.log(list.min());

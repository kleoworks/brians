function SList() {

    this.head = null;
    this.back = back;

}

function Nodey(val) {

    this.val = val;
    this.next = null;

}

function back() {

    runner = this.head;

    if (runner) {

        while (runner.next) {

            runner = runner.next;

        }

    }

    return runner;

}


//tests

list = new SList();
obj1 = new Nodey(1);
obj2 = new Nodey(2);
obj3 = new Nodey(3);
obj4 = new Nodey(4);
list.head = obj1;
// obj1.next = obj2;
// obj2.next = obj3;
// obj3.next = obj4;

console.log(list.back());

function SList() {

    this.head = null;
    this.addBack = addBack;

}

function Nodey(val) {

    this.val = val;
    this.next = null;

}

function addBack(val) {

    runner = this.head;

    while(runner) {

        if (runner.next) {

            runner = runner.next;

        } else {

            runner.next = new Nodey(val);
            return runner.next;

        }
    }
}

// tests
list = new SList();
obj1 = new Nodey(1);
obj2 = new Nodey(2);
obj3 = new Nodey(3);
list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;

console.log(list.addBack(4));

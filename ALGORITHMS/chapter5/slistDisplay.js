function SList() {

    this.head = null;
    this.display = display;

}

function Nodey(name) {

    this.name = name;
    this.next = null;

}

function display() {

    var runner = this.head;

    while(runner) {

        console.log(runner.name);
        runner = runner.next;
    }

}

list = new SList();
obj1 = new Nodey('value1');
obj2 = new Nodey('value2');
obj3 = new Nodey('value3');
obj4 = new Nodey('value4');
list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;
obj3.next = obj4;
list.display();

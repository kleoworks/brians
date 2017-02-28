function SList() {

    this.head = null;
    this.average = average;
    this.count = count;

}

function Nodey(val) {

    this.val = val;
    this.next = null;

}

function count() {

    count = 0;
    cur_nodey = this.head;

    while(true) {

        if (cur_nodey) {

            count++;
            cur_nodey = cur_nodey.next;

        } else {

            return count;

        }
    }
}

function average() {

    count = this.count();
    sum = 0;

    if (count == 0) {

        return 'no values to average!';

    }

    runner = this.head;

    while(runner) {

        sum += runner.val;
        runner = runner.next;

    }

    return sum / count;

}


list = new SList();
obj1 = new Nodey(1);
obj2 = new Nodey(2);
obj3 = new Nodey(4);
obj4 = new Nodey(5);

list.head = obj1;
obj1.next = obj2;
obj2.next = obj3;
obj3.next = obj4;

console.log(list.average());

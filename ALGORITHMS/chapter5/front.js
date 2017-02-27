function NodeList() {

    this.head = null;
    this.front = front;

}

function Node(name) {

    this.name = name;
    this.next = null;

}

function front() {

    if (this.head == null) {

        return null;

    } else {

        return this.head.name;
    }

}

list = new NodeList();
kid1 = new Node('Tad');
kid2 = new Node('Sam');

list.head = kid1;
kid1.next = kid2;

console.log(list.front());

function NodeList() {

    this.head = null;
    this.removeFront = removeFront;

}

function Node(name) {

    this.name = name;
    this.next = null;
}

function removeFront() {

    if (this.head == null) {

        console.log('1st if');
        return null;


    } else if (this.head.next == null) {

        this.head == null;
        return null;

    } else {

        this.head = this.head.next;

    }

}


//tests
list = new NodeList();

kid1 = new Node('Rudy');
kid2 = new Node('Joe');
kid3 = new Node('Brian');

list.head = kid1;
kid1.next = kid2;
kid2.next = kid3;

console.log(list);

list.removeFront();

console.log(list);

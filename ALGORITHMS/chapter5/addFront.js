function NodeList() {

    this.head = null;
    this.addFront = addFront;

}

function Node(data) {

    this.data = data;
    this.next = null;

}

function addFront(node) {

    node.next = this.head;
    this.head = node;

}


//tests
my_list = new NodeList();

kid1 = new Node('Joe');
my_list.head = kid1;

kid2 = new Node('Rudy');
kid2.next = kid1;
my_list.head = kid2;

console.log(my_list);
console.log(kid1);
console.log(kid2);

kid3 = new Node('Brian');
my_list.addFront(kid3);
console.log(kid3);

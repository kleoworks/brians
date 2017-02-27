function NodeList() {

    this.head = null;
    this.contains = contains;

}

function Node(name) {

    this.name = name;
    this.next = null;

}

function contains(val) {

    node = this.head;

    while(true) {

        if (node.name == val) {

            return node;
        } else if (node.next == null) {

            return false;

        }

        node = node.next;

    }

}


//tests

kid1 = new Node('Sam');
kid2 = new Node('George');
kid3 = new Node('Louis');
kid4 = new Node('Tad');
// kid4 = new Node('Taddy');

list = new NodeList();
list.head = kid1;
kid1.next = kid2;
kid2.next = kid3;
kid3.next = kid4;

console.log(list.contains('Tad'));

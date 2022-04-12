package algo;

class Node {
	
	/**
	 * @return the parent
	 */
	public Node getParent() {
		return parent;
	}

	/**
	 * @param parent the parent to set
	 */
	public void setParent(Node parent) {
		this.parent = parent;
	}

	/**
	 * @return the leftChild
	 */
	public Node getLeftChild() {
		return leftChild;
	}

	/**
	 * @param leftChild the leftChild to set
	 */
	public void setLeftChild(Node leftChild) {
		this.leftChild = leftChild;
	}

	/**
	 * @return the rightChild
	 */
	public Node getRightChild() {
		return rightChild;
	}

	/**
	 * @param rightChild the rightChild to set
	 */
	public void setRightChild(Node rightChild) {
		this.rightChild = rightChild;
	}

	/**
	 * @return the prevTail
	 */
	public Node getPrevTail() {
		return prevTail;
	}

	/**
	 * @param prevTail the prevTail to set
	 */
	public void setPrevTail(Node prevTail) {
		this.prevTail = prevTail;
	}

	/**
	 * @return the data
	 */
	public int getData() {
		return data;
	}

	/**
	 * @param data the data to set
	 */
	public void setData(int data) {
		this.data = data;
	}
	
	public int getPriority() {
		return priority;
	}

	/**
	 * @param data the data to set
	 */
	public void setPriority(int priority) {
		this.priority = priority;
	}
	
	
	Node parent;
	Node leftChild;
	Node rightChild;
	Node prevTail;
	int data;
	int priority;
	Node next;

	Node(int data) {
		this.data = data;
	}
}


class LinkedHeap {

	Node root;
	Node tail;
	int size;
	
	
	int peek() { // return the minimum key value
		return root.getData();
	}

	void insert(int data) { // insert data into heap
		if (root == null) {
			root = new Node(data);
			tail = root;
		} else if (tail.getLeftChild() == null) {
			tail.leftChild = new Node(data);
			tail.leftChild.parent = tail;
			heapify(tail.getLeftChild());
		} else {
			tail.rightChild = new Node(data);
			tail.rightChild.parent = tail;
			heapify(tail.getRightChild());
			Node prevTail = tail;
			setTail(tail);
			tail.prevTail = prevTail;
		}
		size++;
	}
	
	void swapNodes(Node a, Node b) {
		int temp = a.data;
		a.data = b.data;
		b.data = temp;
	}
	
	void setTail(Node node) { // set the tail
		if (node.getParent() == null) {
			tail = node;
			while (tail.getLeftChild() != null) {
				tail = tail.getLeftChild();
			}
		}
		else if (node.getParent().getLeftChild() == node) {
			tail = node.getParent().getRightChild();
			while (tail.getLeftChild() != null) {
				tail = tail.getLeftChild();
			}
		} else if (node.getParent().getRightChild() == node) {
			setTail(node.getParent());
		}
	}

	void delete() {
		if (root == null) {
			System.out.println("MinHeap is empty");
			return;
		}
		if (tail == root) {
			tail = null;
			root = null;
		} else {
			if (tail.rightChild != null) {
				swapNodes(tail.rightChild, root);
				tail.rightChild = null;
				reverseHeapify(root);
			} else if (tail.leftChild != null) {
				swapNodes(tail.leftChild, root);
				tail.leftChild = null;
				reverseHeapify(root);
			} else {
				tail = tail.prevTail;
				delete();
				size++;
			}
		}
		size--;
	}

	void heapify(Node node) {
		if (node.parent != null) {
			if (node.parent.data > node.data) {
				swapNodes(node.parent, node);
				heapify(node.parent);
			}
		}
	}

	void reverseHeapify(Node node) { // needed for when you delete
		if (node == null || node.leftChild == null)
			return;
		Node min = node.leftChild;
		if (node.rightChild != null && min.data > node.rightChild.data) {
			min = node.rightChild;
		}
		if (min.data < node.data) {
			swapNodes(node, min);
			reverseHeapify(min);
		}
	}

	void traverse(Node node) { // print out nodes
		if (node != null) {
			traverse(node.leftChild);
			System.out.println(node.data);
			traverse(node.rightChild);
		}
	}
}

class PriorityQueue {
	
	private Node head = null;
	private int size = 0;
	
	public void add(int x, int p) {
        // Create a new node
        Node newNode = new Node(x);
        newNode.setPriority(p);
        // If head is null, this is the first node to be added
        // so make head = newNode
        if (head == null) {
            head = newNode;
            return;
        }
        Node temp = head;
        Node prev = null;
        // search for first node having priority less than p
        while (temp != null && temp.priority > p) {
            prev = temp;
            temp = temp.next;
        }
        if (temp == null) {
            // no node with priority less than this node (Case 1)
            prev.next = newNode;
        } else {
            if (prev == null) {
                // all the nodes have priority less than p (Case 2)
                // add this node at the starting
                newNode.next = head;
                head = newNode;
            } else {
                // Case 3
                // add this node before the node with priority less than p 
                newNode.next = temp;
                prev.next = newNode;
            }
        }
        size++;
    }
	
	public int remove() {
        // head of the linked list contains the maximum priority element
        if (head != null) {
            int data = head.data;
            // removing the highest priority element
            head = head.next;
            size--;
            return data;
        }
        return -1;
    }
	
	public boolean isEmpty() {
		if (head == null) {
            return true;
        } else {
        	return false;
        }
	}
	
	public int getSize() {
		return size;
	}
	
	
}

public class Assignment4 {

	public static void main(String[] args) {
		
		System.out.println("-----------------------");
		System.out.println("Linked Heap");
		System.out.println("-----------------------");

		LinkedHeap minHeap = new LinkedHeap();

		minHeap.insert(0);
		minHeap.insert(1);
		minHeap.insert(2);
		minHeap.insert(3);
		minHeap.insert(4);
		minHeap.insert(5);
		
		System.out.println("size : " + minHeap.size);
		
		System.out.println("Root : " + minHeap.peek());

		System.out.println("Delete : " + minHeap.peek());
		minHeap.delete();

		System.out.println("New Root : " + minHeap.peek());
		System.out.println("New size : " + minHeap.size);
		System.out.println("Heap");
		System.out.println("-----------------------");
		minHeap.traverse(minHeap.root);
		
		System.out.println("-----------------------");
		System.out.println("Priority Queue");
		System.out.println("-----------------------");
		
		PriorityQueue pq = new PriorityQueue();
		pq.add(11, 0);
		pq.add(7, 1);
		pq.add(8, 2);
		pq.add(6, 4);
		pq.add(5, 5);
		pq.add(9, 3);
		pq.add(4, 6);
		System.out.println(pq.remove());
        System.out.println(pq.remove());
        System.out.println(pq.remove());
		System.out.println(pq.getSize());
		
		
		
	}
}

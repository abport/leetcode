This is a solution for the Coding Problem [203. Remove Linked List Elements from LeetCode](https://leetcode.com/problems/remove-linked-list-elements/description):

We are going to learn how to remove all the nodes in a linked list that have a certain value.

A linked list is a list of items that are connected to each other. Each item is called a "node". Each node has a value, and it also has a connection to the next node in the list. The last node in the list does not have a connection to any other node.

To remove a node from a linked list, we need to change the connection of the previous node to the next node. This way, the removed node is no longer connected to the rest of the list.

Here is an example of a linked list with the values `1`, `2`, `3`, and `4`:

    1 -- 2 -- 3 -- 4

Let's say we want to remove the node with the value `2`. Here is what the linked list would look like after we remove it:

    1 -- 3 -- 4

We can see that the node with the value `2` is no longer connected to the rest of the list.

Now, let's write a function to remove all the nodes with a certain value from a linked list.

First, we create a special node called a "dummy" node. We set the value of the dummy node to `-1`. We also set the dummy node to be the head of the linked list. This is so that we don't have to worry about the case where the head node has the value we want to remove.

Next, we set a variable called `curr` to be the dummy node. This will be the node that we are currently looking at.

We start a loop that will run until we reach the end of the linked list. Inside the loop, we check if the value of the next node is the value we want to remove. If it is, we skip over the next node by changing the `curr` node's connection to the next node's next node. If the value is not the one we want to remove, we move on to the next node by setting `curr` to be the next node.

After the loop is finished, we return the next node of the dummy node. This is the new head of the linked list.

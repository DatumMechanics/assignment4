Assignment #4 



_Task_#1_ (25pts) Write a subroutine to count the number of collisions for a hash table 
that has been filled. You are given a declaration of a function here: 



Clearly, nothing is done yet. You are to loop through the array, then 
traverse the linked list, and count the number of collisions. 

_Task_#2_ (25pts) Write an updated hash function. You are given a second hash function, called
``hash_function2()''. You are to change the code so that it is different from 
the hash_function1(). Initially, they are the same. 

Your code should confirm that the number of collisions, counted by the function you
wrote for part #1, should reduce.

Partial credit will be attained for 4 collisions, and full credit for 3 collisions.

_Task_#3_ (30pts) Write a remove function that will remove a particular key/value pair.

You have a template function that you are to implement removal of a key/value pair.

Your code should handle:

* removing from the head of a bucket when needed

* removing from the middle of a bucket when needed.

* removing from the end of a linked list bucket when needed.

* handling the situation when a provided key does not exist. 

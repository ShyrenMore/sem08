Distributed global averaging is a method used in distributed computing to perform the averaging of data across multiple machines or devices in a network. The goal is to find the average of a set of values, but the values are stored on different machines, and the computation must be performed in a distributed manner.

In this method, each machine computes the average of its local data, and then the local averages are sent to a central node or a group of nodes. The central node then calculates the global average by combining the local averages. The central node may also communicate back to the machines to update their data and repeat the process until convergence is achieved.

The distributed global averaging method is commonly used in machine learning, where it is used to update the weights of a neural network in a distributed setting. The weights are updated based on the average of the gradients computed by each machine, and the distributed global averaging method is used to compute the average gradient across all machines. This approach helps to speed up the training process and can handle large datasets that cannot fit on a single machine.

## Working of code

![image](https://user-images.githubusercontent.com/56788568/233801179-41ff8377-acad-4428-b8e1-3d1a3301ad53.png)
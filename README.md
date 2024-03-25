## Non-Touch_Writing_Pad


AIVirtualMouse.py leverages gesture control to manipulate your mouse. It operates locally on your computer, functioning as both the client and the server, and served as the [inspiration](https://github.com/RNCManipal/TouchlessPad) for this project.

![image showcase](./public/example.jpg?raw=true)

We have restructured this file using Distributed Systems principles to establish a client-server communication model. Below are the functionalities:
  
| Function  | Thumb | Index | Middle | Ring | Little |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Left Click  | 0  | 1  | 0  | 0  | 0  |
| Right Click  | 0  | 0  | 0  | 0  | 1  |
| Switch tab  | 1  | 0  | 0  | 0  | 0  |
| Move mouse  | 0  | 1  | 1  | 0  | 0  |
| Double Click  | 0  | 1  | 1  | 1  | 0  |
| Scroll  | 0  | 0  | 0  | 0  | 0  |
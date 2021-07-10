Implement a toy Diffie-Hellman system by completing the Diffie-Hellman key exchange protocol:
supply the **publish** and **compute_secret** methods for both Alice and Bob.

 - Alice's `publish()` should return the message to be sent to Bob
 - Bob's `publish()` should return the message to be sent to Alice
 - Both their `compute_secret()` should, given the message from the other party, return the agreed-upon secret

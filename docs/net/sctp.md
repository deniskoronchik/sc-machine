# SCTP - SC-Code transport protocol

SCTP protocol is designed to implement efficient two sided communication between the `sc-server` and client by network.
It could be implemented with different programming languages. It has two implemntations that differ by underlaying format:

- json
- binary (in progress)

This is a common workflow sequence:

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant Storage
    participant Users

    activate Server

    Note right of Server: sc-server start
    activate Client
    Server->>Storage: Initialize
    activate Storage

    %% handshake >>>
    Client->>Server: Handshake
    activate Server
    
    Server-->>Client: Response
    deactivate Server
    Note right of Client: Resturns salt string

    %% <<< handshake

    %% auth >>>
    Client->>Server: Authorization
    activate Server
    Note right of Client: Sends satled password

    Server->>Users: Check User
    activate Users
    Users->>Server: Response
    deactivate Users

    Server->>Client: Response
    deactivate Server

    %% <<< atuh

    opt Receive events by subscription
      Storage-->>Server: Subscribed event
      Server-->>Client: Subsribed event
    end


    loop Work loop
      Client-->>Server: Request
      activate Server
      Server->>Storage: Do request
      activate Storage

      Storage->>Server: Response
      deactivate Storage
      Server-->>Client: Response
      deactivate Server  
    end

    Client->>Server: Close connection
    activate Server
    Server->>Storage: Destroy event subscriptions
    activate Storage
    Storage->>Server: Response
    deactivate Storage
    Server-->>Client: Response
    deactivate Server
    deactivate Client
    
    Note right of Server: sc-server shutdown
    Server->>Storage: Shutdown
    deactivate Storage

    deactivate Server
```


See `sctp.proto` file for more information
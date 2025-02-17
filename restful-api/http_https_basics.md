# HTTP / HTTPS Basics
1. **HTTP/HTTPS**:
    * **HTTP**:
        Hypertext transfer protocol is an applications layer communication protocol from both, the TCP/IP (layer 5) and OSI (layer 7) network comunications modles.  It is used for transfering data over a network. After a TCP connection (or other form of Transport layer protocol is established), the client and the server can begin to comunicate through HTTP. The ptotocol is divided into two main parts: requests and responses.

        * **HTTP requests**: The client's webrowser creates an http packet (which contains the http header and the payload) and is sent over the network to the specified server. The requst headers include: HTTP method, path to the desired resource, protocol version, optional headers, and the body (if sending a form).  For example:
        ```
        GET /home.html HTTP/1.1
        Host: developer.mozilla.org
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0
        Accept-Language: en-US,en;q=0.5
        ```

        * **HTTP response**: Once the server recieves the *http request* it sends an HTTP response.  This includes an http header which has the protocol version, the status code, status message, and the body of the package.  For example:
        ```
        200 OK
        Access-Control-Allow-Origin: *
        Connection: Keep-Alive
        Content-Encoding: gzip
        Content-Type: text/html; charset=utf-8
        Date: Mon, 18 Jul 2016 16:06:00 GMT
        Etag: "c561c68d0ba92bbeb8b0f612a9199f722e3a621a"
        Keep-Alive: timeout=5, max=997
        Last-Modified: Mon, 18 Jul 2016 02:36:04 GMT
        Server: Apache
        Set-Cookie: my-key=my value; expires=Mon, 17-Jul-2017 16:06:00 GMT; Max-Age=31449600; Path=/; secure
        ```

        The problem with HTTP is that everything is sent via plain text (or easily translatable from binary in HTTP/2).  This means that any intercepted package can be easily read and the information extracted.  That is why **HTTPS** was created.
    * **HTTPS**:
        HTTPS stands for Hypertext Transfer Protocol "Secure".  It acts in the same way regular HTTP does with the added benefit that it utilizes TLS(SSL) encryption.  This also digitally signs those requests and responses in order to authenticate both parties in the comunication. Transport Layer Security (TLS) works through *public key cryptography*.  The server must first go through authentication to get an SSL certificate.  This gives the server a *public* key and a *private* key.  The server shares its *public* key with the client (when a connection is opened) the *public* key is compared with the *private* key to verify the server is the rightful owner of the desired website. Finally, a new key is generated between the client and the server in order to create a session key and packets are sent with a signature that indicate if the data has been tampered with.

        After this process has occured, if anyone other than the client or the server try to view the data inside the packets, instead of seeing a normal http packet like this:
        ```
        304 Not Modified
        Access-Control-Allow-Origin: *
        Age: 2318192
        Cache-Control: public, max-age=315360000
        Connection: keep-alive
        Date: Mon, 18 Jul 2016 16:06:00 GMT
        ```
        They will see an incoherent string that can only be decripted with the session/encryption key such as this one:
        ```
        t8Fw6T8UV81pQfyhDkhebbz7+oiwldr1j2gHBB3L3RFTRsQCpaSnSBZ78Vme+DpDVJPvZdZUZHpzbbcqmSW1+3xXGsERHg9YDmpYk0VVDiRvw1H5miNieJeJ/FNUjgH0BmVRWII6+T4MnDwmCMZUI/orxP3HGwYCSIvyzS3MpmmSe4iaWKCOHQ==
        ```
2. **Common HTTP methods and status codes**:
    * **Methods**:
        * **GET**: Used to request information of a specified resource from the server.  Primarily used to retrieve data.
        * **POST**: Used to submit data to the specified section in the app/webpage. This inforation will be processed and creates changes in the server such as creating new entities.
        * **PUT**: Requests a specific state of the desired resource.
        * **PATCH**:  Applies partial changes to the requested resource.
        * **DELETE**: Used to remove a resource from the server.
    
    * **Status Codes**:
        * **1*xx* Informational Response**: The request was recieved and understood. The reuest will continue to be processed. Among the most common Informational response codes are:
            * *100 Continue*: The client should continue to send the request body.

        * **2*xx* Sucsess**: action has been recieved, understood, and accepted.  Among the most common success codes are:
            * *200 OK*: the client's request has been answered successfuly.
            * *201 Created*: Server responded succesfully to the clients request and created a new resource.
        
        * **3*xx* Redirection**: Indicates the client must take an action to complete the request. Usually involves being redirected to a different URL. Amonf the most common Redirection codes are:
            * *301 Moved Permanently*: Requests should be directed to the specified URI/URL.
            * *302 Found (Moved temporarily)*: Redirects client to another URL
        * **4*xx* Client Errors**: Errors that originate on the client's side.  Among the most common errors are:
            * *400 Bad Request*: Inability to answer request die to incorrect request (syntax error).
            * *401 Unauthorized*: Sent when authentication is required to perform an action but has not yet been provided.
            * *403 Forbidden*: The request was understood and is able to be fulfiled but the client does not have authorization to recieve the data or perform the desired action.
            * *404 Not Found*: The requested resources from the server cannot be found or do not exist.
        
        * **5*xx* Server Errors**: Given when the server is aware it encountered an error or cannot complete the request.  Ammong the most common Server Errors are:
            * *500 Internal Server Error*: The server cannot process the request due to an internal error.
            * *503 Service Unavailable*: The server is unavailable due to high traffic or maintenance.

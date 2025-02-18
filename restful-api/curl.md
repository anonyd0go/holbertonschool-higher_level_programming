# curl
`curl` is a command-line tool used for client-side internet protocol transfers.  It fetches network data and prints it to stdout.  This tool comes in handy in a development environment when you are trying to crate or test things out.

To get an in depth look at the project and what it can do go to: https://ec.haxx.se/index.html

There are many other resources online to learn about `curl`.

## Holberton assignments:
1. Installation and basic interaction:
    * `curl --version`: curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13 zlib/1.3 brotli/1.1.0 zstd/1.5.5 libidn2/2.3.7 libpsl/0.21.2 (+libidn2/2.3.7) libssh/0.10.6/openssl/zlib nghttp2/1.59.0 librtmp/2.3 OpenLDAP/2.6.7
    Release-Date: 2023-12-06, security patched: 8.5.0-2ubuntu10.6
    Protocols: dict file ftp ftps gopher gophers http https imap imaps ldap ldaps mqtt pop3 pop3s rtmp rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd

    * `curl http://example.com` :
    ```
    <!doctype html>
    <html>
    <head>
        <title>Example Domain</title>

        <meta charset="utf-8" />
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
        body {
            background-color: #f0f0f2;
            margin: 0;
            padding: 0;
            font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
            
        }
        div {
            width: 600px;
            margin: 5em auto;
            padding: 2em;
            background-color: #fdfdff;
            border-radius: 0.5em;
            box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
        }
        a:link, a:visited {
            color: #38488f;
            text-decoration: none;
        }
        @media (max-width: 700px) {
            div {
                margin: 0 auto;
                width: auto;
            }
        }
        </style>    
    </head>

    <body>
    <div>
        <h1>Example Domain</h1>
        <p>This domain is for use in illustrative examples in documents. You may use this
        domain in literature without prior coordination or asking for permission.</p>
        <p><a href="https://www.iana.org/domains/example">More information...</a></p>
    </div>
    </body>
    </html>
    ```

2. Fetching Data from an API:
    * `curl https://jsonplaceholder.typicode.com/posts`:
    ```
    [
        {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
        },
        {
            "userId": 1,
            "id": 2,
            "title": "qui est esse",
            "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        },
        ... ,
        {
            "userId": 10,
            "id": 99,
            "title": "temporibus sit alias delectus eligendi possimus magni",
            "body": "quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia"
        },
        {
            "userId": 10,
            "id": 100,
            "title": "at nam consequatur ea labore ea harum",
            "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
        }
    ]
    ```
    The output from this command returns an array of JSON posts placeholders.

3. Using Headers and Other Options with `curl`:
    * Getting HTTP request headers `curl -I https://jsonplaceholder.typicode.com/posts`:
    ```
    HTTP/2 200 
    date: Tue, 18 Feb 2025 16:06:26 GMT
    content-type: application/json; charset=utf-8
    report-to: {"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1739885262&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=HRiheui%2BsNUCaaJ%2FWz26NiN6OVowVCFYGHHZclN5wXg%3D"}]}
    reporting-endpoints: heroku-nel=https://nel.heroku.com/reports?ts=1739885262&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=HRiheui%2BsNUCaaJ%2FWz26NiN6OVowVCFYGHHZclN5wXg%3D
    nel: {"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}
    x-powered-by: Express
    x-ratelimit-limit: 1000
    x-ratelimit-remaining: 999
    x-ratelimit-reset: 1739885270
    vary: Origin, Accept-Encoding
    access-control-allow-credentials: true
    cache-control: max-age=43200
    pragma: no-cache
    expires: -1
    x-content-type-options: nosniff
    etag: W/"6b80-Ybsq/K6GwwqrYkAsFxqDXGC7DoM"
    via: 1.1 vegur
    cf-cache-status: HIT
    age: 9524
    server: cloudflare
    cf-ray: 913f43aeff7309f1-LAS
    alt-svc: h3=":443"; ma=86400
    server-timing: cfL4;desc="?proto=TCP&rtt=7333&min_rtt=7321&rtt_var=2066&sent=4&recv=6&lost=0&retrans=0&sent_bytes=3387&recv_bytes=764&delivery_rate=395574&cwnd=252&unsent_bytes=0&cid=4d7e4d9e6b98aeea&ts=129&x=0"
    ```

    * Using `curl` to make a POST request to the API `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`:
    ```
    {
    "title": "foo",
    "body": "bar",
    "userId": "1",
    "id": 101
    }
    ```




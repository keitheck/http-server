###  Lab 12: Hypertext Transfer Protocol

### Build a Socket HTTP Server

### Specifications
- Create a repository called `http-server` with a directory called `src`
- Create a branch on your `http-server` repository called `cowpy`
- Set up your ENV, and install a package called `cowpy`. Please reference the [Package Repo](https://github.com/jeffbuttars/cowpy) for more information on using the API.
- Create a file called `server.py`, as well as any configurations and documentation requirements for this to become a standalone API.
- In your `README.md`, please document the specification of your API. Each endpoint should be well formatted with markdown to highlight the available endpoints, and any example request syntax and expected response body.

- In `server.py` create the following endpoints:
    1. `GET /` - returns a valid HTML formatted response with a project description and an anchor tag which references a link to `/cow`.
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title> cowsay </title>
        </head>
        <body>
            <header>
                <nav>
                <ul>
                    <li><a href="/cowsay">cowsay</a></li>
                </ul>
                </nav>
            <header>
            <main>
                <!-- project description -->
            </main>
        </body>
        </html>
        ```
    2. `GET /cowsay` - returns a generic cowpy response which displays a helpful message to the client about how they can further interact with the API.
    3. `GET /cow?msg=text` - returns a cowpy response which correctly displays a default cow object including the `text` from your query string.
        ```
        _____________
        < text >
        -------------
        \         __------~~-,
            \      ,'            ,
                /               \
                /                :
                |                  '
                |                  |
                |                  |
                |   _--           |
                _| =-.     .-.   ||
                o|/o/       _.   |
                /  ~          \ |
            (____\@)  ___~    |
                |_===~~~.`    |
            _______.--~     |
            \________       |
                        \      |
                    __/-___-- -__
                    /            _ \
        ```
    4. `POST /cow msg=text` - returns a cowpy response with a JSON body `{"content": "<cowsay cow>"}`
        ```
            {
                "content": " _____________ \n< hello world >\n ------------- \n   \\         __------~~-,\n    \\      ,'            ,\n        /               \\\n         /                :\n        |                  '\n        |                  |\n        |                  |\n         |   _--           |\n         _| =-.     .-.   ||\n         o|/o/       _.   |\n         /  ~       \\ |\n       (____\\@)  ___~    |\n          |_===~~~.`    |\n       _______.--~     |\n       \\________       |\n            \\      |\n              __/-___-- -__\n             /            _ \\"
            }
        ```
    5. Both `GET` and `POST` should handle any paths that are not defined by you, and return with the appropriate `404 Not Found` response and headers.
    6. Ensure that each of your valid routes are also able to handle a malformed request, which should return a `400 Bad Request` response and headers. For example, a request to `GET /cow` which includes a query string message that is not properly formatted for your API should response properly.

- In `test_server.py`:
    1. Create a `module` scoped fixture while will run your server on a background thred while the test suite is executing.
    2. Write a test for each request method, `GET` and `POST` that validates a proper request with a response body, response status code, and headers. These should not be validated in one single test.